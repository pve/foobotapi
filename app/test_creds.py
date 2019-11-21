from credsfromfile import *
from settings import *
# test if the required parameters are actually in the sample secrets file
#https://github.com/GoogleCloudPlatform/storage-file-transfer-json-python/blob/master/client_secrets.json
# split in unit test and integration test
def test_file():
    getit = download_blob("imp-iot-project.appspot.com", "file")
    assert getit == b"aap noot mies"

def test_decoder():
    assert clientsecrets(b'{"foo" : "one"}') == {'foo' : 'one'}

def test_getsecrets():
    res = getsecrets("imp-iot-project.appspot.com", "clientsecrets.json")
    assert 'dataset_id' in res
    assert res['dataset_id'] != 'novalidkey'

gcpexample = """
{
  "installed": {
    "client_id": "INSERT CLIENT ID HERE",
    "client_secret": "INSERT CLIENT SECRET HERE",
    "redirect_uris": [],
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://accounts.google.com/o/oauth2/token"
  }
}
"""
gcpjson = {'installed': {'client_id': 'INSERT CLIENT ID HERE', 'client_secret': 'INSERT CLIENT SECRET HERE', 'redirect_uris': [], 'auth_uri': 'https://accounts.google.com/o/oauth2/auth', 'token_uri': 'https://accounts.google.com/o/oauth2/token'}}
