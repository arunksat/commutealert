
#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

import sys
sys.path.append('/Library/Frameworks/Python.framework/Versions/2.7/bin')
import simplejson
import urllib
from twilio.rest import TwilioRestClient

url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=Tasman Drive+San+Jose+CA&destinations=Sand Hill Road+Menlo+Park+CA&departure_time=now&key=AIzaSyBX1IjQRUvUiW_2p6HoRbATBrVB7ONOotQ"
result = simplejson.load(urllib.urlopen(url))
driving_time = result['rows'][0]['elements'][0]['duration_in_traffic']['text']
print driving_time

accountSID = 'ACa3ddfbf8712b8b08d923fe49b805610f'
authToken = '3b511eaa04490e6de04855f4d8817d83'
twilioCli = TwilioRestClient(accountSID, authToken)
myTwilioNumber = '+19252330852'
myCellPhone = '+1xxxxxxxxxx'
message = twilioCli.messages.create(body='Hello ... your commute time is going to be {}'.format(driving_time), from_=myTwilioNumber, to=myCellPhone)
