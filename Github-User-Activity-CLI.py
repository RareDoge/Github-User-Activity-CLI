import requests

# Fetch Github Data using Github CLI

url = "https://api.github.com/users/RareDoge/events"

params = {
    "login" : "RareDoge"
}

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    repo_commits = {}
    commits = 0

    for event in data:
        repo_name = event['repo']['name']
        if event['type'] == 'PushEvent':
            commits += 1
        if repo_name in repo_commits:
            repo_commits[repo_name] += commits
        else:
            repo_commits[repo_name] = commits
        commits = 0
    print(repo_commits)
else:
    print("keep working...")