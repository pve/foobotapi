import os
from credsfromfile import *

#config = os.environ.get('CONFIGBUCKET') # supposedly a GS bucket.
#secrets = getsecrets(config, "foobot_config.json")

fooboturl = os.getenv('fooboturl','novalidkey')
foobotkey = os.getenv('foobotkey','novalidkey')
isurl = os.getenv('isurl','novalidkey')
isaccesskey = os.getenv('isaccesskey','novalidkey')
isbucketkey = os.getenv('isbucketkey','novalidkey')
logglykey = os.getenv('logglykey','novalidkey')
xivelyurl = os.getenv('xivelyurl','novalidkey')
xivelykey = os.getenv('xivelykey','novalidkey')

# print fooboturl, foobotkey, isurl

fooheaders = {"Accept": "application/json", "X-API-KEY-TOKEN": foobotkey }

isheaders = {"Accept": "application/json",
		"X-IS-AccessKey": isaccesskey,
		"X-IS-BucketKey": isbucketkey
}

xivheaders = {"Accept": "application/json", "X-ApiKey": xivelykey }
