'''
2023-04-18
김유민
두 대의 숫자를 입력받아 두 숫자 사이의 홀수값을 모두 더하여 출력하는 프로그램
#문제분석
    변수
        정수1(su2),정수2(su2),모두더한값(s),반복문(i)
    수식
        s=s+i
#알고리즘
    변수선언
        입력받을 정수두개,홀수값을 더할 정수 하나, 반복문실행할 정수하나
    논리
        반복문
            su1과 su2사이 숫자 반복
        조건문
            if i%2==0:
                s=s+1
    결과출력
'''
su1=int(input("첫 번째수"))
su2=int(input("두 번째수"))
s=0
for i in range(su1,su2+1):
    if(i%2!=0):
        s=s+i
print(s)