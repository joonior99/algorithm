// 베르트랑 공준

// 베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다
// 자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오
// 입력의 마지막에는 0이 주어진다
// 1 ≤ n ≤ 123,456

import math

nums = {x for x in range(2, 246_913) if x == 2 or x % 2 ==1} // 2부터 2n이라 할 수 있는 246,913까지의 자연수 범위에서 소수를 구하였으며, 여기서 2와 홀수로 이루어진 집합을 만들었다

for odd_num in range(3, int(math.sqrt(246_912))+1, 2): // 3부터 최댓값의 제곱근까지 홀수를 for 문으로 반복하여 해당 홀수의 배수로 이루어진 집합을 만들어서 빼주었다
    nums -= {i for i in range(2 * odd_num, 246_913, odd_num) if i in nums} // nums 집합의 차집합을 구하는 방식으로 소수의 집합을 구하는 것이다

while True:
    n = int(input())
    if n == 0:
        break  
    prime_list = [i for i in range(n+1, 2*n+1) if i in nums]
    
    print(len(prime_list))
