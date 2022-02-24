def updateMatrix(matrix):
    distances = dict()
    level = set()
    directions = [(0,1), (0,-1), (-1,0), (1,0)]
    height = len(matrix)
    width = len(matrix[0])
    for i in range(height):
        for j in range(width):
            if matrix[i][j] == 0:
                distances[(i,j)] = 0
                level.add((i,j))
    seen = level
    while len(seen) < height * width:
        print(len(seen))
        newlevel = set()
        for a,b in level:
            for c,d in directions:
                v = (min(max(a+c,0),height-1),min(max(b+d,0),width-1))
                x,y = v
                if v not in seen:
                    try:
                        distances[v] = min(distances[v], distances[(a,b)] + 1)
                    except:
                        distances[v] = distances[(a,b)] + 1
                    newlevel.add(v)
        seen = seen.union(newlevel)
        level = newlevel

    print(distances)
    ## make matrix
    newmatrix = []
    for i in range(height):
        newmatrix.append([distances[(i,j)] for j in range(width)])
    return newmatrix




matrix = [[0,0,0],[0,1,0],[1,1,1]]

print(updateMatrix(matrix))
