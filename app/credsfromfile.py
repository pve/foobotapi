from google.cloud import storage
import json
# export GOOGLE_APPLICATION_CREDENTIALS="IMP iot project-272ba9e6a170private.json"
# permissions...storage.buckets.get access

def download_blob(bucket_name, source_blob_name):
    """Downloads a blob from the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(source_blob_name)

    s = blob.download_as_string()
    return(s)

def clientsecrets(str):
    """Gets the secrets from a string"""
    try:
        secrets = json.loads(str)
    except json.decoder.JSONDecodeError as e:
        print("Json error ")
        print(e)
        secrets = None
    return secrets

def getsecrets(bucket_name, source_blob_name):
    """Get the goodies"""
    s = download_blob(bucket_name, source_blob_name)
    res = clientsecrets(s)
    return res

# todo error message testing + testcases
