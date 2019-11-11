import requests
import json, os, time, datetime
from google.cloud import bigquery

fooboturl = os.getenv('fooboturl','novalidkey')
foobotkey = os.getenv('foobotkey','novalidkey')
isurl = os.getenv('isurl','novalidkey')
isaccesskey = os.getenv('isaccesskey','novalidkey')
isbucketkey = os.getenv('isbucketkey','novalidkey')
logglykey = os.getenv('logglykey','novalidkey')

client = bigquery.Client()
#table_id = "imp-iot-project.demo.fredwilma"

dataset_id = 'foobot'  # replace with your dataset ID
#For this sample, the table must already exist and have a defined schema
table_id = 'sensordata'  # replace with your table ID
table_ref = client.dataset(dataset_id).table(table_id)
table = client.get_table(table_ref)  # API request

# print fooboturl, foobotkey, isurl

fooheaders = {"Accept": "application/json", "X-API-KEY-TOKEN": foobotkey }

isheaders = {"Accept": "application/json",
		"X-IS-AccessKey": isaccesskey,
		"X-IS-BucketKey": isbucketkey
}

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

def oneshot(event, context):
   try:
	   t0 = time.time()
	   incoming = consumeGETRequestSync(fooboturl, fooheaders) # velden mogelijk in willekeurige volgord
	   t1 = time.time()
	   outgoing = transformdata(incoming.text)
	   response = POSTRequestSync(isurl, isheaders, outgoing)
	   t2 = time.time()
	   sampleinput1 = u'{"uuid":"2701466D278044A0","start":1490861042,"end":1490861042,"sensors":["pm","co2"],"units":["ugm3","ppm"],"datapoints":[[2,98]]}' #string, input to json.loads
	   bqin = json.loads(incoming.text)["datapoints"][0]
	   bqin[0] = datetime.datetime.utcfromtimestamp(bqin[0]).strftime('%Y-%m-%d %H:%M:%S')
	   rows_to_insert = [tuple(bqin)]
	   print(rows_to_insert)
	   errors = client.insert_rows(table, rows_to_insert)  # API request
	   print(errors)
	   t3 = time.time()
	   logglypayloadstruct = {
	   "foobotelapsed" : t1 - t0,
	   "foobotstatus" : incoming.status_code,
	   "foobotmessage" : incoming.text[:50],
	   "iselapsed" : t2 - t1,
	   "isstatus" : response.status_code,
	   "ismessage" : response.text[:50],
	   "bqlapse"  : t3 - t2,
	   }
	   logglypayload = json.dumps(logglypayloadstruct)
	   response = POSTRequestSync(logglykey, headers = {}, data=logglypayload)
   except requests.exceptions.RequestException as e:
      print(e)
# we hebben meer exceptions

if __name__ == "__main__":
   oneshot('text', 'contex')
