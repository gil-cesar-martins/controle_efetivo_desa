# Create and Edit/Update
import streamlit as st
from datetime import datetime
from db_functions import (create_table, add_data, view_all_tasks,view_all_worker_names, view_all_unique_worker_names,
                          get_task_by_worker_name, edit_task_data, mobile,view_all_unique_task_names,delete_data)

def run_task_page():
    create_table()
    submenu = st.sidebar.selectbox("Submenu",["Adicionar","Editar"])
    
    if submenu == "Adicionar":
        with st.form(key='Adicionar',clear_on_submit=True):
            col1,col2 = st.columns(2)
        
            with col1:
                colaborador = st.text_input("Colaborador")
                funcao = st.text_input("Função")
            
            with col2:
                data_padrao = st.date_input("Data",format='DD/MM/YYYY')
                data_obj = datetime.strftime(data_padrao,'%d/%m/%Y')
                data = data_obj
                atividade = st.text_input("Atividade")
            
            
            if atividade == "":
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
                add_data(colaborador,funcao,atividade,data)
                st.success("Adicionado:: {}".format(colaborador))
        
            #results = view_all_tasks()  
            #st.write(results)
        
    elif submenu == "Editar":
        st.subheader("Seleção de colaboradores",divider='rainbow')
        
        list_of_tasks = [i[0] for i in view_all_unique_worker_names()]
        selected_task = st.selectbox("Colaborador:",list_of_tasks)
        task_result = get_task_by_worker_name(selected_task)
        
        st.subheader("Atualizar/Editar Dados",divider='rainbow')
        if task_result:
            colaborador = task_result[0][0]
            funcao = task_result[0][1]
            atividade = task_result[0][2]
            data = task_result[0][3]
    
            col1,col2 = st.columns(2)
            
            with col1:
                novo_colaborador = st.text_input("Colaborador",colaborador)
                nova_funcao = st.text_input("Função", funcao)
                
            with col2:
                data_padrao2 = st.date_input("Data",format='DD/MM/YYYY')
                data_obj2 = datetime.strftime(data_padrao2,'%d/%m/%Y')
                nova_data = data_obj2
                nova_atividade = st.text_input("Atividade",atividade)
                if nova_atividade == "":
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
                
            if  st.button("Atualizar"):
                    edit_task_data(novo_colaborador,nova_funcao,nova_atividade,nova_data,colaborador,funcao,atividade,data)
                    add_data(colaborador,funcao,atividade,data)
                    st.success("💻 {} atualizado com sucesso! 💻".format(colaborador))
            
            #st.write("Escolha alguém")
            #hadouken = mobile()
            #for colaborador in hadouken:
            #    st.checkbox(colaborador[0])  
            
if __name__ == '__run_task_page__':
    run_task_page()