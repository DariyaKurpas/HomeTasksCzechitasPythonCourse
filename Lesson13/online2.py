import re
# Náš systém vyžaduje od uživatele zadání uživatelského jména. Uživatelské jméno smí obsahovat pouze malá písmena a smí být maximálně 8 znaků dlouhé. 
# Požádej uživatele o zadání uživatelského jména a pomocí regulárního výrazu vyhodnoť, zda je zadané správné.

regex_user_id = re.compile(r"[a-z]{8}")
print(regex_user_id)

user_id = input("Type in your user ID:\n")

if regex_user_id.fullmatch(user_id):
    print("Accepted.")
else:
    print("Not accepted.")