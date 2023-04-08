import os
import time
import boto3
from github import Github

def get_greengrass_deployment_status():
    client = boto3.client('greengrassv2')
    response = client.get_deployment(
        deploymentId=os.environ['INPUT_DEPLOYMENT_ID']
    )

    return response['deployment']

def update_pr_comment(deployment):
    g = Github(os.environ['INPUT_GITHUB_TOKEN'])
    repo = g.get_repo(os.environ['GITHUB_REPOSITORY'])
    pr = repo.get_pull(int(os.environ['INPUT_PULL_REQUEST_NUMBER']))
    comments = pr.get_issue_comments()

    deployment_status_md = f"""
**Deployment Name:** {deployment['deploymentName']}
**Deployment ID:** {deployment['deploymentId']}
**Time since deploy:** {deployment['createdAt']}
**Status:** {deployment['status']}
"""

    comment_id = None
    for comment in comments:
        if comment.user.login == os.environ['GITHUB_ACTOR']:
            comment_id = comment.id
            break

    if comment_id:
        comment = repo.get_issue_comment(comment_id)
        comment.edit(deployment_status_md)
    else:
        pr.create_issue_comment(deployment_status_md)

def main():
    while True:
        deployment = get_greengrass_deployment_status()
        update_pr_comment(deployment)

        if deployment['status'] in ['SUCCEEDED', 'FAILED']:
            break

        time.sleep(60)

if __name__ == '__main__':
    main()
