# Create and Edit/Update
import streamlit as st
from db_functions import create_table, add_data, view_all_tasks

def run_task_page():
    st.subheader("Preencher e Atualizar Atividades")
    create_table()
    submenu = st.sidebar.selectbox("Submenu",["Adicionar","Editar"])
    
    if submenu == "Adicionar":
        col1,col2 = st.columns(2)
        
        with col1:
            colaborador = st.text_input("Colaborador")
            funcao = st.text_input("Função")
            
        with col2:
            data = st.date_input("Data",format="DD/MM/YYYY")
            atividade = st.selectbox("Atividade",["0000","0001","0003","0004","0005","0008","0012","0193",
                                                "0690","0744","0827","0832","0841","1049","1070","1132",
                                                "1212","1241","1273","1288","1347","1399","1453","1457",
                                                "1462","1492","1517","1548","1584","1589","2003","2027",
                                                "2034","2037","2052","2072","2078","2088","2105","2112",
                                                "2130","2163","2184","2231","2236","2241","2250","2271",
                                                "2328","2335","2376","2392","2394","2413","2452","2478","2479",
                                                "2500","2501","2518","2539","2540","3011","3052","3118","3139",
                                                "3182","3198","3199","3200","3206","3218"])
            
        if st.button("Adicionar"):
            add_data(colaborador,funcao,atividade,data)
            st.success("Adicionado:: {}".format(colaborador))
        
        results = view_all_tasks()  
        st.write(results)