from Cube import Cube

def solutionGenerator():
    cube = Cube()
    cube.printCube()
    print ('\n')
    #cube.shiftSideLayers([cube.up, cube.right, cube.down, cube.left], [[0, 1, 2], [2, 5, 8], [8, 7, 6], [6, 3, 0]])
    #cube.shiftSideLayers([cube.up, cube.right, cube.down, cube.left], [[6, 7, 8], [0, 3, 6], [2, 1, 0], [8, 5, 2]])
    #cube.shiftSideLayers([cube.up, cube.front, cube.down, cube.back], [[0, 3, 6], [0, 3, 6], [0, 3, 6], [6, 3, 0]])
    #cube.shiftSideLayers([cube.up, cube.front, cube.down, cube.back], [[2, 5, 8], [2, 5, 8], [2, 5, 8], [8, 5, 2]])
    #cube.shiftSideLayers([cube.front, cube.right, cube.back, cube.left], [[0, 1, 2], [0, 1, 2], [2, 1, 0], [0, 1, 2]])
    #cube.shiftSideLayers([cube.front, cube.right, cube.back, cube.left], [[6, 7, 8], [6, 7, 8], [8, 7, 6], [6, 7, 8]])
    cube.performScramble(['B2', 'F2', 'L2', 'D\'','B2','D\'','L2','R2','U\'','B','L2','F\'','R2','D\'','B2','F\'','R\'','U','L\''])
    #cube.performScramble(['F2', 'R'])
    pass

def nextDesiredStateGenerator():
    pass

def findShortestFeasiblePath():
    pass

def turnCubeWithGivenNotation(notation):
    pass
