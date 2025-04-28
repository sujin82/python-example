# 입력 구현
# a = input()
# print("okay")

# 입력을 몇가지 변수에 담아서
# f-string, 문자붙이기, 문자반복하기 등 여러 기술을 활용해 출력하세요.
# userName = input()
# userPhone = input()
# print(f'아이디는 {userName}이고, 휴대폰번호는 {userPhone}입니다.')
# print('아이디 : ' + userName + ', ' + '휴대폰번호 : ' + userPhone)

# a = input()
# b = int(a) # 문자를 숫자로 변경
# print(type(b))

# s = 'weniv CEO licat'
# print(s.find('good')) # 해당값이 없으면 -1 반환
# # print(s.index('good')) # ValueError: substring not found
# print(s.find('weniv'))
# print(s.find('licat'))

# s2 = s.replace("CEO","CTO")
# print(s2)

s3 ="weniv-corp"
# s4, s5 = s3.split("-")
# print(s4, s5)

# print('키 몸무게 성별 나이 이름을 입력해주세요')
# profile = input()
# height, weight, gender, age, name =  profile.split()
# print(f'''
#     키 : {height},
#     몸무게 : {weight},
#     성별 : {gender},
#     나이 : {age},
#     이름 : {name} 
# ''')

# print(name*3)


# s20 = ['modu','labs','good']
# print("-".join(s20))

# print(True==1)
# print(False==0)

aa = 1
bb = 0
cc = -1
dd = "okay"
ff = ""

print(bool(aa))
print(bool(bb)) # false
print(bool(cc))
print(bool(dd))
print(bool(ff)) # false


xx = None
# print(xx)
print(bool(xx)) # false