import os
from credsfromfile import *

def getconfigitem(item, secrets):
	try:
		return(secrets[item])
	except KeyError as e:
		return("novalidkey")

config = os.environ.get('CONFIGBUCKET') # supposedly a GS bucket.
secrets = getsecrets(config, "clientsecrets.json")

dataset_id = getconfigitem('dataset_id', secrets)
table_id = getconfigitem('table_id', secrets)

fooboturl = getconfigitem('fooboturl', secrets)
foobotkey = getconfigitem('foobotkey', secrets)
isurl = getconfigitem('isurl', secrets)
isaccesskey = getconfigitem('isaccesskey', secrets)
isbucketkey = getconfigitem('isbucketkey', secrets)
logglykey = getconfigitem('logglykey', secrets)
# print fooboturl, foobotkey, isurl

fooheaders = {"Accept": "application/json", "X-API-KEY-TOKEN": foobotkey }

isheaders = {"Accept": "application/json",
		"X-IS-AccessKey": isaccesskey,
		"X-IS-BucketKey": isbucketkey
}
