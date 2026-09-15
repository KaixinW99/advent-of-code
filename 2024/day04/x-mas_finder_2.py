#
# test the code: python x-mas_finder_2.py < input.txt
# check the time: time python x-mas_finder_2.py < input.txt
x_mas_num = 0
words_map = open(0).read().split()
x_mas_map = [["." for _ in range(len(words_map[0]))] for _ in range (len(words_map))]
x_mas_flag = False
for i in range(len(words_map)):
    for j in range(len(words_map[0])):
        if j < len(words_map[0]) - 2 and i < len(words_map) - 2 and words_map[i][j] == "M" and words_map[i][j+2] == "S" and words_map[i+1][j+1] == "A" and words_map[i+2][j] == "M" and words_map[i+2][j+2] == "S":
            # M . S
            # . A .
            # M . S
            x_mas_num += 1
            x_mas_map[i][j] = "M"; x_mas_map[i][j+2] = "S"; x_mas_map[i+1][j+1] = "A"; x_mas_map[i+2][j] = "M"; x_mas_map[i+2][j+2] = "S"
        if j < len(words_map[0]) - 2 and i < len(words_map) - 2 and words_map[i][j] == "S" and words_map[i][j+2] == "M" and words_map[i+1][j+1] == "A" and words_map[i+2][j] == "S" and words_map[i+2][j+2] == "M":
            # S . M
            # . A .
            # S . M
            x_mas_num += 1
            x_mas_map[i][j] = "S"; x_mas_map[i][j+2] = "M"; x_mas_map[i+1][j+1] = "A"; x_mas_map[i+2][j] = "S"; x_mas_map[i+2][j+2] = "M"
        if j < len(words_map[0]) - 2 and i < len(words_map) - 2 and words_map[i][j] == "M" and words_map[i][j+2] == "M" and words_map[i+1][j+1] == "A" and words_map[i+2][j] == "S" and words_map[i+2][j+2] == "S":
            # M . M
            # . A .
            # S . S
            x_mas_num += 1
            x_mas_map[i][j] = "M"; x_mas_map[i][j+2] = "M"; x_mas_map[i+1][j+1] = "A"; x_mas_map[i+2][j] = "S"; x_mas_map[i+2][j+2] = "S"
        if j < len(words_map[0]) - 2 and i < len(words_map) - 2 and words_map[i][j] == "S" and words_map[i][j+2] == "S" and words_map[i+1][j+1] == "A" and words_map[i+2][j] == "M" and words_map[i+2][j+2] == "M":
            # S . S
            # . A .
            # M . M
            x_mas_num += 1
            x_mas_map[i][j] = "S"; x_mas_map[i][j+2] = "S"; x_mas_map[i+1][j+1] = "A"; x_mas_map[i+2][j] = "M"; x_mas_map[i+2][j+2] = "M"
print(x_mas_num)
if x_mas_flag:
    for i in range(len(x_mas_map)):
        print("".join(x_mas_map[i]))
