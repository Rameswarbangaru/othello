count1=0
count0=0
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> FLIPING FUNCTOION >>
def fun(x,y,n):
    global count1,count0
    count=0
    if l[y][x] != 0 and l[y][x] != 1:
        # VERTICAL UPWARD:
        for i in range(y + 1, 8):
            if l[i][x] == -1:
                break
            if l[i][x] == n:
                for j in range(y + 1, i):
                    l[j][x] =n
                    count += 1
                break

        # VERTICAL DOWNWARD:
        for i in range(y - 1, -1, -1):
            if l[i][x] == -1:
                break
            if l[i][x] == n:
                for j in range(i + 1, y):
                    l[j][x] =n
                    count += 1
                break

        # HORIZONTAL LEFT:
        for i in range(x - 1, -1, -1):
            if l[y][i] == -1:
                break
            if l[y][i] ==n:
                for j in range(i + 1, x):
                    l[y][j] = n
                    count += 1
                break

        # HORIZONTAL RIGHT:
        for i in range(x + 1, 8):
            if l[y][i] == -1:
                break
            if l[y][i] == n:
                for j in range(x + 1, i):
                    l[y][j] = n
                    count += 1
                break

        # DIAGONAL RIGHT UPWARD:
        for i in range(x + 1, 8):
            if -1 < (y + (i - x)) < 8 and -1 < i < 8:
                if l[y + (i - x)][i] == -1:
                    break
                if l[y + (i - x)][i] == n:
                    for j in range(x + 1, i):
                        l[y + (j - x)][j] = n
                        count += 1
                    break

        # DIAGONAL LEFT UPWARD:
        for i in range(x - 1, -1, -1):
            if -1 < (y - (i - x)) < 8 and -1 < i < 8:
                if l[y - (i - x)][i] == -1:
                    break
                if l[y - (i - x)][i] ==n:
                    for j in range(x - 1, i, -1):
                        l[y - (j - x)][j] =n
                        count+=1
                    break

        # DIAGONAL RIGHT DOWNWARD:
        for i in range(x + 1, 8):
            if (y - (i - x)) < 8 and -1 < i < 8:
                if l[y - (i - x)][i] == -1:
                    break
                if l[y - (i - x)][i] == n:
                    for j in range(x + 1, i):
                        l[y - (j - x)][j] = n
                        count += 1
                    break

        # DIAGONAL LEFT DOWNWARD:
        for i in range(x - 1, -1, -1):
            if (y + (i - x)) < 8 and -1 < i < 8:
                if l[y + (i - x)][i] == -1:
                    break
                if l[y + (i - x)][i] == n:
                    for j in range(x - 1, i, -1):
                        l[y + (j - x)][j] = n
                        count += 1
                    break
        if count == 0:
            count = 0
            print("Try another position")
        if count > 0:
            l[y][x] = n
    else:
        print("over other")
    count1=0
    count0=0
    for i in range(0,8):
        for j in range(0,8):
            if l[i][j]==0:
                count0+=1
                # print(f"({j},{i} is black)")
            elif l[i][j]==1:
                count1+=1
                # print(f"({j},{i} is white)")
    print("Black: ",count0)
    print("white: ",count1)
    return count
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CHOICE  SHOWING  FUNCTION   >>>>
def fun1(x,y,n):
    l1=[row[:] for row in l]
    count=0
    if l1[y][x] != 0 and l1[y][x] != 1:
            # VERTICAL UPWARD:
            for i in range(y + 1, 8):
                if l1[i][x] == -1:
                    break
                if l1[i][x] == n:
                    for j in range(y + 1, i):
                        l1[j][x] =n
                        count += 1
                    break

            # VERTICAL DOWNWARD:
            for i in range(y - 1, -1, -1):
                if l1[i][x] == -1:
                    break
                if l1[i][x] == n:
                    for j in range(i + 1, y):
                        l1[j][x] =n
                        count += 1
                    break

            # HORIZONTAL LEFT:
            for i in range(x - 1, -1, -1):
                if l1[y][i] == -1:
                    break
                if l1[y][i] ==n:
                    for j in range(i + 1, x):
                        l1[y][j] = n
                        count += 1
                    break

            # HORIZONTAL RIGHT:
            for i in range(x + 1, 8):
                if l1[y][i] == -1:
                    break
                if l1[y][i] == n:
                    for j in range(x + 1, i):
                        l1[y][j] = n
                        count += 1
                    break

            # DIAGONAL RIGHT UPWARD:
            for i in range(x + 1, 8):
                if -1 < (y + (i - x)) < 8 and -1 < i < 8:
                    if l1[y + (i - x)][i] == -1:
                        break
                    if l1[y + (i - x)][i] == n:
                        for j in range(x + 1, i):
                            l1[y + (j - x)][j] = n
                            count += 1
                        break

            # DIAGONAL LEFT UPWARD:
            for i in range(x - 1, -1, -1):
                if -1 < (y - (i - x)) < 8 and -1 < i < 8:
                    if l1[y - (i - x)][i] == -1:
                        break
                    if l1[y - (i - x)][i] ==n:
                        for j in range(x - 1, i, -1):
                            l1[y - (j - x)][j] =n
                            count+=1
                        break

            # DIAGONAL RIGHT DOWNWARD:
            for i in range(x + 1, 8):
                if (y - (i - x)) < 8 and -1 < i < 8:
                    if l1[y - (i - x)][i] == -1:
                        break
                    if l1[y - (i - x)][i] == n:
                        for j in range(x + 1, i):
                            l1[y - (j - x)][j] = n
                            count += 1
                        break

            # DIAGONAL LEFT DOWNWARD:
            for i in range(x - 1, -1, -1):
                if (y + (i - x)) < 8 and -1 < i < 8:
                    if l1[y + (i - x)][i] == -1:
                        break
                    if l1[y + (i - x)][i] == n:
                        for j in range(x - 1, i, -1):
                            l1[y + (j - x)][j] = n
                            count += 1
                        break
    return count