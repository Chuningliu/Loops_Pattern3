#             1    
#           1 2 
#         1 2 3 
#       1 2 3 4 
#     1 2 3 4 5

# CORRECT:

i=6
while i>1:
    j=1
    while j<i-1:
        print(" ",end=" ")
        j+=1
    while j<6:
        print(j-i+2,end=" ")
        j+=1
    print( )
    i-=1


# &


# i=1
# while i<=5:
#     j=1
#     while j<=5-i:
#         print(" ", end=" ")
#         j+=1
#     b=1
#     while b<=i:
#         print(b,end=" ")
#         b+=1
#     print()
#     i+=1



 # n=int(input("Enter rows:"))
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ", end=" ")
#     for j in range(i+1):
#         print(j+1,end=" ")
#     print()
# i=5
# while i>=1:
#     j=5
#     while j>=i:
#         print(i,end=" ")
#         j-=1
#     print()
#     i-=1
# ab)

# i=1
# while i<=5:
#     b=5
#     while b>=i:
#         print(" ",end="")
#         b-=1
#     j=1
#     while j<=i:
#         print(i,end=" ")
#         j+=1
#     print()
#     i+=1                               


