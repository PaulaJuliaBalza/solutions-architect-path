# FALTAN EXPLICAR DIAPOS
# Resources
## 1-Serverless computing
Removes the heavy lifting, you can focus on building product which scale and that are reliable.

Four key benefits of serverless
1. There is no more need to provision or maintain any servers.
2. You do not need to worry about scaling or capacity planning. AWS automatically scales with your usage.
3. Pay for value. You pay only for what you use and when you are using it.
4. Serverless provides built-in availability and fault tolerance.

AWS Serverless Platform
* Compute - AWS Lambda: it allows you to code withoth provisining or managing servers.
* Compute - Lambda@Edge: it allows you to run Lambda functions at AWS edge locations in response to Amazon CloudFront events.
* Compute - AWS Fargate: is a purpose-built serverless compute engine for containers. It scales and manages the infrastructure requied to run your containers.
* Storage - Amazon S3: provides secure, durable, highly scalable object storage.
* Storage - Amazon Elastic File System: provides simple, scalable elastic file storage. It is built to elastically scale on demand, growing and shrinking automatically as you add or remove files.
* Data stores - Amazon Dynamo DB: is a fast and flexible NoSQL database service for all applications that need consistent single-digit milisecond latency at any scale.
* Data stores - Amazon Aurora Serverless: is an on demans autoscaling configuration for Amazon Aurora, MySQL, and POstgreSQL compatible, where the DB will automatically start up, shut down, and scale capacity up or down based on your application's needs.
* API Proxy - Amazon API Gateway: is a fully managed service that maks it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale.
* App integration - Amazon SNS: is a fully managed publish and subscribe messaging service.
* App integration - Amazon SQS: is a fully managed message queuing service.
* App integration - AWS AppSync: simplifies application developmentr by letting you create a flexible GraphQL API to securely access, manipulate, and combine datafrom one or more data sources.
* App integration - Amazon EventBridge: is a serverless event bus service that makes it easy to access application data from a variety of sources and send it into your AWS environment.
* Analytics - Amazon Kinesis: is a platform for streaming data on AWS.
* Analytics - Amazon Athena: is an interactive query service that makes it easy to analyze data in Amazon S3 using standard SQL.
* Orchestration - AWS Step Functions: lets you coordinate multiple AWS services into serverless workflows, so you can build and update apps quickly.
* Orchestration -  Developer tooling: AWS and its partner ecosystem offer tools for continous integration and delivery, testing, deployments, monitoring and diagnostics SDKs, frameworks, and integrating development environment or IDE, plug ins.

AWS provides a set of fully managed services that you can use to build and run serverless applications. Using AWS and its serverless platform, it enables you to build modern applications with increased agility and lower total cost of ownership.

## 2-AWS Lambda Overview
AWS Lambda is a serverless compute service you can configure with a trigger. AWS Lambda then runs your code automaticallly in response to your trigger.
AWS Lambda manages all the underlying compute resources for you, all you need to do is supply the code. AWS Lambda takes care of everything required to run and scale your code with high availability.

This is how it works:
First, simply upload your code to AWS Lambda or write code in Lambda's code editor. The code you run on AWS Lambda is called a Lambda function.
Next, you can set up your code to trigger from other AWS services, HTTP endpoints, in app activity or run on a schedule.
Then AWS Lambda is ready to run your code only when invoked, using only the compute resoures needed. You just pay for the compute time you use.

Triggers
You can invoke Lambda functions directly or configure triggers to invoke Lambda functions in response to incoming HTTP requests or AWS services.
You can also configure Lambda to read from a queue or a stream and invoke a function or run on a schedule using EventBridge triggers.

Here are some examples:
* Amazon Simple Storage Service (S3): when there is a change in the Amazon S3 bucket content, sucah as when an object file is created, deleted or updated the lambda function is invoked.
* Amazon Simple Notification Service (SNS): when a message is published to an SNS topic that the lambda function subscibed to it, the lambda function is invoked.
* Amazon API Gateway: when the API is called, API Gateway invokes the Lambda function.
* Amazon DynamoDB: when a DynamoDB record is created or modified, the lambda function can be configured to trigger and run the code.
* Amazon Simple Queue service (SQS): you can use AWS Lambda to process messages in an SQS queue. Lambda pulls the queue and invokes your fucntion synchronously.

Benefits:
* You do not need to provision or manage any servers. All you need is to write the code, upload it to Lambda, and then Lambda automatically runs your code for you.
* Continous scaling, in response to each trigger, AWS Lambda automatically scales your application. Your code runs in parallel and processes each trigger individually, scaling precisely with the size of the workload.
* Subsecond metering, with AWS Lambda you pay only for wat you use. Pricing is based on the number of times your code is triggered, that is the number of requests and the duration, the time it takes to run your code. Billing is metered in increments of 1 milisecond. When your code isn't running, you do not pay anything.

With AWS Lambda, it makes it easy to build cost effective serverless applications that respond quickly to your customer needs.

## AWS Lambda invocation