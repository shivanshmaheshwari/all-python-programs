import phonenumbers
from myNumber import number
from phonenumbers  import geocoder
findNumber = phonenumbers.parse(number)
yourLocation = geocoder.description_for_number(findNumber, "en")
print(yourLocation)