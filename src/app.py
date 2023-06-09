from PIL import Image
import pytesseract
import boto3

client_s3 = boto3.resource('s3')

def readS3(bucket, key):
    print(bucket, key)
    object = client_s3.Object(bucket, key)
    response = object.get()
    file_stream = response['Body']
    img = Image.open(file_stream)
    text = pytesseract.image_to_string(img)
    print(text)


def lambda_handler(event: dict, context: dict) -> None:
    print('-----------------start-----------------------')
    readS3("ccm-s3-email-receiving-cloudhq-dev","test.png")
    print('-------------------end---------------------')

