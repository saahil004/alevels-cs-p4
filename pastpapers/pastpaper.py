names = ["" for i in range(11)]
scores = [0 for i in range(11)]

def ReadHighScores(names, scores):
    file = open("HighScore.txt","r")
    name = file.readline().strip()
    score = file.readline().strip()
    count = 0
    while (name != "") and (score != ""):
        names[count] = name
        scores[count] = score
        name = file.readline().strip()
        score = file.readline().strip()
        count += 1
    file.close()
    
def temp(names, scores):
        file = open("HighScore.txt","r")
        for i in range(10):
            name = file.readline().strip()
            score = int(file.readline())
            names[i] = name
            scores[i] = score
        file.close()
        
ReadHighScores(names, scores)
print(names)        
print(scores)        
        