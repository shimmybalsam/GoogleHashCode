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
    file.close()
    return horizontals + verticals

def score(s1, s2):
    together = len(s1[1] | s2[1])
    overlap = (together - len(s1[1]) - len(s2[1])) * (-1)
    foreign1 = len(s1[1]) - overlap
    foreign2 = len(s2[1]) - overlap
    return min(overlap, foreign1, foreign2)


def find_best(cur_slide, sol, cur_score):
    max_i = 0
    max_score = cur_score
    for i in range(len(sol) + 1):
        if i == 0:
            right_score = score(sol[i], cur_slide)
            temp_score = cur_score + right_score
        elif i == len(sol):
            left_score = score(sol[i-1], cur_slide)
            temp_score = cur_score + left_score
        else:
            prev = score(sol[i-1], sol[i])
            left_score = score(sol[i-1], cur_slide)
            right_score = score(sol[i], cur_slide)
            temp_score = cur_score - prev + left_score + right_score

        if max_score < temp_score:
            max_i = i
            max_score = temp_score
    sol.insert(max_i, cur_slide)
    return max_score, sol

def greed(slides):
    slides = sorted(slides, key=lambda v: len(v[1]), reverse=True)
    sol = [slides[0]]
    cur_score = 0
    for s in slides[1:]:
        cur_score, sol = find_best(s, sol, cur_score)
    return sol

def createOutput(sol, filename):
    file = open(filename[:-4]+"_output.txt", "w+")

    file.write(str(len(sol)))

    # slides = order_slides(slides)
    for s in sol:
        file.write("\n" + s[0])

    file.close()

def main(filename):
    slides = filestarter(filename)
    sol = greed(slides)
    createOutput(sol, filename)

# main("a_example.txt")
# main("b_lovely_landscapes.txt")
# main("c_memorable_moments.txt")
# main("d_pet_pictures.txt")
main("e_shiny_selfies.txt")
