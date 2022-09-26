input_list = []
index_position = []
#--------------------------------------------------------------------------
def main():
    f = open('C:\\Users\Eric\Desktop\My Programs\Text Files\spiral.in', 'r')
    for d in f:
        e = int(d)
        input_list.append(e)
    dimensions = input_list[0]
    if dimensions % 2 == 0:
        dimensions +=1
    for i in input_list[1:5]:
        index_position.append(find_index(create_spiral(dimensions), i))
    sum_adjacent_numbers(create_spiral(dimensions), index_position)

# returns integer sum of the numbers adjacent to n
#if n is outside the range return 0
#--------------------------------------------------------------------------
def sum_adjacent_numbers(spiral, n):
    adjacent_sum = 0
    counter = 0
    cardinal1 = ''
    cardinal2 = ''
    b = 0
    for a in spiral[0]:
        b +=1
    b -=1
    y1 = 0
    for i in n:
        counter +=1
    for p in range(counter):
        for l in index_position[p]:
            if y1 == 0:
                y = l
                y1 +=1
            else:
                x = l
                y1 -=1
        if (x+1) > b:
            cardinal1 = 'no_east'
            if (y-1) < 0:
                cardinal2 = "no_north"
            elif (y+1) > b:
                cardinal2 = "no_south"
        elif (x-1) < 0:
            cardinal1 = 'no_west'
            if (y-1) < 0:
                cardinal2 = "no_north"
            elif (y+1) > b:
                cardinal2 = "no_south"
        if cardinal1 == "no_east" and cardinal2 == "no_north":
            adjacent_sum = spiral[y+1][x] + spiral[y+1][x-1] + spiral[y][x-1]
        elif cardinal1 == "no_east" and cardinal2 == "no_south":
            adjacent_sum = spiral[y-1][x] + spiral[y-1][x-1] + spiral[y][x-1]
        elif cardinal1 == "no_west" and cardinal2 == "no_north":
            adjacent_sum = spiral[y+1][x] + spiral[y+1][x+1] + spiral[y][x+1]
        elif cardinal1 == "no_west" and cardinal2 == "no_south":
            adjacent_sum = spiral[y-1][x] + spiral[y-1][x+1] + spiral[y][x+1]
        elif cardinal1 == "no_east":
            adjacent_sum = spiral[y-1][x] + spiral[y-1][x-1] + spiral[y][x-1] + spiral[y+1][x] + spiral[y+1][x-1]
        elif cardinal1 == "no_west":
            adjacent_sum = spiral[y-1][x] + spiral[y-1][x+1] + spiral[y][x+1] + spiral[y+1][x+1] + spiral[y+1][x]
        elif cardinal1 == "no_north":
            adjacent_sum = spiral[y][x+1] + spiral[y][x-1] + spiral[y+1][x] + spiral[y+1][x-1] + spiral[y+1][x+1]
        elif cardinal1 == "no_south":
            adjacent_sum = spiral[y][x-1] + spiral[y][x+1] + spiral[y-1][x-1] + spiral[y-1][x] + spiral[y-1][x+1]
        else:
            adjacent_sum = spiral[y-1][x] + spiral[y-1][x+1] + spiral[y-1][x-1] + spiral[y][x-1] + spiral[y][x+1] + spiral[y+1][x] + spiral[y+1][x-1] + spiral[y+1][x+1]
        print(adjacent_sum)
#--------------------------------------------------------------------------
def find_index(spiral, inputs):
    our_number = inputs
    dimension = 0
    y_index = 0
    x_index = 0

    for i in spiral[0]:
        dimension +=1
    
    for i in range(dimension):
        y_index = i
        eric = spiral[i]
        for j in eric:
            if j == our_number:
                x_index = eric.index(j)
                break
        if j == our_number:
            break
    return(y_index, x_index)
#--------------------------------------------------------------------------
def create_spiral(dimensions):
    start_index = int(dimensions/2)
    x = start_index
    y = start_index
    x1 = 0
    incrementor = 1
    e_o = ''
    array = []
    even_list = [_ for _ in range(2, dimensions**2, 2)]
    for i in range(dimensions):
        array.append(even_list[i])
    break_time = 0
    list = [[0 for i in range(11)] for j in range(11)]
    list[y][x] = incrementor

    for i in array:
        if (array.index(i)+1) % 2 == 0:
            e_o = 'even'
        else:
            e_o = 'odd'
        for z in range(2):
            if x1 == 0 and e_o == 'odd':
                for a in range(int(i/2)):
                    incrementor += 1
                    if incrementor == (dimensions**2+1):
                        break_time = 1
                        break
                    x += 1
                    list[y][x] = incrementor
                    x1 +=1
            elif x1 == 0 and e_o == 'even':
                for b in range(int(i/2)):
                    incrementor += 1
                    if incrementor == (dimensions**2+1):
                        break_time = 1
                        break
                    x -=1
                    list[y][x] = incrementor
                    x1 +=1
            elif e_o == 'odd':
                for j in range(int(i/2)):
                    incrementor += 1
                    if incrementor == (dimensions**2+1):
                        break_time = 1
                        break
                    y +=1
                    list[y][x] = incrementor
                    x1 -=1
            elif e_o == 'even':
                for c in range(int(i/2)):
                    incrementor += 1
                    if incrementor == (dimensions**2+1):
                        break_time = 1
                        break
                    y -=1
                    list[y][x] = incrementor
                    x1 -=1
            if break_time == 1:
                break
        if break_time == 1:
            break
    return list

main()


