#!/usr/bin/python
import sys
import json
import pycurl
from pprint import pprint

#Get event data passed from sensu
event = json.load(sys.stdin)

#get the client passed by the event data
clientname = event["client"]["name"]

#deregister the client
c = pycurl.Curl()
c.setopt(c.URL, "http://<SENSUAPIHERE>/clients/{}".format( clientname ))
c.setopt(c.CUSTOMREQUEST, "DELETE")
c.setopt(c.TIMEOUT, 20)
c.setopt(c.USERPWD, "username:password")
c.perform()
c.close()
print("clientname is deregistered")
