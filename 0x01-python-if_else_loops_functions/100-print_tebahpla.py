#!/usr/bin/python3
j = 0
for i in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(i - j)), end="")
    if j == 0:
        j = 32
    else:
        j = 0
