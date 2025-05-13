import streamlit as st

st.title("Cadastro de Clientes")

nome = st.text_input("Digite o nome do cliente")
endereco = st.text_input("Digite o endereço")
dt_nasc = st.date_input("Escolha a data de nascimento")
tipo_cliente = st.selectbox("Tipo de Cliente",["","Pessoa Física","Pessoa Juridica"])

cadastrar = st.button("Cadastrar Cliente")
    if cadastrar:
        with open ("clientes.txt" , "w") as arquivo:
            arquivo.write(f"{nome}, {endereco},{dt_nasc},{tipo_cliente}")
            

