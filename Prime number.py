# PRIME NUMBER





# n=int(input("Enter the number:"))
# i=0
# while i<n:
#     j=1
#     count=0
#     while j<=n:
#         if i%j==0:
#             count=count+1
#         j=j+1
#     if count==2:
#             print(i, " is prime number")
#     i+=1





        # FOR LOOPS

# num=int(input("Enter the number:"))
# count=0
# for i in range (2,(num//2+1)):
#     count=count+1
#     break
# if (count==0 and num!=1):
#     print(num,"is a prime number")
# else:
#     print(num,"is not a prime number")
    
    # &

num=int(input("Enter the number:"))
if num>1:
    for i in range(2,num):
        if (num%i)==0:
            print(num,"is not a prime number")
            break
        else:
            print(num,"is a prime number")
else:
    print(num,"is not a prime number")
