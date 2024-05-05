from faker import Faker
fake = Faker(["cs_CZ", "de_AT"])

print(fake.name())
# 'Lucy Cechtelar'

print(fake.address())
# '426 Jordy Lodge
#  Cartwrightshire, SC 88120-6700'

print(fake.text(max_nb_chars=20, ext_word_list=["sunshine", "summer", "flowers", "ridiculous", "rainbow", "lovely", "te gusta"]))
print(fake.text())


print("******************************")

for _ in range(10):
    print(f"{fake.name()}, {fake.address()}")

for name in range(20):
    print(fake.name_female())
