# Delete/Analytics
import streamlit as st
from datetime import datetime
from db_functions import *

import pandas as pd
import plotly.express as px

# Data Viz Packages
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

def run_manage_page_complete():
    submenu = ["Análise", "Excluir usuário", "Excluir colaborador"]
    choice = st.selectbox("SubMenu", submenu)
        
    if choice == "Análise":
        result = view_all_tasks()
        df = pd.DataFrame(result, columns=['Colaborador','Função','Atividade','Escalado','Contrato','Data','Responsável'])
        
        with st.expander("Ver todos os registros"):
            st.dataframe(df)
            
        with st.expander("Status das Obras/Atividades"):
            
            data_inicio = st.date_input("Selecione uma data",format="DD/MM/YYYY")
            data_search = data_inicio.strftime("%d/%m/%Y")
            if st.button("Procurar"):
                st.info("Você selecionou a data {}".format(data_search))
                search_result = get_task_by_date(data_search)
                df = pd.DataFrame(search_result, columns=['Colaborador','Função','Atividade','Escalado','Contrato','Data','Responsável'])
                st.dataframe(df) 
                st.subheader("Análise das Atividades",divider='rainbow')
                st.dataframe(df['Atividade'].value_counts())
                new_df = df['Atividade'].value_counts().to_frame()
                new_df = new_df.reset_index()
                #st.dataframe(new_df)
                
                st.bar_chart(new_df,x='Atividade',y='count',use_container_width=True, color="#830b67")
                
    elif choice == "Excluir usuário":
        result = view_all_users()
        df = pd.DataFrame(result, columns=['username','email','password'])
        st.dataframe(df)
        unique_list = [i[0] for i in view_all_unique_user_names()]
        delete_by_worker_name = st.selectbox("Usuário", unique_list)
        st.warning("⚠️ Deseja excluir {} ? ⚠️".format(delete_by_worker_name))
        if st.button("Excluir"):
            delete_user_data(delete_by_worker_name)
            st.info("{} foi excluído".format(delete_by_worker_name))
        
        with st.expander("Banco de dados atual"):
            result2 = view_all_users()
            new_df = pd.DataFrame(result2, columns=['username','email','password'])
            st.dataframe(new_df)  
    else:
        result = view_all_tasks()
        df = pd.DataFrame(result, columns=['Colaborador','Função','Atividade','Escalado','Contrato','Data','Responsável'])
        st.dataframe(df)
        unique_list = [i[0] for i in view_all_unique_worker_names()]
        delete_by_worker_name = st.selectbox("Colaborador", unique_list)
        #data_padrao = st.date_input("Data",format='DD/MM/YYYY')
        #data_obj = datetime.strftime(data_padrao,'%d/%m/%Y')
        #data = data_obj
        indice = st.text_input("Escolha o índice")
        st.warning("⚠️ Deseja excluir {} ? ⚠️".format(delete_by_worker_name))
        if st.button("Excluir"):
            #delete_data(delete_by_worker_name,data)
            delete_data_by_index(indice)
            st.info("{} foi excluído".format(delete_by_worker_name))
        
        with st.expander("Banco de dados atual"):
            result2 = view_all_tasks()
            new_df = pd.DataFrame(result2, columns=['Colaborador','Função','Atividade','Escalado','Contrato','Data','Responsável'])
            st.dataframe(new_df)  
        
def run_manage_page_simple():
        
    with st.expander("Status das Obras/Atividades"):
            
        data_inicio = st.date_input("Selecione uma data",format="DD/MM/YYYY")
        data_search = data_inicio.strftime("%d/%m/%Y")
        if st.button("Procurar"):
            st.info("Você selecionou a data {}".format(data_search))
            search_result = get_task_by_date(data_search)
            df = pd.DataFrame(search_result, columns=['Colaborador','Função','Atividade','Escalado','Contrato','Data','Responsável'])
            st.dataframe(df) 
            st.subheader("Análise das Atividades",divider='rainbow')
            st.dataframe(df['Atividade'].value_counts())
            new_df = df['Atividade'].value_counts().to_frame()
            new_df = new_df.reset_index()
            #st.dataframe(new_df)
            
            st.bar_chart(new_df,x='Atividade',y='count',use_container_width=True, color="#830b67")
   
        #with st.expander("Banco de dados atual"):
        #    result2 = get_task_by_date(data_search)
        #    new_df = pd.DataFrame(result2, columns=['Colaborador','Função','Atividade','Data'])
        #    st.dataframe(new_df)
            
            
            
