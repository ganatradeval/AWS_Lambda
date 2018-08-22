# Schedule EC2
Schedule your EC2 instances stop at perticular time and start again.
Suppose your project has less traffic on night and you want to stop few instances to save cost. Obviously there are other solutions out there. However you want Lambda function to start and stop it on schedule basis, then you are on right place.

In this project, we use AWSCloudWatch events to trigger Lambda function on scheduled basis.

## Prerequisite
![Python Image](https://www.python.org/static/img/python-logo.png)
![AWS Lambda Image](https://conceptdraw.com/a3133c3/p18/preview/640/pict--amazon-lambda-aws-compute-and-networking-vector-stencils-library)

## Instruction
1.  Create Lambda funtion of given python code and assign policy like given.
2.  Optionally give 10 seconds timeout.
3.  Now, Go to CloudWatch console. 
4.  Go to **Create Rule** in **Events** and **Schedule** in **Event Source**.
5.  Just put cron expression and schedule your function by adding target of the Lambda we have just created.
