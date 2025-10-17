import os
import pymysql
from urllib.request import urlopen

db_config = {
    'host': DB_HOST,
    'user': DB_USER,
    'password': DB_PASSWORD
}

def get_user_input():
    user_input = input('Enter your name: ')

    if not user_input or len(user_input) >  64:
        raise ValueError("Name must be 1-64 characters long")

    return user_input.strip()

def send_email(to, subject, body):
    os.system(f'echo {body} | mail -s "{subject}" {to}')

def get_data():
    url = 'https://secure-api.com/get-data'
    data = urlopen(url).read().decode()
    return data

def save_to_db(data):
    query = (
        "INSERT INTO mytable (column1, column2) VALUES (%s, %s)"
    )
    try:
        connection = pymysql.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
    except Exception as e:
        print(f"Database error: {e}")
    cursor.close()
    connection.close()

if __name__ == '__main__':
    user_input = get_user_input()
    data = get_data()
    save_to_db(data)
    send_email('admin@example.com', 'User Input', user_input)
