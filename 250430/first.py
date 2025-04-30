# split() 활용
# a,b 변수에 키,몸무게 입력 받기
# 키와 뭄무게를 나눈 나머지 출력
# 조건문을 활용해서 키가 130 이상이면 a,
# 150 이상이면 b,
# 170 이상이면 c,
# 180 이상이면 d 출력
# a, b = input().split()
# height = float(a)
# weight = float(b)
# result = height % weight
# print(f"나머지 : {result:.2f}")

# if height >= 180 :
#     print('d')
# elif height >= 170 :
#     print('c')
# elif height >= 150 :
#     print('b')
# elif height >= 130 :
#     print('a')
# else :
#     print('아직 어린이?')
    

# 시험 점수를 입력받아 90~100점은 A, 
# 80~89점은 B, 70~79점은 C,
# 60~69점은 D, 나머지 점수는 F 출력
# score = int(input())
# if score < 0 or score > 100 :
#     print('0~100점 입력하세요')
# else :    
#     if score >= 90 :
#         print('A')
#     elif score >= 80 :
#         print('B')
#     elif score >= 70 :
#         print('C')
#     elif score >= 60 :
#         print('D')
#     else :
#         print('F')

# 주사위(1~6까지) 3개를 던져 아래와 같은 규칙에 따라 상금을 받는 게임
    # 같은 눈이 3개가 나오면 10,000 + (같은눈)*1000
    # 같은 눈이 2개가 나오면 1,000 + (같은눈)*100
    # 모두 다른 눈이 나오는 경우 (그 중 가장 큰 눈)*100



# 조건 3개
# 열외 : 1~6만 입력 가능하도록 해야함 ################
num1, num2, num3 = input().split()
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
if num1 == num2 == num3 :
    price = 10000 + num1 * 1000
elif num1 == num2 or num1 == num3 :
    price = 1000 + (num1 * 100)
elif num2 == num3 :
    price = 1000 + (num2 * 100)
else :
    maxNum = num1
    if num2 > maxNum :
        maxNum = num2
    if num3 > maxNum :
        maxNum = num3
    price = maxNum * 100

# if num1!=num2 and num2!=num3 and num1!=num3 :
#     temp = num1
#     if num2 > temp :
#         temp = num2
#     if num3 > temp :
#         temp = num3
#     price = temp * 100

print(f"주사위 눈 : {num1}, {num2}, {num3}")
print(f"상금 {price:,}원")


