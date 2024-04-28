# text = "Ahoj! Jak se máš? Já se mám skvěle. A co ty? Už jsi dokončil Python projekt?"

# interpunction = ".,!?"

# for mark in interpunction:
#     text = text.replace(mark, ",")

# print(text)

# # text_no_interpunction = text.split(", ")

# # print(text_no_interpunction)
# sentences = [sentence.split(" ") for sentence in text.split(", ") if sentence]
# # for sentence in text.split(", "):
# #     temp_list = sentence.split(" ")
# #     text_no_interpunction.append(temp_list)

# print(sentences)

# myDict = {i+1: sentence for i, sentence in enumerate(sentences)}

# # for i, sentence in enumerate(sentences):
# #     myDict[i+1] = sentences[i]

# for key, value in myDict.items():
#     print(f"{key}: {value}")

import re

text = "Ahoj! Jak se máš? Já se mám skvěle. A co ty? Už jsi dokončil Python projekt?"
sentences = [sentence.split()
             for sentence in re.split("[.!?]", text) if sentence]

print(sentences)

myDict = {i+1: sentence for i, sentence in enumerate(sentences)}

print(myDict)


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
