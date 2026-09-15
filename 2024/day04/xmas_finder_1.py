#
# test the code: python xmas_finder_1.py < input.txt
# check the time: time python xmas_finder_1.py < input.txt
xmas_num = 0
words_map = open(0).read().split()
xmas_map = [["." for _ in range(len(words_map[0]))] for _ in range (len(words_map))]
xmas_flag = False
for i in range(len(words_map)):
    for j in range(len(words_map[0])):
        if j < len(words_map[0]) - 3 and words_map[i][j] == "X" and words_map[i][j + 1] == "M" and words_map[i][j + 2] == "A" and words_map[i][j + 3] == "S":
            # forward horizontal
            xmas_num += 1
            xmas_map[i][j] = "X"; xmas_map[i][j + 1] = "M"; xmas_map[i][j + 2] = "A"; xmas_map[i][j + 3] = "S"
        if j < len(words_map[0]) - 3 and words_map[i][j] == "S" and words_map[i][j + 1] == "A" and words_map[i][j + 2] == "M" and words_map[i][j + 3] == "X":
            # backward horizontal
            xmas_num += 1
            xmas_map[i][j] = "S"; xmas_map[i][j + 1] = "A"; xmas_map[i][j + 2] = "M"; xmas_map[i][j + 3] = "X"
        if i < len(words_map) - 3 and words_map[i][j] == "X" and words_map[i + 1][j] == "M" and words_map[i + 2][j] == "A" and words_map[i + 3][j] == "S":
            # forward vertical
            xmas_num += 1
            xmas_map[i][j] = "X"; xmas_map[i + 1][j] = "M"; xmas_map[i + 2][j] = "A"; xmas_map[i + 3][j] = "S"
        if i < len(words_map) - 3 and words_map[i][j] == "S" and words_map[i + 1][j] == "A" and words_map[i + 2][j] == "M" and words_map[i + 3][j] == "X":
            # backward vertical
            xmas_num += 1
            xmas_map[i][j] = "S"; xmas_map[i + 1][j] = "A"; xmas_map[i + 2][j] = "M"; xmas_map[i + 3][j] = "X"
        if i < len(words_map) - 3 and j < len(words_map[0]) - 3 and words_map[i][j] == "X" and words_map[i + 1][j + 1] == "M" and words_map[i + 2][j + 2] == "A" and words_map[i + 3][j + 3] == "S":
            # forward diagonal
            xmas_num += 1
            xmas_map[i][j] = "X"; xmas_map[i + 1][j + 1] = "M"; xmas_map[i + 2][j + 2] = "A"; xmas_map[i + 3][j + 3] = "S"
        if i < len(words_map) - 3 and j < len(words_map[0]) - 3 and words_map[i][j] == "S" and words_map[i + 1][j + 1] == "A" and words_map[i + 2][j + 2] == "M" and words_map[i + 3][j + 3] == "X":
            # backward diagonal
            xmas_num += 1
            xmas_map[i][j] = "S"; xmas_map[i + 1][j + 1] = "A"; xmas_map[i + 2][j + 2] = "M"; xmas_map[i + 3][j + 3] = "X"
        if i < len(words_map) - 3 and j > 2 and words_map[i][j] == "X" and words_map[i + 1][j - 1] == "M" and words_map[i + 2][j - 2] == "A" and words_map[i + 3][j - 3] == "S":
            # forward inverse diagonal
            xmas_num += 1
            xmas_map[i][j] = "X"; xmas_map[i + 1][j - 1] = "M"; xmas_map[i + 2][j - 2] = "A"; xmas_map[i + 3][j - 3] = "S"
        if i < len(words_map) - 3 and j > 2 and words_map[i][j] == "S" and words_map[i + 1][j - 1] == "A" and words_map[i + 2][j - 2] == "M" and words_map[i + 3][j - 3] == "X":
            # backward inverse diagonal
            xmas_num += 1
            xmas_map[i][j] = "S"; xmas_map[i + 1][j - 1] = "A"; xmas_map[i + 2][j - 2] = "M"; xmas_map[i + 3][j - 3] = "X"
print(xmas_num)

if xmas_flag:
    for i in range(len(xmas_map)):
        print("".join(xmas_map[i]))