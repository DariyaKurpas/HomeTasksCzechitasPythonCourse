my_list_rows = []

with open(r"Lesson10\book.txt", encoding="utf-8") as file:
    for line in file:
        my_list_rows.append(line)

print(my_list_rows)

words = []

for segment in my_list_rows:
    words.append(segment.split(" "))

print(words)

all_words = 0

for item in words:
    all_words += len(item)
    print(len(item))

print(f"The number of the words in text is {all_words}")

