import os, requests, json, datetime

def transformdata(datain):
# foobot to initial state, no longer used
  ans = json.loads(datain)
  z= zip(ans["sensors"], ans["datapoints"][0])
  data = dict(zip(ans["sensors"], ans["datapoints"][0]))
  # todo timestamp
  return data

def transform2adafruit(datain):
# foobot to adafruit, not handling the data formats yet
  ans = json.loads(datain)
  sensors = ans["sensors"]
  dp = ans["datapoints"][0]
  res = [{"key": sensors[i], "value": dp[i]} for i in range(min(len(sensors),6))]
  # min because of adafruit limits
#  return json.dumps({ "feeds" : res})
# todo: time field is special.
  return { "feeds" : res}
