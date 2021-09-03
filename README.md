# route53-ddns

This package provide a simple CLI to update a Route53 Hosted Zone. This can be run as
cron job to provide a dynamic DNS functionality.

The package uses [ipfy](https://api.ipify.org) to get the current IP (or it can be provided as argument).

Route53 interaction is achieved using [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html).
Credentials can be provided in any of the supported way boto3 expects them.
See [boto3 credentials](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html)
documentation.
