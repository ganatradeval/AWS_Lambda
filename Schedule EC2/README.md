# Schedule EC2
Schedule your EC2 instances to stop at a particular time and start again.

Suppose your project has less traffic at night and you want to stop a few instances to save cost. Obviously, there are other solutions out there. However you want Lambda function to start and stop it on a scheduled basis, then you are in right place.

In this project, we use AWSCloudWatch events to trigger Lambda function on a scheduled basis.

## Prerequisite
<img src=https://www.python.org/static/img/python-logo.png title="Python Logo"><img src="https://conceptdraw.com/a3133c3/p18/preview/640/pict--amazon-lambda-aws-compute-and-networking-vector-stencils-library" width=80 height=80 title="AWS Lambda Logo">

## Instruction
1.  Create Lambda function of given python code [EC2_Start](./EC2_start.py) [EC2_Stop](./EC2_Stop.py) and assign policy like given.
2.  Optionally, you can give 10 seconds timeout.
3.  Now, Go to **CloudWatch** console. 
4.  Go to **Create Rule** in **Events** and **Schedule** in **Event Source**.
5.  Just put cron expression and schedule your function by adding target of the Lambda we have just created.
