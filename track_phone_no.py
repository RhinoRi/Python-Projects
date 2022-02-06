# Tracking phone number's country using python!

import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

mob_num = input('Enter the mobile number here: ')
country_details = phonenumbers.parse(mob_num, 'CH')
print(geocoder.description_for_number(country_details, 'en'))

service_details = phonenumbers.parse(mob_num, 'RO')
print(carrier.name_for_number(service_details, 'en'))
