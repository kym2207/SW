'''
2023-04-18
김유민
두 과목 모두 75이상 그리고 초점 180이상 "최우수"
총점 160이상 보통 150아상 "보통"
두 과목 모두 75미만이면 "분발 합시다."
#문제분석
    변수:점수1(score1),점수2(score2),합계(total)
#알고리즘
    1.변수선언
        score1,score2에 점수 입력 받기
        수식 total=score1+score2
    2.논리(선택 - 중첩if)
        if (score1>=75)and(score2>=75) 
            if(total)>=180:
                "최우수"
            elif (total)>=160
                "우수"
            else
                "보통"
        else:
            "분발 합시다."
'''
score1=int(input("성적1입력:"))
score2=int(input("성적2입력:"))

total=score1+score2
if score2 >=75 and score1 >= 75:
    if total >=180:
        print("최우수")
    elif total >= 160:
        print("우수")
    else:
        print("보통")
else:
    print("분발합시다.")