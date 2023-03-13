import pulumi
from pulumi_aws import lambda_, iam
import pulumi_awsx as awsx

class CxCrosswalkLbLambda():
    def __init__(self, parent: pulumi.ComponentResource):
        self.lb = awsx.lb.ApplicationLoadBalancer(
            resource_name='cw-alb-demo',
            default_target_group=awsx.lb.TargetGroupArgs(
                target_type='lambda'
            ),
            opts=pulumi.ResourceOptions(parent=parent)
        )

        lambda_role = iam.Role('lambdaRole',
            assume_role_policy="""{
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Action": "sts:AssumeRole",
                        "Principal": {
                            "Service": "lambda.amazonaws.com"
                        },
                        "Effect": "Allow",
                        "Sid": ""
                    }
                ]
            }"""
        )

        iam.RolePolicy('lambdaRolePolicy',
            role=lambda_role.id,
            policy="""{
                "Version": "2012-10-17",
                "Statement": [{
                    "Effect": "Allow",
                    "Action": [
                        "logs:CreateLogGroup",
                        "logs:CreateLogStream",
                        "logs:PutLogEvents"
                    ],
                    "Resource": "arn:aws:logs:*:*:*"
                }]
            }"""
        )

        self.lambda_func = lambda_.Function(
            resource_name='cw-lambda-func',
            code=pulumi.AssetArchive(
                assets={ 
                    "main.py": pulumi.StringAsset(text="""
def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/html"
        },
        "isBase64Encoded": False,
        "body": "Hello from lambda...!!!"
    }
                    """)
                }
            ),
            handler='main.lambda_handler',
            runtime='python3.9',
            role=lambda_role.arn,
            opts=pulumi.ResourceOptions(parent=parent)
        )

        awsx.lb.TargetGroupAttachment(
            resource_name='cw-tg-attachment',
            target_group=self.lb.default_target_group,
            lambda_=self.lambda_func
        )

        pulumi.export(f'{self.lb._type}:arn', self.lb.load_balancer.arn)
        pulumi.export(f'{self.lambda_func._type}:arn', self.lambda_func.arn)