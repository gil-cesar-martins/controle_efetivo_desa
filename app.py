import streamlit as st
from home_page import run_home_page
from post_page import run_task_page
from manage_page import run_manage_page_complete,run_manage_page_simple
from mobi_page import run_mobi_page
from db_functions import create_user_password_table, add_user_data, login_user, view_all_users, query_user

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
                if result:
                    st.success("Seja bem-vindo {} !".format(username))
                    data = query_user(username)
                    st.write(data)
                    task = st.selectbox("Selecione:",["Home","Atividades","Gerenciamento","Ociosidade","Sobre o App"])

                    if task == "Home":
                        st.subheader("Acompanhamento",divider='rainbow')
                        run_home_page()

                    elif task == "Atividades":
                        run_task_page()
                    elif task == "Gerenciamento" and username == "gil.cesar.adm":
                        st.subheader("Gerenciamento",divider='rainbow')
                        run_manage_page_complete()
                    elif task == "Gerenciamento":
                        st.subheader("Gerenciamento",divider='rainbow')
                        run_manage_page_simple()
                    elif task == "Ociosidade":
                        st.subheader("Mobilização", divider='rainbow')
                        run_mobi_page()

                    elif task == "Sobre o App":
                        st.subheader("Saiba mais Sobre o App",divider='rainbow')
                else:
                    st.warning("Usuário ou Senha incorretos !")
        
if __name__ == '__main__':
    main()