for i in range(0, 132):
    for j in range(0, 132):
        if (i ^ j) > 128:
            print(str(i), ", " + str(j))

print(pow(2, 6, 2))