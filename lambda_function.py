import boto3
from PIL import Image

s3 = boto3.client('s3')

DEST_BUCKET = 'thumbnail-output-prajwal'

def lambda_handler(event, context):

    source_bucket = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']

    download_path = '/tmp/input.jpg'
    upload_path = '/tmp/thumb.jpg'

    s3.download_file(source_bucket, object_key, download_path)

    image = Image.open(download_path)
    image.thumbnail((200, 200))
    image.save(upload_path)

    s3.upload_file(
        upload_path,
        DEST_BUCKET,
        f"thumb-{object_key}"
    )

    return {
        "statusCode": 200,
        "body": "Thumbnail Created"
    }