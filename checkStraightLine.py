#1232. Check if it is stright line
def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        const, par = 0,0
        if coordinates[0][0] == coordinates[1][0]:
            for i in range(2,len(coordinates)):
                if coordinates[0][0] != coordinates[i][0]:
                    return False
            return True
        if coordinates[0][0] == 0:
            par = coordinates[0][1]
            if (coordinates[0][0] != coordinates[1][0]):
                const = (coordinates[0][1]-coordinates[1][1])/(coordinates[0][0]-coordinates[1][0])
        else:
            const = (coordinates[0][1]-coordinates[1][1])/(coordinates[0][0]-coordinates[1][0])
            par = coordinates[0][1] - const*coordinates[0][0]
        for i in range(len(coordinates)):
            if coordinates[i][1] != (const * coordinates[i][0]) + par:
                return False
        return True
