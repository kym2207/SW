'''
2023-05-10
김유민
#문제정의
    입력받은 숫자 만큼 줄 반벅 하면서 별 찍기
#문제분석
    변수-숫자(num)
#알고리즘
    1. 변수 초기화
        num변수에 정수 입력
    2. 논리(중첩 반복)
        (반복) for i in range(1,num+1):
                    for j in range(1,i+1):
                        print("*",end='')
                    print()
                        
'''
num=int(input("숫자 입력 : "))

for i in range(1,num+1):
    for j in range(1,i+1):
        print("*",end="")
    print()
#거꾸로 출력
print("\n 거꾸로 출력")
for i in range(1,num+1):
    for j in range(i,num+1):
        print("*",end="")
    print()
