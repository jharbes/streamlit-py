import streamlit as st
from PIL import Image

#Imagem
cachorrinho = Image.open('./Mídia/dog.jpg')
st.subheader('1-Inserindo uma imagem')
st.image(cachorrinho, caption='Um cachorro desconfiado')

#Audio
meu_audio = open('./Mídia/Scratching The Surface.mp3','rb')
abrir_audio = meu_audio.read()
st.subheader('2-Arquivos de Áudio')
st.audio(abrir_audio, format='audio/mp3')

#Vídeo
arquivo_video = open('./Mídia/Buildings.mp4', 'rb')
abrir_video = arquivo_video.read()
st.subheader('3-Inserir um Vídeo')
st.video(abrir_video)