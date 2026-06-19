import os
import sys
import requests


def get_github_user_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    token = os.environ.get("GITHUB_TOKEN")
    headers = {"Authorization": f"token {token}"} if token else {}

    try:
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code == 404:
            print("User not found.")
            return

        if response.status_code == 403:
            print("Rate limit exceeded. Try again later or set a GITHUB_TOKEN env var.")
            return

        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            return

        events = response.json()

        if not events:
            print("No recent activity found.")
            return

        for event in events[:10]:
            event_type = event.get("type", "Unknown")
            repo = event.get("repo", {}).get("name", "unknown/repo")
            payload = event.get("payload", {})

            if event_type == "PushEvent":
                commits = payload.get("size", len(payload.get("commits", [])))
                print(f"- Pushed {commits} commit(s) to {repo}")

            elif event_type == "IssuesEvent":
                action = payload.get("action", "updated")
                print(f"- {action.capitalize()} an issue in {repo}")

            elif event_type == "IssueCommentEvent":
                print(f"- Commented on an issue in {repo}")

            elif event_type == "WatchEvent":
                print(f"- Starred {repo}")

            elif event_type == "ForkEvent":
                print(f"- Forked {repo}")

            elif event_type == "CreateEvent":
                ref_type = payload.get("ref_type", "something")
                print(f"- Created {ref_type} in {repo}")

            elif event_type == "DeleteEvent":
                ref_type = payload.get("ref_type", "something")
                print(f"- Deleted {ref_type} in {repo}")

            elif event_type == "PullRequestEvent":
                action = payload.get("action", "updated")
                pr = payload.get("pull_request", {})
                if action == "closed" and pr.get("merged"):
                    print(f"- Merged a pull request in {repo}")
                else:
                    print(f"- {action.capitalize()} a pull request in {repo}")

            elif event_type == "PullRequestReviewEvent":
                print(f"- Reviewed a pull request in {repo}")

            elif event_type == "ReleaseEvent":
                action = payload.get("action", "published")
                print(f"- {action.capitalize()} a release in {repo}")

            else:
                print(f"- {event_type} in {repo}")

    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python github_activity.py <username>")
        sys.exit(1)

    username = sys.argv[1]
    get_github_user_activity(username)


if __name__ == "__main__":
    main()