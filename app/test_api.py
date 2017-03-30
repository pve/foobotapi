# for use with pytest
import os, requests
from settings import *
from foobotapi import transformdata

def test_env ():
    assert fooboturl.startswith("https://")
    assert foobotkey != 'novalidkey'
    assert isurl.startswith("https://")
    assert isbucketkey != 'novalidkey'
    
def test_get ():
    response = requests.get(fooboturl, headers=fooheaders)
    print "code:"+ str(response.status_code)
    print "******************"
    print "headers:"+ str(response.headers)
    print "******************"
    print "content:"+ str(response.text)
    assert response.ok
    assert "datapoints" in response.text
    assert "sensors" in response.text
    
def test_transform ():
    data = {
    "status": ":thumbsup:",
	"source": "test_api"
    }
    x = u'{"uuid":"2701466D278044A0","start":1490861042,"end":1490861042,"sensors":["time","pm","tmp","hum","co2","voc","allpollu"],"units":["s","ugm3","C","pc","ppm","ppb","%"],"datapoints":[[1490861042,6.8000183,18.255,54.493,1062,293,30.800018]]}'
    y = {u'tmp': 18.255, u'co2': 1062, u'voc': 293, u'hum': 54.493, u'allpollu': 30.800018, u'time': 1490861042, u'pm': 6.8000183}
    r = transformdata(x)
    assert x == r

def test_put ():
    assert True
