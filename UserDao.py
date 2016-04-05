__author__ = 'xbw'
import mysql.connector
class UserDao(object):
    pass
    #
    # def logincheck(self,user):
    #     self.conn = mysql.connector.connect(user='root', password='', database='test')
    #     self.cursor = self.conn.cursor()
    #     print "the username is " + user.username
    #     self.cursor.execute('select * from user where username = %s', [user.username])
    #     values = self.cursor.fetchall()
    #     if values[0][2] == user.password and values :
    #         print "login success"
    #         return True
    #     else:
    #         print "login fail"
    #         return False

    def findByName(self,username):
        conn = mysql.connector.connect(user='root', password='', database='test')
        cursor = conn.cursor()
        cursor.execute('select * from user where username = %s', [username])
        values = cursor.fetchall()
        if values:
            return values[0]
        else:
            return None