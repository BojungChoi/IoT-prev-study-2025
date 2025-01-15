# py09_gugudan.py 구구단 프로그램
# 2 x 1 = 2 ~ 9 x 9 = 81

for i in range(2 , 10): # 2부터 9까지
    # print(i)
    for j in range(1, 10): 
        if j == 9: # 9단을 넣고싶지 않을 때 if문 활용
            break 
        # print(i * j) - 값만 출력
        print(i, 'x', j, '=' , i*j, end='\t')


    print()