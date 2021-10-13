// 큰 수 A+B

// 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오

import sys

a, b = map(int, sys.stdin.readline().split())
print(a+b)

// 파이썬은 메모리양이 정해져 있는 fixed-precision이 아닌, arbitrary-precision이어서 메모리를 유동적으로 운용할 수 있다
