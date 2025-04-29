# a && b
a = True
b = True
c = a and b
d = 10>5 and 10<5
# print(d) # false

f = 10>=10 or False
# print(f)


##
# aa = int(input())
# bb = int(input())
# cc = int(input())

### (조건)항을 3개 이상 and, or는 마음대로 연결하여 결과 출력
# print((aa==bb) or ((aa>bb) and (not(cc==aa))))
# print((bb<cc) or (aa<bb) or (aa>cc))
# print((aa!=bb) and (aa<bb) or (bb>cc))


# 멤버연산
st = "modulabs is good"
sta = "good" in st # in, not in


# 조건문
# age = 17
# if age > 18 :
#     print('성인입니다')

# print('안녕하세요')

# age = 35
# if age <= 19 :
#     print('청소년입니다.')
# elif age < 30 :
#     print('20대입니다.')
# else :
#     print('30대 이상입니다')

# 한줄에 생년월일(yyyy) 월(mm) 일(dd) 가 공백을 기준으로 입력된다.
# 년도가 짝수라면 "짝수 년도에 태어났습니다." 아니라면 "홀수 년도에 태어났습니다 를 출력)
print('생년월일(yyyy) 월(mm) 일(dd) 가 공백을 기준으로 입력하세요')
birth = input().split()
year = int(birth[0])
if (year%2) == 0 :
    print('짝수 연도에 태어났습니다')
else :
    print('홀수 연도에 태어났습니다')
