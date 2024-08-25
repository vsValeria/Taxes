import psycopg2

class Taxes:
    def __init__(self):
        self.connection=psycopg2.connect(
            dbname='Taxes',
            user='postgres',
            password=755642,
            host='localhost',
            port=5434
        )



    def request_sql(self,min_tax,max_tax):
        query = """SELECT o.tax_description, o.report_period_type, c.taxpayer_numder, c.address, c.total_due
        FROM taxes AS o 
        JOIN taxpayers AS c
        ON o.tax_id=c.tax_id
        WHERE c.tax_id
        BETWEEN %s AND %s"""
        cursor=self.connection.cursor()
        cursor.execute(query, (min_tax, max_tax))
        return cursor.fetchall()








