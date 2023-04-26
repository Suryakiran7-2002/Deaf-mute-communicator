import streamlit as st
from streamlit_webrtc import webrtc_streamer
import base64
l=['a','b','c','dance','how']


for t in l:
    try:
        
        
        file_ = open('images/'+t+'.gif', "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="">',
            unsafe_allow_html=True)
    except:
        
        st.image('images/'+t+'.jpg',width = 720)
