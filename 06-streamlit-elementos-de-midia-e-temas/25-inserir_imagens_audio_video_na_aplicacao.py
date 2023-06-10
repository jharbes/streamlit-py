import streamlit as st
from PIL import Image


# INSERINDO IMAGEM

# primeiramente salvamos a variavel importando a imagem com a biblioteca PIL por meio do metodo Image.open
meu_cachorro=Image.open('../Mídia/dog.jpg')
st.subheader('1- Imagem do meu cachorro')

# depois inserimos a imagem na pagina com st.image, o argumento caption colocará uma legenda para a imagem
st.image(meu_cachorro,caption='Um cachorro desconfiado')




# INSERINDO AUDIO

# precisamos especificar ao abrir o caminho do audio, no segundo parametro especificamos 'r' que é apenas leitura e 'b' que é arquivo binario (caso do mp3)
meu_audio=open('../Mídia/Scratching The Surface.mp3','rb')

abrir_audio=meu_audio.read()

st.subheader('2- Minha música')

# em format temos que especificar o formato do audio
st.audio(abrir_audio,format='audio/mp3')




# INSERINDO VIDEO

arquivo_video=open('../Mídia/Buildings.mp4','rb')

abrir_video=arquivo_video.read()

st.subheader('3- Vídeo dos prédios')

st.video(abrir_video)