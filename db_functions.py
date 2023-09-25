import sqlite3
conn = sqlite3.connect("data.db", check_same_thread=False)
c = conn.cursor()

# Create  tasktable

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS tasktable(colaborador TEXT, funcao TEXT, atividade TEXT, data DATE)')
    
def add_data(colaborador,funcao,atividade,data):
    c.execute('INSERT INTO tasktable(colaborador,funcao,atividade,data) VALUES(?,?,?,?)',(colaborador,funcao,atividade,data))
    #c.execute("INSERT INTO tasktable (colaborador, funcao, atividade, data) VALUES (?, ?, ?, strftime('%d/%m/%Y', 'now'))", (colaborador, funcao, atividade))
    conn.commit()

# CREATE USER SECTION
def create_user_password_table():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT, email TEXT, password TEXT)')
    
def add_user_data(username,email,password):
    c.execute('INSERT INTO userstable(username,email,password) VALUES(?,?,?)',(username,email,password))
    conn.commit()

def login_user(username,password):
    c.execute('SELECT * FROM userstable WHERE username=? AND password = ?',(username,password))
    data = c.fetchall()
    return data

def view_all_users():
    c.execute('SELECT * FROM userstable')
    data = c.fetchall()
    return data
# End User Section  
def view_all_tasks():
    c.execute('SELECT * FROM tasktable')
    #c.execute("SELECT colaborador, funcao, atividade, strftime('%d/%m/%Y', data) as data FROM tasktable")
    dados = c.fetchall()
    return dados

def view_all_worker_names():
    c.execute('SELECT colaborador FROM tasktable')
    dados = c.fetchall()
    return dados

def view_all_unique_worker_names():
    c.execute('SELECT DISTINCT colaborador FROM tasktable')
    dados = c.fetchall()
    return dados

def view_all_unique_task_names():
    c.execute('SELECT DISTINCT atividade FROM tasktable')
    dados = c.fetchall()
    return dados


def get_task_by_worker_name(colaborador):
    c.execute('SELECT colaborador, funcao, atividade, data FROM tasktable WHERE colaborador = "{}"'.format(colaborador))
    dados = c.fetchall()
    return dados

def edit_task_data(novo_colaborador,nova_funcao,nova_atividade,nova_data,colaborador,funcao,atividade,data):
    c.execute("UPDATE tasktable SET colaborador = ?, funcao = ?, atividade = ?, data = ? WHERE colaborador = ? and funcao = ? and atividade = ? and data = ?",(novo_colaborador,nova_funcao,nova_atividade,nova_data,colaborador,funcao,atividade,data))
    conn.commit()
    dados = c.fetchall()
    return dados

def mobile_update():
    c.execute('SELECT * FROM tasktable where atividade = "Desmobilizar"')
    dados = c.fetchall()
    c.execute('UPDATE tasktable SET atividade = "Mobilizar" WHERE atividade = "Desmobilizar"')
    conn.commit()
    return dados

def mobile():
    c.execute('SELECT * FROM tasktable where atividade = "Desmobilizar"')
    dados = c.fetchall()
    return dados


def delete_data(colaborador):
    c.execute('DELETE FROM tasktable WHERE colaborador = "{}"'.format(colaborador))
    #c.execute('DELETE FROM tasktable WHERE colaborador= ?',(colaborador))
    conn.commit()

def get_task_by_task_name(atividade):
    c.execute('SELECT * FROM tasktable WHERE atividade = "{}"'.format(atividade))
    dados = c.fetchall()
    return dados

def get_task_by_date(data):
    c.execute('SELECT * FROM tasktable WHERE data = "{}"'.format(data))
    dados = c.fetchall()
    return dados
