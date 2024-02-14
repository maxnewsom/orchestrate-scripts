import os
import requests

def count_post_commands(log_json):
    count = 0
    for command in log_json:
        if command['method'] == 'POST':
            count += 1
    return count

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
        post_commands_count = count_post_commands(log_json)
        print(f"Number of POST commands in log.json: {post_commands_count}")

if __name__ == "__main__":
    main()
