from Cube import*

class ManhattanCube:
    # Makes the Manhattan Cube given a Cube
    # map = the Cube
    def __init__(self, map):
        cublets = [{1, 4, 0}, {1, 2, 0}, {1, 2, 5}, {1, 5, 4}, {0, 4, 3}, {3, 0, 2}, {3, 2, 5}, {3, 4, 5}]
        temp = []
        temp.append([map.state[1][2], map.state[4][1], map.state[0][0]])
        temp.append([map.state[1][3], map.state[2][0], map.state[0][1]])
        temp.append([map.state[1][1], map.state[2][1], map.state[5][3]])
        temp.append([map.state[1][0], map.state[4][0], map.state[5][2]])
        temp.append([map.state[3][0], map.state[4][3], map.state[0][2]])
        temp.append([map.state[3][1], map.state[2][2], map.state[0][3]])
        temp.append([map.state[3][3], map.state[2][3], map.state[5][1]])
        temp.append([map.state[3][2], map.state[4][2], map.state[5][0]])
        self.cube = []
        self.ore = []
        for i in temp:
            c = {i[0],i[1],i[2]}

            for j in range(len(cublets)):
                if c == cublets[j]:
                    self.cube.append(j)
        for i in range(len(temp)):
            if temp[i][0] == 1 or temp[i][0] == 3:
                self.ore.append(0)
            if temp[i][1] == 1 or temp[i][1] == 3:
                self.ore.append(1)
            if temp[i][2] == 1 or temp[i][2] == 3:
                self.ore.append(2)

    def findPiece(self, id):
        for i in range(len(self.cube)):
            if self.cube[i] == id:
                return i

    def cublet(self, a):
        cublets = [{1,4,0}, {1,2,0}, {1,2,5}, {1,5,4}, {0,4,3}, {3,0,2}, {3,2,5}, {3,4,5}]
        returnValue = -1
        if a[0] == 1 or a[0] == 3:
            returnValue = 0
        if a[1] == 1 or a[1] == 3:
            returnValue = 1
        if a[2] == 1 or a[2] == 3:
            returnValue = 2
        temp = {a[0], a[1], a[2]}
        for i in range(len(cublets)):
            if temp == cublets[i]:
                return (i,returnValue)