import streamlit as st
import time as time
import datetime as datetime

# alterando o CSS do documento para editar as cores
custom_css = """
    <style>
        .css-z3au9t{
            color:red;
        }
        .css-cio0dv{
            background-color:purple;
        }
    </style>
"""

st.markdown(custom_css, unsafe_allow_html=True)


varModal=st.sidebar.selectbox(
    'Selecione o modal de transporte:',
    ('Rodoviário','Marítimo','Aéreo','Metroviário','Outro')
)

st.write('O modal selecionado foi: ',varModal)

with st.sidebar:
    varClient=st.radio(
        'Selecione o cliente:',
        ('Space X','Microsoft','Apple','Google','Amazon')
    )

    varBanco=st.multiselect(
        'Selecione o banco:',
        ('Bradesco','Itaú','NuBank','Caixa','Banco do Brasil')
    )

    varParcela=st.slider(
        'Quantas parcelas deseja financiar?',
        # 0 a 60 será o range total e 30 o valor inicial para o slider
        0,60,30
    )

    varData=st.date_input(
        'Selecione a data de vencimento:',
        # aqui colocamos a data inicial a aparecer no app, podemos usar datetime.now() para que seja a data atual
        datetime.date(2023,1,1)
    )

    # criando um spinner para gerar mensagem de que está atualizando quando mudar alguma opção no sidebar, nao funciona muito bem no modo always rerun (fica atualizando sozinho)
    with st.spinner('Carregando...'):
        time.sleep(2)
    # st.success('Pronto!')

    # abaixo temos uma versao onde a mensagem de atualizado desaparece depois de 2 segundos, observar que durante esse tempo o app nao fica resposivo
    placeholder = st.empty()
    placeholder.success('Atualizado!')
    time.sleep(1.5)  # espera 2 segundos
    placeholder.empty()  # Remove a mensagem



st.write('Cliente: ',varClient)
st.write('Banco: ',varBanco)
st.write('Parcelas: ',varParcela)
st.write('Data de Vencimento: ',varData)