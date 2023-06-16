"""
Para isso precisamos criar uma pasta de nome .streamlit na pasta raiz de seu aplicativo e dentro dela criar um arquivo chamado config.toml

Nele vamos adicionar todas as configurações de temas relacionadas ao seu aplicativo ou cores da empresa como tema de seu aplicativo

Outras informações adicionais podem ser preenchidas no mesmo arquivo para outros fins de configuracao da aplicacao 

"""


# Exemplo de preenchimento do config.toml

[theme]
base="dark"
primaryColor="#ffffff"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#9DD1F1" # cor do sidebar
textColor= "#000000"
font="serif"

# Para cores, podemos usar os formatos: "green", "#FFDE5A" ou RGB(61,183,228)
# Para fontes estão disponíveis: "sans serif", "serif", "monospace"
# Pode-se usar uma tema base, com base="light", e fazer alterações

# secondaryBackgroundColor é a cor de fundo do sidebar e menu