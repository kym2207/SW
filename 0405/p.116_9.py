'''
2023-04-05
김유민
본봉 수당을 입력받아서 수령액 구하기(p.116_9)
'''

bon=int((input("본봉"))) #본봉 입력
su=int((input("수당"))) #수당 입력
se=(bon+su)*0.2 #세금 구하기
print("수령액:",bon+su-se) #수령액 구하기, 결과출력
