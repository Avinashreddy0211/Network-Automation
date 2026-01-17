Project Title- **VMware Avi Mock API -Python Automation Framework**



This project was built on a Python automation framework to interact with the mock VMware Avi Load Balancer API.



**Load Balancer Concepts:**



**Virtual Service**- A Virtual Service represents the frontend listener of a load balancer. It accepts client traffic and forwards it to backend servers.



**Pool and Pool Members**- A Pool is a group of backend servers. Pool members are the individual server IPs receiving traffic.





**Service Engine**- Service Engines handle the actual data-plane traffic. The avi Controller manages configuration while SEs process requests.



**Tenant**- Tenants provide logical isolation. Each tenant can have its own Virtual Services, Pools and Service Engines.



**API and Authentication:**

The framework interacts with a REST API using

GET  -> Fetch resources

PUT  -> Update resources



Authentication flow:

1.User registration

2.Login using Basic Authentication

3.Receive Bearer Token

4.Use token in Authorization header for all API calls

Each Virtual Service is accessed using its UUID as required by the API.



**Framework Design:**

YAML files are used to store

1.API base URL

2.User credentials

3.Target Virtual Service name

4.Testcase definitions

Python modules are separated based on functionality:

1.Authentication

2.API communication

3.Pre-fetch

4.Validation

5.Task execution



**Automation Workflow:**

For each testcase, the framework performs:



1.Pre-Fetch- Fetches tenants, virtual services, and service engines.

2.Pre-Validation- Finds the target Virtual Service by name and verify it enable or not.

3.Task- Sends a PUT request to disable the Virtual Service.

4.Post-Validation- Confirms the Virtual Service is now disabled.



Here is the Project Structure:

avi\_test\_framework/

config/        -> YAML configuration files

framework/     -> Modular Python code

main.py        -> Framework entry point

requirements.txt -> Python dependencies

README.md      -> Project documentation



Mock API URL- https://semantic-brandea-banao-dc049ed0.koyeb.app



How to Run these:

1. Install dependencies
2. pip install -r requirements.txt
3. Run the framework
4. python main.py
