a = 7
b = 5

# a = a*b
# b = a / b
# a = a / b
# print(a)
# print(b)

# n = a if a > b else 0

# print(f"the value of n is {n}")


# def sumofproducts(n,q):
#     sum = 0
#     product = 1
#     if q == 1:
#         for i in range(1,n+1):
#             sum = sum + i
#         return sum
#     elif q == 0:
#         for i in range(1,n+1):
#             product = product * i
#         return product

# rows = int(input())

# for i in range(0,rows):
#     for j in range(0,i + 1):
#         print("*", end = "  ")
#     print()

# for i in range(rows):
#     for j in range(i , rows-1):
#         print("_", end = " ")
#     for j in range(i+1):
#         print("*", end = " ")
#     for j in range(i):
#         print("*", end = " ")
#     print()

# def numpat(n):
#     ans = []
#     for i in range(n):
#         temp = i + 1
#         tempstr = int()
#         for j in range(i+1):
#             tempstr = tempstr + temp
#             temp = temp + 1
#         ans.append(tempstr)
#         # print()
#     return ans

# print(numpat(7))

## SETS________________________
# print(a,b)

# data = [1,-4,6,70,6,4,-1]

# for ind , num in (enumerate(data)):
#     if num < 0:
#         data[ind] = 0
#         print(ind)

# print(data)

# a = [1,2,3,4,3,2,1,32,3,4,3,2,1,2,0]
# b = [6,7,8,9,6,3,4,2,1]
# for i in zip(a,b):
#     print(i)

# for i , d in enumerate(zip(a,b)):
#     print(i,d)

# size = 4

# [print(["0" for count in range(size)]) for count in range(size)]

def quad(a,b,c):
    return lambda x: a*x**2 + b*x + c
f = quad(2,3,-5)
f(2)
print("Sudhar jaa")
quad(3,0,1)(2)