n = int(input("n을 입력하세요"))
if 1<= n <= 100:
    for i in range(1, n+1):
        for j in range(i):
            print(" ", end=" ")
        for j in range((n - i + 1)*2-1):
            print("*", end=" ")
        print()
else:
    print("범위 안이 아닙니다.")