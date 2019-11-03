# Setting things up
collections = ['Tirmidhi', 'Nasai', 'Muslim', 'Ibn Maja', 'Bukhari', 'Abu Dawud']

numbersInCollections = []

for i in range(0,len(collections)):
    numbersInCollections.append([0] * 1201)

def FromDeathToLife(collection, lifespan):
    numberOfCommentatorsPerYear = [0] * 1201
    with open(collection+'.txt', 'r') as deathDates:
        for date in deathDates:
            death = int(date)
            birth = int(date)-lifespan
            for year in range(birth,death):
                numberOfCommentatorsPerYear[year-200] += 1
    return numberOfCommentatorsPerYear

# Loading into list of lists
for collection in collections:
    numbersInCollections[collections.index(collection)] = FromDeathToLife(collection, 40)

# Writing to disk for individual Hadith collection
for collection in collections:
    y = 200
    with open('lifespan40commentarieson' + collection + '.csv', 'w') as output:
            output.write("year,commentators,matn")
            for number in numbersInCollections[collections.index(collection)]:
                output.write("\n" + str(y) +"," + str(number)+"," + collection)
                y += 1

# Total commentators six collections
allCommentatorsPerYear = [0] * 1201
for i in range (0,1200):
    for x in range (len(collections)):
        allCommentatorsPerYear[i] += numbersInCollections[x][i]

with open('lifespan40All.csv', 'w') as output:
    y = 200
    output.write("year,commentators,all")
    for number in allCommentatorsPerYear:
        output.write("\n" + str(y) + "," + str(number) + ",all")
        y += 1

# Sahihayn
with open('lifespan40Sahihayn.csv', 'w') as output:
    y = 200
    output.write("year,commentators,matn")
    for number in range(0,1201):
        Bukhari = numbersInCollections[4][number]
        Muslim = numbersInCollections[2][number]
        output.write("\n" + str(y) +"," + str(Bukhari)+",Bukhari")
        output.write("\n" + str(y) + "," + str(Muslim) + ",Muslim")
        y += 1