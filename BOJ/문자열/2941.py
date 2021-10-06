// 크로아티아 알파벳

// 단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='] // 두, 세 글자로 이루어진 알파벳을 한 글자로 변환 
word = input()

for i in croatia:
  word = word.replace(i, '*') // input과 동일한 이름의 변수 사용, 동일한 문자가 없으면 변환하지 않고 있다가 동일한 문자가 있으면 * 기호로 변환
print(len(word))
