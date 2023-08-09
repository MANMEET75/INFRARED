#pip install streamlit langchain openai faiss-cpu tiktoken
import streamlit as st
from streamlit_chat import message
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.vectorstores import FAISS
import tempfile
import os
import config



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

        <h3 style="margin-bottom:100px;"><span style="color: #2b86d9;font-weight:800;text-align:center">Streamlined Excel Query</span>:<span style="color:#000;">Streamlined Excel Query: Effortlessly unravel your messy data files.</span></h3>
        </center>

        

        <div class="cards-list">


        <a href="https://infrared-2p52zc9tdhxech2i8ok9pf.streamlit.app/ExcelQuery">
        <div class="card 2">
        <div class="card_image">
            <img src="https://cdn.dribbble.com/users/489311/screenshots/6691380/excel-icons-animation.gif" />
            </div>
        <div class="card_title title-dark">
            <p>Excel Query</p>
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


st.title("Engage in a conversation with CSV files using the OpenAI API.")




os.environ['OPENAI_API_KEY'] = config.OPENAI_API_KEY






uploaded_file = st.sidebar.file_uploader("upload", type="csv")

if uploaded_file :
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_file_path = tmp_file.name

    loader = CSVLoader(file_path=tmp_file_path, encoding="utf-8")
    data = loader.load()

    embeddings = OpenAIEmbeddings()
    vectors = FAISS.from_documents(data, embeddings)

    chain = ConversationalRetrievalChain.from_llm(llm = ChatOpenAI(temperature=0.0,model_name='gpt-3.5-turbo', openai_api_key=config.OPENAI_API_KEY),
                                                                      retriever=vectors.as_retriever())

    def conversational_chat(query):
        
        result = chain({"question": query, "chat_history": st.session_state['history']})
        st.session_state['history'].append((query, result["answer"]))
        
        return result["answer"]
    
    if 'history' not in st.session_state:
        st.session_state['history'] = []

    if 'generated' not in st.session_state:
        st.session_state['generated'] = ["Hello ! Ask me anything about " + uploaded_file.name + " 🤗"]

    if 'past' not in st.session_state:
        st.session_state['past'] = ["Hey ! 👋"]
        
    #container for the chat history
    response_container = st.container()
    #container for the user's text input
    container = st.container()

    with container:
        with st.form(key='my_form', clear_on_submit=True):
            
            user_input = st.text_input("Query:", placeholder="Talk about your csv data here (:", key='input')
            submit_button = st.form_submit_button(label='Send')
            
        if submit_button and user_input:
            output = conversational_chat(user_input)
            
            st.session_state['past'].append(user_input)
            st.session_state['generated'].append(output)

    if st.session_state['generated']:
        with response_container:
            for i in range(len(st.session_state['generated'])):
                message(st.session_state["past"][i], is_user=True, key=str(i) + '_user', avatar_style="big-smile")
                message(st.session_state["generated"][i], key=str(i), avatar_style="thumbs")
                
#streamlit run tuto_chatbot_csv.py


