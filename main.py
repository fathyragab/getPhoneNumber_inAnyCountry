import phonenumbers
from number import number

from phonenumbers import geocoder
ch_nmber = phonenumbers.parse(number, "CH")
print (geocoder.description_for_number(ch_nmber, "ar"))

from phonenumbers import carrier
service_nmber = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_nmber, "ar"))
