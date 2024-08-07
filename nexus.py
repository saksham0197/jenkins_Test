import json
import requests
from requests.auth import HTTPBasicAuth
import sys

def upload_to_nexus(json_data, repo_url, username, password):
    headers = {'Content-Type': 'application/json'}
    response = requests.put(repo_url, headers=headers, data=json.dumps(json_data), auth=HTTPBasicAuth(username, password))
    return response.status_code, response.text

# Example usage with command line arguments
if __name__ == "__main__":
    json_payload = {
        "requested_by": "user",
        "request_date": "2024-08-05",
        "approval_date": "2024-08-05",
        "approver": "approver",
        "target_repo_name": "target_repo"
    }

    nexus_repo_url = "http://localhost:8081/repository/devopsrepo/path/to/upload/data.json"
    jenkins_username = sys.argv[1]
    jenkins_password = sys.argv[2]

    status_code, response_text = upload_to_nexus(json_payload, nexus_repo_url, jenkins_username, jenkins_password)
    print(f"Status Code: {status_code}\nResponse Text: {response_text}")
