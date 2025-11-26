# Serverless Foundation
Solution request: use AWS Lambda to run code withouth provisioning a server.

## Learn
In this solution, clients run synchronous calls on an AWS Lambda function.
![lambda](images/lambda-1.png)

Lambda, part of the serverless offerings on AWS, can be used to run code withouth provisioning or managing servers so that customers pay only the resources that they use.

A client synchronously invokes the lambda function, which means that the invokation waits for the function to process the event and return a response.

![lambda](images/lambda-2.png)

The Lambda function contains business logic code that processes the invokation. The code can be written in one of several supported programming languages.

Lambda uses compute power only when a function is invoked.

When the function code run is completed, a response is returned to the client.

![lambda](images/lambda-3.png)

Functions can also be invoked asynchronously, which means that users don't need to wait for a response from the function code.

## Practice
Concept:
In this practice lab, you will:
- Use Python to create an AWS Lambda function.
- Deploy the Lambda function.
- Test the Lambda function.

![lambda](images/lambda-4.png)

Concept: 
AWS Lambda runs your code only when needed, and it scale automatically from a few request per day to thousands per second. Using Lambda, you can run code for virtually any type of application or backend service, all with no administration.

1. On the top navigation bar, review the Region selector to ensure that the Region is set to N. Virginia (us-east-1).
2. In the Services search box, type: lambda

3. In the search results, under Services, click Lambda.

![tuto](images/tuto-1.png)

Concept: 
A Lambda function consists of code and any associated dependencies. A Lambda function also has configuration information associated with it.

4. In the Functions section, click Create function.

- You can safely ignore any Lambda functions that are already displayed in the section.

![tuto](images/tuto-2.png)

Concept
Lambda runtimes allow functions in different languages to run un the same base execution environment. You configure your function to use a runtime that matcehs your programming language.

5. For Create function, choose Author from scratch.
6. For Function name, type: LabFunction

- You can give a Lambda function any name that you like. 

7. For Runtime, on the dropdown menu, choose Python 3.11

- The available Python version in the AWS Management Console might be different from what is displayed in the screenshot example.

8. Scroll down the bottom of the page.

![tuto](images/tuto-3.png)

Concept:
A Lambda function's execution role is an AWS Identity and Access Mangemtn (IAM) role that grants the function permission to access AWS services and resources. You provie this role when you create a function, and Lambda assuems the role when your function is invoked.

9. Click to expand Change default execution role.
10. For Execution role, choose Use an existing role.
11. For Existing role, choose lab_function_role.
12. Click Create Function.

![tuto](images/tuto-4.png)

All runtimes share a common prohgramming model that defines the interface between youe code and the runtime code.

Concept:
Using the code editor on the Lambda console, you can write, test,a nd view the execution results of your Lambda function code.

13. On the labFunction page of the AWS Lambda console, scroll down to the Code tab.

![tuto](images/tuto-5.png)

14. In the lambda_function code window, select (highlight) the code.
15. Delete the code.

![tuto](images/tuto-6.png)

Concept:
You tell the runtime which method to run by defining a handler in the function configuration, and the runtime runs that method. The runtime passes in objects to the handler that contains the invocation event and the context, such as the function name and request ID.

16. Paste the code from the sample_code.py file that you downloaded in an earlier step.

- You can open a .py file with IDLE (which comes with Python), Notepad++, or another text editor or IDE.
- Python code blocks are defined by their indentation, so maintain the indentation between copy and paste.

17. Click Deploy.

![tuto](images/tuto-7.png)

18. Review the code contents of the Lambda function.

- Reviewing and understanding the different parts of the Lambda function code is important for the next steps in the lab.

19. Review the parameters used in this Lambda function.

- Reviewing the parameters helps you with the later DIY section of this solution.

![tuto](images/tuto-8.png)

