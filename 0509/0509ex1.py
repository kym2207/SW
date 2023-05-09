'''
2023-05-09
김유민
#문제정의
    두 개의 숫자를 입력 받아서 두 수 사이의 합계 구하기
#문제분석
    변수-정수1(num1),정수2(num2),합계(sum),빈복(i),임시변수(temp)
#알고리즘
    1. 변수선언(변수초기화)
        num1, num2는 정수를 입력 받는다.
        sum=0
    2. 프로그램 논리(선택,반복)
        2-1. (선택조건) - 항상 num1 <= num2
            if num1 < num2
                temp=num1
                num1=num2
                num2=temp
        2-2.(반복) - num1~num2 까지 1씩 증가하면서 더하기
            i=num1
            while num1 <= num2
                s+=num1
                num1+=1
    3. 결과 출력
'''
num1=int(input("첫 번째 숫자 : "))
num2=int(input("두 번째 숫자 : "))
s=0

if num2 < num1 :
    temp=num1
    num1=num2
    num2=temp
i=num1
while i <= num2 :
    s+=i
    i+=1
print("{} 부터 {} 까지의 합은 : {}".format(num1,num2,s))



'''
#문제정의
    두 개의 숫자를 입력 받아서 두 수 사이의 합계 구하기
#문제분석
    변수-정수1(num1),정수2(num2),합계(sum),빈복(i)
#알고리즘
    1. 변수선언(변수초기화)
        num1, num2는 정수를 입력 받는다.
        sum=0
    2. 프로그램 논리(선택,반복)
        2-1. (선택조건) - 항상 num1 <= num2
            if num1 < num2
                num1, num2 = num2, num1
        2-2.(반복) - num1~num2 까지 1씩 증가하면서 더하기
            i=num1
            while num1 <= num2
                s+=num1
                num1+=1
    3. 결과 출력

num1=int(input("첫 번째 숫자 : "))
num2=int(input("두 번째 숫자 : "))
s=0

if num2 < num1 :
    num1, num2 = num2, num1
i=num1
while i <= num2 :
    s+=i
    i+=1
print(f"{num1} 부터 {num2} 까지의 합은 : {s}")'''