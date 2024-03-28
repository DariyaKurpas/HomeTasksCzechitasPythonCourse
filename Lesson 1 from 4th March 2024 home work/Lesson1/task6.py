school_report = [
    ["Český jazyk", 1],
    ["Anglický jazyk", 1],
    ["Matematika", 1],
    ["Přírodopis", 2],
    ["Dějepis", 1],
    ["Fyzika", 2],
    ["Hudební výchova", 4],
    ["Výtvarná výchova", 2],
    ["Tělesná výchova", 3],
    ["Chemie", 4],
]

importantSubjects = ["Český jazyk", "Anglický jazyk", "Matematika", "Fyzika"]
markTotal = 0
numberImpSubj = 0
for subject, mark in school_report:
    if subject in importantSubjects:
        numberImpSubj += 1
        markTotal += mark
averageImpSubj = markTotal / numberImpSubj

print(f"The average mark for the important subjects is {averageImpSubj} points.")
