import unittest
import shutil
import os
from atlassian_server_api.bitbucket import BitBucket
from atlassian_server_api.jira import Jira
from atlassian_server_api.git import Git
from unittest.mock import MagicMock, patch


class AtlassianGitTests(unittest):

    cwd = os.getcwd()
    test_dir = os.path.join(cwd, 'atlassian_server_api', 'test', 'git_test')

    def git_test(self):

        # create test file
        os.mkdir(self.test_dir)
        f = open(os.path.join(self.test_dir, "git_test.txt"), "w+")
        for i in range(10):
            f.write("This is line %d\r\n" % (i + 1))

        # create git repo
        repo = Git(self.test_dir)
        r = repo.git_init()
        self.assertIs(r.decode('utf-8').startswith('Initialized empty Git repository'), True)
        shutil.copyfile(os.path.join(self.cwd, 'atlassian_server_api', 'test', 'git', '.gitignore'),
                        os.path.join(self.test_dir, '.gitignore'))
        repo.git_add_all()
        r = repo.git_status()
        self.assertIs(r.decode('utf-8').startswith(
            'On branch master\n\nNo commits yet\n\nChanges to be committed:\n  '
            '(use "git rm --cached <file>..." to unstage)\n\n\tnew file:   .gitignore\n\tnew file:   git_test.txt'),
                      True)
        r = repo.git_commit_all("init commit")
        self.assertIs(r.decode('utf-8').startswith('[master (root-commit)'), True)

        shutil.rmtree(self.test_dir)

    # TODO: create mock tests
    # @patch('example.models.request')
    def bitbucket_test(self, req):
        # verify API comms
        project_id = ATLASSIAN_SETTINGS['bitbucket']['projects'].values()[0]
        bb_auth = ATLASSIAN_SETTINGS['bitbucket']['username'], ATLASSIAN_SETTINGS['bitbucket']['password']
        bb_http_url = ATLASSIAN_SETTINGS['bitbucket']['http_url']
        bb = BitBucket(base_http_url=bb_http_url, project_key=project_id, auth=bb_auth)

        # get list of repos and check that first repo has at least 1 branch
        repos = bb.get_repos(10).json()['values']
        first_repo = repos[0]['slug']
        self.assertIs(bb.get_repo_branches(repo_name=first_repo).json()['size'] > 0, True)

        # TODO: mock API responses
        # url = MagicMock()
        # self.example._get_page(url)
        # req.assert_called_once_with('GET', url)

    # TODO: create mock tests
    def jira_test(self):
        project_id = ATLASSIAN_SETTINGS['jira']['projects'].values()[0]
        auth = ATLASSIAN_SETTINGS['jira']['username'], ATLASSIAN_SETTINGS['jira']['password']
        jira = Jira(base_http_url=ATLASSIAN_SETTINGS['jira']['http_url'], project_key=project_id, auth=auth)

        # verify issues exist
        issue = jira.get_issues(max_results=10).json()
        if issue['size'] > 0:
            print('ERROR: Issue not created successfully.' + str(issue))

    def cleanup(self):
        shutil.rmtree(self.test_dir)


tests = AtlassianGitTests
tests.git_test
tests.bitbucket_test
tests.jira_test
