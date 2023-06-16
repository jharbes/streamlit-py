import streamlit as st

# cria um menu dentro do sidebar do streamlit ou na parte de cima do app
from streamlit_option_menu import option_menu


# opcao para colocar o menu no sidebar verticalmente

with st.sidebar:
    selected=option_menu(
        # item obrigatorio
        menu_title='Menu Principal', 

        # item obrigatorio
        options=['Início','Vendas','Relatórios','Dashboards','Suporte'],

        # icones do bootstrap https://icons.getbootstrap.com
        # colocamos o nome dos icones da pagina do bootstrap na mesma ordem do options para associar o icone à opcao da pagina
        icons=['house','basket','bandaid','bar-chart','bell'],

        menu_icon='cast',

        default_index=0,

        # podemos também estilizar o menu com CSS por meio da opção styles= usando um dicionario para passar as informacoes do CSS
        
        # styles={
        #     "container": {"padding": "0!important", "background-color": "purple"},
        #     "icon": {"color": "orange", "font-size": "25px"},
        #     "nav-link": {
        #         "font-size": "15px",
        #         "text-align": "left",
        #         "margin": "0px",
        #         "--hover-color": "darkgray",
        #     },
        #     "nav-link-selected": {"background-color": "gray"},
        # },
    )


# podemos tambem colocar o menu na parte superior do aplicativo, fora do sidebar, para isso usamos o seguinte codigo:

# selected=option_menu(
#         # item obrigatorio
#         menu_title='Menu Principal', 

#         # item obrigatorio
#         options=['Início','Vendas','Relatórios','Dashboards','Suporte'],

#         # icones do bootstrap https://icons.getbootstrap.com
#         # colocamos o nome dos icones da pagina do bootstrap na mesma ordem do options para associar o icone à opcao da pagina
#         icons=['house','basket','bandaid','bar-chart','bell'],

#         menu_icon='cast',

#         default_index=0,

#         # faz o menu ficar na horizontal
#         orientation='horizontal'
#     )