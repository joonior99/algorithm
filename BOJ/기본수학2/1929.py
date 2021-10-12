// 소수 구하기

// M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오

import math
import sys

def isPrime(num): 
  if num == 1: // 1은 소수가 아니므로 false 반환
    return false
  sq = int(math.sqrt(num)) // 제곱근까지만 확인
  for i in range(2, sq+1):
    if num%i == 0: // 나누어진다면 소수가 아니므로 false 반환
      return false
    return true
  
m, n = map(int, sys.stdin.readline().split())

for i in range(m, n+1):
  if isPrime(i):
    print(i)
