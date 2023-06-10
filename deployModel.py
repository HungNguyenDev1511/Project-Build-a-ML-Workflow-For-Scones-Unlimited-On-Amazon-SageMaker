import json
import base64
import boto3

# Fill this in with the name of your deployed model
ENDPOINT = "image-classification-2023-06-10-14-17-45-831"


runtime_client = boto3.Session().client('sagemaker-runtime')
def lambda_handler(event, context):

    
    # Decode the image data
    image = base64.b64decode(event['image_data'])

    response = runtime_client.invoke_endpoint(EndpointName=ENDPOINT,Body=image,ContentType='image/png')
    # Instantiate a Predictor
    #predictor.serializer = IdentitySerializer("image/png")

    # For this model the IdentitySerializer needs to be "image/png"
    #predictor.serializer = IdentitySerializer("image/png")

    # Make a prediction:
    inferences = json.loads(response['Body'].read().decode())
    event['inferences'] = inferences 
    # We return the data back to the Step Function    
    #event["inferences"] = inferences.decode('utf-8')
    event['inferences'] = inferences 
    return {
        'statusCode': 200,
        'body': event
    }