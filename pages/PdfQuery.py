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

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text


def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks


def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
    # embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore


def get_conversation_chain(vectorstore):
    llm = ChatOpenAI()
    # llm = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature":0.5, "max_length":512})

    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain


def handle_userinput(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)







    
def UI():
    # Add custom HTML and CSS using Bootstrap
    bootstrap_html = """

        <center>

        <h3 style="margin-bottom:100px;"><span style="color: #2b86d9;font-weight:800;text-align:center">Multiple PDF Query</span>:<span style="color:#000;">Effortlessly conduct precise PDF queries with Multiple PDF Query.</span></h3>
        </center>

        

        <div class="cards-list">


        <a href="https://infrared-2p52zc9tdhxech2i8ok9pf.streamlit.app/PdfQuery">
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
    load_dotenv()

    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header("Engage in a conversation with multiple PDFs")
    user_question = st.text_input("Inquire about your documents:")
    if user_question:
        handle_userinput(user_question)

    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs = st.file_uploader(
            "Upload your PDFs here and click on 'Process'", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing"):
                # get pdf text
                raw_text = get_pdf_text(pdf_docs)

                # get the text chunks
                text_chunks = get_text_chunks(raw_text)

                # create vector store
                vectorstore = get_vectorstore(text_chunks)

                # create conversation chain
                st.session_state.conversation = get_conversation_chain(
                    vectorstore)


if __name__ == '__main__':
    main()
