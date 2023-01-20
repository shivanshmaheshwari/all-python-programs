import phonenumbers
from phonenumbers import carrier, geocoder, timezone

mobileNo = input("ENTER MOBILE NUMBER WITH COUNTRY CODE:")
mobileNo = phonenumbers.parse(mobileNo)

#to get timezone of number
print(timezone.time_zones_for_number(mobileNo))

#to get carrier of the phone number 
print(carrier.name_for_number(mobileNo,"en"))

#getting regional number 
print(geocoder.description_for_number(mobileNo,"en"))

#validating phone number 
print("VALID MOBILE NUMBER: ",phonenumbers.is_valid_number(mobileNo))

#checking possibality of the number 
print("CHECKING POSSIBILITY OF THE NUMBER: ",phonenumbers.is_possible_number(mobileNo))


