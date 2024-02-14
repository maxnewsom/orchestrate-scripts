import os
import requests

def count_method_occurrences(log_json):
    method_count = {}
    for command in log_json:
        method = command.get('method')
        if method:
            method_count[method] = method_count.get(method, 0) + 1
    return method_count

def fetch_log_json(session_id, username, access_key):
    url = f"https://{username}:{access_key}@saucelabs.com/rest/v1/{username}/jobs/{session_id}/assets/log.json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch log.json for session ID {session_id}")
        return None

def main():
    session_id = os.environ.get('SESSION_ID')

    # Retrieve Sauce Labs credentials from environment variables
    username = os.environ.get('SAUCE_USERNAME')
    access_key = os.environ.get('SAUCE_ACCESS_KEY')

    if not username or not access_key:
        print("Sauce Labs credentials not found in environment variables.")
        return

    log_json = fetch_log_json(session_id, username, access_key)
    if log_json:
        method_count = count_method_occurrences(log_json)
        for method, count in method_count.items():
            print(f"breakdown of commands is: {method_count}")

if __name__ == "__main__":
    main()
