'''
2023.04.12
김유민
입력받은 두 수의 크기 비교
#문제분석
    변수-숫자1(num1),숫자2(num2)
#알고리즘
    1변수선언
        num1,num2에 정수 입력
    2.논리(선택)
        if num1>num2:
            큰 수 num1, 작은 수 num2
        else
            큰 수 num2, 작은 수 num1
'''


num1=int(input("첫 번째 수 입력 : "))
num2=int(input("두 번째 수 입력 : "))
if(num1>num2):
    print('두 수중에 큰 수는 ',num1,'이고 작은 수는',num2,'입니다')
else:
    print('두 수중에 큰 수는 ',num2,'이고 작은 수는',num1,'입니다')