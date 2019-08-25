""" ---------------------------------
# 
#  class
# 
#   ----------------------------------
""" 

class UserDTO:
    

    def __init__(self):
        self.__userNum : int
        self.__userId : str
        self.__name : str
        self.__password : str
        self.__auth : int
        self.__gender : int
        self.__mail : str
            
    
    # setter
    def setAll(self, userNum:int, userId:str, name:str, password:str, auth:int, gender:int, mail:str):
        # print("start")
        self.__userNum = userNum
        self.__userId = userId
        self.__name = name
        self.__password = password
        self.__auth = auth
        self.__gender = gender
        self.__mail = mail
    
    def setAllByTuple(self, userList:tuple):    
        self.__userNum = userList[0]
        self.__userId = userList[1]
        self.__name = userList[2]
        self.__password = userList[3]
        self.__auth = userList[4]
        self.__gender = userList[5]
        self.__mail = userList[6]
        
    def setNum(self, userNum:int): # sequence使っているので使わない
        self.__userNum = userNum
    
    def setId(self, userId:str):
        self.__userId = userId
        
    def setName(self, name:str):
        self.__name = name
        
    def setPass(self, password:str):
        self.__password = password
    
    def setAuth(self, auth:int):
        self.__auth = auth
        
    def setGender(self, gender:int):
        self.__gender = gender
        
    def setMail(self, mail:str):
        self.__mail = mail

        
    # getter
    def getNum(self)->int:
        return self.__userNum
    
    def getId(self)->str:
        return self.__userId
    
    def getName(self)->str:
        return self.__name
    
    def getPass(self)->str:
        return self.__password
    
    def getAuth(self)->int:
        return self.__auth
    
    def getGender(self)->int:
        return self.__gender
    
    def getMail(self)->str:
        return self.__mail
    
    
    # print
    def printUser(self):
        print("num: " + str(self.__userNum))
        print("id: " + self.__userId)
        print("name: " + self.__name)
        print("pass: " + self.__password)
        print("auth: " + str(self.__auth))
        print("gend: " + str(self.__gender))
        print("mail: " + str(self.__mail))

    """    
    user = UserDTO()
    user.setAll(1,"smp1","pass1",1,"aaa")
    user.printUser()
    """
