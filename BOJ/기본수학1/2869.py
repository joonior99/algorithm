// 달팽이는 올라가고 싶다

// 땅 위에 있는 달팽이는 높이가 V미터인 나무 막대를 올라갈 것이다
// 달팽이는 낮에 A미터 올라갈 수 있지만, 밤에 잠을 자는 동안 B미터 미끄러지고, 정상에 올라간 후에는 미끄러지지 않는다
// 달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하는 프로그램을 작성하시오
// 첫째 줄에 세 정수 A, B, V가 공백으로 구분되어서 주어진다

import math

a, b, v = map(int, input().split())

day = math.ceil((v-a)/(a-b)) + 1 
print(day)

// 나무 높이를 기준으로 한 식은 (a-b)*n + a = v와 같다
// ceil 함수로 소수를 올림하여 정수로 변환하고 마지막에 a만큼 올라간 날을 고려하여 1을 더해준다

import sys
import math

a, b, v = map(int, sys.stdin.readline().split())
day = (v-b)/(a-b) // 정상에 한번 도달하면 밤에 미끄러지지 않는 것을 고려해준다
print(math.ceil(day))
