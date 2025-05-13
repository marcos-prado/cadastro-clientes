import streamlit as st
import mysql.connector
import crud


def main():
    st.title("Cadastro de Clientes")

    # Display options for CRUD Operations
    option = st.sidebar.selectbox(
        "Selecione uma Opção", ("Cadastrar", "Vizualizar", "Atualizar", "Excluir")
    )
    # Perform Selected CRUD Operation

    if option == "Cadastrar":
        st.subheader("Cadastrar um cliente")
        nome = st.text_input("Informe o nome do cliente:")
        endereco = st.text_input("Informe o endereço:")
        dt_nasc = st.date_input("Informe a data de nascimento")
        tipo_cliente = st.selectbox(
            "Tipo do Cliente", ["Pessoa Física", "Pessoa Juridica"]
        )
        st.write("Tipo de cliente selecionado: ", tipo_cliente)

        if st.button("Registrar Cliente"):
            sql = "INSERT INTO cliente (nome,endereco,dt_nasc,tipo_cliente) VALUES (%s,%s,%s,%s)"
            val = (nome, endereco, dt_nasc, tipo_cliente)
            crud.mycursor.execute(sql, val)
            crud.mydb.commit()
            st.success("Registro salvo com sucesso")

    elif option == "Vizualizar":
        st.subheader("Registros Disponíveis")
        crud.mycursor.execute("SELECT * FROM cliente")
        result = crud.mycursor.fetchall()
        for row in result:
            st.write(row)

    elif option == "Atualizar":
        st.subheader("Atualizar um Registro")
        id = st.number_input("Informe o registro (ID)", min_value=1)
        nome = st.text_input("Atualizar o nome do cliente: ")
        endereco = st.text_input("Atualizar o endereço: ")
        dt_nasc = st.date_input("Corrigir a data de nascimento: ")
        tipo_cliente = st.selectbox(
            "Alterar o Tipo de Cliente", ["Pessoa Física", "Pessoa Juridica"]
        )
        if st.button("Atualizar Dados"):
            sql = "UPDATE cliente SET nome=%s,endereco=%s,dt_nasc=%s,tipo_cliente=%s WHERE id =%s"
            val = (nome, endereco, dt_nasc, tipo_cliente,id)
            crud.mycursor.execute(sql, val)
            crud.mydb.commit()
            st.success("Dados Atualizados com Sucesso!!!")

    elif option == "Excluir":
        st.subheader("Excluir um Registro")
        id = st.number_input("Informe o registro (ID)", min_value=1)
        if st.button("Excluir Registro"):
            sql = "DELETE FROM cliente WHERE id=%s"
            val = (id,)
            crud.mycursor.execute(sql, val)
            crud.mydb.commit()
            st.success("Registro Excluido com Sucesso!!!")


if __name__ == "__main__":
    main()
