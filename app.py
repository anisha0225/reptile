from PIL import Image
#for importing image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
#for inserting the animations
st.set_page_config(page_title="My Webpage",page_icon=":tada:",layout="wide")
def load_lottieurl(url):
  r=requests.get(url)
  #The get() method sends a GET request to the specified url.
  if r.status_code!=200: 
    #A status code informs you of the status of the request. 
    # For example, a 200 OK status means that your request was successful,
    #  whereas a 404 NOT FOUND status means that the resource you were looking for was not found.
    return None
  return r.json()
#The Python requests library provides a helpful method, json(),
#  to convert a Response object to a Python dictionary.
def local_css(file_name):
  with open(file_name) as f:
    st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
local_css("styles/style.css")    
#LOAD ASSETS
lottie_coding=load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_v4isjbj5.json")
#it is taking the images in the folder
img_contact_form=Image.open("images/Screenshot (52).png")
img_animation_lottie=Image.open("images/Screenshot (51).png")
#----HEADER SECTION---
with st.container():
 st.subheader("Hi,I am Anisha :confetti_ball:")
 st.title("A CSE student from JISCE")
 st.write("I love to making websites")
 st.write("[Learn More>](https://youtu.be/VqgUkExPvLY)")
#The first and most obvious use of the st. write() command is to display text.
#Local URL: http://localhost:8501
#Network URL: http://192.168.0.11:8501
with st.container():
  st.write("---")
  #it divids the page
  left_column,right_column=st.columns(2)
  #there will be two columns
  with left_column:
   st.header("What I Do")
   st.write("##")
   st.write(
     """
     About Myself:
     - I am currently pursuing b.tech cse from jisce.
     - and trying to make some web pages by streamlit.
     - After using some languages it seems that streamlit is much easier to make website rather than any language.
     - it is less time consuming.
     - The youtube channel 'Coding is Fun' make this more easy and fun for me to learn streanlit and make web pages by it...
     """
  )
  st.write("[Real page demo link>](https://www.youtube.com/redirect?event=comments&redir_token=QUFFLUhqbGdzVnZMUGZRT21weDBKSGZqX3NOdGlET01iQXxBQ3Jtc0trNHZfdjhDUWNzdEJDcTlJNUxOYlBqQ1pyVUxNbTJHejNEWU9Ta3M2ZzJKUmQ4c01VNjJsdlBQMlZqQXQtUFFWZUdoT3RWelhGTF9jS21fTlRkaS1Pd1RXaFVJdUVScWVYdkJNOFJSYk5HaG5vS2RyVQ&q=https%3A%2F%2Fshare.streamlit.io%2Fsven-bo%2Fpersonal-website-streamlit%2Fapp.py&stzid=Ugw7baMUgu4VstZPswV4AaABAg)")
  with right_column:
    st_lottie(lottie_coding,height=300,key="coding")
    #here it starts how to insert text+image in a page first we are dividing the pag in left and
    #right columns for making it easy
  with st.container():
    st.write("---")
    st.header("Projects")  
    st.write("##")
    image_column,text_column=st.columns((1,2))
    #making the two parts basically two container one for image and other for text
    with image_column:
      st.image(img_animation_lottie)
    with text_column: 
      st.subheader("Integrate Lottie Animations Inside Your Streamlit App")
      st.write(
        """
        I am learning how to insert lottie files in streamlit..
        Animations make our web page more fun and beautiful also eye-catching..
        Lottie files are the easiest way to do this image insert
        """
      )
      st.markdown("[Watch Video...](https://youtu.be/TXSOitGoINE)")
      #markdown makes  [] this written part highlighted and by clicking that text we are redirected to the link 
      #associated with it which is in written here
  with st.container():
    image_column,text_column=st.columns((1,2))
    with image_column:
      st.image(img_contact_form)
    with text_column:
      st.subheader("Integrate contact form Inside your streamlit app")
      st.write(
        """
        It is fun to experience the streamlit part of the python..
        'Codin Is Fun' makes it easier to have the contact form in any streamlit app..
        Let's see how to insert it..
        """
      )  
      st.markdown("[Watch Video...](https://youtu.be/FOULV9Xij_8)")
  with st.container():
    st.write("---")
    st.header("Get in touch with me!")    
    st.write("##")
  contact_form="""
  <form action="https://formsubmit.co/mousumisarkar422002@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name"  placeholder="Your Name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Type your message here" required></textarea>
     <button type="submit">Send</button>
  </form>
  """  
  left_column,right_column=st.columns(2)
  with left_column:
    st.markdown(contact_form,unsafe_allow_html=True)
  with right_column:
    st.empty()  