#!/usr/bin/python3
from http_sockets import *

soc = sock("csec380-core.csec.rit.edu", 82)
soc.post('http://csec380-core.csec.rit.edu:82/getSecure')

