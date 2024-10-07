import psycopg2 as pg
from config import config

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = pg.connect(**params)
        
        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        return conn
    except (Exception, pg.DatabaseError) as error:
        print(error)
        if conn is not None:
            conn.close()
        return None

class UserProfile:
    @staticmethod
    def create_tables(cur):
        command = '''
        CREATE TABLE IF NOT EXISTS user_profile (
            user_id SERIAL PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            age INTEGER NOT NULL,
            gender VARCHAR(20) NOT NULL,
            height FLOAT NOT NULL,
            weight FLOAT NOT NULL
        );
        '''
        try:
            cur.execute(command)
        except Exception as e:
            print(f"Error creating table: {e}")
            raise

    def __init__(self):
        self.conn = connect()
        if self.conn is None:
            raise Exception("Failed to connect to the database")
        
        self.cur = self.conn.cursor()
        UserProfile.create_tables(self.cur)
        self.conn.commit()

        self.user_id = None
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))
        self.gender = input("Enter your gender: ")
        self.height = float(input("Enter your height in cm: "))
        self.weight = float(input("Enter your weight in kg: "))
        #self.activity_level = input("Enter your activity level: ")
        #self.goal = input("Enter your fitness goal: ")
        #self.allergies = input("Enter any allergies: ")

    def save_to_database(self):
        sql = '''
        INSERT INTO user_profile (name, age, gender, height, weight)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING user_id;
        '''
        try:
            self.cur.execute(sql, (self.name, self.age, self.gender, self.height, self.weight,))
            self.user_id = self.cur.fetchone()[0]
            self.conn.commit()
            print(f"User profile saved with ID: {self.user_id}")
        except Exception as e:
            self.conn.rollback()
            print(f"Error saving user profile: {e}")

    def __del__(self):
        if hasattr(self, 'cur') and self.cur is not None:
            self.cur.close()
        if hasattr(self, 'conn') and self.conn is not None:
            self.conn.close()
            print('Database connection closed.')

# Usage
if __name__ == "__main__":
    try:
        user = UserProfile()
        user.save_to_database()
    except Exception as e:
        print(f"An error occurred: {e}")
