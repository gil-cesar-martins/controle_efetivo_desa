import streamlit as st 
from db_functions import *
import pandas as pd

def run_home_page():
    choice = st.sidebar.selectbox("SubMenu",["Efetivo", "Buscar"])
    
    with st.expander("Clique para ver todo o efetivo"):
        result = view_all_tasks()
        df = pd.DataFrame(result, columns=['Colaborador','Função','Atividade','Data'])
        st.dataframe(df)
    
    if choice == "Efetivo":
        c1,c2 = st.columns([1,3])
        
        with c1:
            st.info("Lista de efetivo")
            list_of_workers = [i[0] for i in view_all_unique_worker_names()]
            selected_task = st.selectbox("Colaborador:",list_of_workers)
        
        with c2:
            st.info("Detalhes")
            task_result = get_task_by_worker_name(selected_task)
            st.write(task_result)
            colaborador = task_result[0][0]
            funcao = task_result[0][1]
            atividade = task_result[0][2]
            data = task_result[0][3]
            st.write("Colaborador: {}".format(colaborador))
            st.text("Função: {}".format(funcao))
            st.text("Atividade: {}".format(atividade))
            st.write("Data da atividade:{}".format(data))
    
    else:
        st.subheader("Procura")
        search_term = st.text_input("Digite o nome ou as 4 primeiras letras")
        search_choice = st.radio("Campo para buscar",("Colaborador","Atividade"))
        
        if st.button("Procurar"):
            if search_choice == "Colaborador":
                search_result = get_task_by_worker_initial_name(search_term)
                st.write(search_result)
            else:
                search_result = get_task_by_task_name(search_term)
                st.write(search_result)
            