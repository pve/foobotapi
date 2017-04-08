import requests
import json, os, time
from settings import *

def POSTRequestSync(url, headers, data):
  response = requests.post(url, headers=headers, data=data)
  return response

def consumeGETRequestSync(url, headers):
  response = requests.get(url, headers=headers)
  return(response)
  
def transformdata(datain):
  ans = json.loads(datain)
  z= zip(ans["sensors"], ans["datapoints"][0])
  data = dict(zip(ans["sensors"], ans["datapoints"][0]))
  # nu nog de timestamp
  return data
  
if __name__ == "__main__":
  while True:
    t0 = time.time()
    incoming = consumeGETRequestSync(fooboturl, fooheaders)
    t1 = time.time()
    outgoing = transformdata(incoming.text)
    response = POSTRequestSync(isurl, isheaders, outgoing)
    t2 = time.time()
    logglypayloadstring = { 
      "foobotelapsed" : t1 - t0,
      "foobotstatus" : incoming.status_code,
      "iselapsed" : t2 - t1,
      "isstatus" : response.status_code,
      "ismessage" : response.text[:50],
      "foobotmessage" : incoming.text[:50]}
    logglypayload = json.dumps(logglypayloadstring)
    response = POSTRequestSync(logglykey, headers = {}, data=logglypayload)
    time.sleep(600)
