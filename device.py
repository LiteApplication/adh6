from connexion import NoContent
from itertools import islice

DEVICES = {
    "01:23:45:67:89:AB": {
        'mac'            : '01:23:45:67:89:AB',
        'ipAddress'      : '157.159.42.1',
        'ipv6Address'    :	'ff02::1',
        'connectionType' : 'wired',
        'username'	 : 'coroller'
    },
    "FF:FF:FF:FF:FF:FF": {
        'mac'            : 'FF:FF:FF:FF:FF:FF',
        'ipAddress'      : '157.159.42.2',
        'ipv6Address'    :	'ff02::2',
        'connectionType' : 'wireless',
        'username'	 : 'coroller'
    }
}

def findInDevice( user, terms ):
    txt = ""
    txt += user["mac"] + " "
    txt += user["ipAddress"] + " "
    txt += user["ipv6Address"] + " "
    return txt.lower().find( terms.lower() ) != -1


def filterDevice( limit=100, username=None, terms=None ):

  all_devices = list(DEVICES.values())

  if username != None:
      all_devices = filter( lambda x: x["username"]==username, all_devices ) 
  
  if terms != None:
      all_devices = filter( lambda x: findInDevice(x, terms), all_devices ) 

  return list(islice(all_devices,limit))

def putDevice( macAddress, body ):
  if macAddress in DEVICES:
    retVal = ("Updated", 204)
  else:
    retVal = ("Created", 201)

  if macAddress != body["mac"]:
    del DEVICES[macAddress]
  
  DEVICES[body["mac"]] = body
  return retVal

def getDevice( macAddress ):
  if macAddress in DEVICES:
    return DEVICES[ macAddress ]
  else:
    return 'Not found', 404

def deleteDevice( macAddress ):
  if macAddress in DEVICES:
    del DEVICES[macAddress]
    return NoContent, 204
  else:
    return 'Not found', 404




  
