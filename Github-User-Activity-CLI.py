import requests
import sys

 # Fetch Github Data using Github CLI API

def process_events(user, data):

    event_map = {
        "IssuesEvent": f"- {user.capitalize()} Opened a new issue in",
        "CreateEvent": f"- {user.capitalize()} Created a new repository",
        "PullRequestEvent": f"- {user.capitalize()} opened pull request on",
        "IssueCommentEvent": f"- {user.capitalize()} commented on issue on",
        'ForkEvent':f"- {user.capitalize()} forked ",
        'PublicEvent': f"- {user.capitalize()} made repository public",
        "WatchEvent": f"- {user.capitalize()} Began a Watch Event on"
    }
    user_activities = []

    repo_commits = {}
    for event in data:
        repo_name = event['repo']['name']
        if event['type'] in event_map:
            action = event_map[event['type']]
            user_activities.append(f"{action} {repo_name}")
        elif event['type'] == "PushEvent":
            if repo_name in repo_commits:
                repo_commits[repo_name] += 1
            else:
                repo_commits[repo_name] = 1
    for repo,count in repo_commits.items():
        user_activities.append( f"- {user.capitalize()} Pushed {count} commits in {repo}")
    
    return user_activities
        


def main():

    if len(sys.argv) < 2:
        print("Usage: python Github-User-Activity-CLI.py <username>")
        return

    username = sys.argv[1]
    url = f"https://api.github.com/users/{username}/events"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            user_test = process_events(username ,data)

            for user in user_test:
                print(user)
        elif response.status_code == 404:
            raise ValueError(f"{response.status_code}\nThis is not a valid username, please try again...")
        else:
            raise ValueError(f"Unable to Fetch data, {response.status_code}")
            
    except Exception as error:
        print(f"Error {error}")

if __name__ == "__main__":
    main()