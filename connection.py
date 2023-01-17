from sqlalchemy import create_engine

engine =  create_engine('mysql+pymysql://root@localhost:3306/cinema')
response = engine.execute('select * from filmes;')

for row in response:
    print(row.titulo)