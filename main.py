class AnswerBox():
    def __init__(self):
        self.possibleNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.actualNumber = 0
        self.solved = False
        self.removed = False

    def checkIfSolved(self):
        if self.solved == False:
            number = 0
            answer = 0
            for poss in self.possibleNumbers:
                if poss != 0:
                    number += 1
                    answer = poss
            if number == 1:
                self.actualNumber = answer
                self.solved = True

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
    f = open("fiendish.txt")
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
    change = False
    for i in range(len(boxList)):
        if boxList[i].solved == False:
            boxList[i].checkIfSolved()
        if boxList[i].actualNumber != 0 and boxList[i].removed == False:
            if boxList[i].actualNumber != 0:
                boxList = nakedRemoval(boxList, i, getRow(i))
                boxList = nakedRemoval(boxList, i, getColumn(i))
                boxList = nakedRemoval(boxList, i, getNonet(i))
                boxList[i].removed = True
                change = True
    return boxList, change

def nakedRemoval(boxList, ident, refs):
    number = boxList[ident].actualNumber
    for ref in refs:
        if ref != ident and boxList[ref].solved == False:
            boxList[ref].possibleNumbers[(number-1)] = 0
    return boxList

def hiddenRemoval(boxList, ident, change, element):
    answerField = [ -1, -1, -1, -1, -1, -1, -1, -1, -1]
    unsolved = []
    changed = change
    for ref in element:
        num = boxList[ref].actualNumber
        if num != 0:
            answerField[num-1] = ref
        else:
            unsolved.append(ref)
    needSolving = []
    for val in range(9):
        if answerField[val] == -1:
            needSolving.append(val+1)
    for item in needSolving:
        number = 0
        poss = 0
        for i in range(len(unsolved)):
            if boxList[unsolved[i]].possibleNumbers[item-1] != 0:
                number += 1
                poss = unsolved[i]
        if number == 1:
            boxList[poss].setValue(item)
            changed = True
    return boxList, changed

def getRow(ident):
    refs = []
    start = (ident // 9) * 9
    for i in range(9):
        refs.append(start+i)
    return refs

def getColumn(ident):
    refs = []
    remainder = (ident % 9)
    for i in range(9):
        refs.append( i * 9 + remainder)
    return refs

def getNonet(ident):
    refs = []
    row = (ident // 9) / 3
    collumn = (ident % 9) // 3
    pointer = (row * 3 * 9) + (collumn * 3)
    for i in range(3):
        for j in range(3):
            refs.append(pointer + i * 9 + j)
    return refs

def main():
    boxList = setup()
    boxList = parser(boxList)
    change = True
    while change:
        boxList,change= basicRemover(boxList)
        if change == False:
            for i in range(9):
                boxList,change=hiddenRemoval(boxList,i, change, getRow(i*9))
                boxList, change = hiddenRemoval(boxList, i, change, getColumn(i))
        if change == False:
            for i in range (3):
                for j in range(3):
                    boxList, change = hiddenRemoval(boxList, i, change, getNonet((i * 3)+j))
    print finalPuzzle(boxList)
    for box in boxList:
        print box.possibleNumbers
main()