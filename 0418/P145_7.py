'''
2023-04-18
김유민
3장 연습문제 7번
두 정수 입력 x<y->x//y,x<y->x+y,x==y->x*y
단, 나눗셈의 몫 계산할 때 y는 0 안됨
'''
x=int(input("x의 값"))
y=int(input("y의 값"))

if(x>y):
    if(y>0):
        print("x // y=",x//y)
    else:
        print("y의 값이 0입니다.")
elif(x<y):
    print("x + y=",x+y)
else:
    print("x * y=",x*y)
