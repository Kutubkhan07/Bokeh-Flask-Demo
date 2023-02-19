import hashlib
import time
import random

def genId(id):
    idstr=str(id)
    x="".join([str(random.randint(0,9)) for x in list(range(10))])
    y=str(time.time())
    z=x+y+idstr
    z=z.encode('utf-8')
    hash = hashlib.sha1()
    hash.update(z)
    return hash.hexdigest()