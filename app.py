import streamlit as st
from home_page import run_home_page
from post_page import run_task_page
from manage_page import run_manage_page
from mobi_page import run_mobi_page
from PIL import Image

logo = Image.open('./img/background.png')
st.image(logo, use_column_width=True)

menu = ["Login","SignUp"]
choice1 = st.sidebar.selectbox("",menu)

if choice1 == "Login":
    username = st.sidebar.text_input("Usuário: ")
    password = st.sidebar.text_input("Senha :",type='password')
        
    if st.sidebar.button('Login'):
        st.success("Seja bem-vindo {} !".format(username))

        def application():
    
            st.title("Controle de Efetivo")
            menu = ["Home","Atividades","Gerenciamento","Ociosidade","Sobre o APP"]
            choice = st.sidebar.selectbox("Menu", menu)
    
            if choice == "Home":
                st.subheader("Acompanhamento",divider='rainbow')
                run_home_page()

            elif choice == "Atividades":
                run_task_page()

            elif choice == "Gerenciamento":
                st.subheader("Gerenciamento",divider='rainbow')
                run_manage_page()

            elif choice == "Ociosidade":
                st.subheader("Mobilização", divider='rainbow')
                run_mobi_page()

            else:
                st.subheader("Sobre o App",divider='rainbow')

        if __name__ == '__main__':
            application()