def spiral_matrix():
    a = int(input())
    l = [[0 for b in range(a)] for i in range(a)]
    i, row, col, r, d = 0, 0, 0, True, True
    b1, c1, br, cr = 0, 0, a, a
    while i < a ** 2:
        i += 1

        l[row][col] = i

        if col == cr - 1 and r:
            r = False
            cr -= 1
        elif col == c1 and not r:
            c1 += 1
            r = True

        if row != b1 and row == br - 1 and d:
            d = False
            br -= 1
        elif row == c1 and row != br - 1 and not d:
            b1 += 1
            d = True

        if (a ** 2) == i + 1 and (a ** 2) % 2 != 0:
            r = True
            d = True

        if r and d:
            col += 1
        elif d and not r:
            row += 1
        elif not r and not d:
            col -= 1
        else:
            row -= 1

    return l


for l1 in spiral_matrix():
    print(*l1)
