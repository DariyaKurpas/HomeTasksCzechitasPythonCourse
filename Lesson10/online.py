with open(r"Lesson10\text.txt", encoding="utf-8") as file: # I can have either the relative path or the complete path this way
    text = file.read() # this is the context
    
print(text)

# file = open(r"C:\Users\dasha\HomeTasksCzechitasPythonCourse\Lesson10\text.txt", encoding="utf-8")
# print(file.read()) # the file will be opened, but not closed. risks: memory etc many open files





# lines = []

# with open(r"Lesson10\text.txt", encoding="utf-8") as file:
#     for line in file:
#         lines.append(line)

# print(lines)





# with open(r"Lesson10\text.txt", encoding="utf-8") as file:
#     text = file.readlines() # output is the same as for the for cycle

# print(text)



output = []

with open(r"Lesson10\text.txt", encoding="utf-8") as file:
    for line in file:
        # print(line.split('\t'))
        day, temp = line.split("\t")
        output.append([day, float(temp)])
        # if I had put only day, temp --> the \n will stay

print(output)