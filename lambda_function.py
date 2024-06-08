import boto3
import botocore.config
import json

def generate_blog(blog_topic : str) -> str:
    prompt=f"""<s>[INST]Write a 200 words blog on the topic {blogtopic}[/INST]
    """

    body = {
        "promt": prompt,
        "max_gen_len": 512,
        "temperature": 0.5,
        "top_p": 0.9
    }


def lambda_handler(event,context):

    event = json.loads(event)
    blog_topic = event["blog_topic"]

    blog = generate_blog(blog_topic= blog_topic)

    return {
        "statusCode": 200,
        "body": json.dumps(blog)
    }
