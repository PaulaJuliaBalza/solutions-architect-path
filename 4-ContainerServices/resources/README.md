# Learn
## Containers on AWS
With traditional software deployment you will have hardware or infrastructure that runs an OS. And on top of that you will run multiple app like Python, Node.js or Ruby. These app require specific libraries and dependencies to run properly. And that can cause difficult installations or app version conflicts that make scaling your app challenging.

Software deployment usiing containers provides a standard way to package your app's code, libraries and dependencies into a single object. Here you have infrastructure and an OS as well as a containr engine, like Docker that share the resource of the underlying OS with your application and create container packages that include the libraries and dependencies needed for your app to run. This enables you to move your applications across differents platforms with these.
This make containers lightwight, portable, and scalable wich makes containrs suitable for use cases like microservices apps, batch jobs, and migrating applications to the cloud. 

AWS Container services offers the broadest choice of services to run your containers.
You can choose AWS Fargate if you want serverless compute for containers, or Amazon EC2 if you need control over the installation, configuration and management of your compute environment.
You can also choose which container orchestrator to use, either Amazon Elastic Container Service ECS, or Amazon Elastic Kubernetes Service EKS.
AWS container services are deeply integrated with AWS by design. This allows your container apps to leverage the breadth and depth of the AWS Cloud, providing security and elasticity for your applications.

Container Management on AWS
Registry: secure place to store and manage your container images like Amazon ECR.
Orchestration: helps you manage when and where your containers run, as well as the flexible compute engines that power your containers with ECS, EKS and the Red Hat OpenShift service for AWS.
Compute: AWS can hepl manage your containers and their deployments for you, so you dont have to worry about the underlying infrastructure with AWS Fargate or AWS App Runner. Or you can choose to control your own virtual infrastructure with EC2 instances.

## Amazon Elastic Container Services
Is a fully managed, highly scalable and high performance Container orchestrations service, you can use it to run, stop manage and scale containerized apps across AZs without the complexity of managing control plane or nodes.
For more control you can run your containr workloads on EC2 instances. Or use AWS Fargate that is a serverless service.
Amazon ECS Anywhere Enables you to run apps in both the cloud and on premise.
You can use Amazon ECS when you require low latencies to on premise.