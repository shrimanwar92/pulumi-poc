import os
import boto3
from pulumi import automation

os.environ["PULUMI_CONFIG_PASSPHRASE"] = "test"

def test():
    stack = automation.select_stack(
        stack_name='dev',
        work_dir=os.path.join(os.path.dirname(__file__))
    )

    outputs = stack.outputs()
    lb_arn = outputs['awsx:lb:ApplicationLoadBalancer:arn'].value
    function_arn = outputs['aws:lambda/function:Function:arn'].value
    
    client_elb = boto3.client('elbv2')
    client_lambda = boto3.client('lambda')
    
    lb_response = client_elb.describe_load_balancers(
        LoadBalancerArns=[
            lb_arn,
        ],
    )

    lambda_response = client_lambda.get_function(
        FunctionName=function_arn
    )

    assert lb_response['ResponseMetadata']['HTTPStatusCode'] == 200, "Application loadbalancer is present"
    assert lambda_response['ResponseMetadata']['HTTPStatusCode'] == 200, "Lambda function is present"


            