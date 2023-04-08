#!/bin/sh -l

if [ -n "${INPUT_AWS_ACCESS_KEY_ID}" ] && [ -n "${INPUT_AWS_SECRET_ACCESS_KEY}" ]; then
    export AWS_ACCESS_KEY_ID="${INPUT_AWS_ACCESS_KEY_ID}"
    export AWS_SECRET_ACCESS_KEY="${INPUT_AWS_SECRET_ACCESS_KEY}"
fi

export AWS_REGION="${INPUT_AWS_REGION}"
export INPUT_DEPLOYMENT_ID="${INPUT_DEPLOYMENT_ID}"

chmod +x /greengrass_status.py

python /greengrass_status.py
