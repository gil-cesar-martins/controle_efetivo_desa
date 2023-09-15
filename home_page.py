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
            #st.write(task_result)
            colaborador = task_result[0][0]
            funcao = task_result[0][1]
            #atividade = task_result[0][2]
            #data = task_result[0][3]
            st.write("Colaborador: {}".format(colaborador))
            st.text("Função: {}".format(funcao))
            #st.text("Atividade: {}".format(atividade))
            #st.write("Data da atividade:{}".format(data))
    
    else:
        st.subheader("Campo para buscar",divider='rainbow')
        search_choice = st.radio("Escolha uma opção",("Colaborador","Atividade","Data"))
        
        if search_choice == "Colaborador":
            list_of_workers = [i[0] for i in view_all_unique_worker_names()]
            search_term = st.selectbox("Colaborador:",list_of_workers)
            #search_term = st.text_input("Digite o nome ou as 4 primeiras letras")
            if st.button("Procurar"):
                search_result = get_task_by_worker_name(search_term)
                df = pd.DataFrame(search_result, columns=['Colaborador','Função','Atividade','Data'])
                st.dataframe(df)
                     
        elif search_choice == "Atividade":
            list_of_tasks = [i[0] for i in view_all_unique_task_names()]
            search_term = st.selectbox("Atividade ou Centro de Custo:",list_of_tasks)
            #search_term = st.text_input("Digite o Centro de Custo")
            if st.button("Procurar"):
                search_result = get_task_by_task_name(search_term)
                #st.write(search_result)
                df = pd.DataFrame(search_result, columns=['Colaborador','Função','Atividade','Data'])
                st.dataframe(df)
        else:
            data_inicio = st.date_input("Selecione uma data",format="DD/MM/YYYY")
            data_search = data_inicio.strftime("%d/%m/%Y")
            if st.button("Procurar"):
                st.info("Você selecionou a data {}".format(data_search))
                search_result = get_task_by_date(data_search)
                df = pd.DataFrame(search_result, columns=['Colaborador','Função','Atividade','Data'])
                st.dataframe(df) 
                
            
            
            

                
                
        
            