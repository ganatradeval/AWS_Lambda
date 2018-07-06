'''
This is a sample function to send AWS Health event messages to a Slack channel. 
Follow these steps to configure the webhook in Slack:
  1. Navigate to https://<your-team-domain>.slack.com/apps
  2. Search for and select "Incoming WebHooks".
  3. Select "Add Configuration" and choose the default channel where messages will be sent. Then click "Add Incoming WebHooks Integration".
  4. Copy the webhook URL from the setup instructions and use it in the configuration section bellow
You can also use KMS to encrypt the webhook URL as shown here: https://aws.amazon.com/blogs/aws/new-slack-integration-blueprints-for-aws-lambda/
'''

from __future__ import print_function

import boto3
import json
import logging
import os
import botocore.vendored.requests.packages.urllib3

from botocore.vendored.requests.packages.urllib3 import request,poolmanager,exceptions
from botocore.vendored.requests.packages.urllib3.exceptions import HTTPError
#configuration

# The Slack channel to send a message to stored in the slackChannel environment variable
SLACK_CHANNEL = "<Slack Channel Name Here>"
# Add the webhook URL from Slack below
HOOK_URL = "<Slack Channel HookURL Here>"
# Setting up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

#main function

def lambda_handler(event, context):
    #These messages are for formatting purpose. You can change it according to your need.
    message = str("Detail Type: " + event['detail-type'] + "\n")
    message += str("\nStart Time: " + event['detail']['startTime'])
    message += str("\nEnd Time: " + event['detail']['endTime'])
    message +=  str("\nEvent Description: " + event['detail']['eventDescription'][0]['latestDescription'] )
    message += str("\n\n<https://phd.aws.amazon.com/phd/home?region=us-east-1#/event-log?eventID=" + event['detail']['eventArn'] + "|Click here> for details.")
    
    json.dumps(message)
    slack_message = {
        'channel': SLACK_CHANNEL,
        'text': message,
        'username': 'AWS-Health-Notification',
        'icon_emoji': ":ghost:"
    }
    logger.info(str(slack_message))
    print("Received Event: ",message)
        
    try:
	  	botocore.vendored.requests.packages.urllib3.disable_warnings(botocore.vendored.requests.packages.urllib3.exceptions.InsecureRequestWarning)
	  	http = botocore.vendored.requests.packages.urllib3.PoolManager()
	  	response = http.request('POST', HOOK_URL, headers={'Content-Type':'application/json'}, body=json.dumps(slack_message) )    
	  	print("JSON Message here:",json.dumps(slack_message))
	  	logger.info("Message posted to %s", slack_message['channel'])
    except  HTTPError as e:
        logger.error("Request failed: %d %s", e.code, e)
    except Exception as e:
        logger.error("Server connection failed: %s", e)
