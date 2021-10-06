// 숫자의 합

// N개의 숫자가 공백 없이 쓰여있고, 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오

n = int(input())
print(sum(map(int, input()))) // 공백없는 문자열인 점을 고려하여 map 함수로 각 자리수 int로 변환

n = input()
nums = input()
total = 0
for i in range(n):
  total += int(nums[i])
print(total)
