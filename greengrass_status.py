import os
import time
import boto3

def get_greengrass_deployment_status():
    client = boto3.client('greengrassv2', region_name=os.environ['AWS_REGION'])
    response = client.get_deployment(
        deploymentId=os.environ['DEPLOYMENT_ID']
    )
    return response['deploymentStatus']

def main():
    while True:
        deployment_status = get_greengrass_deployment_status()
        print(f"Deployment status ({os.environ['DEPLOYMENT_ID']}): {deployment_status} - {time.asctime(time.localtime(time.time()))}")
        if deployment_status in ['ACTIVE', 'FAILED']:
            if deployment_status == 'FAILED':
                return 1
            else:
                return 0

        time.sleep(20)

if __name__ == '__main__':
    main()
