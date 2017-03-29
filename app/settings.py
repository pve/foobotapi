import os
fooboturl = os.getenv('fooboturl','novalidkey')
foobotkey = os.getenv('foobotkey','novalidkey')
isurl = os.getenv('isurl','novalidkey')
isaccesskey = os.getenv('isaccesskey','novalidkey')
isbucketkey = os.getenv('isbucketkey','novalidkey')
logglykey = os.getenv('logglykey','novalidkey')

fooheaders = {"Accept": "application/json", "X-API-KEY-TOKEN": foobotkey }

isheaders = {"Accept": "application/json", 
		"X-IS-AccessKey": isaccesskey,
		"X-IS-BucketKey": isbucketkey
}

