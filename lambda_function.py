import json
import boto3

Model_Name = "meta.llama2-13b-chat-v1"

def generate_blog(blog_topic : str) -> str:
    
    prompt = f"write a 100 word blog on {blog_topic} and start with the word {blog_topic}"
    
    body = json.dumps({
        "prompt": prompt,
        "max_gen_len": 512,
        "temperature": 0.5,
        "top_p": 0.9
    })
    
    
    try:
        bedrock_runtime = boto3.client(
                service_name='bedrock-runtime',
                region_name='us-east-1'
            )
        
        response=bedrock_runtime.invoke_model(body=body,modelId="meta.llama2-13b-chat-v1")
        
        response_content=response.get('body').read()
        response_data=json.loads(response_content)
        
        blog_details=response_data['generation']
        return blog_details
    except Exception as e:
        print(f"Error generating the blog:{e}")
        return ""
    
    
    
def lambda_handler(event, context):
    
    # extract the blog topic
    blog_topic = event["blog_topic"]
    
    # get generated blog
    generated_blog = generate_blog(blog_topic)

    return {
        'statusCode': 200,
        'generated_blog': generated_blog
    }
