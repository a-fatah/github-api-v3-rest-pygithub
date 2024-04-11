import os
from github import Github
from dotenv import load_dotenv

class GithubService:
    def __init__(self):
        load_dotenv()
        access_token = os.getenv('GITHUB_TOKEN')
        self.github = Github(access_token)

    def create_repository(self, name):
        user = self.github.get_user()
        return user.create_repo(name)

    def create_issue(self, repo_name, title, body=None, assignee=None, labels=None):
        repo = self.github.get_user().get_repo(repo_name)
        return repo.create_issue(title=title, body=body, assignee=assignee, labels=labels)

    def create_gist(self, description, files, public=True):
        return self.github.get_user().create_gist(public, files, description)
