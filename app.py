import streamlit as st

from crud import inserir_aluno, listar_aluno, atualizar_alunos, deletar_alunos
# python -m pip install streamlit

#Rodar o streamlit
# python -m streamlit run app.py

st.set_page_config(page_title="Gerenciamento de alunos", page_icon="👩‍🎓")

st.title("Sistema de alunos com MYSQL")

menu = st.sidebar.radio("Menu", ["Adicionar aluno", "Listar alunos", "Atualizar idade", "Deletar aluno"])

if menu == "Adicionar aluno":
    st.subheader("➕ Inserir aluno")
    nome = st.text_input("Nome", placeholder="Digite seu nome")
    idade = st.number_input("Idade", min_value=8, step=1)
    if st.button("Cadastrar"):
        if nome.strip() != "":
            inserir_aluno(nome, idade)
            st.success(f"Aluno {nome} cadastrado com sucesso!")
        else:
            st.warning("O campo nome não pode ser vazio.")
elif menu =="Listar aluno":
    st.subheader ("Lista de aluno cadastrados. ")
    alunos = listar_aluno()
    if alunos:
        st.dataframe(alunos)
    else:
        st.info("Nenhum aluno cadastrado.")

elif menu == "Atualizar idade":
    st.subheader("Atualizar idade")
    alunos = listar_aluno()
    if alunos:
    






