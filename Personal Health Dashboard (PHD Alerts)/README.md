# Personal Health Dashboard Alerts to Slack
This function will forward AWS Personal Health Dashboard events - coming to your account - directly to your Slack Channel.

1. Create one Lambda function 
2. Check the Slack channel URL
3. Modify your function from given funtion
4. Add CloudWatch Event which will trigger Lambda Function whenever 'AWS Health Events' arrive.

And you are Done!!

We are using [Sample Json](https://github.com/ganatradeval/AWS_Lambda/blob/master/Personal%20Health%20Dashboard%20(PHD%20Alerts)/AWS_PHD_Sample.json) for testing our Lambda.

[!Sample Image ](https://d1.awsstatic.com/support/brath/PHD_Alert.1e0608887bb0353d05e2ae6666ca6ea099f66462.jpeg)
