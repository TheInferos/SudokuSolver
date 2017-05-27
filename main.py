import os

class AnswerBox():
    possibleNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    actualNumber = 0
    solved = False
    removed = False

    def checkIfSolved(self):
        if self.solved == False:
            number = 0
            answer = 0
            for poss in self.possibleNumbers:
                if poss != 0:
                    number += 1
                    answer = poss
            print "got here", number
            if number == 1:
                self.actualNumber = answer
                self.solved = True
                print "fuck yer got one", answer

    def setValue(self, val):
        self.actualNumber = val
        self.solved = True
        self.possibleNumbers = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.possibleNumbers[val-1] = val

def setup():
    boxs = []
    for i in range(81):
        boxs.append(AnswerBox())
    return boxs

def parser(boxList):
    f = open("sudoku.txt")
    line = f.read().split()
    ident = 0
    for num in line:

        if num != "0":
            boxList[ident].setValue(int(num))
        ident += 1

    return boxList

def finalPuzzle(boxList):
    puzzleString = ""
    ident = 0
    for box in boxList:
        puzzleString += str(box.actualNumber) + " "
        ident += 1
        if ident == 9:
            puzzleString += "\n"
            ident = 0
    return puzzleString

def basicRemover(boxList):
    for i in range(len(boxList)):
        if boxList[i].solved == False:
            print i
            boxList[i].checkIfSolved()
        if boxList[i].actualNumber != 0 and boxList[i].removed == False:
            if boxList[i].actualNumber != 0:
                boxList = rowRemover(boxList, i)
                boxList = columnRemover(boxList, i)
                boxList= nonetRemover(boxList, i)
                boxList[i].removed = True

    return boxList



def rowRemover(boxList, ident):
    number = boxList[ident].actualNumber
    start = (ident//9) *9
    for i in range(9):
        ref = start+ i
        if i != ident and boxList[ref].solved == False:
            #print number, number-1, ref
            print boxList[ref].possibleNumbers
            boxList[ref].possibleNumbers[(number-1)] = 0
            print boxList[ref].possibleNumbers
    return boxList


def columnRemover(boxList, ident):
    number = boxList[ident].actualNumber
    remainder = (ident % 9)
    for i in range(9):
        ref = i * 9 + remainder
        if ref != ident:
            print boxList[ref].possibleNumbers
            boxList[ref].possibleNumbers[(number - 1)] = 0
            print boxList[ref].possibleNumbers
    return boxList

    
def nonetRemover(boxList, ident):
    number = boxList[ident].actualNumber
    row = (ident//9) /3
    collumn = (ident % 9) //3
    pointer = (row * 3 * 9) + (collumn * 3)
    for i in range(3):
        for j in range(3):
            ref = pointer + i * 9 + j
            print "removing ", number, "from ", ref, ident
            if ref != ident:
                print boxList[ref].possibleNumbers
                boxList[ref].possibleNumbers[(number - 1)] = 0
                print boxList[ref].possibleNumbers
    return boxList


def main():
    boxList = setup()
    boxList = parser(boxList)
    for box in boxList:
        pass#print box.possibleNumbers
    for attempts in range(1):
        boxList= basicRemover(boxList)
    i=0
    for box in boxList:
        pass#print i, box.possibleNumbers
        i+=1
    print finalPuzzle(boxList)

main()