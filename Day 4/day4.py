from typing import Optional


class Board:

    def __init__(self, contents):
        self.board = []
        for row in contents:
            nums = row.split()
            tupleNums = []
            for num in nums:
                tupleNums.append([num, False])
            self.board.append(tupleNums)
    
    def getBoard(self):
        return self.board

        
    def guess(self, num_guessed):
        for row in self.board:
            for num in row:
                if num_guessed == num[0]:
                    num[1] = True
                    if self.is_finished():
                        return self.calc_score(num_guessed)
        return 0
    
    def is_finished(self):
        for row in self.board:
            if all(map(isMarked,row)):
                return True
        for i in range (0,5):
            col = map((lambda a : a[i]), self.board)
            if all(map(isMarked,col)):
                return True
        return False

    def calc_score(self, last_guess):
        unmarked = 0
        for row in self.board:
            for num in row:
                if not isMarked(num):
                    unmarked = unmarked + int(num[0])
        return unmarked * int(last_guess)


def isMarked(num):
    return num[1]

def playGame():
    with open ("input.txt", 'r') as f:
        lines = f.readlines()
    listOfNums = lines[0].split(",")
    boardList = []
    boards = []
    for i in range(2, len(lines)):
        if lines[i] != "\n":
            boardList.append(lines[i])
        else:
            boards.append([Board(boardList),False])
            boardList = []
    for num in listOfNums:
        for board in boards:
            if board[0].guess(num) != 0:
                if (not board[1]) and (count(False, map(isMarked, boards))==1):
                    return (board[0].guess(num))
                else:
                    board[1] = True

def count(elem, list):
    sum = 0
    for item in list:
        if item == elem:
            sum += 1
    return sum

print(playGame())


