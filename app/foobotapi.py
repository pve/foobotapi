import requests
import json, os, time
from settings import *

def POSTRequestSync(url, headers, data):
  response = requests.post(url, headers=headers, data=data)
  return response

def consumeGETRequestSync(url, headers):
  response = requests.get(url, headers=headers)
  return(response.text)
  
def transformdata(datain):
  ans = json.loads(datain)
  z= zip(ans["sensors"], ans["datapoints"][0])
  data = dict(zip(ans["sensors"], ans["datapoints"][0]))
  # nu nog de timestamp
  return data
  
while True:
  incoming = consumeGETRequestSync(fooboturl, fooheaders)
  outgoing = transformdata(incoming)
  response = POSTRequestSync(isurl, isheaders, outgoing)
  print "IS code:"+ str(response.status_code)
  # if any of this fails: report to loggly
  time.sleep(600)