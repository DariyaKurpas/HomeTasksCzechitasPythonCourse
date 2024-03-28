# def pozdrav():
#     print("Ahoj!")

# def pozdrav(jmeno):
#     print(f"Ahoj, {jmeno}!")

# pozdrav("Dariya")

# def addingUpNumbers(a, b):
#     return a + b

# sumUp = addingUpNumbers(11, 23)
# print(sumUp)
# print(addingUpNumbers(11, 11))

# exchangeRate = 25

# def countExchangeCZK(czk):
#     return exchangeRate * czk
# print(countExchangeCZK(2))

# def iDontKnowYet(input1, input2):
#     pass #tohle nechava Python ignorovat nedokoncenou funkci

# def pozdrav(jmeno = "clovece"):
#     print(f"Ahoj, {jmeno}!")

# pozdrav()
# pozdrav("Dariya")

# def pozdrav(jmeno = ""):
#     print(f"Ahoj, {jmeno}!")

# pozdrav()
# pozdrav("Dariya")


G = ["alice", "bob"]

def Fx(a, b, G):
    r = "123"
    G.append("Eve")
    return r

Fx(1, 2, [])
print(G)