class TreasureChest:
    def __init__(self, question, answer, points):
        self.__question = question # DECLARE question : STRING
        self.__answer = answer # DECLARE answer : INTEGER
        self.__points = points # DECLARE points : INTEGER

    def getQuestion(self):
        return self.__question
    
    def checkAnswer(self, useranswer):
        if self.__answer == useranswer:
            return True
        else:
            return False
        
    def GetPoints(self, attempts):
        if attempts == 1:
            return self.__points
        elif attempts == 2:
            return self.__points // 2
        elif attempts in [3, 4]:
            return self.__points // 4
        else:
            return 0
        




def readData(filename):
    arrayTreasure = []
    try:
        with open(filename, "r") as file:
            lines = file.readlines()

            for i in range(0, len(lines), 3):
                question = lines[i].strip()
                answer = int(lines[i+1].strip())
                points = int(lines[i+2].strip())

                arrayTreasure.append(TreasureChest(question, answer, points))
        return arrayTreasure
    except FileNotFoundError:
        print("file not found...")


questions = readData("TreasureChestData.txt")
userinput = int(input("Enter a number between 1-5: "))
selectedquestion = questions[userinput -1]
attempts = 0

while True:
    print(selectedquestion.getQuestion())
    answer = int(input("Answer: "))
    attempts += 1
    if selectedquestion.checkAnswer(answer):
        print("correct!")
        break
    else:
        print("wrong!")
        continue
points = selectedquestion.GetPoints(attempts)
print(f"Points awarded: {points}")
