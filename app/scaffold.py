
import json, os, time, datetime
# sample output from foobot api (already a dict, after json.loads)
samplefoobot = {"uuid":"2701466D278044A0","start":1571513969,"end":1571513969,"sensors":["time","pm","tmp","hum","co2","voc","allpollu"],"units":["s","ugm3","C","pc","ppm","ppb","%"],"datapoints":[[1571513969,12.360016,17.733,63.555,1309,362,42.52668]]}

tstdata = samplefoobot
transformed = dict(zip(tstdata["sensors"], tstdata["datapoints"][0]))
assert transformed == {'time': 1571513969, 'pm': 12.360016, 'tmp': 17.733, 'hum': 63.555, 'co2': 1309, 'voc': 362, 'allpollu': 42.52668}
bqin = tstdata["datapoints"][0]
bqin[0] = datetime.datetime.utcfromtimestamp(bqin[0]).strftime('%Y-%m-%d %H:%M:%S')

from google.cloud import bigquery
# requires GOOGLE_APPLICATION_CREDENTIALS or run from Google Cloud Shell
# export GOOGLE_APPLICATION_CREDENTIALS="/Users/peter/apps/foobotapi/app/IMP iot project-272ba9e6a170.json"
client = bigquery.Client()
#table_id = "imp-iot-project.demo.fredwilma"

dataset_id = 'demo'  # replace with your dataset ID
#For this sample, the table must already exist and have a defined schema
table_id = 'foobotx'  # replace with your table ID
table_ref = client.dataset(dataset_id).table(table_id)
table = client.get_table(table_ref)  # API request

rows_to_insert = [tuple(bqin)]
print(rows_to_insert)
errors = client.insert_rows(table, rows_to_insert)  # API request
assert errors == []
