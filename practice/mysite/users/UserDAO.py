""" ---------------------------------
# 
#  class
# 
#   ----------------------------------
""" 
# from users import UserDTO as dto
from users.UserDTO import UserDTO as dto
import datetime
class UserDAO:
    
    # userDTO = dto.UserDTO()
    
    def __init__(self, connection):
        # super(self, connection)
        self.conn = connection

        
    def getAll(self) -> list:
        userDTOs = list()
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM account ORDER BY id;")
            for rs in cur:
                userDTO = dto.UserDTO()
                userDTO.setAllByTuple(rs)
                userDTOs.append(userDTO)
                # print(rs)
            cur.close()
        except InterfaceError as e:
            print("InterfaceError")
            print("connectionが見つかってないはず、")
            raise e
        finally:
            return userDTOs
        

    def getUserById(self, userId:str) -> dto:
        userDTO = dto.UserDTO()
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM account WHERE id = %s;",(userId,))
            userDTO.setAllByTuple(cur.fetchone())
            cur.close()
        except InterfaceError as e:
            print("InterfaceError")
            print("connectionが見つかってないはず、")
            raise e
        finally:
            return userDTO

#     def addUserByDTO(self, dto1:dto.UserDTO):
    def addUserByDTO(self, dto):
        # dto1 = dto.UserDTO()
        # dto1.setAll(1003, "test3", "smp1","pass1",1,1,"aaa")
        try:
            dt = datetime.date.today()
            cur = self.conn.cursor()
            cur.execute("INSERT INTO account(id, name, password, auth) VALUES (%s, %s, %s, %s)",(dto1.getId(), dto1.getName(), dto1.getPass(), dto1.getAuth(),))
            cur.execute("INSERT INTO account_date(id, regist_date) VALUES (%s, %s)",(dto1.getId(), dt)) #
            # コミット
            self.conn.commit()
            cur.close()
        except InterfaceError as e:
            print("InterfaceError")
            print("connectionが見つかってないはず、")
            raise e


