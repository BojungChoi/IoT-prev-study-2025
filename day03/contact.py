# contact.py - 연락처를 담는 클래스
# 2. 클래스정의
class contact: # 클래스를 정의
    # 클래스에 속하는 함수들은 인자(매개변수)의 첫번째에 self를 반드시 기재!!!!!
    def __init__(self, name, phone, email, addr): # 객체 생성시 초기화 self는 무조건 적어줘야함.(나타나진않음)
        self.__name = name # 클래스 멤버변수에 함수 매개변수를 할당
        self.__phone = phone
        self.__email = email
        self.__addr = addr

    # 4. 사용자가 편하게 볼 수 있게 출력을 변경
    def __str__(self):
        str_res = ('이름:' + self.__name + '\n'
                   '핸드폰:' + self.__phone + '\n'
                   '이메일:' + self.__email + '\n'
                   '주소:' + self.__addr)
        return str_res
    
    # 11. 이름이 존재하는 객체 확인함수
    def isNameExist(self, name):
        if self.__name == name:
            return True # 같은 이름의 객체가 있어요!
        else:
            return False # 없네요..
        
    # 13. 각 멤버변수 가져오기
    def getName(self):
        return self.__name
    
    def getPhone(self):
        return self.__phone
    
    def getEmail(self):
        return self.__email
    
    def getAddr(self):
        return self.__addr
    