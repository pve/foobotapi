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
# foobot to initial state  
  ans = json.loads(datain)
  z= zip(ans["sensors"], ans["datapoints"][0])
  data = dict(zip(ans["sensors"], ans["datapoints"][0]))
  # nu nog de timestamp
  return data
  
def transform2xively(datain):
# foobot to xively
  ans = json.loads(datain)
  sensors = ans["sensors"]
  dp = ans["datapoints"][0]
  res = [{"id": sensors[i], "current_value": dp[i]} for i in range(len(sensors))]
  return json.dumps({ "datastreams" : res})
  
if __name__ == "__main__":
  while True:
    try:  
      t0 = time.time()
      incoming = consumeGETRequestSync(fooboturl, fooheaders)
      t1 = time.time()
      outgoing = transformdata(incoming.text)
      response = POSTRequestSync(isurl, isheaders, outgoing)
      t2 = time.time()
      sampleinput1 = u'{"uuid":"2701466D278044A0","start":1490861042,"end":1490861042,"sensors":["pm","co2"],"units":["ugm3","ppm"],"datapoints":[[2,98]]}' #string, input to json.loads
      outx = transform2xively(sampleinput1)
      outx = transform2xively(incoming.text)
      responsex = requests.put(xivelyurl, headers = xivheaders, data=outx)
      t3 = time.time()
      logglypayloadstruct = { 
        "foobotelapsed" : t1 - t0,
        "foobotstatus" : incoming.status_code,
        "foobotmessage" : incoming.text[:50],
        "iselapsed" : t2 - t1,
        "isstatus" : response.status_code,
        "ismessage" : response.text[:50],
        "xielapse"  : t3 - t2,
        "xistatus" : responsex.status_code,
        "ximessage"  : responsex.text[:200]
      }
      logglypayload = json.dumps(logglypayloadstruct)
      response = POSTRequestSync(logglykey, headers = {}, data=logglypayload)
    except requests.exceptions.RequestException as e: 
      print(e)
    time.sleep(600)
