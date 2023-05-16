'''
2023-05-16
김유민
파일 입출력
'''
ft=open("C:/data/test.txt","w")#파일 객체 ft 생성(쓰기)

for i in range(1,11): #10번 반복
    ft.write("%d번째 줄입니다.\n"%i)

ft.close()

