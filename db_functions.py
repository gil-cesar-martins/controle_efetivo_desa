import sqlite3
conn = sqlite3.connect("data.db", check_same_thread=False)
c = conn.cursor()

# Table
# Table must have field/columns
# Fied must datatype

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS tasktable(colaborador TEXT, funcao TEXT, atividade TEXT, data DATE)')

def add_data(colaborador,funcao,atividade,data):
    c.execute('INSERT INTO tasktable(colaborador,funcao,atividade,data) VALUES(?,?,?,?)',(colaborador,funcao,atividade,data))
    #c.execute("INSERT INTO tasktable (colaborador, funcao, atividade, data) VALUES (?, ?, ?, strftime('%d/%m/%Y', 'now'))", (colaborador, funcao, atividade))
    conn.commit()
    
def view_all_tasks():
    #c.execute('SELECT * FROM tasktable')
    c.execute("SELECT colaborador, funcao, atividade, strftime('%d/%m/%Y', data) as data FROM tasktable")
    dados = c.fetchall()
    return dados
    