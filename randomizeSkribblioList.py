import random

contents = None
with open("words.txt", "r") as f:
    contents = f.read()
    f.close()

wordList = contents.split(',')
print(wordList)
newWordList = []

contents = ""

while(len(contents) < 4968):
    randomChoice = random.choice(wordList)
    contents = contents + randomChoice + ","
    wordList = list(filter((randomChoice).__ne__, wordList))

    
with open("randomwords.txt", "w") as f:
    f.write(contents)
