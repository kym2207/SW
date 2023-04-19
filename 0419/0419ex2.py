'''
2023-04-19
김유민
입력된 수가 양수, 0, 음수인지 판별하는 프로그램
#문제분석
    변수-정수(num)
    논리(선택)
        if num>0
            양수
        if num==0
            0
        if num<0
            음수
        
        if num>0
            양수
        elif num==0
            0
        else
            음수
'''
num=int(input("숫자 입력 : "))
if num>0:
    print("입력값 %d은(는) 양수입니다."%num)
if num<0:
    print("입력값 %d은(는) 음수입니다."%num)
if num==0:
    print("입력값 %d은(는) 0입니다."%num)

if num>0:
    print("입력값 %d은(는) 양수입니다."%num)
elif num<0:
    print("입력값 %d은(는) 음수입니다."%num)
else:
    print("입력값 %d은(는) 0입니다."%num)