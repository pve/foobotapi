import os, requests, json, datetime

def transformdata(datain):
# foobot to initial state
  ans = json.loads(datain)
  z= zip(ans["sensors"], ans["datapoints"][0])
  data = dict(zip(ans["sensors"], ans["datapoints"][0]))
  # nu nog de timestamp
  return data

def transform2adafruit(datain):
# foobot to adafruit
  ans = json.loads(datain)
  sensors = ans["sensors"]
  dp = ans["datapoints"][0]
  res = [{"key": sensors[i], "value": dp[i]} for i in range(min(len(sensors),5))]
  # min because of adafruit limits
#  return json.dumps({ "feeds" : res})
# todo: time field is special.
  return { "feeds" : res}
