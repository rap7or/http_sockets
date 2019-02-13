#!/usr/bin/python
from http_sockets import *

soc = sock("csec380-core.csec.rit.edu", 82)
tok = soc.post('http://csec380-core.csec.rit.edu:82/getSecure')
tok = tok.split()[-1].strip('"')
print(tok)

capt = soc.post('http://csec380-core.csec.rit.edu:82/getFlag3Challenge', {'token' : tok })
capt = capt.split()[-1].strip('"')
print(capt)
sol = eval(capt)
flag = soc.post('http://csec380-core.csec.rit.edu:82/getFlag3Challenge', {'token' : tok, 'solution' : sol })
#print(flag)
soc.close()


soc2 = sock("csec380-core.csec.rit.edu", 82)
get = soc2.get('http://csec380-core.csec.rit.edu/')
print(get)
soc2.close()