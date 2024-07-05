import re

regex_email_address = re.compile(r"[a-z\.]@[a-z\.]")
print(regex_email_address)

user_email_address = input("Type in your email address:\n")

if regex_email_address.fullmatch(user_email_address):
    print("Accespted.")
else:
    print("Not accepted.")