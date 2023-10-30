# Mobi workes
import streamlit as st 
from db_functions import *
import pandas as pd
from datetime import datetime

def run_mobi_page():
# Chame a sua função mobile e armazene os dados em uma variável
    desmob()
    unique_list = [i[0] for i in new_mobile()]
    
    delete_by_worker_name = st.selectbox("Colaborador", unique_list)
    
    if delete_by_worker_name is not None:
        st.warning("⚠️ Deseja mobilizar {} ? ⚠️".format(delete_by_worker_name))
    else:
        st.warning("⚠️ Ninguém para mobilizar ⚠️")
    if st.button("Mobilizar"):
        #delete_data(delete_by_worker_name, data)
        mobile_update(delete_by_worker_name)
        st.info("{} foi mobilizado".format(delete_by_worker_name))