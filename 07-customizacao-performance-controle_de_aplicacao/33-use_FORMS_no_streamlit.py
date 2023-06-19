import streamlit as st
import datetime


# Uma opção muito utilizada para formulários é usar um st.form, isso faz com que os dados selecionados só sejam processados após o envio por um botão de submit, evitando alterações em tempo real ao mexer nos formulários, ensejando assim apenas uma atualização única após o envio completo do formulário
with st.form('Formulário de seleção de parâmetros'):

    st.subheader('Formulários no Streamlit')

    varClient=st.radio(
        '1- Selecione o cliente:',
        ('Space X','Microsoft','Apple','Google','Amazon')
    )

    varBanco=st.multiselect(
        '2- Selecione o banco:',
        ('Bradesco','Itaú','NuBank','Caixa','Banco do Brasil')
    )

    varParcela=st.slider(
        '3- Quantas parcelas deseja financiar?',
        # 0 a 60 será o range total e 30 o valor inicial para o slider
        0,60,30
    )

    varData=st.date_input(
        '4- Selecione a data de vencimento:',
        # aqui colocamos a data inicial a aparecer no app, podemos usar datetime.now() para que seja a data atual
        datetime.date(2023,1,1)
    )


    '----------------------------------------------------'

    botao_formulario=st.form_submit_button('Filtrar')

st.write('')
st.write('')

st.write('Cliente: ',varClient)
st.write('Banco: ',varBanco)
st.write('Parcelas: ',varParcela)
st.write('Data de Vencimento: ',varData)

