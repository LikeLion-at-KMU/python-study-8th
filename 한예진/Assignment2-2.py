# 과제2-별찍기(역삼각형)
x=int(input("번호를 입력하세요: "))
for j in range(x,0,-1):
    for i in range(x+1-j):
        print(" ",end="")
    for i in range(2*j-1):
        print("*",end="")
    print()