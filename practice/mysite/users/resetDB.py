""" ---------------------------------
# 
#  reset DB
#
#  python3 mysite/users/resetDB.py 
# 
#  ver1. 19/08/22
# 
#   ----------------------------------
""" 

import datetime
import TransactionManagerByPostgres as tmbp
class ResetPostgresDB:
    def resetAccount(self):
        tm = tmbp.TransactionManagerByPostgres()
        conn = tm.getConnection()
        cur = conn.cursor()
        cur.execute("DROP TABLE IF EXISTS account_date;")
        cur.execute("DROP TABLE IF EXISTS account;")
        cur.execute("CREATE TABLE account(num serial UNIQUE, id varchar(20) PRIMARY KEY,  name varchar(20) NOT NULL, password varchar(20) NOT NULL, auth INTEGER NOT NULL, gender INTEGER, mail varchar(100));")
        cur.execute("CREATE TABLE account_date(id varchar(20) REFERENCES account (id), regist_date date, renew_date date);")
        cur.execute("SELECT SETVAL('account_num_seq', 1000);")
        dt = datetime.date.today()
        cur.execute("INSERT INTO account(id, name, password, auth) VALUES (%s, %s, %s, %s)",("user1","name1", "pass1", 1))
        cur.execute("INSERT INTO account_date(id, regist_date) VALUES (%s, %s)",("user1", dt)) #
        cur.execute("INSERT INTO account(id, name, password, auth) VALUES (%s, %s, %s, %s)",("user2","name2", "pass2", 2))
        cur.execute("INSERT INTO account_date(id, regist_date) VALUES (%s, %s)",("user2", dt)) #
        conn.commit()
        cur.close()
        conn.close()
        print("RESET DB END")
resetDB = ResetPostgresDB()
resetDB.resetAccount()
