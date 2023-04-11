# Greengrass Deployment Status - Action

```yaml
permissions:
  contents: read
  id-token: write

jobs:
  greengrass:
    - name: Deploy Greengrass component
      id: deploy
      run: |
        export AWS_REGION=ap-southeast-2
        DEPLOYMENT_ID=$(aws greengrassv2 create-deployment \
          --output text \
          --no-paginate \
          --cli-input-json file://deployment.json \
          --query 'deploymentId')

        echo "::set-output name=deployment_id::${DEPLOYMENT_ID}"

    - name: Greengrass Deployment Status
      uses: t04glovern/greengrass-deployment-status-action@main
      with:
        aws_region: ap-southeast-2
        deployment_id: ${{ steps.deploy.outputs.deployment_id }}
```
