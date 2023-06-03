from rest_framework import serializers
import base64
import boto3
import environ
import uuid
from botocore.exceptions import NoCredentialsError

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, True)
)

s3_resource = boto3.resource('s3',
                             aws_access_key_id=env('AWS_ACCESS_KEY_ID'),
                             aws_secret_access_key=env(
                                 'AWS_SECRET_ACCESS_KEY'),
                             region_name=env('AWS_DEFAULT_REGION'))


def upload_base64_image_to_s3(base64_image, file_name):
    # Do it better with io.ByteIO
    # TODO: boto3 documentation: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/bucket/put_object.html
    try:
        image_data = base64.b64decode(base64_image)
        bucket = s3_resource.Bucket(env('AWS_STORAGE_BUCKET_NAME'))
        bucket.put_object(
            Body=image_data, Key=f'Image/{file_name}', ACL='bucket-owner-full-control')
        return True
    except NoCredentialsError:
        print("Credential Error")
        return False
    except:
        print("Some other Error")
        return False


def generate_image_file_name():
    fileName = str(uuid.uuid4())[:12]
    return f'{fileName}.jpg'


def generate_image_url(file_name):
    return f"https://{env('AWS_STORAGE_BUCKET_NAME')}.s3.{env('AWS_DEFAULT_REGION')}.amazonaws.com/Image/{file_name}"


class ChoiceField(serializers.ChoiceField):
    # Explain choice field customization bug:
    # https://github.com/encode/django-rest-framework/discussions/8586
    def to_representation(self, obj):
        if obj == '' and self.allow_blank:
            return obj
        return self._choices[obj]

    def to_internal_value(self, data):
        # support inserts with value
        if data == '' and self.allow_blank:
            return ''

        try:
            return self.choice_strings_to_values[str(data)]
        except KeyError:
            self.fail('invalid_choice', input=data)
