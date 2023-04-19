'''
2023-04-19
김유민
성별, 키, 몸무게를 입력받아 각각 '표준체중','과체중','비만 체중'을 출력하고, 성별이 맞지 않는 경우 '성별 입력이 잘못 되었습니다.'를 출력하는 프로그램
#문제분석
    변수-성별(sex), 키(hei), 몸무게(wei) ,표준체중(avg)
    수식-avg=hei*hei*22, avg=hei*hei*21, wei/avg*100
#알고리즘
    변수선언
        성별, 키, 몸무게, 표준체중 선언
    논리(선택 if elif else)
        if(sex=='M' or sex=='m'):
            avg=hei*hei*21
            if 110<= wei/avg*100 <= 119:
             과체중
            elif wei/avg*100 <= 120:
                비만체중
            else
                표준체중
        elif(sex=='F' of sex=='f')
            avg=hei*hei*21
            if 110<= wei/avg*100 <= 119:
             과체중
            elif wei/avg*100 <= 120:
                비만체중
            else
                표준체중
    '''
sex=input("성별 입력('M' or 'm' 또는 'F' or 'f'):")
hei=float(input("키 입력(cm):"))/100
wei=float(input("몸무게 입력(kg):"))

if(sex=='M' or sex=='m'):
    avg=hei*hei*22
    if 110<= wei/avg*100 <= 119 :
        print("과체중")
    elif wei/avg*100 <= 120 :
        print("비만체중")
    else:
        print("표준체중")
elif(sex=='F' or sex=='f') :
    avg=hei*hei*21
    if 110<= wei/avg*100 <= 119 :
        print("과체중")
    elif wei/avg*100 <= 120 :
        print("비만체중")
    else:
        print("표준체중")
else:
    print("성별 입력이 잘못 되었습니다.")