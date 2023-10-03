# Mobi workes
import streamlit as st 
from db_functions import *
import pandas as pd
from datetime import datetime


def run_mobi_page():
# Chame a sua função mobile e armazene os dados em uma variável
    dados = mobile()

# Converta os dados em uma lista de listas, onde cada sublista representa uma linha do dataframe
# Você pode usar um loop for para fazer isso, ou alguma outra forma que preferir
# Suponha que os dados tenham quatro colunas: colaborador, função, atividade e data
    lista_de_listas = []
    for linha in dados:
        lista_de_listas.append([linha[0], linha[1], linha[2], linha[3], linha [4], linha[5], linha[6]])
        
# Crie o dataframe a partir da lista de listas, especificando os nomes das colunas
    df = pd.DataFrame(lista_de_listas, columns=["colaborador", "função", "atividade" , "escalado", "contrato", "data", "responsável"])

# O restante do código é o mesmo que o anterior
    escolhido = []
    col1, col2 = st.columns(2)
    with col1:
        st.text("Escolha alguém")
        for colaborador in df["colaborador"]:
            checkbox = st.checkbox(colaborador)
            # Coloque o if checkbox no mesmo nível do for colaborador
            if checkbox:
                escolhido.append(colaborador)
    with col2:
        st.text("Resultado")
        df_filtrado = df[df["colaborador"].isin(escolhido)]
        st.dataframe(df_filtrado)
     
        if st.button("Mobilizar"):
            if st.dataframe == "":
                st.write("Não há ninguém para Mobilizar")
            else:
                mobile_update()

if __name__ == '__run_mobi_page__':
    run_mobi_page()
    
    
