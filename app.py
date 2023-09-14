import streamlit as st
#from home_page import run_home_page
from post_page import run_task_page
from manage_page import run_manage_page
from PIL import Image

logo = Image.open('./img/logodesa2.png')
st.image(logo, width=200)

def application():
    
    st.title("Controle de Efetivo")
    menu = ["Home","Atividades","Gerenciamento","Sobre o APP"]
    choice = st.sidebar.selectbox("Menu", menu)
    
    if choice == "Home":
        st.subheader("Home")
        #run_home_page()
        
    elif choice == "Atividades":
        st.subheader("Atividades realizadas")
        run_task_page()
        
    elif choice == "Gerenciamento":
        st.subheader("Gerenciamento")
        run_manage_page()
    else:
        st.subheader("Sobre o App")

if __name__ == '__main__':
    application()