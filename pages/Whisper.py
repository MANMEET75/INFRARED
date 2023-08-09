import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmlTemplates import css, bot_template, user_template
from langchain.llms import HuggingFaceHub
import os
import config

os.environ['OPENAI_API_KEY'] = config.OPENAI_API_KEY


st.set_page_config(
    page_title="Infrared",
    page_icon="https://revoquant.com/assets/img/logo/logo-dark.png"
)


def sidebar():
    with st.sidebar:
        st.markdown(
            f"""
           
            <a href="http://revoquant.com" target="_blank">
              <div style="padding: 0px; border-radius: 0px; text-decoration: none; font-family: cursive; font-size: 16px; white-space: nowrap; text-align: center; position: absolute; bottom: 0; width: 100%;">
              <center>
               <img style="position:relative;bottom:250px;" src="https://github.com/MANMEET75/INFRARED/raw/main/ilogo.png" width="270">
              </center>
              </div>

            </a>
          
            
            """,
            unsafe_allow_html=True,
        )

if __name__ == "__main__":
    sidebar()







    
def UI():
    # Add custom HTML and CSS using Bootstrap
    bootstrap_html = """

        <center>

        <h3 style="margin-bottom:100px;"><span style="color: #2b86d9;font-weight:800;text-align:center">Multiple PDF Query</span>:<span style="color:#000;">Effortlessly conduct precise PDF queries with Multiple PDF Query.</span></h3>
        </center>

        

        <div class="cards-list">


        <a href="https://infrared-2p52zc9tdhxech2i8ok9pf.streamlit.app/Whisper">
        <div class="card 2">
        <div class="card_image">
            <img src="https://i.pinimg.com/originals/83/37/a5/8337a5a27a627d7b54f4526dc8a53f1f.gif" />
            </div>
        <div class="card_title title-dark">
            <p>PDF Query</p>
        </div>
        </div>
        </a>
       
    




        
        

    


    """

    # CSS code for Bootstrap
    bootstrap_css = """
    <style>
        [data-testid=stHeader]{
        background-color: #2b86d9;
        }
        [data-testid=stSidebar] {
        background-color: #D6E4E5;
        }
        [data-testid=stHeader] {
            background-color: #2b86d9;
        }
        [data-testid=stVerticalBlock] {
        position: relative;
        top: 100px;
        }

                
        [data-testid=stAppViewContainer] {
            background-color: #F1F6F5;
        }
    
        [data-testid=stMarkdownContainer] {
            color: #2b86d9;
        }
        [id='tabs-bui2-tab-0'] {
            color: #2b86d9;
        }
        .st-c7{
        background-color: #ccc;
        }


        
     
      
        a{
            text-decoration: none;
        }
      
        .cards-list {
        z-index: 0;
        width: 100%;
        display: flex;
        justify-content: space-around;
        flex-wrap: wrap;
        }

        .card {
        margin: 70px auto;
        width: 300px;
        height: 300px;
        border-radius: 40px;
        box-shadow: 5px 5px 30px 7px rgba(0,0,0,0.25), -5px -5px 30px 7px rgba(0,0,0,0.22);
        cursor: pointer;
        transition: 0.4s;
        }

        .card .card_image {
        width: inherit;
        height: inherit;
        border-radius: 40px;
        }

        .card .card_image img {
        width: inherit;
        height: inherit;
        border-radius: 40px;
        object-fit: cover;
        }

        .card .card_title {
        text-align: center;
        border-radius: 0px 0px 40px 40px;
        font-family: sans-serif;
        font-weight: bold;
        font-size: 30px;
        margin-top: -80px;
        height: 40px;
        font-weight:800;
        position: relative;
        top: 110px;
        }
        .card_title p{
        color: #000;
        text-decoration: none;
        }
        a:link {
        text-decoration: none;
        }

        .card:hover {
        transform: scale(0.9, 0.9);
        box-shadow: 5px 5px 30px 15px rgba(0,0,0,0.25), 
            -5px -5px 30px 15px rgba(0,0,0,0.22);
        }

        .title-white {
        color: white;
        }

        .title-black {
        color: black;
        }

        @media all and (max-width: 500px) {
        .card-list {
            /* On small screens, we are no longer using row direction but column */
            flex-direction: column;
        }
        }


        /*
        .card {
        margin: 30px auto;
        width: 300px;
        height: 300px;
        border-radius: 40px;
        background-image: url('https://i.redd.it/b3esnz5ra34y.jpg');
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
        background-repeat: no-repeat;
        box-shadow: 5px 5px 30px 7px rgba(0,0,0,0.25), -5px -5px 30px 7px rgba(0,0,0,0.22);
        transition: 0.4s;
        }
        */
        .container{
            margin:50px;
        }
       
        /* Add your custom CSS here or link to an external stylesheet */
        /* For Bootstrap classes to work, make sure you have included the Bootstrap CSS and JS files in your index.html file */
    </style>
    """

    # JavaScript code to enhance the app
    bootstrap_js = """
    <script>
        // Add your custom JavaScript here or link to an external JS file
        // For Bootstrap JavaScript components to work, make sure you have included the Bootstrap CSS and JS files in your index.html file
    </script>
    """

    # Combine and render the HTML, CSS, and JavaScript
    st.markdown(bootstrap_css, unsafe_allow_html=True)
    st.markdown(bootstrap_html, unsafe_allow_html=True)
    st.components.v1.html(bootstrap_js)
    
if __name__ == "__main__":
    UI()


footer="""<style>


.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: #2b86d9;
color: black;
text-align: center;

}
#footerText{
color:#D6E4E5;
position: relative;
text-align: center;
margin-top:20px;
margin-bottom:20px;
}
</style>
<center>
<div class="footer">
<p id="footerText">Copyright © 2023 All Rights Reserved Passion By RevoQuantAI</p>
</div>
</center>
"""
st.markdown(footer,unsafe_allow_html=True)


def main():
    st.write("working on whisper")
   


if __name__ == '__main__':
    main()
