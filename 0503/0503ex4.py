'''
2023-05-03
김유민
#문제정의
    입력받은 구구단 출력 하기
#문제분석
    변수-단(dan),반복횟수(i)
#알고리즘
    1.변수선언
        dan은 정수로 입력
        i=1
    2.논리(반복-while)
        (조건)while i<=9
                구구단 출력
'''
dan=int(input('단 입력:'))
print(dan,'단')
i=1
while i<=9:
    print('{} * {} = {}'.format(dan,i,dan*i))
    i=i+1