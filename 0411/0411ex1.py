'''
2023.04.11
김유민
선택문 if. if else

(1) 입력받은 성적이 80이상이면 '합격' 출력
    그리고 성적 상관없이 '수고하셨습니다' 출력

(2) 성적이 80이상이면 '합격' 출력
    성적이 80미만이면 '불합격'출력80
    그리고 성적 상관없이 '수고하셨습니다' 출력
'''
#단순if

score=int(input("점수 입력:"))#점수 정수로 입력

if score>=80:
    print('합격')
print('수고하셨습니다')

#if-else

jumsu=int(input("점수 입력:"))#점수 정수로 입력

if jumsu>=80:
    print('합격')
else: 
    print('불합격')
print('수고하셨습니다')


