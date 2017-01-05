import pymysql
import itertools

class DB_test():
    def ___ini___(self):
        self.date=[]
        self.Open=[]
        self.low=[]
        self.high=[]
        self.close=[]        
    
    def convert(self,Tuple):
        new=[list(item) for item in Tuple]
        Tuple = list(itertools.chain.from_iterable(new))
        return Tuple
        
        # Open database connection
    def connectAndload(self):
        db = pymysql.connect(host='127.0.0.1',port=3306, user='root', passwd='cc840724',db='stock')
        
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
    
        # instructions
        sql = "Select date FROM test "
        sql2= "Select open FROM test "
        sql3= "Select high FROM test "
        sql4= "Select low FROM test "
        sql5 = "Select close FROM test "
        #date
        cursor.execute(sql)
        self.date = cursor.fetchall()
        self.date = self.convert(self.date)
        #open
        cursor.execute(sql2)
        self.Open = cursor.fetchall()
        self.Open=self.convert(self.Open)
        #high
        cursor.execute(sql3)
        self.high = cursor.fetchall()
        self.high = self.convert(self.high)
        #low
        cursor.execute(sql4)
        self.low = cursor.fetchall()
        self.low = self.convert(self.low)
        #close
        cursor.execute(sql5)
        self.close = cursor.fetchall()
        self.close = self.convert(self.close)
        
        # disconnect from server        
        db.close()
    
    #drawing