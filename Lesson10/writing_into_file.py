text = "I DO want to write this text into a file."

with open(r"C:\Users\dasha\HomeTasksCzechitasPythonCourse\Lesson10\file_text.txt", mode="a", encoding="utf-8") as writiing_file: # a append, r read, w write, muzu napsat cely path nebo jenom nazev souboru
    print(text, file=writiing_file)

names = ["Darinka", "Filip", "Snouma"] 

with open("teilnehmer.txt", mode="w", encoding="utf-8") as output:
    for name in names:
        print(name, file=output)

