from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="taiseer.Ai" , page_icon=":tada:", layout="wide")

def load_lottieurl(url1):
    r = requests.get(url1)
    if r.status_code !=200:
        return None
    return  r.json()
#---- LOAD ASSETS ----
#lottie_coding = load_lottieurl("https://lottiefiles.com/free-animation/coding-line-4xkhlrq99j")
img_contact_form1 = Image.open("images/hello_world.png")
img_contact_form2 = Image.open("images/i_touch_grass.jpg")
img_contact_form3 = Image.open("images/rock_and_roll.png")
#----- HEADER SECTION -----
with st.container():
    st.subheader("Hi im taiseer ur fav not working Ai :wave:")
    st.title("my music taste is OLD")
    st.write("i was made to not compete with chatgpt")
    st.write("[learn more >](https://istodaytietuesday.com/)")
#---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("what i do")
        st.write("##")
        st.write(
                 """
                 - nothing
                 """)
    with right_column:
        st.write("##")
        st.write("""              
                                            your maw
                  """)
with st.container():
    st.write("---")
    st.header("your 1 and only AI")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_contact_form3)
    with text_column:
        st.subheader("check dis out")
        st.write("""
        me playing
        """
                 )
        st.markdown("[watch video...](https://www.instagram.com/p/C-hw6hzgL8ViAvF21nrJoTEoH5RZsEEjaZtK4s0/)")
with st.container():
    image_column1, image_column2 = st.columns((1,1))
    with image_column1:
        st.image(img_contact_form1)
    with image_column2:
        st.image(img_contact_form2)
#---- CONTACT ----
with st.container():
    st.write("---")
    st.header("get in touch with me!")
    st.write("##")
    contact_form = """
    <form action="https://www.linkedin.com/in/ahmed-taiseer-00a01a228?trk=contact-info" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="your name" required>
     <input type="email" name="email" placeholder="your email" required>
     <textarea name="message" placeholder="your message here" required></textarea>
     <button type="submit">Send</button>
</form> 
"""

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()
