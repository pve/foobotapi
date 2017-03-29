# for use with pytest
import os, requests
from settings import *
# from 

data = {
    "status": ":thumbsup:",
	"source": "test_api"
}

def test_env ():
    assert fooboturl != 'novalidkey'
    assert foobotkey != 'novalidkey'
    
def test_get ():
    response = requests.get(fooboturl, headers=fooheaders)
    print "code:"+ str(response.status_code)
    print "******************"
    print "headers:"+ str(response.headers)
    print "******************"
    print "content:"+ str(response.text)
    # check data kind of ok.
    assert response.ok
    # 
    
def test_transform ():
    assert True
    
def test_put ():
    assert True
