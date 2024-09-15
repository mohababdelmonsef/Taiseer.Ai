from PIL import Image
import streamlit as st
import os

st.set_page_config(page_title="taiseer.Ai", page_icon=":tada:", layout="wide")

# Define the absolute path to your image folder
image_folder = r"C:\Users\LENOVO\PycharmProjects\pythonProject\images"

#---- LOAD ASSETS ----
img_contact_form1 = Image.open(os.path.join(image_folder, "shehata.png"))
img_contact_form2 = Image.open(os.path.join(image_folder, "i_touch_grass.jpg"))
img_contact_form3 = Image.open(os.path.join(image_folder, "rock_and_roll.png"))

#----- HEADER SECTION -----
with st.container():
    st.subheader("Hi I'm Taiseer, your fav not working AI :wave:")
    st.title("My music taste is OLD")
    st.write("I was made to not compete with ChatGPT")
    st.write("[learn more >](https://istodaytietuesday.com/)")

#---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I Do")
        st.write("##")
        st.write(
            """
            - Nothing
            """
        )
    with right_column:
        st.write("##")
        st.write("Your Maw")

#---- IMAGE SECTION ----
with st.container():
    st.write("---")
    st.header("Your one and only AI")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form3)
    with text_column:
        st.subheader("Check this out")
        st.write("Me playing")
        st.markdown("[Watch video...](https://www.instagram.com/p/C-hw6hzgL8ViAvF21nrJoTEoH5RZsEEjaZtK4s0/)")

#---- DISPLAY OTHER IMAGES ----
with st.container():
    image_column1, image_column2 = st.columns((1, 1))
    with image_column1:
        st.image(img_contact_form1)
    with image_column2:
        st.image(img_contact_form2)

#---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get in touch with me!")
    st.write("##")
    contact_form = """
    <form action="https://www.linkedin.com/in/ahmed-taiseer-00a01a228?trk=contact-info" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form> 
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.write("This website was made by Krafs")
