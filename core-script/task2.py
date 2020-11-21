
##
# NLP Hackathon Task 1 by:
# Isha Gupta
# Moritz Reihs
# Luca Entremont
##
 
#create all combinations of two categories
def twoCombinations(categories):
    categoriesCom = []
 
    for i in range(1, len(categories)):
        for j in range(i, len(categories)):
            categoriesCom.append([categories[i],categories[j]])
 
    return categoriesCom
 
#find maximum combination
def findMax(categoriesCom):
    score = []
 
    for in in range categoriesCom:
        score.append(testComb(categoriesCom[i]))
 
    return max(score)