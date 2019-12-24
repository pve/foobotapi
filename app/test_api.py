# for use with pytest
import os, requests, json, datetime
from settings import *
from main import *
# see credsfromfile.py for local testing settings.

def test_secrets ():
    assert fooboturl.startswith("https://")
    assert foobotkey != 'novalidkey'
    assert dataset_id != 'novalidkey'

def test_get ():
    response = consumeGETRequestSync(fooboturl, headers=fooheaders)
    print("code:"+ str(response.status_code))
    print ("headers:"+ str(response.headers))
    print ("content:"+ str(response.text))
    assert response.ok
    assert "datapoints" in response.text
    assert "sensors" in response.text

def test_af (): # adafruit
    data = { "feeds": [ { "key": "a", "value": "42" }, { "key": "b", "value": "8" }]}
    response = requests.post(afurl + "/" + afuser + "/groups/test/data", headers=afheaders, json=data)
    assert response.ok

def test_loggly():
    payload = {
    "status": ":thumbsup:",
	"source": "foobot_test_api",
	"number" : 3.141592653589793,
	"inumber" : 42
    }
    response = POSTRequestSync(logglykey, headers = {}, data=json.dumps(payload))
    assert response.ok

def test_date():
    assert datetime.datetime.utcfromtimestamp(1413917402).isoformat()=='2014-10-21T18:50:02'

'{:06.2f}'.format(3.141592653589793)
# http://api.foobot.io/v2/device/2701466D278044A0/datapoint/0/last/0/
#curl -X GET --header "Accept: text/csv;charset=UTF-8" --header "X-API-KEY-TOKEN: eyJhbGciOiJIUzI1NiJ9.eyJncmFudGVlIjoicHZlaWprQGdtYWlsLmNvbSIsImlhdCI6MTQ4ODMxOTUyMCwidmFsaWRpdHkiOi0xLCJqdGkiOiIwNTlmODMwMC01ODM3LTQwOTMtOWFjNi1lNmM4ZGJlNTlmYTUiLCJwZXJtaXNzaW9ucyI6WyJ1c2VyOnJlYWQiLCJkZXZpY2U6cmVhZCJdLCJxdW90YSI6MjAwLCJyYXRlTGltaXQiOjV9.auPttWcJa-mE8Ck8-52JOrJawo3Jf6kHIhq4lzRpq-g" "http://api.foobot.io/v2/device/2701466D278044A0/datapoint/0/last/0/"
#curl -X GET --header "X-API-KEY-TOKEN: eyJhbGciOiJIUzI1NiJ9.eyJncmFudGVlIjoicHZlaWprQGdtYWlsLmNvbSIsImlhdCI6MTQ4ODMxOTUyMCwidmFsaWRpdHkiOi0xLCJqdGkiOiIwNTlmODMwMC01ODM3LTQwOTMtOWFjNi1lNmM4ZGJlNTlmYTUiLCJwZXJtaXNzaW9ucyI6WyJ1c2VyOnJlYWQiLCJkZXZpY2U6cmVhZCJdLCJxdW90YSI6MjAwLCJyYXRlTGltaXQiOjV9.auPttWcJa-mE8Ck8-52JOrJawo3Jf6kHIhq4lzRpq-g" "http://api.foobot.io/v2/device/2701466D278044A0/datapoint/0/last/0/"
# sample answer : {"uuid":"2701466D278044A0","start":1571513969,"end":1571513969,"sensors":["time","pm","tmp","hum","co2","voc","allpollu"],"units":["s","ugm3","C","pc","ppm","ppb","%"],"datapoints":[[1571513969,12.360016,17.733,63.555,1309,362,42.52668]]}
