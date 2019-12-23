import os, requests, json, datetime

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

def transform2adafruit(datain):
# foobot to adafruit
  ans = json.loads(datain)
  sensors = ans["sensors"]
  dp = ans["datapoints"][0]
  res = [{"key": sensors[i], "value": dp[i+1]} for i in range(len(sensors))]
  return json.dumps({ "feeds" : res})

#transform2adafruit(sampleadafruitin)
