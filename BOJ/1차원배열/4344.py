// 평균은 넘겠지

// 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다
// 첫째 줄에는 테스트 케이스의 개수 C가 주어진다

n = int(input())

for _ in range(n):
  nums = list(map(int, input().split()))
  avg = sum(nums[1:])/nums[0] // nums[1:] 학생 수, nums[0] 점수
  cnt = 0
  for score in nums[1:]:
    if score > avg: // 평균 이상인 학생 수 
      cnt += 1
  rate = cnt/nums[0] * 100
  print(f'{rate: .3f}%') 
  
  // f-string 표기법으로 문자열을 작성하면 {} 중괄호를 이용하여 변수를 삽입할 수 있다
  // 소수점 셋째 자리까지 출력  
