import boto3
import botocore.config
import json

Model_Name = "meta.llama2-13b-chat-v1"

def generate_blog(blog_topic : str) -> str:
    prompt=f"""<s>[INST]Write a 20 words blog on the topic {blogtopic}[/INST]
    """

    body = {
        "promt": prompt,
        "max_gen_len": 512,
        "temperature": 0.5,
        "top_p": 0.9
    }

    bedrock = boto3.client("bedrock-runtime", region_name = "us-east-1",
                           config = botocore.config.Config(read_timeout = 300, retries = {"max_attemps":3})
                          )
    response = bedrock.invoke_model(modelId = Model_Name , body = json.dumps(body))
    response_content = response.get("body").read()
    print(response_content)

def lambda_handler(event,context):

    event = json.loads(event)
    blog_topic = event["blog_topic"]

    blog = generate_blog(blog_topic= blog_topic)

    return {
        "statusCode": 200,
        "body": json.dumps(blog)
    }
