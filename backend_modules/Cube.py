class Cube:
    outerLayer = [0, 1, 2, 5, 8, 7, 6, 3]

    def __init__(self):
        self.up = self.GetUpperLayer()
        self.down = self.GetLowerLayer()
        self.left = self.GetLeftLayer()
        self.right = self.GetRightLayer()
        self.back = self.GetBackLayer()
        self.front = self.GetFrontLayer()
        self.symbolExecution = {'U': self.turnUpper, 'D': self.turnDown, 'L': self.turnLeft, 'R': self.turnRight, 'F': self.turnFront, 'B': self.turnBack}

    ## ['WHITE', 'RED', 'BLUE', 'ORANGE', 'GREEN', 'YELLOW']
    def dummyLayer(self):
        return [x for x in range(9)]

    def GetUpperLayer(self):
        return [0]*9

    def GetFrontLayer(self):
        return [1]*9

    def GetRightLayer(self):
        return [2]*9

    def GetBackLayer(self):
        return [3]*9

    def GetLeftLayer(self):
        return [4]*9

    def GetLowerLayer(self):
        return [5]*9

    def GetBlank(self):
        return [' ']*9

    def printCube(self):
        blank = self.GetBlank()
        self.printLayers([blank, self.up, blank, blank])
        self.printLayers([self.left, self.front, self.right, self.back])
        self.printLayers([blank, self.down, blank, blank])

    def printLayers(self, faces):
        i=0
        while i<9:
            print (faces[0][i], " ",faces[0][i+1]," ",faces[0][i+2]," ",faces[1][i], " ",faces[1][i+1]," ",faces[1][i+2]," ",faces[2][i], " ",faces[2][i+1]," ",faces[2][i+2]," ",faces[3][i+2], " ",faces[3][i+1]," ",faces[3][i]," ")
            i+= 3

    def turnUpper(self, prime=1):
        print ('Upper')
        self.shiftLayer(self.up)
        self.shiftSideLayers([self.front, self.right, self.back, self.left], [[0, 1, 2], [0, 1, 2], [2, 1, 0], [0, 1, 2]])
        self.printCube()

    def turnDown(self, prime=1):
        print ('Down')
        self.shiftLayer(self.down)
        self.shiftSideLayers([self.front, self.left, self.back, self.right], [[6, 7, 8], [6, 7, 8], [8, 7, 6], [6, 7, 8]])
        self.printCube()

    def turnLeft(self, prime=1):
        print ('Left')
        self.shiftLayer(self.left)
        self.shiftSideLayers([self.up, self.back, self.down, self.front], [[0, 3, 6], [6, 3, 0], [0, 3, 6], [0, 3, 6]])
        self.printCube()

    def turnRight(self, prime=1):
        print ('Right')
        self.shiftLayer(self.right)
        self.shiftSideLayers([self.up, self.front, self.down, self.back], [[2, 5, 8], [2, 5, 8], [2, 5, 8], [8, 5, 2]])
        self.printCube()

    def turnFront(self, prime=1):
        print ('Front')
        self.shiftLayer(self.front)
        self.shiftSideLayers([self.up, self.left, self.down, self.right], [[6, 7, 8], [8, 5, 2], [2, 1, 0], [0, 3, 6]])
        self.printCube()

    def turnBack(self, prime=1):
        print ('Back')
        self.shiftLayer(self.back)
        self.shiftLayer(self.back)
        self.shiftLayer(self.back)
        self.shiftSideLayers([self.up, self.right, self.down, self.left], [[0, 1, 2], [2, 5, 8], [8, 7, 6], [6, 3, 0]])
        self.printCube()

    def swapPieces(self, a, b, side1, side2):
        length = len(side1)
        for i in range(length):
            a[side1[i]], b[side2[i]] = b[side2[i]], a[side1[i]]

    def shiftLayer(self, layer):
        temp = [x for x in layer]
        for i in range(8):
            layer[self.outerLayer[(i+2)%8]] = temp[self.outerLayer[i]]

    def shiftSideLayers(self, layers, outerPath):
        temp = [layers[0][i] for i in outerPath[0]]
        temp += [layers[1][i] for i in outerPath[1]]
        temp += [layers[2][i] for i in outerPath[2]]
        temp += [layers[3][i] for i in outerPath[3]]

        shiftedList = [x for x in temp]

        j = 0
        for i in range(4):
            for l in outerPath[i]:
                layers[i][l] = temp[(j + 3)%12]
                j += 1

    def executeSymbol(self, symbol):
        if len(symbol) > 1:
            if symbol[1] == '2':
                self.symbolExecution[symbol[0]]()
                self.symbolExecution[symbol[0]]()
            else:
                self.symbolExecution[symbol[0]]()
                self.symbolExecution[symbol[0]]()
                self.symbolExecution[symbol[0]]()
        else:
            self.symbolExecution[symbol[0]]()

    def performScramble(self, scramble):
        if len(scramble) != 0:
            self.executeSymbol(scramble.pop(0))
            self.performScramble(scramble)
        else:
            print ('\n')
            self.printCube()
