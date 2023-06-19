import streamlit as st
import datetime


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


st.write('Cliente: ',varClient)
st.write('Banco: ',varBanco)
st.write('Parcelas: ',varParcela)
st.write('Data de Vencimento: ',varData)