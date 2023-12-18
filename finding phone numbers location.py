import phonenumbers
from phonenumbers import geocoder
phone_number1=phonenumbers.parse("+919503200610")
#phone_number2=phonenumbers.parse("+919860986369")

print("\nPhone Numbers Location\n")
print(geocoder.description_for_number(phone_number1,"en"));
print(geocoder.description_for_number(phone_number2,"en"));

