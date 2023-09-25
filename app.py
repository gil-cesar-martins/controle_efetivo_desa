import streamlit as st
from home_page import run_home_page
from post_page import run_task_page
from manage_page import run_manage_page
from mobi_page import run_mobi_page
from db_functions import create_user_password_table, add_user_data, login_user, view_all_users

from PIL import Image


def main():

    menu = ["Home","Login","SignUp"]
    choice1 = st.sidebar.selectbox("Menu",menu)
   
    if choice1 == "Home":
        logo = Image.open('./img/background.png')
        st.image(logo, use_column_width=True)
        st.subheader("Acompanhamento",divider='rainbow')
        run_home_page()

    elif choice1 == "Login":
        logo = Image.open('./img/background.png')
        st.image(logo, use_column_width=True)
        st.sidebar.subheader("Login",divider='rainbow')
        
        username = st.sidebar.text_input("Usuário: ")
        password = st.sidebar.text_input("Senha :",type='password')
        
        if st.sidebar.checkbox('Login'):
            # if password == "123456":
            create_user_password_table()
            result = login_user(username,password)
            if result:
                st.success("Seja bem-vindo {} !".format(username))
            
                task = st.selectbox("Selecione:",["Atividades","Gerenciamento","Ociosidade","Sobre o APP"])
                
                if task == "Atividades":
                    run_task_page()

                elif task == "Gerenciamento":
                    st.subheader("Gerenciamento",divider='rainbow')
                    run_manage_page()

                elif task == "Ociosidade":
                    st.subheader("Mobilização", divider='rainbow')
                    run_mobi_page()

                else:
                    st.subheader("Sobre o App",divider='rainbow')
            else:
                st.warning("Senha incorreta !")
            
    elif choice1 == "SignUp":
        logo = Image.open('./img/background.png')
        st.image(logo, use_column_width=True)
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
            
        
        
           
if __name__ == '__main__':
    main()