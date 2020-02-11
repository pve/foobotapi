import requests
import json, os, time, datetime, logging
from settings import *
from transform import *
from google.cloud import bigquery

client = bigquery.Client()
# dataset_id retrieved through settings
# For this sample, the table must already exist and have a defined schema
table_ref = client.dataset(dataset_id).table(table_id)
table = client.get_table(table_ref)  # API request

def POSTRequestSync(url, headers, data):
  response = requests.post(url, headers=headers, data=data)
  if response.status_code != requests.codes.ok:
	  logging.error(response.text)
  return response

def consumeGETRequestSync(url, headers):
  response = requests.get(url, headers=headers)
  if response.status_code != requests.codes.ok:
	  logging.error(response.text)
  # check if we really get an answer, logging.error instead
  return(response)

def oneshot(event, context):
   try:
	   t0 = time.time()
	   incoming = consumeGETRequestSync(fooboturl, fooheaders) # velden mogelijk in willekeurige volgord
	   t1 = time.time()
	   outgoing = transform2adafruit(incoming.text)
#	   print(outgoing)
	   response = POSTRequestSync(afurl + "/" + afuser + "/groups/foobot/data",
	   		headers=afheaders, data=json.dumps(outgoing))
#	   print(response.text)
	   t2 = time.time()
	   bqin = json.loads(incoming.text)["datapoints"][0]
	   bqin[0] = datetime.datetime.utcfromtimestamp(bqin[0]).strftime('%Y-%m-%d %H:%M:%S')
	   rows_to_insert = [tuple(bqin)]
#	   print("time, pm, tmp: " + str(rows_to_insert))
	   errors = client.insert_rows(table, rows_to_insert)  # API request
	   if errors:
	   	  logging.error(errors)
	   t3 = time.time()
	   logglypayloadstruct = {
	   "foobotelapsed" : t1 - t0,
	   "foobotstatus" : incoming.status_code,
	   "foobotmessage" : incoming.text[:50],
	   "afelapsed" : t2 - t1,
	   "afstatus" : response.status_code,
	   "afmessage" : response.text[:50],
	   "bqlapse"  : t3 - t2,
	   }
	   logglypayload = json.dumps(logglypayloadstruct)
	   logging.info(logglypayload)
	   response = POSTRequestSync(logglykey, headers = {}, data=logglypayload)
   except requests.exceptions.RequestException as e:
      print(e)
# there are more types of exceptions.
# add some code to run this
if __name__ == '__main__':
	oneshot("", "")
