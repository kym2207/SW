"""
2023-04-04
김유민
표준입력(input())함수 연습
"""

name=input('이름: ')#키보드로 이름을 입력박아서 name변수에 저장
score1=input('국어 점수: ')#키보드로 이름을 입력박아서 score1변수에 저장
score2=input('수학 점수: ')#키보드로 이름을 입력박아서 score2변수에 저장
print('{}의 점수 합계는 {}이다.'.format(name,score1+score2))
print('\n')
name=input('이름: ')#키보드로 이름을 입력박아서 name변수에 저장
jumsu1=int(input('국어 점수: '))#키보드로 이름을 입력박아서 score1변수에 저장
jumsu2=int(input('수학 점수: '))#키보드로 이름을 입력박아서 score2변수에 저장
print('{}의 점수 합계는 {}이다.'.format(name,jumsu1+jumsu2))