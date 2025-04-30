# 6001
# print('Hello') 

# 6002
# print('Hello World')

# 6003
# print('Hello')
# print('World')

# 6004, 6005
# print("'Hello'")
# print('"Hello World"')

# 6006
# print("\"!@#$%^&*()'")

# 6007
# print("\"C:\\Download\\\'hello\'.py\"")

# 6008
# print('print("Hello\\nWorld")')

# 6009
# c=input()
# print(c)

# 6010
# n = input()
# n = int(n)
# print(n)

# 6011
# f = input()
# fcopy = float(f)
# print(fcopy)

# 6012
# a = input()
# b = input()
# a = int(a)
# b = int(b)
# print(a)
# print(b)

# 6013
# a = input()
# b = input()
# print(b)
# print(a)

# 6014
# num = input()
# num2 = float(num) 
# print(num2)
# print(num2)
# print(num2)

# 6015
# nums = input()
# num1, num2 = nums.split()
# a = int(num1)
# b = int(num2)
# print(a)
# print(b)

# 6016
# str1, str2 = input().split()
# print(str2, str1)

# 6017
# a = input()
# print(a, a, a)

# 6018
# time = input()
# hour, minute = time.split(':')
# print(hour, minute, sep=':')

# 6019
# date = input()
# year, month, day = date.split('.')
# print(day, month, year, sep='-')

# 6020
# rrn = input()
# rrn1, rrn2 = rrn.split('-')
# print(rrn1+rrn2)

# 6021 알파벳과 숫자로 이루어진 단어 1개가 입력된다.
# 입력받은 단어의 각 문자를 한 줄에 한 문자씩 분리해 출력한다.
# txt = input()
# chars = list(txt)
# print(*chars, sep='\n')

# 6022 (6자리의 연월일(YYMMDD)을 입력받아 나누어 출력해보자)
# print('연월일 입력(YYMMDD)')
# ymd = input()
# yy = ymd[0:2]
# mm = ymd[2:4]
# dd = ymd[4:]
# print(yy,mm,dd,sep=' ')

# 6023 (시:분:초 형식으로 시간이 입력될 때 분만 출력해보자)
# print('시:분:초 형식으로 입력')
# hsm = input()
# hsmList = hsm.split(':')
# print(f"{hsmList[1]}")

# 6024 (알파벳 문자와 숫자로 이루어진 단어 2개를 입력받아 순서대로 붙여 출력하는 프로그램을 작성해보자.)
# print("알파벳 문자와 숫자로 이루어진 문자 입력")
# print("알파벳 문자와 숫자로 이루어진 또 다른 문자 입력")
# txt1, txt2 = input().split()
# print(txt1 + txt2)


# 6025 (정수 2개를 입력받아 합을 출력하는 프로그램을 작성해보자)
# a, b = input().split()
# c = int(a) + int(b)
# print(c)

# 6026 (실수 2개를 입력받아 합을 출력하는 프로그램을 작성해보자)
# a = input()
# b = input()
# c = float(a) + float(b)
# print(c)

# 6027~6031 건너뛰기

# 6032 (정수 1개 입력받아 부호 바꾸기 - 설명 참고)
# num = int(input())
# result = -(num)
# print(result)

# 6033 (문자 1개를 입력받아 그 다음 문자를 출력해보자.)
# 영문자 'A'의 다음 문자는 'B'이고, 숫자 '0'의 다음 문자는 '1'이다.
    # ord() : 문자를 아스키코드(정수)로 변환
    # chr() : 아스키코드를 문자로 변환
# c = input()
# c1 = ord(c)
# c2 = c1+1
# c3 = chr(c2)
# print(c3)

# 6034 (정수 2개(a,b)를 입력받아 a에서 b를 뺀 차를 출력하는 프로그램)


# 6035 (실수 2개(f1, f2)를 입력받아 곱을 출력하는 프로그램을 작성해보자.)
# 6036 (단어와 반복 횟수를 입력받아 여러 번 출력해보자.)
# 6037 (반복 횟수와 문장을 입력받아 여러 번 출력해보자.)
# 6038 (정수 2개(a, b)를 입력받아 a를 b번 곱한 거듭제곱을 출력하는 프로그램을 작성해보자.)
# 6039 (정수 2개(a, b)를 입력받아 a를 b번 곱한 거듭제곱을 출력하는 프로그램을 작성해보자.)
# 6040 (정수 2개(a, b) 를 입력받아 a를 b로 나눈 몫을 출력해보자.)
# 6041 (정수 2개(a, b) 를 입력받아 a를 b로 나눈 나머지를 출력해보자.)


# 6042 실수 1개를 입력받아 소숫점 이하 두 번째 자리까지의 정확도로 반올림한 값을 출력
# fl = float(input())
# print(f"{fl:.2f}")


# 6043 (실수 2개(f1, f2)를 입력받아 f1 을 f2 로 나눈 값을 출력해보자. 이 때 소숫점 넷째자리에서 반올림하여 무조건 소숫점 셋째 자리까지 출력한다.)
# 6044 (정수 2개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 자동으로 계산해보자. 단, b는 0이 아니다.)

# 6045 정수 3개를 입력받아 합과 평균을 출력
# val = input()
# a, b, c = val.split()
# sum = int(a)+int(b)+int(c)
# avg = sum/3
# print(f"합:{sum} 평균:{avg:.2f}")

# 6048~~~





# 6025

# 6026 -----------

# 6032

