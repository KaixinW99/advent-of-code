#
# test the code: python3 HotAir.py < test.dat
# check the time: time python3 HotAir.py < test.dat
total = 0
for line in open(0).read().splitlines():
    coef = 1
    for x in line[::-1]:
        total += ("=-012".find(x)-2)*coef
        coef *=5

output = ""
while total:
    rem = total%5
    total //= 5

    if rem <= 2:
        output = str(rem) + output
    else:
        output = "   =-"[rem] + output  # make up for the -1===(4) and (-2)===(3)
        total += 1                      # to get +1 in higher digit to compensate
print("Answer to Part 1:",output)
