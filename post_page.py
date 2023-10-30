# Create and Edit/Update
import streamlit as st
from datetime import datetime
from db_functions import *
import time

def run_task_page_complete():
    create_table()
    submenu = st.selectbox("Submenu",["Adicionar","Editar"])
    st.subheader('Adicionar / Editar Atividades', divider='rainbow')
    if submenu == "Adicionar":
        with st.form(key='Adicionar',clear_on_submit=True):
            col1,col2 = st.columns(2)
        
            with col1:
                colaborador = st.text_input("Colaborador")
                funcao = st.text_input("Função")
                contrato = st.text_input("Contrato")
            with col2:
                data_padrao = st.date_input("Data",format='DD/MM/YYYY')
                data_obj = datetime.strftime(data_padrao,'%d/%m/%Y')
                data = data_obj
                atividade = st.text_input("Atividade")
                escalado = st.text_input("Escalado ?")
                responsavel = st.text_input("Responsável")
            
            
                #if atividade == "" and colaborador == "":
                st.warning("FUNCIONÁRIO OCIOSO", icon="⚠️")
                    
                sub_col1, sub_col2 = st.columns(2)
                    
                with sub_col1:
                    opcoes = st.radio(
                            "Informe o motivo:",
                        ["Atestado","Falta","Desmobilizar"],
                        captions= ["Envie o atestado médico","Justifique o motivo", "Conferir na aba OCIOSIDADE"]
                    )
                    
                with sub_col2:
                    if opcoes == "Atestado":
                        st.info('📋 Não esqueça de enviar o atestado. Vá ao menu "Gerenciamento", clique em Atestados')
                    elif opcoes == "Falta":
                        detalhes = st.text_area('👷🏽‍♂️ ***Justifique com poucas palavras***')
                        opcoes = "Falta: {}".format(detalhes)
                    else:
                        if "Desmobilizar" not in st.session_state:
                            st.info("🚀 Após você atualizar esses dados, verifique se o(a) colabor(a) estará na aba OCIOSOS.")
                            
                        atividade = opcoes 
            submit_button = st.form_submit_button("Adicionar")   
            if submit_button:
                add_data(colaborador,funcao,atividade,escalado,contrato,data,responsavel)
                st.success("Adicionado:: {}".format(colaborador))
                
               
    elif submenu == "Editar":
        create_table()
        st.subheader('Selecione o colaborador', divider='rainbow')        
        list_of_tasks = [i[0] for i in view_all_unique_worker_names()]
        selected_task = st.selectbox("Colaborador:",list_of_tasks)
        task_result = get_task_by_worker_name(selected_task)
    
        st.subheader("Editar Dados",divider='rainbow')
        if task_result:
            colaborador = task_result[0][0]
            funcao = task_result[0][1]
            atividade = task_result[0][2]
            escalado = task_result[0][3]
            contrato = task_result[0][4]
            data = task_result[0][5]
            responsavel = task_result[0][6]
    
            col1,col2 = st.columns(2)
            
            with col1:
                novo_colaborador = st.text_input("Colaborador",colaborador)
                nova_funcao = st.text_input("Função", funcao)
                novo_contrato = st.text_input("Contrato", contrato)

            with col2:
                data_padrao2 = st.date_input("Data",format='DD/MM/YYYY')
                data_obj2 = datetime.strftime(data_padrao2,'%d/%m/%Y')
                nova_data = data_obj2
                nova_atividade = st.text_input("Atividade",atividade)
                novo_escalado = st.text_input("Escalado?",escalado)
                novo_responsavel = st.text_input("Responsável", responsavel)
                #if nova_atividade == "" and novo_colaborador == "":
                st.warning("FUNCIONÁRIO OCIOSO", icon="⚠️")
                sub_col1, sub_col2 = st.columns(2)   
                with sub_col1:
                    opcoes = st.radio(
                        "Informe o motivo:",
                        ["Atestado","Falta","Desmobilizar"],
                        captions= ["Envie o atestado médico","Justifique o motivo", "Conferir na aba OCIOSIDADE"]
                    )

                with sub_col2:
                    if opcoes == "Atestado":
                        st.info('📋 Não esqueça de enviar o atestado. Vá ao menu "Gerenciamento", clique em Atestados')
                    elif opcoes == "Falta":
                        detalhes = st.text_area('👷🏽‍♂️ ***Justifique com poucas palavras***')
                        opcoes = "Falta: {}".format(detalhes)
                    else:
                        if "Desmobilizar" not in st.session_state:
                            st.info("🚀 Após você atualizar esses dados, verifique se o(a) colabor(a) estará na aba OCIOSOS.")

                    nova_atividade = opcoes

                submit_button = st.button("Atualizar")   
                if  submit_button:
                    edit_task_data(novo_colaborador,nova_funcao,nova_atividade,novo_escalado,novo_contrato,nova_data,novo_responsavel,colaborador,funcao,atividade,escalado,contrato,data,responsavel)
                    add_data(colaborador,funcao,atividade,escalado,contrato,data,responsavel)
                    st.success("💻 {} atualizado com sucesso! 💻".format(colaborador))
                    
def run_task_page_simple():
    create_table()
    st.subheader('Selecione o colaborador', divider='rainbow')        
    list_of_tasks = [i[0] for i in view_all_unique_worker_names()]
    selected_task = st.selectbox("Colaborador:",list_of_tasks)
    task_result = get_task_by_worker_name(selected_task)
    
    st.subheader("Editar Dados",divider='rainbow')
    if task_result:
        colaborador = task_result[0][0]
        funcao = task_result[0][1]
        atividade = task_result[0][2]
        escalado = task_result[0][3]
        contrato = task_result[0][4]
        data = task_result[0][5]
        responsavel = task_result[0][6]
    
        col1,col2 = st.columns(2)
            
        with col1:
            novo_colaborador = st.text_input("Colaborador",colaborador)
            nova_funcao = st.text_input("Função", funcao)
            novo_contrato = st.text_input("Contrato", contrato)
                
        with col2:
            data_padrao2 = st.date_input("Data",format='DD/MM/YYYY')
            data_obj2 = datetime.strftime(data_padrao2,'%d/%m/%Y')
            nova_data = data_obj2
            nova_atividade = st.text_input("Atividade",atividade)
            novo_escalado = st.text_input("Escalado?",escalado)
            novo_responsavel = st.text_input("Responsável", responsavel)
            #if nova_atividade == "" and novo_colaborador == "":
            st.warning("FUNCIONÁRIO OCIOSO", icon="⚠️")
                    
            sub_col1, sub_col2 = st.columns(2)   
            with sub_col1:
                opcoes = st.radio(
                    "Informe o motivo:",
                    ["Atestado","Falta","Desmobilizar"],
                    captions= ["Envie o atestado médico","Justifique o motivo", "Conferir na aba OCIOSIDADE"]
                )
            
            with sub_col2:
                if opcoes == "Atestado":
                    st.info('📋 Não esqueça de enviar o atestado. Vá ao menu "Gerenciamento", clique em Atestados')
                elif opcoes == "Falta":
                    detalhes = st.text_area('👷🏽‍♂️ ***Justifique com poucas palavras***')
                    opcoes = "Falta: {}".format(detalhes)
                else:
                    if "Desmobilizar" not in st.session_state:
                        st.info("🚀 Após você atualizar esses dados, verifique se o(a) colabor(a) estará na aba OCIOSOS.")
                
                nova_atividade = opcoes

            submit_button = st.button("Atualizar")   
            if  submit_button:
                edit_task_data(novo_colaborador,nova_funcao,nova_atividade,novo_escalado,novo_contrato,nova_data,novo_responsavel,colaborador,funcao,atividade,escalado,contrato,data,responsavel)
                add_data(colaborador,funcao,atividade,escalado,contrato,data,responsavel)
                st.success("💻 {} atualizado com sucesso! 💻".format(colaborador))
         
