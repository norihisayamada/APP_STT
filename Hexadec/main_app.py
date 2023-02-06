import streamlit as st
from PIL import Image
#ImageのIは大文字

st.title('Hexadec')
st.caption('Streamlitで作成した動画用のテストアプリです')
# 画像
image = Image.open('images.png')
st.image(image, width=200)
