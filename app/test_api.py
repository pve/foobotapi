# for use with pytest
import os, requests, json, datetime
from settings import *
from main import *
# see credsfromfile.py for local testing settings.

def test_secrets ():
    assert fooboturl.startswith("https://")
    assert foobotkey != 'novalidkey'
    assert isurl.startswith("https://")
    assert isbucketkey != 'novalidkey'
    assert dataset_id != 'novalidkey'

def test_get ():
    response = consumeGETRequestSync(fooboturl, headers=fooheaders)
    print("code:"+ str(response.status_code))
    print ("******************")
    print ("headers:"+ str(response.headers))
    print ("******************")
    print ("content:"+ str(response.text))
    assert response.ok
    assert "datapoints" in response.text
    assert "sensors" in response.text

def test_put (): # initialstate
    data = {
    "status": ":thumbsup:",
	"source": "test_api",
	"epoch": 1413917402
    }
    response = POSTRequestSync(isurl, headers=isheaders, data=data)
    assert True #response.ok

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
