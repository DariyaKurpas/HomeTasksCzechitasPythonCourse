text = "Tento text bude zapsán do souboru."

with open('my_excerices\soubor.txt', mode='w', encoding='utf-8') as output_file:
    print(text, file=output_file)

names = ['Roman', 'Jana', 'Radek', 'Petra', 'Vlasta']

with open('my_excerices\\uzivatele.txt', mode='w', encoding='utf-8') as output_file:
    for name in names:
        print(name, file=output_file)