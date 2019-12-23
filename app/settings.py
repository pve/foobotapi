import os
from credsfromfile import *

def getconfigitem(item, secrets):
	try:
		return(secrets[item])
	except KeyError as e:
		return("novalidkey")

config = os.environ.get('CONFIGBUCKET') # supposedly a GS bucket.
secrets = getsecrets(config, "foobotsecrets.json")

dataset_id = getconfigitem('dataset_id', secrets)
table_id = getconfigitem('table_id', secrets)

fooboturl = getconfigitem('fooboturl', secrets)
foobotkey = getconfigitem('foobotkey', secrets)
isurl = getconfigitem('isurl', secrets)
isaccesskey = getconfigitem('isaccesskey', secrets)
isbucketkey = getconfigitem('isbucketkey', secrets)
logglykey = getconfigitem('logglykey', secrets)
# logging fooboturl, foobotkey, isurl
#adafruit
afkey = getconfigitem('adafruitkey', secrets)
afurl = getconfigitem('adafruiturl', secrets)
afuser = getconfigitem('adafruituser', secrets)

fooheaders = {"Accept": "application/json", "X-API-KEY-TOKEN": foobotkey }
afheaders = { "X-AIO-Key": "b063f2a23f76478a9a8be4daaf52fde6" }

isheaders = {"Accept": "application/json",
		"X-IS-AccessKey": isaccesskey,
		"X-IS-BucketKey": isbucketkey
}
