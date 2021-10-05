// 최소, 최대

// N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오

n = int(input())
arr = list(map(int, input().split()))
print(min(arr), max(arr))

n = int(input())
arr = list(map(int, input().split()))
arr.sort() // sort() 함수 사용시 오름차순으로 정렬
print(arr[0], arr[-1]) // index의 처음과 마지막을 출력
