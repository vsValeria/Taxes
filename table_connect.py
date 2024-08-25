import psycopg2

connection = psycopg2.connect(
    host='localhost',
    user='postgres',
    password=755642,
    database='Taxes',
    port=5434
)

    #input_vat=input('Enter Tax ID')
cursor=connection.cursor()
input_var1=str(input('Enter taxpayer ID1'))
#input_var2=input('Enter taxpayer ID2')
#cursor.execute(f"SELECT year, total_due FROM due WHERE taxpayer_id BETWEEN {input_var1} AND {input_var2};")
cursor.execute(f"SELECT a.tax_description, o.address, o.total_due, o.taxpayer_numder FROM taxes a JOIN taxpayers o ON a.tax_id=o.tax_id WHERE a.report_period_type={input_var1};")
for row in cursor:
    print(row)
#print(cursor)
