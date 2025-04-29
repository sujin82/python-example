# a && b
a = True
b = True
c = a and b
d = 10>5 and 10<5
# print(d) # false

f = 10>=10 or False
# print(f)


##
aa = int(input())
bb = int(input())
cc = int(input())

### (조건)항을 3개 이상 and, or는 마음대로 연결하여 결과 출력
print((aa==bb) or ((aa>bb) and (not(cc==aa))))
print((bb<cc) or (aa<bb) or (aa>cc))
print((aa!=bb) and (aa<bb) or (bb>cc))


