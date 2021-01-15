def pairVs(verticles):
    sorted_v = sorted(verticles,key=lambda v: len(v[1]), reverse=True)
    if len(sorted_v)%2 == 1:
        sorted_v = sorted_v[:-1]
    paired = []
    n = len(sorted_v)
    for i in range(len(sorted_v)//2):
        id = str(sorted_v[i][0])+ " " +str(sorted_v[n - i - 1][0])
        set = sorted_v[i][1] | sorted_v[n - i - 1][1]
        paired.append((id, set))
    return paired

def filestarter(filename):
    file = open(filename, 'r')
    horizontals = []
    verticals = []
    counter = -1
    for line in file.readlines():
        temp = line.split()
        if temp[0] == 'H':
            horizontals.append((str(counter), set(temp[2:])))
        if temp[0] == 'V':
            verticals.append((counter, set(temp[2:])))
        counter+=1
    len = counter + 1
    # horizontals = horizontals[1:]
    verticals = pairVs(verticals)
    # print(horizontals)
    # print("\n")
    # print(verticals)
    return horizontals + verticals


print(filestarter("a_example.txt"))