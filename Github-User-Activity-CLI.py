import requests
import sys

 # Fetch Github Data using Github CLI API

def process_events(data):

    event_map = {
        "IssuesEvent": f"- Opened a new issue in",
        "CreateEvent": f"- Created a new repository",
        "PullRequestEvent": f"- opened pull request on",
        "IssueCommentEvent": f"- commented on issue on",
        'ForkEvent':f"- forked ",
        'PublicEvent': f"- made repository public",
        "WatchEvent": f"- Began a Watch Event on"
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
        user_activities.append( f"- Pushed {count} commits in {repo}")
    
    return user_activities
        


def main():
    invalid_username = True
    while invalid_username : 
        username = input("Enter a username: ")
        url = f"https://api.github.com/users/{username}/events"
        response = requests.get(url)

        if response.status_code == 200:
            invalid_username = False
            data = response.json()
            user_test = process_events(data)

            for user in user_test:
                print(user)

        elif response.status_code == 404:
            print("This is not a valid username, please try again...")
        else:
            print(f"Unable to Fetch data, {response.status_code}")

if __name__ == "__main__":
    main()