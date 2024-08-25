import psycopg2

def setup_database():
    connection = psycopg2.connect(host='localhost', user='postgres', password=755642, database='Taxes', port=5434)
    print(connection)
if __name__=='__main__':
    setup_database()