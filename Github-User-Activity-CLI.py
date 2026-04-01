import requests

# Fetch Github Data using Github CLI API
invalid_username = True
while invalid_username : 
    username = input("Enter a username: ")
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)

    if response.status_code == 200:
        invalid_username = False
        data = response.json()
        user_activities = []
        repo_commits = {}

        for event in data:
            repo_name = event['repo']['name']
            if event['type'] == "PushEvent":
                if repo_name in repo_commits:
                    repo_commits[repo_name] += 1
                else:
                    repo_commits[repo_name] = 1
            elif event['type'] == "IssuesEvent":
                user_activities.append(f"- Opened a new issue in {repo_name}.")
            elif event['type'] == "CreateEvent":
                user_activities.append(f"- Created a new repository {repo_name}.")
            elif event['type'] == "PullRequestEvent":
                user_activities.append(f"- opened pull request on {repo_name}.")
            elif event['type'] == 'IssueCommentEvent':
                user_activities.append(f"- commented on issue on {repo_name}.")
            elif event['type'] == 'ForkEvent':
                user_activities.append(f"- forked {repo_name}.")
            elif event['type'] == 'PublicEvent':
                user_activities.append(f"- made repository {repo_name} public.")
            else:
                user_activities.append(f"- Did something in {repo_name}.")

        for repo, count in repo_commits.items():
            user_activities.append(f"- Pushed {count} commits in {repo}")
        

        for user in user_activities:
            print(user)

    elif response.status_code == 404:
        print("This is not a valid username, please try again...")
    else:
        print(f"Unable to Fetch data, {response.status_code}")