'''
2023-05-03
김유민
1~입력받은 숫자까지의 합계구하기
#문제 분석
    변수 정수(su),합계(sum),반복문(i)
    수식 s+=i
#알고리즘
    1.변수선언
        su에 정수입력
        sum=0
    2.논리(반복)
        for i in range(1,su+1):
            sum+=i
    3.결과출력
'''
su=int(input('합계 구할 숫자:'))
sum=0
for i in range(1,su+1):
    sum+=i
print('1~{}까지의 합은 : {}'.format(su,sum))

i=1
sum=0
while i<=su:
    sum+=i
    i+=1
print('1~{}까지의 합은 : {}'.format(su,sum))
