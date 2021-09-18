// 정수 2개 입력받아 큰 값 출력하기

a, b = input().split()
a = int(a)
b = int(b)
c = a if a >= b else b
print(c)
