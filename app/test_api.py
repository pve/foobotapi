# for use with pytest
import os, requests, json, datetime
from settings import *
from main import *

def test_env ():
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

def test_put ():
    data = {
    "status": ":thumbsup:",
	"source": "test_api",
	"epoch": 1413917402
    }
    response = POSTRequestSync(isurl, headers=isheaders, data=data)
    assert True #response.ok
#http://docs.initialstateeventsapi.apiary.io/#reference/event-data/events-json

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
