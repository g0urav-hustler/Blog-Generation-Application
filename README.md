---

title: Document Assistant

emoji: 📃

colorFrom: blue

colorTo: yellow

sdk: streamlit

sdk_version: 1.35.0

app_file: app.py

pinned: false

license: mit

---

  

## Blog Generation App

  
**Website Link -** https://huggingface.co/spaces/g0urav-hustler/Blog-Generation-App
**RestApi Link -**   https://3obv4jibod.execute-api.us-east-1.amazonaws.com/first_stage/generate-blog

This applications help to generate blog on your desired topic using AI.


## How to use App

#### Web UI
![Web image](https://github.com/g0urav-hustler/Blog-Generation-Application/blob/main/readme_sources/photo_1.png)


#### Write the topic of blog 
##### Example1:
![Web image](https://github.com/g0urav-hustler/Blog-Generation-Application/blob/main/readme_sources/photo_2.png)

##### Example2:
![Web image](https://github.com/g0urav-hustler/Blog-Generation-Application/blob/main/readme_sources/photo_3.png)


## Technical Aspect

This application uses Aws Bedrock services that has variety of LLMs for different function.


### Aws Bedrock
Amazon Bedrock is a fully managed service that offers a choice of high-performing foundation models (FMs) from leading AI companies like AI21 Labs, Anthropic, Cohere, Meta, Mistral AI, Stability AI, and Amazon through a single API, along with a broad set of capabilities you need to build generative AI applications with security, privacy, and responsible AI. Using Amazon Bedrock, you can easily experiment with and evaluate top FMs for your use case, privately customize them with your data using techniques such as fine-tuning and Retrieval Augmented Generation (RAG), and build agents that execute tasks using your enterprise systems and data sources.

**For More Details** [Reference](https://aws.amazon.com/bedrock/#:~:text=Amazon%20Bedrock%20is%20a%20fully,build%20generative%20AI%20applications%20with)

### AWS Lambda Function
AWS Lambda is a serverless, event-driven compute service that lets you run code for virtually any type of application or backend service without provisioning or managing servers. You can trigger Lambda from over 200 AWS services and software as a service (SaaS) applications, and only pay for what you use.

**For More Details** [Reference](https://aws.amazon.com/lambda/#:~:text=AWS%20Lambda%20is%20a%20serverless,pay%20for%20what%20you%20use.)


### AWS Api Gateway
Amazon API Gateway is an AWS service for creating, publishing, maintaining, monitoring, and securing REST, HTTP, and WebSocket APIs at any scale. API developers can create APIs that access AWS or other web services, as well as data stored in the AWS Cloud As an API Gateway API developer, you can create APIs for use in your own client applications.
**For More Details** [Reference](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html#:~:text=Amazon%20API%20Gateway-,What%20is%20Amazon%20API%20Gateway%3F,stored%20in%20the%20AWS%20Cloud%20.)

### HuggingFace Spaces

Each Spaces environment is limited to 16GB RAM, 2 CPU cores and 50GB of (not persistent) disk space by default, which you can use free of charge. You can upgrade to better hardware, including a variety of GPU accelerators and persistent storage, for a [competitive price](https://huggingface.co/pricing#spaces). To request an upgrade, please click the _Settings_ button in your Space and select your preferred hardware environment.
**Deploy Streamlit app on huggingface -** [Reference](https://huggingface.co/docs/hub/en/spaces-overview)

