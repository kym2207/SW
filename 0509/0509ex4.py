'''
2023-05-09
김유민
#문제정의
    1-100까지의 입력받은 숫자의 배수만 더하기
#뮨재분석
    변수-정수(num), 합계(sum), 반복(i)
#알고리즘
    1.변수 초기화
        num변수에 정수 입력
        sum=0
        i=0
    2.프로그램 논리(반복while)
    while i<100:
        i+=1
        if i % num != 0:
            continue
        sum+=i
    3.결과 출력
'''
num=int(input("합을 원하는 배수 입력 : "))
sum=0
i=0
while i<100:
    i+=1
    if i % num != 0:
        continue
    sum+=i
print("1부터 100까지의 {}의 배수의 합은 : {}".format(num,sum))