# Delete/Analytics
import streamlit as st
from datetime import datetime
from db_functions import (create_table, add_data, view_all_tasks,view_all_worker_names, view_all_unique_worker_names,
                          get_task_by_worker_name, edit_task_data, mobile,delete_data)

import pandas as pd

def run_manage_page():
    submenu = ["Excluir colaborador", "Analytics"]
    choice = st.sidebar.selectbox("SubMenu",submenu)
    
    if choice == "Excluir colaborador":
        result = view_all_tasks()
        df = pd.DataFrame(result, columns=['Colaborador','Função','Atividade','Data'])
        st.dataframe(df)
        pass
    else:
        st.subheader("Analytics")