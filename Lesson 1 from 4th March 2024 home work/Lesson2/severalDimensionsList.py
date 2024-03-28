results = [
    ["Brunner Radek", [3, 0, 9]], 
    ["Urban Jaroslav", [3, 11, 44]], 
    ["Andrle Jakub", [3, 12, 21]], 
    ["Fiala Stanislav", [3, 13, 31]]
]

# winner = results[0]
# timeWinner = results[0][1]

# threeWinners = results[:3]



# timeGold = results[0][1][0]*60 + results[0][1][1]
# timeSilver = results[1][1][0]*60 + results[1][1][1]
# print(timeGold)
# print(timeSilver)
# print(f"The Golden medal was lacking {abs(timeGold - timeSilver)} and {results[1][1][2] - results[0][1][2]} minutes to get to Gold")

timeForAll = []


# for i in range(1, 5):
#     for times in results:
#         temporaryList = []
#         secsToMinutes = round(100 * results[i-1][1][2] / 60 / 100, 2)
#         timeInMinutes = 60 * results[i-1][1][0] + results[i-1][1][1] + secsToMinutes
#         temporaryList.append(i)
#         temporaryList.append(timeInMinutes)
#         timeForAll.append(temporaryList)
#         break

# for index, times in enumerate(results, 1):
#     secsToMinutes = round(100 * times[1][2] / 60 / 100, 2)
#     timeInMinutes = 60 * times[1][0] + times[1][1] + secsToMinutes
#     timeForAll.append([index, timeInMinutes])
# print(timeForAll)

# timeToWin = [timeForAll[0]]

# for index in range(1, len(timeForAll)):
#     timeDifference = round(timeForAll[index][1] - timeForAll[0][1], 2)
#     timeToWin.append([index+1, timeDifference])


# for index, runner in enumerate(timeForAll, 1):
#     timeDifference = round(runner[1] - runner[1], 2)
#     timeToWin.append([index+1, timeDifference])


# print(timeToWin)