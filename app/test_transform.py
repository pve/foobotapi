# for use with pytest
import os, requests, json, datetime
from settings import *
from foobotapi import *

def test_transform ():
    x = u'{"uuid":"2701466D278044A0","start":1490861042,"end":1490861042,"sensors":["time","pm","tmp","hum","co2","voc","allpollu"],"units":["s","ugm3","C","pc","ppm","ppb","%"],"datapoints":[[1490861042,6.8000183,18.255,54.493,1062,293,30.800018]]}'
    y = {u'tmp': 18.255, u'co2': 1062, u'voc': 293, u'hum': 54.493, u'allpollu': 30.800018, u'time': 1490861042, u'pm': 6.8000183}
    r = transformdata(x)
    assert y == r

sampleinput1 = u'{"uuid":"2701466D278044A0","start":1490861042,"end":1490861042,"sensors":["pm","co2"],"units":["ugm3","ppm"],"datapoints":[[2,100]]}' #string, input to json.loads
payload2xively = {'datastreams': [{'current_value': 2, 'id': 'pm'}, {'current_value': 100, 'id': 'co2'}]}  #pyhon object

payload2xivelystring = '{"datastreams": [{"current_value": 2, "id": "pm"}, {"current_value": 100, "id": "co2"}]}' #string, result of json.dumps

def test_transform2xively ():
    x = sampleinput1
    r = transform2xively(x)
    assert payload2xivelystring == r

