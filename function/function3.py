import random

print("Please guezz number 1 - 9")
answerNumber = int(input())

def getAnswer(answerNumber):
    if answerNumber == 1:
        return "Good"
    elif answerNumber == 2:
        return "please c'mon"
    elif answerNumber == 3:
        return "are you crazy"
    elif answerNumber == 4:
        return "Make a good gezzz"
    elif answerNumber == 5:
        return "please thinking"
    elif answerNumber == 6:
        return "No"
    elif answerNumber == 7:
        return "Ouch"
    elif answerNumber == 8:
        return "neee"
    elif answerNumber == 9:
        return "Guezzz again"
    
r = random.randint(1,9)
fortune = getAnswer(r)
print(fortune)
    
