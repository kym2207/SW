'''
김유민
1: 3+6+9+12+...+N 형태로 3의 배수를 더한다.
2: 하나의 숫자를 입력받는다.
3: 3의 배수의 총합이 입력된 숫자를 넘었으 때의 N 값과 총합계, N 값이 몇 번째인지를 while 반복문을 사용해 프로그램작성하시오
#문제분석
    변수-반복횟수(i),총합(total),정수(su),카운트(c)
    수식-total+=i
#알고리즘
    변수선언
        i=0,total=0,s=0
    논리(반복)
        while 1:
            i+=1
            if i%3==0:
                s+=1
                if i >= su:
                    break
                total+=i
    결과 출력
'''
su=int(input("사용자 입력 : "))
i=1
total=0
c=0
while 1:
    if i%3==0:
        c+=1
        total+=i
        if total >= su:
            break   
    i+=1
    
print(su,"를 넘었을 때의 값 : ",i)
print(su,"를 넘었을 때까지의 총합계 : ",total)
print(su,"를 넘었을 때까지 몇 번째 3의 배수인가 : ",c)
