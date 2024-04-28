# import re

# var = "Ahoj světe, učíme se Python!"
# split_var = var.split(", ")

# print(split_var)

# text = "Ahoj! Jak se máš? Já se mám skvěle. A co ty? Už jsi dokončil Python projekt?"
# text_no_interpunction = list(re.split("[.!?]", text))
# print(text_no_interpunction)

# no_interpunction_split_in_words = []

# for sentence in text_no_interpunction:
#     temp_list = sentence.split()
#     no_interpunction_split_in_words.extend(temp_list)

# print(no_interpunction_split_in_words)

# for sentence in text_no_interpunction:
#     word = sentence.split()
#     if word:
#         no_interpunction_split_in_words.append(word)

# print(no_interpunction_split_in_words)

# myDict = {}
# for i in range(len(no_interpunction_split_in_words)):
#     myDict[i+1] = no_interpunction_split_in_words[i]

# print(myDict)

# text_no_interpunction = list(re.findall("[^.!?]*[.!?]", text))
# print(text_no_interpunction)


var = "Ahoj světe, učíme se Python!"


text = "Ahoj! Jak se máš? Já se mám skvěle. A co ty? Už jsi dokončil Python projekt?"
interpunction = "!,.?"
for sign in interpunction:
    text = text.replace(sign, ",")

print(text)

# separate_sentences = []
# separate_sentences = [
#     sentence for sentence in text.split(",") if sentence.strip()]
# for sentence in text.split(", "):
#     if sentence.strip():
#         separate_sentences.append(sentence)

separate_sentences = text.split(", ")
for i in range(len(separate_sentences)):
    if separate_sentences[i]:
        if separate_sentences[i].strip():
            separate_sentences[i] = separate_sentences[i].strip()
print(separate_sentences)
