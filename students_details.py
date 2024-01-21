import mysql.connector

class Students:
    # Class variable to store the database connection
    db_conn = None

    # required details of the student
    def __init__(self, name, marks1, marks2):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
    
    @classmethod
    def db_connection(cls):
        # Check if the connection is already established
        if cls.db_conn is None:
            # If not, create a new connection
            cls.db_conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='1234',
                database='school_mng',
                auth_plugin='mysql_native_password'
            )
        return cls.db_conn

    @classmethod
    def add_student(cls, cursor, details):
        try:
            query = "INSERT INTO STUDENTS (Name, marks1, marks2) VALUES (%s, %s, %s)"
            values = (details.name, details.marks1, details.marks2)
            cursor.execute(query, values)
            db_conn.commit()

            print("Student details added Successfully")

        except Exception as e:
            print(f"Error Occurred {e}")

    @staticmethod
    def view_student(cursor, rollno):
        try:
            query = "SELECT * FROM STUDENTS WHERE Roll_No = %s"
            cursor.execute(query, (rollno,))
            result = cursor.fetchone()
            if result:
                print('Student Details:')
                print(f"Name : {result[1]}")
                print(f"Roll No : {result[0]}")
                print(f"marks1 : {result[2]}")
                print(f"marks2 : {result[3]}")

            else:
                print('Student Not Found')

        except Exception as e:
            print(f"Error Occurred {e}")

    @staticmethod
    def view_all_students(cursor):
        try:
            query = "SELECT * FROM STUDENTS"
            cursor.execute(query)
            results = cursor.fetchall()

            if results:
                print("All Students")
                for result in results:
                    print(f"Name: {result[1]}, Roll No: {result[0]}, marks1: {result[2]}, marks2: {result[3]}")
            else:
                print("No Students Found")

        except Exception as e:
            print(f"Error Occurred {e}")

    @staticmethod
    def update_student(cursor, rollno, **kwargs):   
    
        try:
            set_clause = ", ".join(f"{field} = %s " for field in kwargs)
            query = f"UPDATE STUDENTS SET {set_clause} WHERE Roll_No= %s"
            values = [kwargs[field] for field in kwargs] + [rollno]
            cursor.execute(query, values)

            print("Student details updated successfully")

        except Exception as e:
            print(f"Error Occurred {e}")

    @staticmethod
    def delete_student(cursor, rollno):
        try:
            query = "DELETE FROM STUDENTS WHERE Roll_No = %s"
            cursor.execute(query, (rollno,))

            print("Student details Deleted Successfully")
            db_conn.commit()

        except Exception as e:
            print(f"Error Occurred {e}")

    @staticmethod
    def delete_all_students(cursor):
        try:
            query = "DELETE FROM STUDENTS"
            cursor.execute(query)
            print("All Students deleted successfully")

            db_conn.commit()

        except Exception as e:
            print(f"Error Occurred {e}")

# Usage example
# student2 = Students(name='RS', marks1=87, marks2=59)

db_conn = Students.db_connection()
cursor = db_conn.cursor()

# The following line will automatically assign a roll_no
# Students.add_student(cursor, student2)
# Students.update_student(cursor, 2,marks2= 16, marks1=41)
# Students.view_student(cursor, 2)
# Students.delete_student(cursor, 1)
Students.view_all_students(cursor)
db_conn.commit()
db_conn.close()
