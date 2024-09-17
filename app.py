from PIL import Image
import streamlit as st

st.set_page_config(page_title="taiseer.Ai", page_icon=":tada:", layout="wide")

# ---- Function to Load Image ----
def load_image(image_path):
    try:
        return Image.open(image_path)
    except FileNotFoundError:
        st.warning(f"File not found: {image_path}")
        return None

# ---- Load Images ----
img_contact_form1 = load_image("images/alive.png")
img_contact_form2 = load_image("images/i_touch_grass.jpg")
img_contact_form3 = load_image("images/rock_and_roll.png")

# ----- HEADER SECTION -----
with st.container():
    st.subheader("Hi I'm taiseer, your fav not working Ai :wave:")
    st.title("My music taste is OLD")
    st.write("I was made to not compete with chatgpt")
    st.write("[learn more >](https://istodaytietuesday.com/)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I Do")
        st.write("##")
        st.write("- Nothing")
    with right_column:
        st.write("##")
        st.write("Your maw")

# ---- SHOW IMAGES ----
with st.container():
    st.write("---")
    st.header("Your 1 and Only AI")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        if img_contact_form3:
            st.image(img_contact_form3)
    with text_column:
        st.subheader("Check This Out")
        st.write("Me playing")
        st.markdown("[Watch video...](https://www.instagram.com/p/C-hw6hzgL8ViAvF21nrJoTEoH5RZsEEjaZtK4s0/)")

with st.container():
    image_column1, image_column2 = st.columns((1, 1))
    with image_column1:
        if img_contact_form1:
            st.image(img_contact_form1)
    with image_column2:
        if img_contact_form2:
            st.image(img_contact_form2)

# ---- CONTACT FORM ----
with st.container():
    st.write("---")
    st.header("Get in touch with me!")
    st.write("##")
    contact_form = """
    <form action="ahmed.theeditor@gmail.com" method="POST">
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
        st.write("This website was made by Krafs")
