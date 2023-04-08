# Greengrass Deployment Status - Action

```yaml
permissions:
  contents: read
  pull-requests: write
  id-token: write

jobs:
  greengrass:
    name: Greengrass Deployment Status
    uses: t04glovern/greengrass-deployment-status-action@main
    with:
      aws_region: ap-southeast-2
      github_token: ${{ secrets.GITHUB_TOKEN }}
      deployment_id: 848ee2bd-c89b-4b79-97b3-53b4f0f7e3ed
```
