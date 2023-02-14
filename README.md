#1 # Lab 3
 2 [Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repo and clone it to your machine to get started!
 3
 4 ## Team Members
 5 - Kameran Mody
 6 - Greg Sarandi
 7
 8 ## Lab Question Answers
 9
10 Answer for Question 1:
11 Question 1: Why are RESTful APIs scalable?
12 Restful APIs are scalable because the server does not
13 store past client information so there is no server load. In addition,
14 REST optimizes client-server interactions so even when scaled up,
15 it is still very operational.  
16
17 Question 2: According to the definition of “resources” provided in the AWS article above,
18 What are the resources the mail server is providing to clients?
19 The resources the mail server is providing to clients is the access to the mail coming in
20 that the API will search through and provide functions to.
21
22
23 Question 3: What is one common REST Method not used in our mail server? How could
24 we extend our mail server to use this method?
25 PUT is a common Rest method not used in our mail server. We could extend our mail server
26 to use this method by adding a new put function that edits existing emails in the list
27 and edits their content that can be updated.
28
29
30
Question 4: Why are API keys used for many RESTful APIs? What purpose do they
32 serve? Make sure to cite any online resources you use to answer this question!
33 API keys are used for so many Restful APIs because they provide added protection and easy access to projects
34 They provide authentication for entering the project and identify the project
35 that is making a call to the API.
36 source: https://cloud.google.com/endpoints/docs/openapi/when-why-api-key
37 ...
38
