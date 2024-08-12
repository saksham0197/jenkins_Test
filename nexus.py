# import json
# import requests
# from requests.auth import HTTPBasicAuth

# def upload_to_nexus(data, nexus_url, username, password):
#     headers = {
#         'Content-Type': 'application/json'
#     }
#     auth = HTTPBasicAuth(username, password)
#     response = requests.put(nexus_url, headers=headers, data=json.dumps(data), auth=auth)
#     if response.status_code == 201:
#         print("Upload successful!")
#     else:
#         print(f"Failed to upload. Status code: {response.status_code}, Response: {response.text}")

# if __name__ == "__main__":
#     data = json.loads('''${jsonPayload}''')
#     nexus_url = "${env.NEXUS_URL}"
#     username = "${env.NEXUS_CREDENTIALS_USR}"
#     password = "${env.NEXUS_CREDENTIALS_PSW}"

#     upload_to_nexus(data, nexus_url, username, password)


def main():
    print("Hello, Jenkins!")

if __name__ == "__main__":
    main()
