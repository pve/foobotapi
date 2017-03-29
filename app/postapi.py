import requests

url = 'https://groker.initialstate.com/api/events'

def restpost(url, headers, data):
# call service with headers and params
  response = requests.post(url, headers=headers, data=data)
  return response

#response = POSTRequestSync(url, headers, data)
#print "code:"+ str(response.status_code)
#print "******************"
#print "headers:"+ str(response.headers)
#print "******************"
#print "content:"+ str(response.text)
