# A
# B  B
# C  C  C
# D  D  D  D
# E   E  E   E   E



i=0
while i<5:
    print(" "*(4-1),end=" ")
    j=0
    while j-1<i:
        print(chr(65+i),end=" ")
        j+=1
    print()
    i+=1

