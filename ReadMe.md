# Python Atlassian Server API

Communicate with Atlassian's JIRA and BitBucket REST API's.

This package uses the requests library to communicate with Atlassian's JIRA and BitBucket REST API's. It satarted as a 
way to quickly create local repos, push them to BitBucket, and create JIRA issues for that repo since Atlassian's only 
works with their cloud API.

## Setup

The easiest way to set up the app is a settings file and what's below, but you could just do it in the code.

Add the following to ```settings.py```:

```
ATLASSIAN_SETTINGS = {
    'jira': {
        'url': 'your_url',
        'username': 'your_username',
        'password': 'your_password'
    },
    'bitbucket': {
        'http_url': 'your_url',   # HTTP address
        'ssh_url': 'your_url',   # SSH address
        'username': 'your_username',
        'password': 'your_password'
    }
}
```


To disable of SSH host checking, add the following lines to the beginning of /etc/ssh/ssh_config:

```
Host 192.168.0.*
   StrictHostKeyChecking=no
   UserKnownHostsFile=/dev/null
```

See https://www.shellhacks.com/disable-ssh-host-key-checking/ for more details.
   
Options:

* The Host subnet can be * to allow unrestricted access to all IPs.
* Edit /etc/ssh/ssh_config for global configuration or ~/.ssh/config for user-specific configuration.

## Usage

### Create Repository

```create_repo(uploaded_file_path, project_id, repo_slug)```


### Branch Repository

```branch_repo(project_id, repo_slug, 'test_branch')```


### Create Jira Issue

