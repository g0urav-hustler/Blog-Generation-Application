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

    try:
        bedrock=boto3.client("bedrock-runtime",region_name="us-east-1",
                             config=botocore.config.Config(read_timeout=300,retries={'max_attempts':3}))
        response=bedrock.invoke_model(body=json.dumps(body),modelId="meta.llama2-13b-chat-v1")

        response_content=response.get('body').read()
        response_data=json.loads(response_content)
        blog_details=response_data['generation']
        return blog_details
    except Exception as e:
        print(f"Error generating the blog:{e}")
        return ""

def lambda_handler(event,context):

    event = json.loads(event)
    blog_topic = event["blog_topic"]


    blog_topic = event["blog_topic"]
    
    generated_blog = generate_blog(blog_topic)
    
    
    return {
        'statusCode': 200,
        'body': json.dumps(generated_blog)
    }
