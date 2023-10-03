import streamlit as st

import pandas as pd
import plotly.express as px

from home_page import run_home_page
from post_page import run_task_page_simple, run_task_page_complete
from manage_page import run_manage_page_complete,run_manage_page_simple
from mobi_page import run_mobi_page
from db_functions import create_user_password_table, add_user_data, login_user, view_all_users, query_user, get_task_by_date, get_task_by_date_by_user,view_all_tasks

from PIL import Image

def main():
    username = []
    menu = ["Login"]
    choice1 = st.sidebar.selectbox("Menu",menu)
    
    if choice1 == "Login":
        logo = Image.open('./img/background.png')
        st.image(logo, use_column_width=True)
        st.sidebar.subheader("Login",divider='rainbow')
        username = st.sidebar.text_input("Usuário: ")
        password = st.sidebar.text_input("Senha :",type='password')
        
        if st.sidebar.checkbox('Login'):
            if username == "gil.cesar":
                result = login_user(username,password)
                if result:
                    st.success("Seja bem-vindo {} !".format(username))
                
                menu = ["SignUp"]
                choice2 = st.sidebar.selectbox("Menu",menu)
                choice2 == "SignUp"
                st.subheader("Criar novo usuário",divider='rainbow')
        
                new_user = st.text_input("Usuário :")
                email = st.text_input("Email :",placeholder="Digite o email corporativo")
                new_password = st.text_input("Senha :",placeholder="Digite a senha", type="password")
                new_password_confirm = st.text_input("Confirme a senha",placeholder="Confirme a senha",type='password')
        
                if new_user is not "" and email is not "" and new_password is not "" and new_password == new_password_confirm:
                    if st.button("SignUp"):
                        create_user_password_table()
                        add_user_data(new_user,email,new_password)
                        st.success("Você criou uma conta válida.")
                        st.info("Vá ao menu de Login para acessar.")
                else:
                    st.warning("O usuário deve ser criado e as senhas precisam ser iguais")


                create_user_password_table()
                
            else:
                result = login_user(username,password)
                if result :
                    st.success("Seja bem-vindo {} !".format(username))
                    if username == "gil.cesar.adm":
                        result = view_all_tasks()
                        df_adm = pd.DataFrame(result, columns=['Colaborador','Função','Atividade','Escalado','Contrato','Data','Responsável'])
                        with st.expander("Ver todos os registros"):
                            st.dataframe(df_adm)
                    else:
                        result = query_user(username)
                        df = pd.DataFrame(result, columns=['Colaborador','Função','Atividade','Escalado','Contrato','Data','Responsável'])
                        with st.expander("Ver todos os registros"):
                                st.dataframe(df)
                    
                    st.subheader("Selecione alguma opção",divider='rainbow')
                    task = st.selectbox("Selecione:",["Home","Atividades","Gerenciamento","Ociosidade","Sobre o App"])

                    if task == "Home":
                        st.subheader("Acompanhamento",divider='rainbow')
                        run_home_page()

                    elif task == "Atividades" and username == "gil.cesar.adm":
                        run_task_page_complete()
                    elif task == "Atividades":
                        run_task_page_simple()
                    elif task == "Gerenciamento" and username == "gil.cesar.adm":
                        st.subheader("Gerenciamento",divider='rainbow')
                        run_manage_page_complete()
                    elif task == "Gerenciamento":
                        st.subheader("Gerenciamento",divider='rainbow')
                        result = query_user(username)
                        df = pd.DataFrame(result, columns=['Colaborador','Função','Atividade','Escalado','Contrato','Data','Responsável'])
    
                        with st.expander("Ver todos os registros"):
                            st.dataframe(df)
                            
                        
        
                        with st.expander("Status das Obras/Atividades"):

                                data_inicio = st.date_input("Selecione uma data",format="DD/MM/YYYY")
                                data_search = data_inicio.strftime("%d/%m/%Y")
                                if st.button("Procurar"):
                                    st.info("Você selecionou a data {}".format(data_search))
                                    search_result = get_task_by_date_by_user(data_search,username)
                                    df = pd.DataFrame(search_result, columns=['Colaborador','Função','Atividade','Escalado','Contrato','Data','Responsável'])
                                    st.dataframe(df) 
                                    st.subheader("Análise das Atividades",divider='rainbow')
                                    st.dataframe(df['Atividade'].value_counts())
                                    new_df = df['Atividade'].value_counts().to_frame()
                                    new_df = new_df.reset_index()
                                    #st.dataframe(new_df)

                                    st.bar_chart(new_df,x='Atividade',y='count',use_container_width=True, color="#830b67")
   
                    elif task == "Ociosidade":
                        st.subheader("Mobilização", divider='rainbow')
                        run_mobi_page()

                    elif task == "Sobre o App":
                        st.subheader("Saiba mais Sobre o App",divider='rainbow')
                else:
                    st.warning("Usuário ou Senha incorretos !")
        
if __name__ == '__main__':
    main()