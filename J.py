from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
import numpy as np
from streamlit_option_menu import option_menu

# more emojis here : https://www.webfx.com/tools/emoji-cheat-sheet/

def home_page():
    st.title(f" {'Home'}")
    def load_image(img):
        im = Image.open(img)
        image = np.array(im)
        return image
    def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    #load assets
    lottie_Coding = "https://iconscout.com/lotties/smart-building"
    img_contact_form = Image.open('C:/Users/mrsam/Pictures/Jackie1.png')
    img_lottie_animation = Image.open('C:/Users/mrsam/Pictures/Jackie1.png')
    #header section
    with st.container():
        st.subheader("Hello my name is Jacqueline Lara :wave: ")
        st.title("I am a architect from Philadelphia")
        st.write("I am passionate about making buildings and adding my own twist to the design.")
        st.write("[Learn More >](link)")

        #what i do
        with st.container():
            st.write("---")
            left_column, right_column = st.columns(2)
            with left_column:
                st.header("What I do")
    st.write("##")
    st.write(0)
    st.write("[Renderings >](Link for rendering)")
    with right_column: 
        st_lottie(lottie_Coding, height=300, key="coding" )
#scroll loop the portfolio
def projects_page():
    with open("D:/Newfolder/WebJ/parallaxscroll.html", "r") as file:
        html_code = file.read()

    st.components.v1.html(html_code, height=4000)
    st.title(f" {'Portfolio'}")
    st.write("W")
    image = Image.open('C:/Users/mrsam/Pictures/page_1.JPG')
    st.image(image, caption= "First Page", use_column_width=True)
    image = Image.open('C:/Users/mrsam/Pictures/page_2.JPG')
    st.image(image, caption= "Second Page", use_column_width=True)
    image = Image.open('C:/Users/mrsam/Pictures/page_3.JPG')
    st.image(image, caption= "Third Page", use_column_width=True)
    image = Image.open('C:/Users/mrsam/Pictures/page_4.JPG')
    st.image(image, caption= "Fourth Page", use_column_width=True)
    image = Image.open('C:/Users/mrsam/Pictures/page_5.JPG')
    st.image(image, caption= "Fifth Page", use_column_width=True)
    image = Image.open('C:/Users/mrsam/Pictures/page_6.JPG')
    st.image(image, caption= "Sixth Page", use_column_width=True)
    image = Image.open('C:/Users/mrsam/Pictures/page_7.JPG')
    st.image(image, caption= "Seventh Page", use_column_width=True)
    image = Image.open('C:/Users/mrsam/Pictures/page_8.JPG')
    st.image(image, caption= "Eighth Page", use_column_width=True)
    image = Image.open('C:/Users/mrsam/Pictures/page_9.JPG')
    st.image(image, caption= "Nineth Page", use_column_width=True)
    image = Image.open('C:/Users/mrsam/Pictures/page_10.JPG')
    st.image(image, caption= "Tenth Page", use_column_width=True)
    image = Image.open('C:/Users/mrsam/Pictures/page_11.JPG')
    st.image(image, caption= "Eleventh Page", use_column_width=True)
    image = Image.open('C:/Users/mrsam/Pictures/page_12.JPG')
    st.image(image, caption= "Twelveth Page", use_column_width=True)
    image = Image.open('C:/Users/mrsam/Pictures/page_13.JPG')
    st.image(image, caption= "Thirtenth Page", use_column_width=True)
    image = Image.open('C:/Users/mrsam/Pictures/page_14.JPG')
    st.image(image, caption= "Fourtheenth Page", use_column_width=True)
def contact_page():
    st.title(f" {'Contact'}")
    st.write("Lets go")

with st.sidebar:
    selected = option_menu(
         menu_title=None,
        options=["Home","Portfolio","Contact"],
        icons=["house","book","envelope"],
        menu_icon="cast",
        default_index=0, 
    )

if selected == "Home":
     home_page()
elif selected == "Portfolio":
     projects_page()
elif selected == "Contact":
     contact_page()
