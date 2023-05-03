'''
2023-05-03
김유민
1~10까지 합계 구하기
'''
#while
i=1
s=0
while i<=100:
    s=s+i
    i=i+1
print('1~100까지의 합계:',s)

s=0
for i in range(1,11):
    s=s+i
print('1~10까지의 합계:',s)