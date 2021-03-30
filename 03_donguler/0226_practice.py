i, j = 0, 0
while i < 10:
    while j < 10:
        if i % 2 == 0:
            if j % 2 == 0 :
                print(" * ", end=" ")
            else:
                print(" $ ", end=" ")
        else:            
            if j % 2 == 0 :
                print(" $ ", end=" ")
            else:
                print(" * ", end=" ")

        j += 1
    j=0
    print()
    i += 1