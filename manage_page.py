# Delete/Analytics
import streamlit as st
from datetime import datetime
from db_functions import (create_table, add_data, view_all_tasks,view_all_worker_names, view_all_unique_worker_names,
                          get_task_by_worker_name, edit_task_data, mobile,delete_data, get_task_by_date)

import pandas as pd
import plotly.express as px

# Data Viz Packages
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

def run_manage_page():
    submenu = ["Excluir colaborador", "Análise"]
    choice = st.sidebar.selectbox("SubMenu", submenu)
    
    if choice == "Excluir colaborador":
        result = view_all_tasks()
        df = pd.DataFrame(result, columns=['Colaborador','Função','Atividade','Data'])
        st.dataframe(df)
        unique_list = [i[0] for i in view_all_unique_worker_names()]
        delete_by_worker_name = st.selectbox("Colaborador", unique_list)
        st.warning("⚠️ Deseja excluir {} ? ⚠️".format(delete_by_worker_name))
        if st.button("Excluir"):
            delete_data(delete_by_worker_name)
            st.info("{} foi excluído".format(delete_by_worker_name))
        
        with st.expander("Banco de dados atual"):
            result2 = view_all_tasks()
            new_df = pd.DataFrame(result2, columns=['Colaborador','Função','Atividade','Data'])
            st.dataframe(new_df)         
        
    else:
        result = view_all_tasks()
        df = pd.DataFrame(result, columns=['Colaborador','Função','Atividade','Data'])
        
        with st.expander("Ver todos os registros"):
            st.dataframe(df)
            
        with st.expander("Status das Obras/Atividades"):
            
            
            data_inicio = st.date_input("Selecione uma data",format="DD/MM/YYYY")
            data_search = data_inicio.strftime("%d/%m/%Y")
            if st.button("Procurar"):
                st.info("Você selecionou a data {}".format(data_search))
                search_result = get_task_by_date(data_search)
                df = pd.DataFrame(search_result, columns=['Colaborador','Função','Atividade','Data'])
                st.dataframe(df) 
                st.subheader("Análise das Atividades",divider='rainbow')
                st.dataframe(df['Atividade'].value_counts())
                new_df = df['Atividade'].value_counts().to_frame()
                new_df = new_df.reset_index()
                #st.dataframe(new_df)
                
                st.bar_chart(new_df,x='Atividade',y='count',use_container_width=True, color="#830b67")
            
            
            
