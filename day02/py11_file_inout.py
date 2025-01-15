# py11_file_inout.py - 파일 입출력

# 쓰기
# a(추가) r(읽기) w(쓰기)
f = open('./day02/textfile.txt', mode='w', encoding='utf-8') # ./day02/ 를 붙히면 day02 파일 내에 txt 파일이 들어감 , incoding을 해줘야 글이 안깨짐 (���� �ѱ�����Դϴ�.)
# 아무것도 안함
f.write('나는 한국사람입니다.\n') 
f.write('남자입니다.')
f.close()

print('텍스트파일이 생성되었습니다.')

## 읽기
f = open('./day02/textfile.txt', mode='r', encoding='utf-8')

while True: # 무한반복
    line = f.readline() # 한줄씩 읽고
    if not line: break # 읽을 줄이 없으면 반복문 탈출

    print(line)

f.close()