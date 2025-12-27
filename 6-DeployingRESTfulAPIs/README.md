# Learn
Use Amazon API Gateway and and AWS Lambda function to create and deploy an API.

In this solution, Amazon API GW acts as the front door for applications to access data, bussiness logic, and functionality from backend services.

![learn](images/learn-1.png)

An application makes an HTTP request to access the backend.

API Gateway handles the request and all the tasks involved in accepting and processing the API call.

API Gateway invokes AWS Lambda, which processes the request and returns a response. API Gateway receives the response and returns it to the app.

With the ability to make synchronous calls from API Gateway to Lambda, users can create fully serverless apps and serverless microservices.

Using API Gateway, users can create multiple new endpoints and point them to different Lambda functions.

# Practice
In this practice Lab, you will:
- Create an Amazon API Gateway REST API.
- Deploy the REST API.
- Invoke an AWS Lambda function by using API Gateway proxy integration.

Concept 
AWS Lambda is a compute service that helps you run code without provisioning or managing servers. Lambda runs tour code only when needed, and it can scale automatically from a few requests per day to thousands per second. You pay only for the compute time that you use with no charge when your code is not running. Using AWS, you can run code for virtually any type of app or backend service, all with no administration.

1. In the top navigation bar search box, type:
lambda
			
2. In the search results, under Services, click Lambda.

Concept 
A Lambda function