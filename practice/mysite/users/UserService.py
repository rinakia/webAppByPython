
"""
import TransactionManagerByPostgres as tmbp
import UserDAO as dao
import UserDTO as dto

from users.TransactionManagerByPostgres import TransactionManagerByPostgres as tmbp
from users.UserDAO import UserDAO as dao
from users.UserDTO import UserDTO as dto
"""

from users.TransactionManagerByPostgres import TransactionManagerByPostgres as tm
from users import UserDAO as dao
from users.UserDTO import UserDTO as dto


class UserService:
    # アトリビュート値 user
    #    def makeAttrFromDTO(request, dto1:dto.UserDTO):
    def makeAttrFromDTO(request, dto1:dto):
        user = {}
        if hasattr(userDTO, "_UserDTO__userNum" ):
            request.session['user_num'] = userDTO.getNum()
            # user['user_num'] = userDTO.getNum()
        if hasattr(userDTO, "_UserDTO__userId" ):
            request.session['user_id'] = userDTO.getId()
            # user['user_id'] = userDTO.getId()
        if hasattr(userDTO, "_UserDTO__name" ):
            request.session['user_name'] = userDTO.getName()
            # user['user_name'] = userDTO.getName()
        if hasattr(userDTO, "_UserDTO__password" ):
            request.session['user_pass'] = userDTO.getPass()
            # user['user_pass'] = userDTO.getPass()
        if hasattr(userDTO, "_UserDTO__auth" ):
            request.session['user_auth'] = userDTO.getAuth()
            # user['user_auth'] = userDTO.getAuth()
        if hasattr(userDTO, "_UserDTO__gender" ):
            request.session['user_gender'] = userDTO.getGender()
            # user['user_gender'] = userDTO.getGender()
        if hasattr(userDTO, "_UserDTO__mail" ):
            request.session['user_mail'] = userDTO.getMail()
            # user['user_mail'] = userDTO.getMail()
        return request
        # return user
        
    # ユーザログイン認証
    def loginCheck(request, userId, password):
        # tm = tmbp.TransactionManagerByPostgres()
        conn = tm.getConnection
        userDAO = dao.UserDAO(conn)
        userDTO = userDAO.getUserById(userId)
        conn.close()
        # id存在チェック
        if not hasattr(userDTO, "_UserDTO__userId" ):
            # print("存在しないユーザIDチェック id: " + userId)
            # raise IdExistError("存在しないユーザIDです")
            messageE = "存在しないユーザIDです"
            return messageE
        # パスワード認証チェック
        elif(userDTO.getPass() != password):
            # print("一致しないパスワードチェック id: " + userId)
            # raise PassCheckError("パスワードが異なります")
            messageE = "パスワードが異なります"
            return messageE
        else:
            userDTO.setPass(None)
            request = makeAttrFromDTO(request, userDTO)
            return request

