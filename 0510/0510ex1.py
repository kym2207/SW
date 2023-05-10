'''
2023-05-10
김유민
#문제정의
    입력받은 숫자가 소수인지 아닌지 판별하는 프로그램
#문제분석
    변수-숫자(num)
#알고리즘
    1.변수 초기화
        num에 정수 입력
    2. 논리(반복안에 선택 포함)
        (반복) for i in range(2,num+1):
                if num%i==0:
                    break

'''
num=int(input('소수 검증 숫자 입력 : '))
for i in range(2,num+1):
    if num%i==0:
        break
if num==i:
    print(f'{num}은(는) 소수.')
else:
    print(f"{num}은(는) 소수아님")
print("소수 판별 프로그램을 이용해주셔서 감사합니다")