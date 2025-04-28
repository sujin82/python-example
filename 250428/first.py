# 정수
a = "10"
b = 20
c = 0
d = -40

print(type(a), type(b), type(c), type(d)) # 실제 출력해보면 값 사이에 ',(쉼표)'는 띄어쓰기 되서 출력됨
print(int(9.33333))


# 실수
number1 = 3.12
number2 = -0.12
print(type(number1),type(number2))
print(float(3))

# 무한대
inf = float("inf")

# 문자열
str1 = 'abcd'
str2 = "abcd"
str3 = '''
    오늘은 4월 28일입니다.

    5월이 멀지 않았네요.
'''
# print(str3)

# 개인정보 출력해보기
## 1. 성, 이름 변수를 따로 만들어서 +로 합친 후 출력
## 2. 주민등록번호도 1번과 같이
## 3. 이메일 {아이디} {@} {네이버, 구글}
lastName = "Ryu"
firstName = "sujin"
# print('이름 : ', firstName + ' ' + lastName)

ssn1 = "001231"
ssn2 = "1234567"
# print('주민등록번호 : ', ssn1 + '-' + ssn2)

emailId = "jin"
at = "@"
emailDomain = "gmail.com"
# print('이메일 : ', emailId + at + emailDomain)



str10 = str1 * 10
print(str10)
test2 = '30'
# print(str1 * test2) # 'abcd' * '30'

# 오늘은 4월 28일입니다.  # f-string
month = 4
day = 280
# print(f"오늘은 {month}월 {day}입니다")

s = "weniv CEO licat"
# print(s[0])
# print(s[100]) # IndexError: string index out of range (예외처리 필요)

# 문자열 슬라이싱 [start:stop:step]
# print(s[0:5])
# print(s[::-1])

#문제
# 1. ip address문자열을 슬라이싱 기법을 활용해 변수에 담아 출력
# 2. a,b,c,d 라는 변수에 슬라이싱 기법을 통해 .을 기준으로 각각 담는다
# 3. f-string을 사용해서 172100200100 문자 나오게 하기
ipAddr = "172.100.200.100"

addr1 = ipAddr[0:3]
addr2 = ipAddr[4:7]
addr3 = ipAddr[8:11]
addr4 = ipAddr[12:]

print(ipAddr)
print(addr1, addr2, addr3, addr4)
print(f'{addr1}{addr2}{addr3}{addr4}')

# 언팩킹 방식 : 각 부분을 한 번에 여러 변수에 할당하므로 코드가 간결해지고 가독성이 좋아집니다.
aa,bb,cc,dd = ipAddr[0:3], ipAddr[4:7], ipAddr[8:11], ipAddr[12:]
print(aa, bb, cc, dd)