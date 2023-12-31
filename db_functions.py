import sqlite3
conn = sqlite3.connect("data.db", check_same_thread=False)
c = conn.cursor()

# Create  tasktable

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS tasktable(colaborador TEXT, funcao TEXT, atividade TEXT, escalado TEXT, contrato TEXT, data DATE, responsavel TEXT)')
    
def add_data(colaborador,funcao,atividade,escalado,contrato,data,responsavel):
    c.execute('INSERT INTO tasktable(colaborador,funcao,atividade,escalado,contrato,data,responsavel) VALUES(?,?,?,?,?,?,?)',(colaborador,funcao,atividade,escalado,contrato,data,responsavel))    
    conn.commit()

def query_user(username):
    c.execute('SELECT tasktable.* FROM tasktable JOIN userstable ON tasktable.responsavel = userstable.username WHERE userstable.username = "{}"'.format(username))
    data = c.fetchall()
    return data

# CREATE USER SECTION

def create_user_password_table():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT, email TEXT, password TEXT)')
    
def add_user_data(username,email,password):
    c.execute('INSERT INTO userstable(username,email,password) VALUES(?,?,?)',(username,email,password))
    conn.commit()
    
def delete_user_data(username):
    c.execute('delete from userstable where username = "{}"'.format(username))
    conn.commit()
    
def view_all_unique_user_names():
    c.execute('SELECT DISTINCT username FROM userstable')
    dados = c.fetchall()
    return dados

def get_task_by_date_by_user(data,username):
    c.execute('SELECT tasktable.* FROM tasktable JOIN userstable ON tasktable.responsavel = userstable.username WHERE userstable.username = ? AND  tasktable.data = ?',(username,data))
    dados = c.fetchall()
    return dados

def login_user(username,password):
    c.execute('SELECT * FROM userstable WHERE username=? AND password = ?',(username,password))
    data = c.fetchall()
    return data

def view_all_users():
    c.execute('SELECT * FROM userstable')
    data = c.fetchall()
    return data

def choose_unique_username():
    c.execute('SELECT DISTINCT username FROM userstable')
    data = c.fetchall()
    return data

# End User Section

def view_all_tasks():
    c.execute('SELECT * FROM tasktable')
    #c.execute("SELECT colaborador, funcao, atividade, strftime('%d/%m/%Y', data, responsavel) as data FROM tasktable")
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
    c.execute('SELECT colaborador, funcao, atividade, escalado, contrato, data, responsavel FROM tasktable WHERE colaborador = "{}"'.format(colaborador))
    dados = c.fetchall()
    return dados

def edit_task_data(novo_colaborador,nova_funcao,nova_atividade,novo_escalado,novo_contrato,nova_data,novo_responsavel,colaborador,funcao,atividade,escalado,contrato,data,responsavel):
    c.execute("UPDATE tasktable SET colaborador = ?, funcao = ?, atividade = ?, escalado = ?, contrato = ?, data = ?, responsavel = ? WHERE colaborador = ? and funcao = ? and atividade = ? and escalado = ? and contrato = ? and data = ? and responsavel = ?",(novo_colaborador,nova_funcao,nova_atividade,novo_escalado,novo_contrato,nova_data,novo_responsavel,colaborador,funcao,atividade,escalado,contrato,data,responsavel))
    conn.commit()
    dados = c.fetchall()
    return dados

# Mobilização
def mobile_update(colaborador):
    c.execute('UPDATE tasktable SET atividade = "Mobilizar" WHERE atividade = "Desmobilizar" AND colaborador = "{}"'.format(colaborador))
    conn.commit()
    c.execute('SELECT * FROM tasktable WHERE colaborador = "{}"'.format(colaborador))
    dados = c.fetchall()
    return dados

def desmob():
    c.execute('SELECT DISTINCT colaborador FROM tasktable where atividade = "Desmobilizar"')
    dados = c.fetchall()
    return dados

def mobile():
    c.execute('SELECT DISTINCT colaborador FROM tasktable where atividade = "Mobilizar"')
    dados = c.fetchall()
    return dados

def new_mobile():
    c.execute('SELECT DISTINCT colaborador FROM tasktable where atividade = "Desmobilizar"')
    dados = c.fetchall()
    return dados

def delete_data(colaborador,data):
    c.execute('DELETE FROM tasktable WHERE colaborador = "{}" and data = "{}"'.format(colaborador,data))
    conn.commit()

def delete_data_by_index(indice):
    c.execute('DELETE FROM tasktable WHERE ROWID = "{}"'.format(indice))
    conn.commit()

def get_task_by_task_name(atividade):
    c.execute('SELECT * FROM tasktable WHERE atividade = "{}"'.format(atividade))
    dados = c.fetchall()
    return dados

def get_task_by_date(data):
    c.execute('SELECT * FROM tasktable WHERE data = "{}"'.format(data))
    dados = c.fetchall()
    return dados
