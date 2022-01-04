import sqlite3

class student:
    def __init__(self):
        self.name=input("Kindly provide Student Name: ")
        self.classroom=input("Kindly enter Student Classroom: ")
        self.age=int(input("Kindly enter the age: "))

        try:
            cursor = conn.execute('select max(Roll) from students where Class=?',(self.classroom,))
        except Exception as e:
            print("exception")
            self.roll=1
        else:
            val=cursor.fetchone()
            print(val)
            if val is None:
                self.roll = 1
                print("here")
            else:
                self.roll = val[0] + 1
                print(val[0],self.roll)
                print("not")

        path='E:\\Python\\Pycharm Programs'
        self.remarks_path = str(self.name)+str(self.classroom)+str(self.roll)
        self.marksheet_path = str(self.name)+str(self.classroom)+str(self.roll)+'Marksheet'

        self.insertdb()

    def insertdb(self):
        try:
            conn.execute(f'INSERT INTO students VALUES(?,?,?,?,?,?)',(self.roll,self.name,self.age,self.remarks_path,self.classroom,self.marksheet_path))
        except Exception as e:
            print("Unable to write in database",e)
        else:
            conn.commit()

    def display(self,roll):
        try:
            cursor=conn.execute('select * from students where roll=?',(roll,))
        except Exception as e:
            print("Unable to fetch",e)
        else:
            print(cursor.fetchone())

if __name__=="__main__":

    try:
        conn = sqlite3.connect('file:Library.db?mode=rw', uri=True)
    except Exception as e:
        print("Database does not exist")
        conn = sqlite3.connect('Library.db')
    finally:
        cursor = conn.execute('select name from sqlite_master where Type="table"')
        lst_tables = cursor.fetchone()
        if lst_tables is not None and 'students' in lst_tables:
            print("Table already present:students")
        else:
            conn.execute('''CREATE TABLE students
                (Roll INTEGER PRIMARY KEY ,
                Name           TEXT    NOT NULL,
                Age            INT     NOT NULL,
                Remarks        VARCHAR(100),
                Class          VARCHAR(50),
                Marksheet      VARCHAR(100));''')
            print("Table Successfully created")
    cursor=conn.execute('select * from students')
    print(cursor.fetchall())
    stud1=student()
    stud1.display(1)
    cursor = conn.execute('select * from students')
    print(cursor.fetchall())