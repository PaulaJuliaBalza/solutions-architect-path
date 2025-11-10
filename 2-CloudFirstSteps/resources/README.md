# Resources
## 1-Amazon EC2 Overview
## 2-Amazon EC2 Storage Networking
## 3-Amazon EBS Overview
## 4-Amazon EBS Features
## 5-Amazon EBS Benefits
## 6-Amazon EBS Volume Types
## 7-DNS Overview
DNS (Domain Name System)
Computers on the internet comunicate with one another by using numbers known as IP addresses. When you visit a website you don't have to remember a long number.
You can enter a domain name like www.example.com, that is easier to remember.

A DNS service such as Amazon Route 53 is a globally distributed service that transalates human readable names like www.example.com into numeric IP addresses that computers use to comunicate to one another.

The internet's DNS (system) works much like a phone book by managing the mapping between names and numbers,
DNS servers translates requiests for names into IP addresses, controlling which server an end user will reach when they type a domain name into their web browser. These requests are called queries.

DNS query process
First, the host sends a DNS request to the local DNS server.
Second, the DNS server which is preconfigured with the list of root name servers, randomly selects one root name server for the A record www.example.com. An A record maps a domain name to an IP address of the computer that hosts the domain.
Third, the root name server responds with a list of authoritative name servers for the .com zone, along with a list of the IP addresses.
Fourth, the DNS server randomly selects one of the autoritative name servers returned in step three and sends another DNS query for the A record example.com to the top level domain server. 
Fifth, the top level domain name server responds with a list of name servers that are authoritative for the domain example.com.
Sixth, the DNS server randomply selects one of the authoritative name serers returned in step five and sends another DNS query for the A record example.com.
Seventh, since the name server receiving the query in step six is authoritative for the domain example.com, the name server responds to the DNS server with the IPaddress value of the A record for example.com.
And for the final step, the DNS server sends the DNS responde with the IP address back to the host, which enables the host computer to connect to www.example.com.

## 8-AWS Support, Resources and Documentation Overview
AWS Support Overview
AWS provides multiples tiers of support to help customers succeed with their AWS Implementations.
The support plans include Basic, which is free and automatic for all customers, Developer, BUsiness, Enterprise On Ramp, Enterprise.

The Basic plan offers customer service for account and billing questions, support forums, service health checks, and documentation. 

The other paid plans provide all of these options plus unlimited technical support cases with monthly prices ans no long term contracts.

Technical resources and documentation overview
Numerous other AWS technical resources are available across different environments and repositories.
* AWS documentation website to find resources as User Guides, whitepapers, tutorials, code samples, software development kits and references.
* AWS Prescriptive Guidance provides time-tested strategies, guides and patterns to help accelerate your cloud migration, modernization and optimization projects. 
These resources were developed by AWS technology experts and the global community of AWS partners.
* AWS rePost provides serveral types of knowledge resources, such as knowledge center articles, community articles and questions and answers. 
* The AWS Trust and Safety Center provides information on how to report activity or content on AWS that you  suspect is abusive, how to address and abuse notice that you receive from AWS Trust and Safety, AWS services that you can use to protect your applications, and nest practices for digital messaging. 

AWS Trusted Advisor
* Monitors AWS infrastructure services, identifies customer configurations compares them to know best practices and notifies customers about opportunities to save money, improve system performance, or close security gaps.
* Evaluates AWS accounts by using checks across 5 key categories, Cost optimization, Security, Fault Tolerance, Performance and Service Limits.
* Basic and Development support customers get access to 6 security checks and 50 service limits checks, while Business support and Enterprise support customers have access to all 115 Trusted Advisor checks.

