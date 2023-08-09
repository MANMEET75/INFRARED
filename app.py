import os
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.decomposition import PCA
import io
import pptx
import base64
import warnings
from sklearn.preprocessing import OrdinalEncoder
import plotly.graph_objs as go
from sklearn.svm import OneClassSVM
from sklearn.neighbors import LocalOutlierFactor
import plotly.io as pio
import io
import pptx
from scipy.spatial.distance import mahalanobis
import base64
import tempfile
import numpy as np
from sklearn.linear_model import SGDOneClassSVM
import plotly.graph_objs as go
from sklearn.preprocessing import StandardScaler
import plotly.io as pio
import pandas as pd
import base64
from io import BytesIO
import tensorflow as tf
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense
from sklearn.ensemble import IsolationForest
import scipy.stats as stats
from sklearn.neighbors import KernelDensity
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
from scipy.stats import norm
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import plotly.express as px
import webbrowser
import streamlit as st
from matplotlib import style




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
style.use("ggplot")
st.set_option('deprecation.showPyplotGlobalUse', False)

# setting the configuration
st.set_page_config(
    page_title="Infrared",
    page_icon="https://revoquant.com/assets/img/logo/logo-dark.png"
)















# Define the HTML code with CSS for the marquee

# Add custom CSS
st.markdown(
    """
    <style>
    body {
        background-color: #ffffff; /* Set the background color */
        color: #222222; /* Set the text color */
        font-weight: bold; /* Set the text weight */
        font-family: sans-serif; /* Set the font family */
    }
    </style>
    """,
    unsafe_allow_html=True
)



# Add CSS styling to position the HTML code near the top
st.markdown(
    """
    <style>
    #right {
        display: flex;
        justify-content: space-between;
        margin-top: 0px;
        margin-bottom: 0px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the HTML code
st.markdown(
    """
    <div id="right">
            <img style="position:relative;" src="https://github.com/MANMEET75/INFRARED/raw/main/ilogo.png" width="350">
        <a href="http://revoquant.com/">
            <img src="https://revoquant.com/assets/img/logo/logo-dark.png" class="logo" style="width: 100px; height: auto;" />
        </a>
    </div>
    """,
    unsafe_allow_html=True
)


marquee_html = """
<html>
<head>
  <title>Beautify Image</title>
  <style>
    .heading {
      font-size: 2rem;
      color: red;
      text-shadow: 2px 2px 2px #000;
    }

    .marquee {
      width: 100%;
      overflow: hidden;
      background-color: #2b86d9;
      color: #E3F4F4;
      padding: 20px;
      margin-top: 0; /* Adjust the margin-top value here */
      text-align: center;
    }

    .marquee span {
      display: inline-block;
      animation: marquee 20s linear infinite;
      color: #E3F4F4;
      font-size: 1.2rem;
      width: 2000px; /* Slim the span */
      /* height: 50px; Slim the span in height */
      max-height: 40px; /* This will make the span 50px tall at most */
    }

    .logo {
      width: 75px;
      position: relative;
      bottom: 20px;
    }
   
       .logo1 {
      width: 75px;
      position: relative;
      bottom: 20px;
    }




    .P_logo {
      width: 150px;
      position: relative;
      bottom: 20px;
    }

    h1 {
      font-size: 60px;
      text-align: left;
      position: relative;
      top: 100px;
    }

    @keyframes marquee {
      0% { transform: translateX(100%); }
      100% { transform: translateX(-100%); }
    }
    #gif_card{
    width: 100%;
    border-radius:0%;
    }

    .cardGif .card_image_gif {
    width: inherit;
    height: inherit;
    border-radius: 0%;
    }

    .cardGif .card_image_gif img {
    width: inherit;
    height: inherit;
    border-radius: 0%;
    object-fit: cover;
    }
  </style>
</head>
<body>

  <div class="marquee">
    <span style="color: #E3F4F4; background-color: #2b86d9;">It comes with pre-built statistical and machine learning models specifically designed to identify outliers in large-scale data.</span>
  </div>
  <center>
  <br>
    <a href="https://github.com/ravipratap366/LLM_chatbot">
        <div class="cardGif 2" id="gif_card">
        <div class="card_image_gif" id="gif_card">
            <img src="https://github.com/MANMEET75/INFRARED/raw/main/lifecycle1.gif" />
            </div>
    </a>
    </div>

  </center>
</body>
</html>

"""

# Create a search bar
#search_bar = st.text_input(label="Search", placeholder="Enter your search term")
#if search_bar:
#    search_term = search_bar.lower()
#    st.write("Search results for '{}'".format(search_term))

def main():
    with st.sidebar:
        st.markdown(
            f"""
           
            <a href="http://revoquant.com" target="_blank">
              <div style="padding: 0px; border-radius: 0px; text-decoration: none; font-family: cursive; font-size: 16px; white-space: nowrap; text-align: center; position: absolute; bottom: 0; width: 100%;">
              <center>
               <img style="position:relative;top:30px;" src="https://github.com/MANMEET75/INFRARED/raw/main/ilogo.png" width="270">
              </center>
              </div>

            </a>
          
            
            """,
            unsafe_allow_html=True,
        )

if __name__ == "__main__":
    main()


import streamlit as st

# changing the color of side bar over here
st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: #D6E4E5;
    }
    [data-testid=stHeader] {
        background-color: #2b86d9;
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
  
    .st-c7 {
    background-color: #f2f2f2;
    }
    .st-d8{
    background-color:#f2f2f2
    }
    .st-d8{
    background-color:#f2f2f2
    }
    .st-cw{
    background-color:#000;
    }     
    .st-cn{
    background-color:#F1F6F5;
    }  
               
    .st-f1{
    background-color:#000;
    }  
    .eqr7zpz0{
    color:#2b86d9;
    }  
    .css-16idsys{
    color:#2b86d9;
    letter-spacing:1px;
    }  
         
    .css-5rimss{
    color:#000;
    letter-spacing:1px;
    }  
         
    #tabs-bui2-tab-0{
    color:#000;
    }  
    .css-zt5igj{
    font-size:30px;
    text-align:center;
    }  
   
         
               

            

                    
    
}
            
  
</style>
""", unsafe_allow_html=True)

st.markdown(
    f"""
    <style>
    
    </style>
    """,
    unsafe_allow_html=True
)


# Set the background color using CSS styling
background_color = """
    <style>
   
    body {
        background-color: #E3F4F4;
        font-family: Roboto, sans-serif;
    }

    .stApp {
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
    }

    .stTabs {
        margin-bottom: 2rem;
    }

    .stTab {
        background-color: #E3F4F4;
        color: #ffffff;
        padding: 0.75rem 1.5rem;
        border: none;
        border-radius: 5px 5px 0 0;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
        font-weight: bold;
    }

    .stTab:hover {
        background-color: #E3F4F4;
        cursor: pointer;
    }

    .stTab--active {
        background-color: #E3F4F4;
        color: #ffffff;
    }

    .stTabContent {
        padding: 1.5rem;
        border: 1px solid #dddddd;
        border-radius: 0 5px 5px 5px;
        background-color: #E3F4F4;
    }
    </style>
"""





# Define the CSS styles for each tab
tab_styles1 = """
<style>
    /* Main Tab */
    .button[data-baseweb="tab"]::before {
        color: #2b86d9;
        background-color: #E3F4F4;
    }

    /* About Infrared Tab */
    .button[data-baseweb="tab"]::before {
        color: #2b86d9;
        background-color: #E3F4F4;
    }

    /* Benford's Law Tab */
    .button[data-baseweb="tab"]::before {
        color: #2b86d9;
        background-color: #E3F4F4;
    }

    /* pdf Tab */
    .button[data-baseweb="tab"]::before {
        color: #2b86d9;
        background-color: #E3F4F4;
    }

    /* Z-score Tab */
    .button[data-baseweb="tab"]::before {
        color: #2b86d9;
        background-color: #E3F4F4;s
    }

    /* Isolation Forest Tab */
    .button[data-baseweb="tab"]::before {
        color: #2b86d9;
        background-color: #E3F4F4;
    }

    /* Auto-encoder Tab */
    .button[data-baseweb="tab"]::before {
        color: #2b86d9;
        background-color: #E3F4F4;
    }

    /* Process Mining Tab */
    .button[data-baseweb="tab"]::before {
        color: #2b86d9;
        background-color: #E3F4F4;
    }

    /* Other Tab Here */
    .button[data-baseweb="tab"]::before {
        color: #2b86d9;
        background-color: #E3F4F4;
   
</style>
"""



# Render the CSS styling
st.markdown(tab_styles1, unsafe_allow_html=True)

# Add your Streamlit code here
# tabs = ["HOME", "ABOUT","ExceltoCSV", "ProcessMining", "Benford's Law", "pdf", "Z-score", "Isolation Forest", "Auto-encoder" ,"other tab here"]
tabs = ["HOME", "ABOUT","EXCEL TO CSV", "PROCESS MINING","EXPLORATORY DATA ANALYSIS", "STATISTICAL METHODS", "MACHINE LEARNING METHODS", "DEEP LEARNING METHODS", "TIME SERIES METHODS"]
tab0, tab1,tab2, tab3,tab8,tab4, tab5, tab6, tab7 = st.tabs(tabs)


with tab0:
    pass
with tab8:
    pass

with tab1:
    st.header("Infrared")
    st.write("A first of its kind concept that lets you discover counterintuitive patterns and insights often invisible due to limitations of the human mind, biases, and voluminous data.")
    st.write("Unleash the power of machine learning and advanced statistics to find outliers and exceptions in your data. This application provides an instant output that can be reviewed and acted upon with agility to stop revenue leakages, improve efficiency, and detect/prevent fraud.")

    st.image("http://revoquant.com/assets/img/infra.jpg", use_column_width=True)


with tab2:
        
        def convert_excel_to_csv(uploaded_file, page_number):
            if page_number == 1:
                excel_data = pd.read_excel(uploaded_file)
            else:
                excel_data = pd.read_excel(uploaded_file, sheet_name=page_number - 1)
            csv_file = BytesIO()
            excel_data.to_csv(csv_file, index=False)
            csv_file.seek(0)
            return csv_file.getvalue()


        st.header("Excel to CSV Converter")
        uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx", "xls"])
        selected_page = st.number_input("Enter the page number", min_value=1, value=1)

        if uploaded_file is not None:
            csv_data = convert_excel_to_csv(uploaded_file, selected_page)
            st.download_button(
                "Download CSV file",
                csv_data,
                file_name="output.csv",
                mime="text/csv"
            )

            with st.expander("Excel Data"):
                excel_data = pd.read_excel(uploaded_file, sheet_name=selected_page - 1)
                st.dataframe(excel_data)

            with st.expander("Converted CSV Data"):
                csv_data = pd.read_csv(BytesIO(csv_data))
                st.dataframe(csv_data)


        

# Move this code block below the page

with tab4:
    st.header("Benford's Law: The Mystery Behind the Numbers")
    st.image("https://image2.slideserve.com/4817711/what-is-benford-s-law-l.jpg", use_column_width=True)
    st.write("Have you ever wondered why certain numbers appear more frequently as the first digit in a dataset? "
                 "This phenomenon is known as Benford's Law, and it has been a subject of fascination for mathematicians, "
                 "statisticians, and data analysts for decades.")

    st.subheader("What is Benford's Law?")
    st.write(
            "Benford's Law, also called the First-Digit Law, states that in many naturally occurring numerical datasets, "
            "the first digit is more likely to be small (e.g., 1, 2, or 3) than large (e.g., 8 or 9). Specifically, "
            "the probability of a number starting with digit d is given by the formula: P(d) = log10(1 + 1/d), where "
            "log10 represents the base-10 logarithm.")

    st.subheader("Applications of Benford's Law")
    st.write(
            "Benford's Law has found applications in various fields, including forensic accounting, fraud detection, "
            "election analysis, and quality control. Its ability to uncover anomalies in large datasets makes it "
            "particularly useful for identifying potential irregularities or discrepancies.")

    st.subheader("Real-World Examples")
    st.write(
            "Benford's Law can be observed in numerous real-world datasets. For instance, if you examine the lengths "
            "of rivers worldwide, the population numbers of cities, or even the stock prices of companies, you are "
            "likely to find that the leading digits follow the predicted distribution.")

    st.subheader("Exceptions and Limitations")
    st.write("While Benford's Law holds true for many datasets, it is not universally applicable. Certain datasets "
                 "with specific characteristics may deviate from the expected distribution. Additionally, Benford's Law "
                 "should not be considered as definitive proof of fraudulent or irregular activities but rather as a tool "
                 "for further investigation.")

    st.subheader("Conclusion")
    st.write("Benford's Law offers a fascinating insight into the distribution of numbers in various datasets. "
                 "Understanding its principles can help data analysts and researchers identify potential outliers and "
                 "anomalies in their data. By harnessing the power of Benford's Law, we can gain valuable insights and "
                 "uncover hidden patterns in the vast sea of numerical information that surrounds us.")

    st.write("---")
    st.write("References:")
    st.write("1. Hill, T. P. (1995). A Statistical Derivation of the Significant-Digit Law. _Statistical Science_, "
                 "10(4), 354-363.")
    st.write("2. Berger, A., & Hill, T. P. (2015). Benford’s Law Strikes Back: No Simple Explanation in Sight for "
                 "Mathematician’s Rule. _Mathematical Association of America_, 122(9), 887-903.")



    
    st.write(
        "In probability theory and statistics, a Probability Distribution Function (PDF) is a function that describes the likelihood of a random variable taking on a particular value or falling within a specific range of values. It provides valuable information about the probabilities associated with different outcomes of a random variable.")

    st.subheader("Properties of PDF")
    st.write(
        "1. Non-negative: The PDF is always non-negative, meaning its values are greater than or equal to zero for all possible values of the random variable.")
    st.write(
        "2. Area under the curve: The total area under the PDF curve is equal to 1, representing the total probability of all possible outcomes.")
    st.write(
        "3. Describes likelihood: The PDF describes the likelihood of different values or ranges of values of the random variable.")

    st.subheader("Example: Normal Distribution")
    st.write(
        "One of the most commonly used probability distributions is the Normal Distribution, also known as the Gaussian Distribution. It is characterized by its bell-shaped curve.")

    st.image("https://image3.slideserve.com/6467891/properties-of-normal-distributions3-l.jpg", use_column_width=True, caption="Normal Distribution")

    st.write("The PDF of the Normal Distribution is given by the equation:")
    st.latex(r"f(x) = \frac{1}{{\sigma \sqrt{2\pi}}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}")

    st.write("Where:")
    st.write("- \(\mu\) is the mean of the distribution.")
    st.write("- \(\sigma\) is the standard deviation of the distribution.")
    st.write("- \(e\) is the base of the natural logarithm.")

    st.subheader("Applications of PDF")
    st.write("The PDF is used in various areas such as:")
    st.write("- Statistical modeling and inference.")
    st.write("- Risk analysis and decision-making.")
    st.write("- Machine learning and data science.")
    st.write("- Finance and investment analysis.")
    st.write("- Quality control and process optimization.")

    st.write(
        "Understanding and utilizing PDFs is essential for analyzing and interpreting data, making predictions, and solving problems involving uncertainty.")

    st.markdown("---")
    st.write(
        "This blog post provides a brief introduction to Probability Distribution Functions (PDFs) and their significance in probability theory and statistics. PDFs are fundamental tools for understanding and quantifying uncertainty in various fields. They describe the probabilities associated with different outcomes of a random variable and play a crucial role in statistical modeling, risk analysis, and decision-making.")
    st.write(
        "Whether you are a data scientist, a researcher, or simply interested in understanding the principles of probability, having a solid grasp of PDFs is essential. They provide a mathematical framework for describing the likelihood of events and enable us to make informed decisions based on probabilities.")
    st.write(
        "In this blog post, we explored the properties of PDFs, highlighted the example of the Normal Distribution as a widely used PDF, and discussed the applications of PDFs in different domains. We hope this introduction has piqued your curiosity and motivated you to dive deeper into the fascinating world of probability and statistics.")
    st.write(
        "Remember, probabilities are all around us, and understanding them can empower us to make better decisions and gain valuable insights from data!")

    st.write(
        "In statistics, a Z-score, also known as a standard score, is a measurement that indicates how many standard deviations an element or observation is from the mean of a distribution. It provides a standardized way to compare and interpret data points in different distributions.")

    st.subheader("Calculating Z-Score")
    st.write("The formula to calculate the Z-score of a data point is:")
    st.latex(r"Z = \frac{{X - \mu}}{{\sigma}}")

    st.write("Where:")
    st.write("- X is the individual data point.")
    st.write("- \(\mu\) is the mean of the distribution.")
    st.write("- \(\sigma\) is the standard deviation of the distribution.")

    st.subheader("Interpreting Z-Score")
    st.write(
        "The Z-score tells us how many standard deviations a data point is away from the mean. Here's how to interpret the Z-score:")
    st.write("- A Z-score of 0 means the data point is exactly at the mean.")
    st.write("- A Z-score of +1 indicates the data point is 1 standard deviation above the mean.")
    st.write("- A Z-score of -1 indicates the data point is 1 standard deviation below the mean.")
    st.write("- A Z-score greater than +1 suggests the data point is above average, farther from the mean.")
    st.write("- A Z-score less than -1 suggests the data point is below average, farther from the mean.")

    st.subheader("Standardizing Data with Z-Score")
    st.write(
        "One of the main applications of Z-scores is to standardize data. By converting data points into Z-scores, we can compare observations from different distributions and identify outliers or extreme values.")

    st.subheader("Example:")
    st.write(
        "Let's consider a dataset of students' test scores. The mean score is 75, and the standard deviation is 10. We want to calculate the Z-score for a student who scored 85.")

    st.write("Using the formula, we can calculate the Z-score as:")
    st.latex(r"Z = \frac{{85 - 75}}{{10}} = 1")

    st.write("The Z-score of 1 indicates that the student's score is 1 standard deviation above the mean.")

    st.subheader("Applications of Z-Score")
    st.write("Z-scores have various applications in statistics and data analysis, including:")
    st.write("- Identifying outliers: Z-scores can help identify data points that are unusually far from the mean.")
    st.write(
        "- Comparing data points: Z-scores enable us to compare and rank data points from different distributions.")
    st.write("- Hypothesis testing: Z-scores are used in hypothesis testing to assess the significance of results.")
    st.write("- Data normalization: Z-scores are used to standardize data and bring it to a common scale.")

    st.markdown("---")
    st.write(
        "This blog post provides an overview of Z-scores and their significance in statistics. Z-scores allow us to standardize data and compare observations from different distributions. They provide valuable insights into the relative position of data points within a distribution and help identify outliers or extreme values.")
    st.write(
        "We discussed how to calculate Z-scores using the formula and interpret their values in terms of standard deviations from the mean. Additionally, we explored the applications of Z-scores in various statistical analyses, including outlier detection, data comparison, hypothesis testing, and data normalization.")
    st.write(
        "By understanding and utilizing Z-scores, we can gain deeper insights into our data and make informed decisions based on standardized measurements. Whether you're working with test scores, financial data, or any other quantitative information, Z-scores can be a valuable tool in your statistical toolkit.")
    st.write(
        "We hope this blog post has provided you with a clear understanding of Z-scores and their applications. Remember to explore further and practice applying Z-scores to real-world datasets to enhance your statistical analysis skills.")
    st.write("Happy analyzing!")


    
with tab5:
    st.write(
        "Isolation Forest is an unsupervised machine learning algorithm used for anomaly detection. It is particularly effective in detecting outliers or anomalies in large datasets. The algorithm works by isolating anomalous observations by recursively partitioning the data into subsets. The main idea behind the Isolation Forest is that anomalies are more likely to be isolated into small partitions compared to normal data points.")

    st.subheader("How does Isolation Forest work?")
    st.write(
        "1. Random Selection: Isolation Forest selects a random feature and a random split value to create a binary tree partition of the data.")
    st.write(
        "2. Recursive Partitioning: The algorithm recursively partitions the data by creating more binary tree partitions. Each partitioning step creates a split point by selecting a random feature and a random split value.")
    st.write(
        "3. Isolation: Anomalies are expected to be isolated in smaller partitions since they require fewer partitioning steps to be separated from the majority of the data points.")
    st.write(
        "4. Anomaly Scoring: The algorithm assigns an anomaly score to each data point based on the average path length required to isolate it. The shorter the path length, the more likely it is an anomaly.")

    st.subheader("Advantages of Isolation Forest")
    st.write("- It is efficient for outlier detection, especially in large datasets.")
    st.write("- It does not rely on assumptions about the distribution of the data.")
    st.write("- It can handle high-dimensional data effectively.")
    st.write("- It is robust to the presence of irrelevant or redundant features.")

    st.subheader("Applications of Isolation Forest")
    st.write("Isolation Forest can be applied in various domains, including:")
    st.write("- Fraud detection: Identifying fraudulent transactions or activities.")
    st.write("- Network intrusion detection: Detecting anomalous behavior in network traffic.")
    st.write("- Manufacturing quality control: Identifying defective products or anomalies in production processes.")
    st.write("- Anomaly detection in sensor data: Detecting abnormalities in IoT sensor readings.")
    st.write("- Credit card fraud detection: Identifying fraudulent credit card transactions.")

    st.subheader("Example: Anomaly Detection in Network Traffic")
    st.write(
        "Let's consider the application of Isolation Forest in network intrusion detection. The algorithm can help identify anomalous network traffic patterns that may indicate potential attacks or breaches.")

    st.image("https://velog.velcdn.com/images%2Fvvakki_%2Fpost%2Fc59d0a7f-7a1c-4589-b799-cf40c6463d26%2Fimage.png", use_column_width=True, caption="Isolation Forest Anomaly Detection")

    st.write(
        "In this example, the Isolation Forest algorithm analyzes network traffic data and identifies anomalies that deviate from the normal patterns. By isolating and scoring the anomalies, security teams can prioritize their investigation and take appropriate actions to prevent potential threats.")

    st.markdown("---")
    st.write(
        "In this blog post, we explored Isolation Forest, an unsupervised machine learning algorithm used for anomaly detection. The algorithm leverages the concept of isolation to identify anomalies by recursively partitioning the data into subsets. It is particularly effective in detecting outliers or anomalies in large datasets.")
    st.write(
        "We discussed the working principle of Isolation Forest, which involves random selection, recursive partitioning, isolation, and anomaly scoring. We also highlighted the advantages of Isolation Forest, such as its efficiency, distribution-free nature, and ability to handle high-dimensional data.")
    st.write(
        "Furthermore, we explored several real-world applications of Isolation Forest, including fraud detection, network intrusion detection, quality control, and anomaly detection in sensor data.")
    st.write(
        "By utilizing Isolation Forest, data scientists and analysts can effectively identify anomalies and outliers in various domains, enabling them to make informed decisions and take appropriate actions. The algorithm's ability to handle large datasets and its robustness to irrelevant features make it a valuable tool for anomaly detection tasks.")
    st.write(
        "We hope this blog post has provided you with a comprehensive understanding of Isolation Forest and its applications. Remember to explore further and apply the algorithm to real-world datasets to enhance your anomaly detection capabilities.")
    st.write("Happy anomaly detection!")
with tab6:
    st.write(
        "Autoencoders are a type of artificial neural network used for unsupervised learning and data compression. They are particularly useful for feature extraction and anomaly detection tasks. The basic idea behind autoencoders is to learn a compressed representation of the input data and then reconstruct it as accurately as possible.")

    st.subheader("Architecture of Autoencoder")
    st.write("An autoencoder consists of two main parts: the encoder and the decoder.")
    st.write(
        "1. Encoder: The encoder takes the input data and learns a compressed representation, also known as the encoding or latent space.")
    st.write(
        "2. Decoder: The decoder takes the encoded representation and reconstructs the original input data from it.")

    st.write(
        "The encoder and decoder are typically symmetric in structure, with the number of neurons decreasing in the encoder and increasing in the decoder.")

    st.subheader("Training an Autoencoder")
    st.write(
        "Autoencoders are trained using an unsupervised learning approach. The goal is to minimize the reconstruction error between the original input and the reconstructed output. This is typically done by minimizing a loss function, such as mean squared error (MSE) or binary cross-entropy (BCE).")

    st.subheader("Applications of Autoencoder")
    st.write("Autoencoders have various applications, including:")
    st.write(
        "- Dimensionality reduction: Learning compressed representations that capture the most important features of the data.")
    st.write(
        "- Anomaly detection: Detecting unusual or anomalous patterns in the data by comparing reconstruction errors.")
    st.write(
        "- Image denoising: Removing noise or artifacts from images by training the autoencoder to reconstruct clean images.")
    st.write("- Recommendation systems: Learning user preferences and generating personalized recommendations.")
    st.write("- Data generation: Generating new data samples similar to the training data.")

    st.subheader("Example: Image Denoising")
    st.write(
        "One application of autoencoders is image denoising. By training an autoencoder on noisy images and minimizing the reconstruction error, we can effectively remove the noise and reconstruct clean images.")

    st.image("https://miro.medium.com/v2/resize:fit:4266/1*QEmCZtruuWwtEOUzew2D4A.png", use_column_width=True, caption="Autoencoder Image Denoising")

    st.markdown("---")
    st.write(
        "In this blog post, we explored autoencoders, a type of artificial neural network used for unsupervised learning and data compression. Autoencoders consist of an encoder and a decoder, which learn a compressed representation of the input data and reconstruct it as accurately as possible.")
    st.write(
        "We discussed the training process of autoencoders, which involves minimizing the reconstruction error between the original input and the reconstructed output. Autoencoders have various applications, including dimensionality reduction, anomaly detection, image denoising, recommendation systems, and data generation.")
    st.write(
        "We also provided an example of image denoising using autoencoders, where the network learns to remove noise from noisy images and reconstruct clean images.")
    st.write(
        "By utilizing autoencoders, data scientists and researchers can effectively extract features, detect anomalies, denoise images, and generate new data samples. Autoencoders have wide-ranging applications and are particularly valuable in unsupervised learning scenarios.")
    st.write(
        "We hope this blog post has provided you with a clear understanding of autoencoders and their applications. Remember to explore further and apply autoencoders to different domains and datasets to unlock their full potential.")
    st.write("Happy autoencoding!")


with tab3:


    # Get the Power BI iframe URL
    #'<iframe title="Report Section" width="800" height="450" src="https://app.powerbi.com/view?r=eyJrIjoiNzBlNTM4ZmQtMWZhOC00YWRmLWEwNmMtZjQ5NjFhZjU2ODE1IiwidCI6IjMyNTRjOGVlLWQxZDUtNDFmNy05ZTY5LTUxMzQxYjJhZWU3NCJ9" frameborder="0" allowFullScreen="true"></iframe>'
    iframe_url = '<iframe title="process mining" width="1000" height="700" src="https://app.powerbi.com/view?r=eyJrIjoiNWE5ZDM0MDYtYmUwNC00ZjhiLTllOGMtNjFjNmY2M2M4YzkxIiwidCI6IjMyNTRjOGVlLWQxZDUtNDFmNy05ZTY5LTUxMzQxYjJhZWU3NCJ9&embedImagePlaceholder=true" frameborder="0" allowFullScreen="true"></iframe>'

    # Embed the Power BI report in the Streamlit app
    st.markdown(iframe_url, unsafe_allow_html=True)

    #################################################################### for PDF
    # pdf_file = 'r"C:\Users\LENOVO\Downloads\jindal (1).pdf"'
    #def embed_pdf(pdf_file):
    #    with open(pdf_file, "rb") as f:
    #        base64_pdf = base64.b64encode(f.read()).decode("utf-8")
    #    pdf_display = f"<iframe src='data:application/pdf;base64,{base64_pdf}' width='700' height='1000' type='application/pdf'></iframe>"
    #    st.markdown(pdf_display, unsafe_allow_html=True)


    #if __name__ == "__main__":
    #    embed_pdf(pdf_file)



# Render the marquee in Streamlit
st.markdown(marquee_html, unsafe_allow_html=True)







################################################################################excel









def get_download_link(file_path):
    with open(file_path, "rb") as file:
        contents = file.read()
    encoded_file = base64.b64encode(contents).decode("utf-8")
    href = f'<a href="data:file/csv;base64,{encoded_file}" download="{file_path}">Click here to download</a>'
    return href



    
def drop_features_with_missing_values(data):
    # Calculate the number of missing values in each column
    missing_counts = data.isnull().sum()

    # Get the names of columns with missing values
    columns_with_missing_values = missing_counts[missing_counts > 0].index

    # Drop the columns with missing values
    data_dropped = data.drop(columns=columns_with_missing_values)
    return data_dropped



def apply_anomaly_detection_Mahalanobis(data):
    # Assuming 'data' is a pandas DataFrame with numerical columns
    # You may need to preprocess and select appropriate features for Mahalanobis distances

    # Calculate the mean and covariance matrix of the data
    data_mean = data.mean()
    data_cov = data.cov()

    # Calculate the inverse of the covariance matrix
    data_cov_inv = np.linalg.inv(data_cov)

    # Calculate Mahalanobis distances for each data point
    mahalanobis_distances = data.apply(lambda row: mahalanobis(row, data_mean, data_cov_inv), axis=1)

    # Set a threshold to identify anomalies (you can adjust this threshold based on your dataset)
    threshold = mahalanobis_distances.mean() + 2 * mahalanobis_distances.std()

    # Create a new column 'Anomaly' to indicate anomalies (1 for anomalies, 0 for inliers)
    data['Anomaly'] = (mahalanobis_distances > threshold).astype(int)

    return data

# Function to define and train the autoencoder model
def train_autoencoder(data):
    # Standardize the data
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)

    # Define the autoencoder model architecture
    input_dim = data.shape[1]
    encoding_dim = int(input_dim / 2)  # You can adjust this value as needed
    autoencoder = tf.keras.models.Sequential([
        tf.keras.layers.Dense(encoding_dim, activation='relu', input_shape=(input_dim,)),
        tf.keras.layers.Dense(input_dim, activation='linear')
    ])

    # Compile and train the autoencoder with verbose=1
    autoencoder.compile(optimizer='adam', loss='mean_squared_error')
    autoencoder.fit(scaled_data, scaled_data, epochs=10, batch_size=64, shuffle=True, verbose=1)  # Set verbose to 1

    # Get the encoded data
    encoded_data = autoencoder.predict(scaled_data)

    # Calculate the reconstruction error
    reconstruction_error = np.mean(np.square(scaled_data - encoded_data), axis=1)

    # Add the reconstruction error as a new column 'ReconstructionError' to the data
    data['ReconstructionError'] = reconstruction_error

    return data

# Function to apply autoencoder for anomaly detection
def apply_anomaly_detection_autoencoder(data):
    # Train the autoencoder and get the reconstruction error
    data_with_reconstruction_error = train_autoencoder(data)

    # Set a threshold for anomaly detection (you can adjust this threshold)
    threshold = data_with_reconstruction_error['ReconstructionError'].mean() + 3 * data_with_reconstruction_error['ReconstructionError'].std()

    # Classify anomalies based on the threshold
    data_with_reconstruction_error['Anomaly'] = np.where(data_with_reconstruction_error['ReconstructionError'] > threshold, 1, 0)

    return data_with_reconstruction_error

def apply_anomaly_detection_IsolationForest(data):
    # Make a copy of the data
    data_copy = data.copy()

    # Fit the Isolation Forest model
    isolation_forest = IsolationForest(contamination=0.03, random_state=42)
    isolation_forest.fit(data_copy)

    # Predict the anomaly labels
    anomaly_labels = isolation_forest.predict(data_copy)

    # Create a new column in the original DataFrame for the anomaly indicator
    data['Anomaly'] = np.where(anomaly_labels == -1, 1, 0)
    return data

def apply_anomaly_detection_LocalOutlierFactor(data, neighbors=200):
    lof = LocalOutlierFactor(n_neighbors=neighbors, contamination='auto')
    data['Anomaly'] = lof.fit_predict(data)
    data['Anomaly'] = np.where(data['Anomaly'] == -1, 1, 0)
    return data


# def apply_anomaly_detection_LocalOutlierFactor(data):
#     # Make a copy of the data
#     data_copy = data.copy()

#     from sklearn.neighbors import LocalOutlierFactor

#     # Step 3: Apply Local Outlier Factor
#     lof = LocalOutlierFactor(n_neighbors=200, metric='euclidean', contamination=0.04)

#     outlier_labels = lof.fit_predict(data_copy)

#     # Display the outlier labels for each data point
#     data['Outlier_Label'] = outlier_labels
#     return data




def find_duplicate_vendors(vendors_df, threshold):
    duplicates = []
    lf = vendors_df.copy()
    lf['NAME1'] = lf['NAME1'].astype(str)
    vendor_names = lf['NAME1'].unique().tolist()
    columns = ['Vendor 1', 'Vendor 2', 'Score']
    df_duplicates = pd.DataFrame(data=[], columns=columns)

    for i, name in enumerate(vendor_names):
        # Compare the current name with the remaining names
        matches = process.extract(name, vendor_names[i+1:], scorer=fuzz.ratio)

        # Check if any match exceeds the threshold
        for match, score in matches:
            if score >= threshold:
                duplicates.append((name, match))
                df_duplicates.loc[len(df_duplicates)] = [name, match, score]

    return duplicates, df_duplicates



def apply_anomaly_detection_OneClassSVM(data):
    # Copy the original data to avoid modifying the original dataframe
    data_with_anomalies = data.copy()

    # Perform One-Class SVM anomaly detection
    clf = OneClassSVM(nu=0.05)
    y_pred = clf.fit_predict(data)
    data_with_anomalies['Anomaly'] = np.where(y_pred == -1, 1, 0)

    return data_with_anomalies


def apply_anomaly_detection_SGDOCSVM(data):
    # Copy the original data to avoid modifying the original dataframe
    data_with_anomalies = data.copy()

    
    # Perform One-Class SVM anomaly detection using SGD solver
    clf = SGDOneClassSVM(nu=0.05)
    clf.fit(data)
    y_pred = clf.predict(data)
    data_with_anomalies['Anomaly'] = np.where(y_pred == -1, 1, 0)

    return data_with_anomalies



def calculate_first_digit(data):
    idx = np.arange(0, 10)
    first_digits = data.astype(str).str.strip().str[0].astype(int)
    counts = first_digits.value_counts(normalize=True, sort=False)
    benford = np.log10(1 + 1 / np.arange(0, 10))

    df = pd.DataFrame(data.astype(str).str.strip().str[0].astype(int).value_counts(normalize=True, sort=False)).reset_index()
    df1 = pd.DataFrame({'index': idx, 'benford': benford})
    return df, df1, counts, benford

def calculate_2th_digit(data):
    idx = np.arange(0, 100)
    nth_digits = data.astype(int).astype(str).str.strip().str[:2]
    numeric_mask = nth_digits.str.isnumeric()
    counts = nth_digits[numeric_mask].astype(int).value_counts(normalize=True, sort=False)
    benford = np.log10(1 + 1 / np.arange(0, 100))

    df = pd.DataFrame(data.astype(int).astype(str).str.strip().str[:2].astype(int).value_counts(normalize=True, sort=False)).reset_index()
    df1 = pd.DataFrame({'index': idx, 'benford': benford})

    return df, df1, counts, benford

def calculate_3th_digit(data):
    idx = np.arange(100, 1000)
    nth_digits = data.astype(int).astype(str).str.strip().str[:3]
    numeric_mask = nth_digits.str.isnumeric()
    counts = nth_digits[numeric_mask].astype(int).value_counts(normalize=True, sort=False)
    benford = np.log10(1 + 1 / np.arange(100, 1000))

    df = pd.DataFrame(data.astype(int).astype(str).str.strip().str[:3].astype(int).value_counts(normalize=True, sort=False)).reset_index()
    df1 = pd.DataFrame({'index': idx, 'benford': benford})

    return df, df1, counts, benford





def apply_anomaly_detection_GMM(data):

    from sklearn.mixture import GaussianMixture
    gmm = GaussianMixture()
    data['Anomaly'] = gmm.fit_predict(data)
    data['Anomaly'] = np.where(data['Anomaly'] == 1, 0, 1)
    return data


def z_score_anomaly_detection(data, column, threshold):

    # Calculate the z-score for the specified column
    z_scores = stats.zscore(data[column])

    # Identify outliers based on the z-score exceeding the threshold
    outlier_indices = np.where(np.abs(z_scores) > threshold)[0]

    # Create a copy of the data with an "Anomaly" column indicating outliers
    data_with_anomalies_zscore = data.copy()
    data_with_anomalies_zscore['Anomaly'] = 0
    data_with_anomalies_zscore.iloc[outlier_indices, -1] = 1

    return data_with_anomalies_zscore


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
    #llm = ChatOpenAI()
    llm = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature":0.5, "max_length":512})

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













def main():




        # starting of basic information side bar
        st.sidebar.header("Exploratory Data Analysis")
        info_options = ["None",
                        "Number of one time vendor account",
                        "Duplicate vendor account basis name and fuzzy logic",
                        "Changes in vendor bank account",
                        "Vendor details matching with employee (common address, common bank account, common PAN)",
                        "Dormant vendor",
                        "Vendor bank account is in different country or city than the country or city registered with",
                        "Vendor belongs to country in Africa, Turkey, Bangkok etc",
                        "Vendor having email address domain as gmail, yahoomail, Hotmail, rediffmail etc",
                        "Vendor is not private limited or public limited or LLP",
                        "Vendor who is having maximum quality rejections",
                        "Vendor who is having tendency to do delayed delivery. This could result in short supply",
                        "Vendor who is having tendency to delivery well in advance. This raises risk of build up inventory",
                        "Vendor who is having tendency to deliver the goods on same date of PO or nearby date of PO",
                        "Vendor with transactions of return PO using 161 mvt type and for those specific material-vendor combination, the avg return price is lower than the procurement price",
                        "Vendor where quality rejection takes significant time and the invoice is already paid or posted",
                        "Vendor which gets considered during invoice posting but not at the time of PO. This means, in PO vendor is showing X whereas in invoice posting vendor is showing as Y",
        ]
        selected_info = st.sidebar.selectbox("Select an Exploratory Data Analysis (EDA) technique", info_options)

        if selected_info == "None":
            st.write(" ")
        elif selected_info == "Number of one time vendor account":
            st.header("Upload your :blue[lfa1] file")
            data_file1 = st.file_uploader("Upload CSV", type=["csv"], key="lfa1")

            if data_file1 is not None:
                data1 = pd.read_csv(data_file1, encoding='latin1')  # Specify the correct encoding
                st.write(data1.head(2))

            st.header("Upload your :blue[lfb1] file")

            data_file2 = st.file_uploader("Upload CSV", type=["csv"], key="lfb1")

            if data_file2 is not None:
                data2 = pd.read_csv(data_file2, encoding='latin1')  # Specify the correct encoding
                st.write(data2.head(2))

                # Merge data1 and data2 based on LIFNR using inner join
                merged_data = pd.merge(data1, data2, on="LIFNR", how="inner")
                st.write(merged_data.head(2))

                # Calculate the total number of unique vendors from 'NAME1' feature
                unique_vendors = merged_data['NAME1'].nunique()
                st.write("Total number of unique vendors:", unique_vendors)

                # Filter merged_data for rows where NAME1 occurs only once
                filtered_x2 = merged_data[merged_data['NAME1'].map(merged_data['NAME1'].value_counts()) == 1]
                st.write(filtered_x2)

                # Filter merged_data for rows where XCPDK is equal to 'X'
                one_time_vendor = merged_data[merged_data['XCPDK'] == 'X']
                st.write(one_time_vendor)

        elif selected_info == "Duplicate vendor account basis name and fuzzy logic":
            st.header("Upload your lfa1 file")
            data_file1 = st.file_uploader("Upload CSV", type=["csv"], key="lfa1")

            if data_file1 is not None:
                data1 = pd.read_csv(data_file1, encoding='latin1')  # Specify the correct encoding
                st.write(data1.head(2))

                # Perform duplicate vendor detection
                threshold = 95
                duplicates, df_duplicates = find_duplicate_vendors(data1, threshold)

                # Display duplicate vendor pairs
                st.write("Duplicate Vendor Accounts:")
                for vendor1, vendor2 in duplicates:
                    st.write(vendor1, "--", vendor2)

                # Display dataframe with duplicate vendor pairs
                st.write("Duplicate Vendor Accounts DataFrame:")
                st.write(df_duplicates)

        elif selected_info == "Changes in vendor bank account":
            st.header("Upload your lfbk file")
            data_file1 = st.file_uploader("Upload CSV", type=["csv"], key="lfbk")

            if data_file1 is not None:
                data1 = pd.read_csv(data_file1, encoding='latin1')  # Specify the correct encoding
                st.write(data1.head(2))

                # Calculate the count of unique BANKN values for each LIFNR
                series_data = data1.groupby('LIFNR')['BANKN'].nunique()

                # Create a DataFrame with the count of BANKN values
                x1 = pd.DataFrame({'BANKN': series_data})
                x1 = x1.rename(columns={'BANKN': 'count_BankN'})
                x1 = x1.reset_index()

                # Get the list of LIFNR values with count_BankN greater than 1
                l1 = list(x1[x1['count_BankN'] > 1]['LIFNR'])

                # Filter x1 for rows where count_BankN is greater than 1
                x1_filtered = x1[x1['count_BankN'] > 1]

                # Count the number of people with multiple accounts
                num_people = len(x1_filtered)

                # Display the number of people with multiple accounts
                st.write("Number of people with multiple accounts:", num_people)
                st.write(x1_filtered)

        elif selected_info == "Vendor details matching with employee (common address, common bank account, common PAN)":
            st.header("Upload your lfa1 file")
            data_file1 = st.file_uploader("Upload CSV", type=["csv"], key="lfa1")
            data1 = None  # Initialize data1 variable
            data2 = None  # Initialize data2 variable
            data3 = None  # Initialize data3 variable
            data4 = None  # Initialize data4 variable

            if data_file1 is not None:
                data1 = pd.read_csv(data_file1, encoding='latin1')  # Specify the correct encoding
                data1['KTOKK'] = data1['KTOKK'].astype(str)  # Convert 'KTOKK' column to string
                data1['KTOKK'] = data1['KTOKK'].str.replace("'", "")  # Replace single quotes in 'KTOKK' column
                st.write(data1.head(2))

            st.header("Upload your Vendor_acc file")
            data_file2 = st.file_uploader("Upload CSV", type=["csv"], key="Vendor_acc")

            if data_file2 is not None:
                data2 = pd.read_csv(data_file2, encoding='latin1')  # Specify the correct encoding
                data2['Group'] = data2['Group'].astype(str)  # Convert 'Group' column to string
                st.write(data2.head(2))

            if data1 is not None and data2 is not None:
                lfa1_vd = pd.merge(data1, data2, left_on='KTOKK', right_on='Group', how='left')
                st.write(lfa1_vd)

                st.header("Upload your j_1 file")
                data_file3 = st.file_uploader("Upload CSV", type=["csv"], key="j_1")

                if data_file3 is not None:
                    data3 = pd.read_csv(data_file3, encoding='latin1')  # Specify the correct encoding
                    st.write(data3.head(2))

                st.header("Upload your lfbk file")
                data_file4 = st.file_uploader("Upload CSV", type=["csv"], key="lfbk")

                if data_file4 is not None:
                    data4 = pd.read_csv(data_file4, encoding='latin1')  # Specify the correct encoding
                    st.write(data4.head(2))

                if data3 is not None:
                    lfa1_vd_j = pd.merge(lfa1_vd, data3, on='LIFNR', how='left')

                    lfa1_vd_j_lfbk = pd.merge(lfa1_vd_j, data4, on='LIFNR', how='left')

                    lfa1_vd_j1 = lfa1_vd_j_lfbk[['LIFNR', 'LAND1', 'NAME1', 'ORT01', 'STRAS', 'STCD3', 'Name', 'BANKN', 'J_1IPANNO_x', 'J_1IPANNO_y']]
                    emp = lfa1_vd_j1[lfa1_vd_j1['Name'].str.contains('Empl')]
                    vendor = lfa1_vd_j1[~(lfa1_vd_j1['Name'].str.contains('Empl'))]

                    table1_bankn_set = set(vendor['BANKN'])
                    employee_bankn_set = set(emp['BANKN'])

                    common_bankn = table1_bankn_set.intersection(employee_bankn_set)
                    common_bankn_count = len(common_bankn)
                    emp[['LIFNR','BANKN']].dropna(inplace=True)
                    st.write(f"Total number of persons having a common bank account: {common_bankn_count}")
                    # for bankn in common_bankn:
                    #     st.write(bankn)

                    table1_J_1IPANNO_x_set = set(vendor['J_1IPANNO_x'])
                    employee_J_1IPANNO_x_set = set(emp['J_1IPANNO_x'])

                    common_J_1IPANNO_x = table1_J_1IPANNO_x_set.intersection(employee_J_1IPANNO_x_set)
                    common_J_1IPANNO_x_count = len(common_J_1IPANNO_x)
                    st.write(f"Total number of persons having a common pan: {common_J_1IPANNO_x_count}")

                    # for pan in common_J_1IPANNO_x:
                    #     st.write(pan)


                    table1_bankn_set = set(vendor['STRAS'])
                    employee_bankn_set = set(emp['STRAS'])

                    common_J_1IPANNO_xa = table1_bankn_set.intersection(employee_bankn_set)
                    common_J_1IPANNO_xa_count =len(common_J_1IPANNO_xa)
                    st.write(f"Total number of persons having a common address: {common_J_1IPANNO_xa_count}")

                    # for bankn in common_J_1IPANNO_x:
                    #     print(bankn)
                else:
                    st.write("Please upload the j_1 file.")
            else:
                st.write("Please upload both lfa1 and Vendor_acc files.")

        elif selected_info == "Vendor belongs to country in Africa, Turkey, Bangkok etc":
            st.header("Upload your lfa1 file")
            data_file1 = st.file_uploader("Upload CSV", type=["csv"], key="lfa1")
            if data_file1 is not None:
                data1 = pd.read_csv(data_file1, encoding='latin1')  # Specify the correct encoding
                st.write(data1.head(2))

            st.header("Upload your t005t file")
            data_file2 = st.file_uploader("Upload CSV", type=["csv"], key="t005t")

            if data_file2 is not None:
                data2 = pd.read_csv(data_file2, encoding='latin1')  # Specify the correct encoding
                st.write(data2.head(2))

                t005t = data2  # Assign data2 to t005t variable
                ltf = pd.merge(data1, t005t, on='LAND1', how='left')
                st.write(ltf)

                ltf1 = ltf[['LIFNR','LAND1', 'LANDX50']]
                filter_values = ['Africa', 'Turkey', 'Bangkok']  # Example filter values
                filter_country = ltf1[ltf1['LANDX50'].isin(filter_values)]
                country_counts = filter_country['LANDX50'].value_counts()
                st.write(country_counts.head(5))



                #st.sidebar.header("Feature Engineering")
                #info_options = [
                #    "None",
                #    "Perform feature engineering",
                #]


                #selected_info = st.sidebar.selectbox("Choose the option", info_options)

                #if selected_info == "None":
                #    st.write(" ")
                #else:
                    #pass










         # ending of basic information side bar


        #  starting of anomaly detection algorithms over here
        #  starting of anomaly detection algorithms over here
        st.sidebar.header("Statistical Methods for Numerical Variable")
        anomaly_options = ["None",
                           "Z-Score/Standard Deviation",
                           "Boxplot",
                           "Probability Density Function",
                           "RSF",
                           "Benford law 1st digit",
                           "Benford law 2nd digit",
                           "Benford law 3rd digit"
                           ]
        selected_anomalyAlgorithm = st.sidebar.selectbox("Select appropriate statistical techniques", anomaly_options)

        if selected_anomalyAlgorithm == "None":
            st.write(" ")
        elif selected_anomalyAlgorithm == "Z-Score/Standard Deviation":

            st.markdown(
                "<h2 style='font-size: 24px; color: blue;'>Upload Dataset, Unleash Statistical Magic for Numerical Variables!</h2>",
                unsafe_allow_html=True)
            data_file = st.file_uploader("Upload File", type=["csv", "xlsx", "XLSX"])

            if data_file is not None:
                file_extension = data_file.name.split(".")[-1]
                if file_extension == "csv":
                    data = pd.read_csv(data_file)
                elif file_extension in ["xlsx", "XLSX"]:
                    data = pd.read_excel(data_file)
                else:
                    st.error("Unsupported file format. Please upload a CSV or Excel file.")

                st.write(data.head())
                st.write("Dealing with missing values:")
                threshold = 0.1  # Set the threshold to 10% (0.1)
                missing_percentages = data.isnull().mean()  # Calculate the percentage of missing values in each column
                columns_to_drop = missing_percentages[
                    missing_percentages > threshold].index  # Get the columns exceeding the threshold
                data = data.drop(columns=columns_to_drop)  # Drop the columns
                st.write(f"Features with more than {threshold * 100:.2f}% missing values dropped successfully.")

                data = drop_features_with_missing_values(data)

                st.write("Dealing with duplicate values...")
                num_duplicates = data.duplicated().sum()  # Count the number of duplicate rows
                data_unique = data.drop_duplicates()  # Drop the duplicate rows
                st.write(f"Number of duplicate rows: {num_duplicates}")

                st.write("Downloading the dataset...")

                numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
                newdf = data.select_dtypes(include=numerics)


                # Select the column to use for z-score calculation
                column = st.selectbox("Select column for z-score", newdf.columns)

                # Set the threshold for anomaly detection
                # threshold = st.slider("Threshold", value=3, min=1, max=10, step=1)
                threshold = st.slider('Threshold', 3, 10, )

                # Calculate the z-score and perform anomaly detection
                data_with_anomalies_zscore = z_score_anomaly_detection(data, column, threshold)

                st.download_button(
                    label="Download Data",
                    data=data_with_anomalies_zscore.to_csv(index=False),
                    file_name="ZScoreAnomaly.csv",
                    mime="text/csv"
                )

                # Plot the results using Plotly Express
                fig = px.scatter(data_with_anomalies_zscore, x=column, y="Anomaly")
                fig.update_layout(title='Z-Score Anomaly Detection')

                # Save the Plotly figure as an HTML file
                fig_html_path = "plot.html"
                fig.write_html(fig_html_path)

                # Provide a button to open the Plotly chart in a new tab
                if st.button("Open Plotly Chart"):
                    new_tab = webbrowser.get()
                    new_tab.open(fig_html_path, new=2)

                # Display the data with anomaly indicator
                st.write(data_with_anomalies_zscore)



        elif selected_anomalyAlgorithm == "Boxplot":

            st.markdown(

                "<h2 style='font-size: 24px; color: blue;'>Upload Dataset, Unleash Statistical Magic for Numerical Variables!</h2>",

                unsafe_allow_html=True)

            data_file = st.file_uploader("Upload File", type=["csv", "xlsx", "XLSX"])

            if data_file is not None:

                file_extension = data_file.name.split(".")[-1]

                if file_extension == "csv":

                    data = pd.read_csv(data_file)

                elif file_extension in ["xlsx", "XLSX"]:

                    data = pd.read_excel(data_file)

                else:

                    st.error("Unsupported file format. Please upload a CSV or Excel file.")

                st.write(data.head())

                st.write("Dealing with missing values:")

                threshold = 0.1  # Set the threshold to 10% (0.1)

                missing_percentages = data.isnull().mean()  # Calculate the percentage of missing values in each column

                columns_to_drop = missing_percentages[
                    missing_percentages > threshold].index  # Get the columns exceeding the threshold

                data = data.drop(columns=columns_to_drop)  # Drop the columns

                st.write(f"Features with more than {threshold * 100:.2f}% missing values dropped successfully.")

                data = drop_features_with_missing_values(data)

                st.write("Dealing with duplicate values...")

                num_duplicates = data.duplicated().sum()  # Count the number of duplicate rows

                data_unique = data.drop_duplicates()  # Drop the duplicate rows

                st.write(f"Number of duplicate rows: {num_duplicates}")

                st.write("Downloading the dataset...")



                numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
                newdf = data.select_dtypes(include=numerics)

                # Select the feature to visualize
                selected_feature = st.selectbox("Select a feature:", newdf.columns)

                # Generate the boxplot using Plotly Express

                fig = px.box(data, y=selected_feature)

                fig.update_layout(title="Boxplot of " + selected_feature)

                # Save the Plotly figure as an HTML file

                fig_html_path = "boxplot.html"

                fig.write_html(fig_html_path)

                # Provide a link to open the Plotly chart in a new tab

                if st.button("Open Boxplot"):
                    new_tab = webbrowser.get()

                    new_tab.open(fig_html_path, new=2)

                # Calculate interquartile range (IQR)

                Q1 = data[selected_feature].quantile(0.25)

                Q3 = data[selected_feature].quantile(0.75)

                IQR = Q3 - Q1

                # Calculate upper and lower limits

                lower_limit = Q1 - 1.5 * IQR

                upper_limit = Q3 + 1.5 * IQR

                # Find outliers and create the anomaly feature

                data['anomaly'] = 0  # Initialize anomaly feature as 0

                data.loc[(data[selected_feature] < lower_limit) | (data[selected_feature] > upper_limit), 'anomaly'] = 1

                # Calculate the percentage of outliers

                total_data_points = data.shape[0]

                total_outliers = data['anomaly'].sum()

                percentage_outliers = (total_outliers / total_data_points) * 100

                # Show the updated dataframe with the anomaly feature and the percentage of outliers

                st.write("Updated Dataframe:")

                st.write(data)

                # Download the dataframe with the feature name in the file name

                file_name = "Anomaly_" + selected_feature.replace(" ", "_") + ".csv"

                st.download_button(

                    label="Download",

                    data=data.to_csv(index=False),

                    file_name=file_name,

                    mime="text/csv"

                )

                st.write("Percentage of outliers: {:.2f}%".format(percentage_outliers))



        elif selected_anomalyAlgorithm == "Probability Density Function":

            st.markdown(
                "<h2 style='font-size: 24px; color: blue;'>Upload Dataset, Unleash Statistical Magic for Numerical Variables!</h2>",
                unsafe_allow_html=True)
            data_file = st.file_uploader("Upload File", type=["csv", "xlsx", "XLSX"])

            if data_file is not None:
                file_extension = data_file.name.split(".")[-1]
                if file_extension == "csv":
                    data = pd.read_csv(data_file)
                elif file_extension in ["xlsx", "XLSX"]:
                    data = pd.read_excel(data_file)
                else:
                    st.error("Unsupported file format. Please upload a CSV or Excel file.")

                st.write(data.head())
                st.write("Dealing with missing values:")
                threshold = 0.1  # Set the threshold to 10% (0.1)
                missing_percentages = data.isnull().mean()  # Calculate the percentage of missing values in each column
                columns_to_drop = missing_percentages[
                    missing_percentages > threshold].index  # Get the columns exceeding the threshold
                data = data.drop(columns=columns_to_drop)  # Drop the columns
                st.write(f"Features with more than {threshold * 100:.2f}% missing values dropped successfully.")

                data = drop_features_with_missing_values(data)

                st.write("Dealing with duplicate values...")
                num_duplicates = data.duplicated().sum()  # Count the number of duplicate rows
                data_unique = data.drop_duplicates()  # Drop the duplicate rows
                st.write(f"Number of duplicate rows: {num_duplicates}")

                st.write("Downloading the dataset...")




                numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
                newdf = data.select_dtypes(include=numerics)
                
                # Select the feature to visualize
                selected_feature = st.selectbox("Select a feature:", newdf.columns)

                # Calculate mean and standard deviation
                mean = data[selected_feature].mean()
                std = data[selected_feature].std()

                # Create a range of values for the PDF
                x = np.linspace(data[selected_feature].min(), data[selected_feature].max(), 100)
                # Calculate the PDF using Gaussian distribution
                pdf = norm.pdf(x, mean, std)

                # Create a DataFrame for the PDF data
                pdf_data = pd.DataFrame({'x': x, 'pdf': pdf})
                # Plot the PDF using Plotly Express
                fig = px.line(pdf_data, x='x', y='pdf')
                fig.update_layout(
                    title="Probability Density Function of " + selected_feature,
                    xaxis_title=selected_feature,
                    yaxis_title="PDF"
                )

                # Save the Plotly figure as an HTML file
                fig_html_path = "pdf_plot.html"
                fig.write_html(fig_html_path)

                # Provide a link to open the Plotly chart in a new tab
                if st.button("Open PDF Plot"):
                    new_tab = webbrowser.get()
                    new_tab.open(fig_html_path, new=2)

                # Apply the PDF to identify outliers
                threshold = 0.01  # Adjust the threshold as needed
                data['anomaly'] = 0  # Initialize anomaly feature as 0
                data.loc[data[selected_feature] < norm.ppf(threshold, mean, std), 'anomaly'] = 1

                # Calculate the percentage of outliers
                total_data_points = data.shape[0]
                total_outliers = data['anomaly'].sum()
                percentage_outliers = (total_outliers / total_data_points) * 100

                # Show the updated dataframe with the anomaly feature and the percentage of outliers
                st.write("Updated Dataframe:")
                st.write(data)

                file_name = "Anomaly_" + selected_feature.replace(" ", "_") + ".csv"
                st.download_button(
                    label="Download",
                    data=data.to_csv(index=False),
                    file_name=file_name,
                    mime="text/csv"
                )

                st.write("Percentage of outliers: {:.2f}%".format(percentage_outliers))


        elif selected_anomalyAlgorithm == "RSF":
            st.markdown(
                "<h2 style='font-size: 24px; color: blue;'>Upload Dataset, Unleash Statistical Magic for Numerical Variables!</h2>",
                unsafe_allow_html=True)
            data_file = st.file_uploader("Upload File EKKO_EKPO data with these column ['WERKS', 'MATNR', 'EBELN', 'EBELP', 'LIFNR', 'MENGE', 'NETPR', 'PEINH', 'NETWR',]", type=["csv", "xlsx", "XLSX"])
            columns_to_include = ['WERKS', 'MATNR', 'EBELN', 'EBELP', 'LIFNR', 'MENGE', 'NETPR', 'PEINH', 'NETWR', ]
            if data_file is not None:
                file_extension = data_file.name.split(".")[-1]
                if file_extension == "csv":
                    data = pd.read_csv(data_file,usecols=columns_to_include)
                elif file_extension in ["xlsx", "XLSX"]:
                    data = pd.read_excel(data_file,usecols=columns_to_include)
                else:
                    st.error("Unsupported file format. Please upload a CSV or Excel file.")


                st.write("Dealing with duplicate values...")
                num_duplicates = data.duplicated().sum()  # Count the number of duplicate rows
                data_unique = data.drop_duplicates()  # Drop the duplicate rows
                st.write(f"Number of duplicate rows: {num_duplicates}")

                st.write("Downloading the dataset...")

                #dfx = pd.read_csv(r"C:\Users\LENOVO\Downloads\ekko_ekpo_v1.csv",encoding='latin1',
                #usecols=['WERKS', 'MATNR', 'EBELN', 'EBELP', 'LIFNR', 'MENGE', 'NETPR', 'PEINH','NETWR'])

                st.write(data.head())
                dfx=data[['WERKS','MATNR','EBELN','EBELP','LIFNR','MENGE','NETPR','PEINH','NETWR']]
                ebeln_count = dfx.groupby('LIFNR')['EBELN'].nunique().reset_index()
                ebeln_count.rename(columns={'EBELN': 'EBELN_Count'}, inplace=True)

                netwr_sum_by_vendor = dfx.groupby('LIFNR')['NETWR'].sum().reset_index()
                netwr_sum_by_vendor.rename(columns={'NETWR': 'NETWR_Sum_ByVendor'}, inplace=True)

                netwr_sum_by_vendor_ebeln = dfx.groupby(['LIFNR', 'EBELN'])['NETWR'].sum().reset_index()
                netwr_sum_by_vendor_ebeln.rename(columns={'NETWR': 'NETWR_Sum_ByVendor_EBELN'}, inplace=True)

                dfx = pd.merge(dfx, ebeln_count, on='LIFNR')
                dfx = pd.merge(dfx, netwr_sum_by_vendor, on='LIFNR')
                dfx = pd.merge(dfx, netwr_sum_by_vendor_ebeln, on=['LIFNR', 'EBELN'])

                netwr_max = dfx.groupby(['LIFNR'])['NETWR_Sum_ByVendor_EBELN'].max().reset_index()
                netwr_max.rename(columns={'NETWR_Sum_ByVendor_EBELN': 'netwr_max'}, inplace=True)

                dfx = pd.merge(dfx, netwr_max, on='LIFNR')

                dfx['Avg_exclu_max'] = (dfx['NETWR_Sum_ByVendor'] - dfx['netwr_max']) / (dfx['EBELN_Count'] - 1)
                dfx['RSF'] = dfx['netwr_max'] / dfx['Avg_exclu_max']

                anomaly = np.where((dfx['EBELN_Count'] > 5) & (dfx['RSF'] > 10), 1, 0)
                dfx['Anomaly'] = anomaly

                #dfx1 = dfx[(dfx['EBELN_Count'] > 5) & (dfx['RSF'] > 10)]
                #dfx.to_csv("RSF_ekko_ekpo_after_excluding_zero.csv")

                st.write(dfx)

                file_name = "Anomaly_" + "rsf".replace(" ", "_") + ".csv"
                st.download_button(
                    label="Download",
                    data=dfx.to_csv(index=False),
                    file_name=file_name,
                    mime="text/csv"
                )

                dfx['Anomaly Flag'] = dfx['Anomaly'].apply(lambda x: 'Anomaly' if x == 1 else 'Not Anomaly')
                dfx['Anomaly Flag'] = dfx['Anomaly Flag'].astype(str)

                # Create the graph
                fig = px.scatter(
                    dfx,
                    x="RSF",
                    y="EBELN_Count",
                    hover_name="LIFNR",
                    color="Anomaly Flag",  # Change 'color' to 'Anomaly Flag' for the fill color

                    # Assuming you want different colors for Anomaly and Not Anomaly points
                    color_discrete_map={"Not Anomaly": "blue", "Anomaly": "red"},
                )

                # Add the title and caption
                fig.update_layout(title="Higher the RSF and EBELN_Count more the Chances of Anomaly")

                # Write the Plotly chart to an HTML file
                fig_html_path = "RSF_Anomaly_graph.html"
                fig.write_html(fig_html_path)

                # Provide a link to open the Plotly chart in a new tab
                if st.button("Open RSF Plot"):
                    new_tab = webbrowser.get()
                    new_tab.open(fig_html_path, new=2)

















        elif selected_anomalyAlgorithm == "Benford law 1st digit":
            st.markdown(
                "<h2 style='font-size: 24px; color: blue;'>Upload Dataset, Unleash Statistical Magic for Numerical Variables!</h2>",
                unsafe_allow_html=True)
            data_file = st.file_uploader("Upload File", type=["csv", "xlsx", "XLSX"])

            if data_file is not None:
                file_extension = data_file.name.split(".")[-1]
                if file_extension == "csv":
                    data = pd.read_csv(data_file)
                elif file_extension in ["xlsx", "XLSX"]:
                    data = pd.read_excel(data_file)
                else:
                    st.error("Unsupported file format. Please upload a CSV or Excel file.")

                st.write(data.head())



                # Assuming you have a DataFrame named 'data' with a column of numeric data named 'selected_feature'


                numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
                newdf = data.select_dtypes(include=numerics)

                selected_feature = st.selectbox("Select a feature:", newdf.columns)

                # Calculate the distribution of first digits using Benford's Law
                df, df1, counts, benford  = calculate_first_digit(data[selected_feature])
                df2 = pd.merge(df, df1, left_on=df.iloc[:, 0],right_on='index',how='right')
                # st.write(df2)



                    # Create a button to open the chart
                if st.button("Open Chart"):
                    # Calculate the distribution of first digits using Benford's Law
                    df, df1, counts, benford = calculate_first_digit(data[selected_feature])
                    df2 = pd.merge(df, df1, left_on=df.iloc[:, 0],right_on='index',how='right')
                    st.write(df2)

                    # Create the observed and expected bar plots
                    observed_trace = go.Bar(x=counts.index, y=counts * 100, name='Observed')
                    expected_trace = go.Scatter(x=np.arange(0, 10), y=benford * 100, mode='lines', name='Expected')

                    # Create the layout
                    layout = go.Layout(
                        title="Benford's Law Analysis of " + selected_feature,
                        xaxis=dict(title="First Digit"),
                        yaxis=dict(title="Percentage"),
                        legend=dict(x=0, y=1)
                    )

                    # Create the figure and add the traces
                    fig = go.Figure(data=[observed_trace, expected_trace], layout=layout)

                    # Display the figure
                    st.plotly_chart(fig)

                    # Option to save the plot
                    save_plot_option = st.checkbox("Save plot")
                    if save_plot_option:
                        file_name = "Benford_Plot_" + selected_feature.replace(" ", "_") + ".html"
                        pio.write_html(fig, file_name)
                        st.write(f"Plot saved as {file_name}")

                # Calculate the deviation from expected percentages
                deviation = (counts - benford) * 100

                # Create the results DataFrame
                results = pd.DataFrame(
                    {'Digit': counts.index, 'Observed (%)': counts * 100, 'Expected (%)': benford * 100,
                    'Deviation (%)': deviation})

                # Option to save the results as CSV
                save_csv_option = st.checkbox("Save results as CSV")
                if save_csv_option:
                    file_name = "Benford_Analysis_" + selected_feature.replace(" ", "_") + ".csv"
                    st.download_button(
                        label="Download CSV",
                        data=df2.to_csv(index=False),
                        file_name=file_name,
                        mime="text/csv"
                    )

                # Display the results DataFrame
                st.write("Results:")
                st.write(df2)
            #  starting of anomaly detection algorithms over here

        elif selected_anomalyAlgorithm == "Benford law 2nd digit":
            st.markdown(
                "<h2 style='font-size: 24px; color: blue;'>Upload Dataset, Unleash Statistical Magic for Numerical Variables!</h2>",
                unsafe_allow_html=True)
            data_file = st.file_uploader("Upload File", type=["csv", "xlsx", "XLSX"])

            if data_file is not None:
                file_extension = data_file.name.split(".")[-1]
                if file_extension == "csv":
                    data = pd.read_csv(data_file)
                elif file_extension in ["xlsx", "XLSX"]:
                    data = pd.read_excel(data_file)
                else:
                    st.error("Unsupported file format. Please upload a CSV or Excel file.")

                st.write(data.head())






                # Assuming you have a DataFrame named 'data' with a column of numeric data named 'selected_feature'


                numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
                newdf = data.select_dtypes(include=numerics)

                selected_feature = st.selectbox("Select a feature:", newdf.columns)

                # Calculate the distribution of second digits using Benford's Law
                df, df1, counts, benford = calculate_2th_digit(data[selected_feature])
                df2 = pd.merge(df, df1, left_on=df.iloc[:, 0],right_on='index',how='right')
                # st.write(df2)

                #counts, benford = calculate_2th_digit(data[selected_feature])



                # Create a button to open the chart
                if st.button("Open Chart"):
                    # Calculate the distribution of second digits using Benford's Law
                    df, df1, counts, benford = calculate_2th_digit(data[selected_feature])
                    df2 = pd.merge(df, df1, left_on=df.iloc[:, 0],right_on='index',how='right')
                    st.write(df2)

                    # Create the observed and expected bar plots
                    observed_trace = go.Bar(x=counts.index, y=counts * 100, name='Observed', marker=dict(color='blue'))
                    expected_trace = go.Scatter(x=np.arange(0, 100), y=benford * 100, mode='lines', line=dict(color='red'),
                                                name='Expected')

                    # Create the layout
                    layout = go.Layout(
                        title="Benford's Law Analysis of Second Digit in " + selected_feature,
                        xaxis=dict(title="Second Digit"),
                        yaxis=dict(title="Percentage"),
                        legend=dict(x=0, y=1)
                    )

                    # Create the figure and add the traces
                    fig = go.Figure(data=[observed_trace, expected_trace], layout=layout)

                    # Display the figure
                    st.plotly_chart(fig)

                    # Option to save the plot
                    save_plot_option = st.checkbox("Save plot")
                    if save_plot_option:
                        file_name = "Benford_Plot_2nd_Digit_" + selected_feature.replace(" ", "_") + ".html"
                        pio.write_html(fig, file_name)
                        st.write(f"Plot saved as {file_name}")

                # Calculate the deviation from expected percentages
                deviation = (counts - benford) * 100

                # Create the results DataFrame
                results = pd.DataFrame(
                    {'Digit': counts.index, 'Observed (%)': counts * 100, 'Expected (%)': benford[:len(counts)] * 100,
                    'Deviation (%)': deviation})

                # Option to save the results as CSV
                save_csv_option = st.checkbox("Save results as CSV")
                if save_csv_option:
                    file_name = "Benford_Analysis_2nd_Digit_" + selected_feature.replace(" ", "_") + ".csv"
                    st.download_button(
                        label="Download CSV",
                        data=df2.to_csv(index=False),
                        file_name=file_name,
                        mime="text/csv"
                    )

                # Display the results DataFrame
                st.write("Results:")
                st.write(df2)
            #  starting of anomaly detection algorithms over here


        elif selected_anomalyAlgorithm == "Benford law 3rd digit":
            st.markdown(
                "<h2 style='font-size: 24px; color: blue;'>Upload Dataset, Unleash Statistical Magic for Numerical Variables!</h2>",
                unsafe_allow_html=True)
            data_file = st.file_uploader("Upload File", type=["csv", "xlsx", "XLSX"])

            if data_file is not None:
                file_extension = data_file.name.split(".")[-1]
                if file_extension == "csv":
                    data = pd.read_csv(data_file)
                elif file_extension in ["xlsx", "XLSX"]:
                    data = pd.read_excel(data_file)
                else:
                    st.error("Unsupported file format. Please upload a CSV or Excel file.")

                st.write(data.head())

                # Option to select the feature for analysis

                numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
                newdf = data.select_dtypes(include=numerics)
                selected_feature = st.selectbox("Select a feature:", newdf.columns)


                # Assuming you have a DataFrame named 'data' with a column of numeric data named 'selected_feature'


                # Calculate the distribution of second digits using Benford's Law
                df, df1, counts, benford = calculate_3th_digit(data[selected_feature])

                df2 = pd.merge(df, df1, left_on=df.iloc[:, 0],right_on='index',how='right')
                # st.write(df2)



                # Exclude the first digit (0) from the observed distribution
                #counts = counts.iloc[1:]


            # Create a button to open the chart
                if st.button("Open Chart"):
                    # Create the observed and expected bar plots
                    counts = counts[counts.index > 99]
                    observed_trace = go.Bar(x=counts.index, y=counts * 100, name='Observed', marker=dict(color='blue'))
                    expected_trace = go.Scatter(x=np.arange(100, 1000), y=benford * 100, mode='lines', line=dict(color='red'),
                                                name='Expected')

                    # Create the layout
                    layout = go.Layout(
                        title="Benford's Law Analysis of 3rd Digit in " + selected_feature,
                        xaxis=dict(title="3rd Digit"),
                        yaxis=dict(title="Percentage"),
                        legend=dict(x=0, y=1)
                    )

                    # Create the figure and add the traces
                    fig = go.Figure(data=[observed_trace, expected_trace], layout=layout)

                    # Display the figure
                    st.plotly_chart(fig)

                    # Option to save the plot
                    save_plot_option = st.checkbox("Save plot")
                    if save_plot_option:
                        file_name = "Benford_Plot_3nd_Digit_" + selected_feature.replace(" ", "_") + ".html"
                        pio.write_html(fig, file_name)
                        st.write(f"Plot saved as {file_name}")

                # Calculate the deviation from expected percentages
                deviation = (counts - benford) * 100

                # Create the results DataFrame
                results = pd.DataFrame(
                    {'Digit': counts.index, 'Observed (%)': counts * 100, 'Expected (%)': benford[:len(counts)] * 100,
                     'Deviation (%)': deviation})

                # Option to save the results as CSV
                save_csv_option = st.checkbox("Save results as CSV")
                if save_csv_option:
                    file_name = "Benford_Analysis_3nd_Digit_" + selected_feature.replace(" ", "_") + ".csv"
                    st.download_button(
                        label="Download CSV",
                        data=df2.to_csv(index=False),
                        file_name=file_name,
                        mime="text/csv"
                    )

                # Display the results DataFrame
                st.write("Results:")
                #st.write(results)
            #  starting of anomaly detection algorithms over here











        st.sidebar.header("Machine Learning Methods")
        anomaly_options = ["None",
                        "Isolation Forest",
                        "Kernel Density Estimation (KDE)",
                        "K-Means",
                        # "Gaussian Mixture Models (GMM)",
                        # "DBSCAN",
                        "Local Outlier Factor",
                        "Robust Covariance",
                        "One-Class SVM",
                        "One-Class SVM (SGD)"


        ]
        selected_anomalyAlgorithm = st.sidebar.selectbox("Select machine learning algorithms", anomaly_options)



        if selected_anomalyAlgorithm == "None":
            st.write(" ")


        elif selected_anomalyAlgorithm == "Isolation Forest":


            st.markdown(
                "<h2 style='font-size: 24px; color: blue;'>Upload Dataset, Empower Machine Learning Algorithms!</h2>",
                unsafe_allow_html=True)
            data_file = st.file_uploader("Upload File", type=["csv", "xlsx", "XLSX"])

            if data_file is not None:
                file_extension = data_file.name.split(".")[-1]
                if file_extension == "csv":
                    data = pd.read_csv(data_file)
                elif file_extension in ["xlsx", "XLSX"]:
                    data = pd.read_excel(data_file)
                else:
                    st.error("Unsupported file format. Please upload a CSV or Excel file.")






                st.write("Dealing with missing values:")
                threshold = 0.1  # Set the threshold to 10% (0.1)
                missing_percentages = data.isnull().mean()  # Calculate the percentage of missing values in each column
                columns_to_drop = missing_percentages[missing_percentages > threshold].index  # Get the columns exceeding the threshold
                data = data.drop(columns=columns_to_drop)  # Drop the columns
                st.write(f"Features with more than {threshold*100:.2f}% missing values dropped successfully.")



                data = drop_features_with_missing_values(data)




                st.write("Dealing with duplicate values...")
                num_duplicates = data.duplicated().sum()  # Count the number of duplicate rows
                data_unique = data.drop_duplicates()  # Drop the duplicate rows
                st.write(f"Number of duplicate rows: {num_duplicates}")
                st.write("Dealing done with duplicates.")

                st.write("Performing categorical feature encoding...")
                # creating the copy of the original dataset over here
                copy_data=data.copy()
                # st.write(copy_data)
                categorical_features = [feature for feature in data_unique.columns if data_unique[feature].dtype == 'object']
                data_encoded = data_unique.copy()
                for feature in categorical_features:
                    labels_ordered = data_unique.groupby([feature]).size().sort_values().index
                    labels_ordered = {k: i for i, k in enumerate(labels_ordered, 0)}
                    data_encoded[feature] = data_encoded[feature].map(labels_ordered)
                data = data_encoded  # Update the original dataset with encoded features
                st.write("Categorical features encoded successfully.")

                st.write("Performing feature scaling...")
                numeric_columns = data.select_dtypes(include=["int", "float"]).columns

                if len(numeric_columns) == 0:
                    st.write("No numeric columns found.")
                else:
                    scaler = MinMaxScaler()
                    data_scaled = data.copy()
                    data_scaled[numeric_columns] = scaler.fit_transform(data_scaled[numeric_columns])
                    data = data_scaled  # Update the original dataset with scaled features
                    st.write("Feature scaling performed successfully.")

                st.write("Downloading the dataset...")

                # Save the modified dataset to a file
                modified_dataset_filename = "modified_dataset.csv"
                # data.to_csv(modified_dataset_filename, index=False)
                st.write(data.head())
                st.write(data.shape)





                # Applying the anomaly detection
                
                data_with_anomalies_IsolationForest = apply_anomaly_detection_IsolationForest(data)
                AnomalyFeature=data_with_anomalies_IsolationForest[["Anomaly"]]
                # st.write(AnomalyFeature)
                
                st.subheader("Data with Anomalies")
                final_data=pd.concat([copy_data,AnomalyFeature],axis=1)
                st.write(final_data)
                ##################################################
                selected_x_col = st.selectbox("Select X-axis column", data.columns)
                selected_y_col = st.selectbox("Select Y-axis column", data.columns)

                # Create a scatter plot using Seaborn
                plt.figure(figsize=(10, 6))
                sns.scatterplot(data=data_with_anomalies_IsolationForest, x=selected_x_col, y=selected_y_col, hue='Anomaly', palette={0: 'blue', 1: 'red'})

                # Get the current legend
                current_handles, current_labels = plt.gca().get_legend_handles_labels()

                # Customize the legend
                legend_labels = ['Not Anomaly', 'Anomaly']
                legend_title = 'Anomaly'
                custom_legend = plt.legend(current_handles, legend_labels, title=legend_title, loc='upper right')

                # Set colors for the legend
                for handle, label in zip(custom_legend.legendHandles, legend_labels):
                    if label == 'Not Anomaly':
                        handle.set_color('blue')
                    elif label == 'Anomaly':
                        handle.set_color('red')

                # Show the Seaborn plot
                st.pyplot()

                # Save the Seaborn plot as an image file (optional)
                # plt.savefig("isolation_forest_plot.png")

                st.write("Download the data with anomaly indicator")
                st.download_button(
                    label="Download",
                    data=final_data.to_csv(index=False),
                    file_name="IsolationForestAnomaly.csv",
                    mime="text/csv"
                )

                # Count the number of anomalies
                num_anomalies = data_with_anomalies_IsolationForest['Anomaly'].sum()

                # Total number of data points
                total_data_points = len(data_with_anomalies_IsolationForest)

                # Calculate the percentage of anomalies
                percentage_anomalies = (num_anomalies / total_data_points) * 100

                st.write(f"Number of anomalies: {num_anomalies}")
                st.write(f"Percentage of anomalies: {percentage_anomalies:.2f}%")

        elif selected_anomalyAlgorithm == "Kernel Density Estimation (KDE)":


            st.markdown(
                "<h2 style='font-size: 24px; color: blue;'>Upload Dataset, Empower Machine Learning Algorithms!</h2>",
                unsafe_allow_html=True)
            data_file = st.file_uploader("Upload File", type=["csv", "xlsx", "XLSX"])

            if data_file is not None:
                file_extension = data_file.name.split(".")[-1]
                if file_extension == "csv":
                    data = pd.read_csv(data_file)
                elif file_extension in ["xlsx", "XLSX"]:
                    data = pd.read_excel(data_file)
                else:
                    st.error("Unsupported file format. Please upload a CSV or Excel file.")






                st.write("Dealing with missing values:")
                threshold = 0.1  # Set the threshold to 10% (0.1)
                missing_percentages = data.isnull().mean()  # Calculate the percentage of missing values in each column
                columns_to_drop = missing_percentages[missing_percentages > threshold].index  # Get the columns exceeding the threshold
                data = data.drop(columns=columns_to_drop)  # Drop the columns
                st.write(f"Features with more than {threshold*100:.2f}% missing values dropped successfully.")



                data = drop_features_with_missing_values(data)




                st.write("Dealing with duplicate values...")
                num_duplicates = data.duplicated().sum()  # Count the number of duplicate rows
                data_unique = data.drop_duplicates()  # Drop the duplicate rows
                st.write(f"Number of duplicate rows: {num_duplicates}")
                st.write("Dealing done with duplicates.")

                st.write("Performing categorical feature encoding...")
                copy_data=data.copy()
                categorical_features = [feature for feature in data_unique.columns if data_unique[feature].dtype == 'object']
                data_encoded = data_unique.copy()
                for feature in categorical_features:
                    labels_ordered = data_unique.groupby([feature]).size().sort_values().index
                    labels_ordered = {k: i for i, k in enumerate(labels_ordered, 0)}
                    data_encoded[feature] = data_encoded[feature].map(labels_ordered)
                data = data_encoded  # Update the original dataset with encoded features
                st.write("Categorical features encoded successfully.")

                st.write("Performing feature scaling...")
                numeric_columns = data.select_dtypes(include=["int", "float"]).columns

                if len(numeric_columns) == 0:
                    st.write("No numeric columns found.")
                else:
                    scaler = MinMaxScaler()
                    data_scaled = data.copy()
                    data_scaled[numeric_columns] = scaler.fit_transform(data_scaled[numeric_columns])
                    data = data_scaled  # Update the original dataset with scaled features
                    st.write("Feature scaling performed successfully.")

                st.write("Downloading the dataset...")

                # Save the modified dataset to a file
                modified_dataset_filename = "modified_dataset.csv"
                # data.to_csv(modified_dataset_filename, index=False)
                st.write(data.head())
                st.write(data.shape)




                # Perform anomaly detection using Kernel Density Estimation
                kde = KernelDensity()
                kde.fit(data)
                log_densities = kde.score_samples(data)
                threshold = np.percentile(log_densities, 5)  # Adjust the percentile as needed

                # Identify outliers based on log densities below the threshold
                outlier_indices = np.where(log_densities < threshold)[0]

                # Create a copy of the data with an "Anomaly" column indicating outliers
                data_with_anomalies_kde = data.copy()
                data_with_anomalies_kde['Anomaly'] = 0
                data_with_anomalies_kde.iloc[outlier_indices, -1] = 1

                st.subheader("Data with Anomalies (KDE)")
                AnomalyFeature=data_with_anomalies_kde[["Anomaly"]]
                final_data=pd.concat([copy_data,AnomalyFeature],axis=1)
                st.write(final_data)

                selected_feature = st.selectbox("Select a feature", data.columns)

                # Create a DataFrame for the KDE results
                kde_data = pd.DataFrame({'Feature': data[selected_feature], 'Density': np.exp(log_densities)})

                # Plot the results using Seaborn
                plt.figure(figsize=(10, 6))
                sns.lineplot(data=kde_data, x='Feature', y='Density', color='blue')
                sns.scatterplot(data=kde_data.loc[kde_data.index.isin(outlier_indices)], x='Feature', y='Density', color='red')

                plt.title('Kernel Density Estimation Anomaly Detection')
                plt.xlabel(selected_feature)
                plt.ylabel('Density')

                st.pyplot()

                # Counting the number of anomalies
                num_anomalies = data_with_anomalies_kde['Anomaly'].sum()

                # Total number of data points
                total_data_points = len(data_with_anomalies_kde)

                # Calculating the percentage of anomalies
                percentage_anomalies = (num_anomalies / total_data_points) * 100

                st.write(f"Number of anomalies: {num_anomalies}")
                st.write(f"Percentage of anomalies: {percentage_anomalies:.2f}%")

                # Download the data with anomaly indicator
                st.write("Download the data with anomaly indicator (KDE)")
                st.download_button(
                    label="Download",
                    data=final_data.to_csv(index=False),
                    file_name="KDEAnomaly.csv",
                    mime="text/csv"
                )









        elif selected_anomalyAlgorithm == "K-Means":

            st.markdown(
                "<h2 style='font-size: 24px; color: blue;'>Upload Dataset, Empower Machine Learning Algorithms!</h2>",
                unsafe_allow_html=True)
            data_file = st.file_uploader("Upload File", type=["csv", "xlsx", "XLSX"])

            if data_file is not None:
                file_extension = data_file.name.split(".")[-1]
                if file_extension == "csv":
                    data = pd.read_csv(data_file)
                elif file_extension in ["xlsx", "XLSX"]:
                    data = pd.read_excel(data_file)
                else:
                    st.error("Unsupported file format. Please upload a CSV or Excel file.")






                st.write("Dealing with missing values:")
                threshold = 0.1  # Set the threshold to 10% (0.1)
                missing_percentages = data.isnull().mean()  # Calculate the percentage of missing values in each column
                columns_to_drop = missing_percentages[missing_percentages > threshold].index  # Get the columns exceeding the threshold
                data = data.drop(columns=columns_to_drop)  # Drop the columns
                st.write(f"Features with more than {threshold*100:.2f}% missing values dropped successfully.")



                data = drop_features_with_missing_values(data)




                st.write("Dealing with duplicate values...")
                num_duplicates = data.duplicated().sum()  # Count the number of duplicate rows
                data_unique = data.drop_duplicates()  # Drop the duplicate rows
                st.write(f"Number of duplicate rows: {num_duplicates}")
                st.write("Dealing done with duplicates.")

                st.write("Performing categorical feature encoding...")
                copy_data=data.copy()
                categorical_features = [feature for feature in data_unique.columns if data_unique[feature].dtype == 'object']
                data_encoded = data_unique.copy()
                for feature in categorical_features:
                    labels_ordered = data_unique.groupby([feature]).size().sort_values().index
                    labels_ordered = {k: i for i, k in enumerate(labels_ordered, 0)}
                    data_encoded[feature] = data_encoded[feature].map(labels_ordered)
                data = data_encoded  # Update the original dataset with encoded features
                st.write("Categorical features encoded successfully.")

                st.write("Performing feature scaling...")
                numeric_columns = data.select_dtypes(include=["int", "float"]).columns

                if len(numeric_columns) == 0:
                    st.write("No numeric columns found.")
                else:
                    scaler = MinMaxScaler()
                    data_scaled = data.copy()
                    data_scaled[numeric_columns] = scaler.fit_transform(data_scaled[numeric_columns])
                    data = data_scaled  # Update the original dataset with scaled features
                    st.write("Feature scaling performed successfully.")

                st.write("Downloading the dataset...")

                # Save the modified dataset to a file
                modified_dataset_filename = "modified_dataset.csv"
                # data.to_csv(modified_dataset_filename, index=False)
                st.write(data.head())
                st.write(data.shape)






                # Applying K-means clustering
                kmeans = KMeans(n_clusters=2)  # You can adjust the number of clusters as needed
                kmeans.fit(data)

                # Predicting cluster labels
                cluster_labels = kmeans.predict(data)
                data_with_clusters = data.copy()
                data_with_clusters['Cluster'] = cluster_labels

                # Calculate the percentage of outliers
                outlier_percentage = (data_with_clusters['Cluster'].value_counts()[1] / len(data_with_clusters)) * 100

                # Create an anomaly indicator
                data_with_clusters['Anomaly'] = np.where(data_with_clusters['Cluster'] == 1, 1, 0)

                st.subheader("Data with Anomaly Indicator")

                AnomalyFeature=data_with_clusters[["Anomaly"]]
                final_data=pd.concat([copy_data,AnomalyFeature],axis=1)
                st.write(final_data)

                selected_x_col = st.selectbox("Select X-axis column", data.columns)
                selected_y_col = st.selectbox("Select Y-axis column", data.columns)

                # Define custom color palette for Seaborn
                colors = {0: 'blue', 1: 'red'}

                # Create a scatter plot using Seaborn with the custom color palette
                plt.figure(figsize=(10, 6))
                sns.scatterplot(data=data_with_clusters, x=selected_x_col, y=selected_y_col, hue='Anomaly', palette=colors)
                plt.title('K-means Clustering')
                plt.xlabel(selected_x_col)
                plt.ylabel(selected_y_col)

                # Customize the legend
                legend_labels = ['Not Anomaly', 'Anomaly']
                legend_title = 'Anomaly'
                plt.legend(title=legend_title, labels=legend_labels, loc='upper right')

                # Show the Seaborn plot
                st.pyplot()

                # Save the Seaborn plot as an image file (optional)
                # plt.savefig("kmeans_plot.png")

                # Counting the number of anomalies
                num_anomalies = data_with_clusters['Anomaly'].sum()

                # Total number of data points
                total_data_points = len(data_with_clusters)

                # Calculating the percentage of anomalies
                percentage_anomalies = (num_anomalies / total_data_points) * 100

                st.write(f"Number of anomalies: {num_anomalies}")
                st.write(f"Percentage of anomalies: {percentage_anomalies:.2f}%")

                # Download the data with anomaly indicator
                st.write("Download the data with anomaly indicator")
                st.download_button(
                    label="Download",
                    data=final_data.to_csv(index=False),
                    file_name="KMeansAnomaly.csv",
                    mime="text/csv"
                )



        #  ending of anomaly detection algorithms over here


        elif selected_anomalyAlgorithm == "Gaussian Mixture Models (GMM)":
            st.markdown(
                "<h2 style='font-size: 24px; color: blue;'>Upload Dataset, Empower Machine Learning Algorithms!</h2>",
                unsafe_allow_html=True)
            data_file = st.file_uploader("Upload File", type=["csv", "xlsx", "XLSX"])

            if data_file is not None:
                file_extension = data_file.name.split(".")[-1]
                if file_extension == "csv":
                    data = pd.read_csv(data_file)
                elif file_extension in ["xlsx", "XLSX"]:
                    data = pd.read_excel(data_file)
                else:
                    st.error("Unsupported file format. Please upload a CSV or Excel file.")






                st.write("Dealing with missing values:")
                threshold = 0.1  # Set the threshold to 10% (0.1)
                missing_percentages = data.isnull().mean()  # Calculate the percentage of missing values in each column
                columns_to_drop = missing_percentages[missing_percentages > threshold].index  # Get the columns exceeding the threshold
                data = data.drop(columns=columns_to_drop)  # Drop the columns
                st.write(f"Features with more than {threshold*100:.2f}% missing values dropped successfully.")



                data = drop_features_with_missing_values(data)




                st.write("Dealing with duplicate values...")
                num_duplicates = data.duplicated().sum()  # Count the number of duplicate rows
                data_unique = data.drop_duplicates()  # Drop the duplicate rows
                st.write(f"Number of duplicate rows: {num_duplicates}")
                st.write("Dealing done with duplicates.")

                st.write("Performing categorical feature encoding...")
                categorical_features = [feature for feature in data_unique.columns if data_unique[feature].dtype == 'object']
                data_encoded = data_unique.copy()
                for feature in categorical_features:
                    labels_ordered = data_unique.groupby([feature]).size().sort_values().index
                    labels_ordered = {k: i for i, k in enumerate(labels_ordered, 0)}
                    data_encoded[feature] = data_encoded[feature].map(labels_ordered)
                data = data_encoded  # Update the original dataset with encoded features
                st.write("Categorical features encoded successfully.")

                st.write("Performing feature scaling...")
                numeric_columns = data.select_dtypes(include=["int", "float"]).columns

                if len(numeric_columns) == 0:
                    st.write("No numeric columns found.")
                else:
                    scaler = MinMaxScaler()
                    data_scaled = data.copy()
                    data_scaled[numeric_columns] = scaler.fit_transform(data_scaled[numeric_columns])
                    data = data_scaled  # Update the original dataset with scaled features
                    st.write("Feature scaling performed successfully.")

                st.write("Downloading the dataset...")

                # Save the modified dataset to a file
                modified_dataset_filename = "modified_dataset.csv"
                # data.to_csv(modified_dataset_filename, index=False)
                st.write(data.head())
                st.write(data.shape)




                # Applying the anomaly detection using Gaussian Mixture Models
                data_with_anomalies_GMM = apply_anomaly_detection_GMM(data)

                st.subheader("Data with Anomalies (GMM)")
                st.write(data_with_anomalies_GMM)

                selected_x_col = st.selectbox("Select X-axis column", data.columns)
                selected_y_col = st.selectbox("Select Y-axis column", data.columns)

                # Create a scatter plot using Seaborn
                plt.figure(figsize=(10, 6))
                sns.scatterplot(data=data_with_anomalies_GMM, x=selected_x_col, y=selected_y_col, hue='Anomaly', palette={0: 'blue', 1: 'red'})

                # Get the current legend
                current_handles, current_labels = plt.gca().get_legend_handles_labels()

                # Customize the legend
                legend_labels = ['Not Anomaly', 'Anomaly']
                legend_title = 'Anomaly'
                custom_legend = plt.legend(current_handles, legend_labels, title=legend_title, loc='upper right')

                # Set colors for the legend
                for handle, label in zip(custom_legend.legendHandles, legend_labels):
                    if label == 'Not Anomaly':
                        handle.set_color('blue')
                    elif label == 'Anomaly':
                        handle.set_color('red')

                plt.title('Gaussian Mixture Models Anomaly Detection')
                plt.xlabel(selected_x_col)
                plt.ylabel(selected_y_col)

                st.pyplot()

                # Save the Seaborn plot as an image file (optional)
                # plt.savefig("gmm_plot.png")

                st.write("Download the data with anomaly indicator")
                st.download_button(
                    label="Download",
                    data=final_data.to_csv(index=False),
                    file_name="GMMAnomaly.csv",
                    mime="text/csv"
                )

                # Count the number of anomalies
                num_anomalies = data_with_anomalies_GMM['Anomaly'].sum()

                # Total number of data points
                total_data_points = len(data_with_anomalies_GMM)

                # Calculate the percentage of anomalies
                percentage_anomalies = (num_anomalies / total_data_points) * 100

                st.write(f"Number of anomalies: {num_anomalies}")
                st.write(f"Percentage of anomalies: {percentage_anomalies:.2f}%")



            



        elif selected_anomalyAlgorithm == "DBSCAN":
            st.header("Try other technique we are working on Gaussian Mixture Models (GMM).......")
           





        elif selected_anomalyAlgorithm == "Local Outlier Factor":

            st.markdown(
                "<h2 style='font-size: 24px; color: blue;'>Upload Dataset, Empower Machine Learning Algorithms!</h2>",
                unsafe_allow_html=True)
            data_file = st.file_uploader("Upload File", type=["csv", "xlsx", "XLSX"])

            if data_file is not None:
                file_extension = data_file.name.split(".")[-1]
                if file_extension == "csv":
                    data = pd.read_csv(data_file)
                elif file_extension in ["xlsx", "XLSX"]:
                    data = pd.read_excel(data_file)
                else:
                    st.error("Unsupported file format. Please upload a CSV or Excel file.")






                st.write("Dealing with missing values:")
                threshold = 0.1  # Set the threshold to 10% (0.1)
                missing_percentages = data.isnull().mean()  # Calculate the percentage of missing values in each column
                columns_to_drop = missing_percentages[missing_percentages > threshold].index  # Get the columns exceeding the threshold
                data = data.drop(columns=columns_to_drop)  # Drop the columns
                st.write(f"Features with more than {threshold*100:.2f}% missing values dropped successfully.")



                data = drop_features_with_missing_values(data)




                st.write("Dealing with duplicate values...")
                num_duplicates = data.duplicated().sum()  # Count the number of duplicate rows
                data_unique = data.drop_duplicates()  # Drop the duplicate rows
                st.write(f"Number of duplicate rows: {num_duplicates}")
                st.write("Dealing done with duplicates.")

                st.write("Performing categorical feature encoding...")
                copy_data=data.copy()
                categorical_features = [feature for feature in data_unique.columns if data_unique[feature].dtype == 'object']
                data_encoded = data_unique.copy()
                for feature in categorical_features:
                    labels_ordered = data_unique.groupby([feature]).size().sort_values().index
                    labels_ordered = {k: i for i, k in enumerate(labels_ordered, 0)}
                    data_encoded[feature] = data_encoded[feature].map(labels_ordered)
                data = data_encoded  # Update the original dataset with encoded features
                st.write("Categorical features encoded successfully.")

                st.write("Performing feature scaling...")
                numeric_columns = data.select_dtypes(include=["int", "float"]).columns

                if len(numeric_columns) == 0:
                    st.write("No numeric columns found.")
                else:
                    scaler = MinMaxScaler()
                    data_scaled = data.copy()
                    data_scaled[numeric_columns] = scaler.fit_transform(data_scaled[numeric_columns])
                    data = data_scaled  # Update the original dataset with scaled features
                    st.write("Feature scaling performed successfully.")

                st.write("Downloading the dataset...")

                # Save the modified dataset to a file
                modified_dataset_filename = "modified_dataset.csv"
                # data.to_csv(modified_dataset_filename, index=False)
                st.write(data.head())
                st.write(data.shape)






                # Applying the anomaly detection
                data_with_anomalies_LocalOutlierFactor = apply_anomaly_detection_LocalOutlierFactor(data)
                AnomalyFeature=data_with_anomalies_LocalOutlierFactor[["Anomaly"]]
                final_data=pd.concat([copy_data,AnomalyFeature],axis=1)
                st.subheader("Data with Anomalies")


                st.write(final_data)

                selected_x_col = st.selectbox("Select X-axis column", data.columns)
                selected_y_col = st.selectbox("Select Y-axis column", data.columns)

                # Create a scatter plot using Seaborn
                plt.figure(figsize=(10, 6))
                sns.scatterplot(data=data_with_anomalies_LocalOutlierFactor, x=selected_x_col, y=selected_y_col, hue='Anomaly', palette={0: 'blue', 1: 'red'})

                # Get the current legend
                current_handles, current_labels = plt.gca().get_legend_handles_labels()

                # Customize the legend
                legend_labels = ['Not Anomaly', 'Anomaly']
                legend_title = 'Anomaly'
                custom_legend = plt.legend(current_handles, legend_labels, title=legend_title, loc='upper right')

                # Set colors for the legend
                for handle, label in zip(custom_legend.legendHandles, legend_labels):
                    if label == 'Not Anomaly':
                        handle.set_color('blue')
                    elif label == 'Anomaly':
                        handle.set_color('red')

                plt.title('LocalOutlierFactor Anomaly Detection')
                plt.xlabel(selected_x_col)
                plt.ylabel(selected_y_col)

                st.pyplot()

                # Save the Seaborn plot as an image file (optional)
                # plt.savefig("local_outlier_factor_plot.png")

                st.write("Download the data with anomaly indicator")
                st.download_button(
                    label="Download",
                    data=final_data.to_csv(index=False),
                    file_name="LocalOutlierFactor.csv",
                    mime="text/csv"
                )

                # Count the number of anomalies
                num_anomalies = data_with_anomalies_LocalOutlierFactor['Anomaly'].sum()

                # Total number of data points
                total_data_points = len(data_with_anomalies_LocalOutlierFactor)

                # Calculate the percentage of anomalies
                percentage_anomalies = (num_anomalies / total_data_points) * 100

                st.write(f"Number of anomalies: {num_anomalies}")
                st.write(f"Percentage of anomalies: {percentage_anomalies:.2f}%")

        elif selected_anomalyAlgorithm == "Robust Covariance":
                st.markdown(
                "<h2 style='font-size: 24px; color: blue;'>Upload Dataset, Empower Machine Learning Algorithms!</h2>",
                unsafe_allow_html=True)
                data_file = st.file_uploader("Upload File", type=["csv", "xlsx", "XLSX"])

                if data_file is not None:
                    file_extension = data_file.name.split(".")[-1]
                    if file_extension == "csv":
                        data = pd.read_csv(data_file)
                    elif file_extension in ["xlsx", "XLSX"]:
                        data = pd.read_excel(data_file)
                    else:
                        st.error("Unsupported file format. Please upload a CSV or Excel file.")






                    st.write("Dealing with missing values:")
                    threshold = 0.1  # Set the threshold to 10% (0.1)
                    missing_percentages = data.isnull().mean()  # Calculate the percentage of missing values in each column
                    columns_to_drop = missing_percentages[missing_percentages > threshold].index  # Get the columns exceeding the threshold
                    data = data.drop(columns=columns_to_drop)  # Drop the columns
                    st.write(f"Features with more than {threshold*100:.2f}% missing values dropped successfully.")



                    data = drop_features_with_missing_values(data)




                    st.write("Dealing with duplicate values...")
                    num_duplicates = data.duplicated().sum()  # Count the number of duplicate rows
                    data_unique = data.drop_duplicates()  # Drop the duplicate rows
                    st.write(f"Number of duplicate rows: {num_duplicates}")
                    st.write("Dealing done with duplicates.")

                    st.write("Performing categorical feature encoding...")
                    copy_data=data.copy()
                    categorical_features = [feature for feature in data_unique.columns if data_unique[feature].dtype == 'object']
                    data_encoded = data_unique.copy()
                    for feature in categorical_features:
                        labels_ordered = data_unique.groupby([feature]).size().sort_values().index
                        labels_ordered = {k: i for i, k in enumerate(labels_ordered, 0)}
                        data_encoded[feature] = data_encoded[feature].map(labels_ordered)
                    data = data_encoded  # Update the original dataset with encoded features
                    st.write("Categorical features encoded successfully.")

                    st.write("Performing feature scaling...")
                    numeric_columns = data.select_dtypes(include=["int", "float"]).columns

                    if len(numeric_columns) == 0:
                        st.write("No numeric columns found.")
                    else:
                        scaler = MinMaxScaler()
                        data_scaled = data.copy()
                        data_scaled[numeric_columns] = scaler.fit_transform(data_scaled[numeric_columns])
                        data = data_scaled  # Update the original dataset with scaled features
                        st.write("Feature scaling performed successfully.")

                    st.write("Downloading the dataset...")

                    # Save the modified dataset to a file
                    modified_dataset_filename = "modified_dataset.csv"
                    # data.to_csv(modified_dataset_filename, index=False)
                    st.write(data.head())
                    st.write(data.shape)







                    # Applying the anomaly detection
                    data_with_anomalies_RobustCovariance = apply_anomaly_detection_Mahalanobis(data)
                    AnomalyFeature=data_with_anomalies_RobustCovariance[["Anomaly"]]
                    final_data=pd.concat([copy_data,AnomalyFeature],axis=1)

                    st.subheader("Data with Anomalies")
                    st.write(final_data)
                    ##################################################
                    selected_x_col = st.selectbox("Select X-axis column", data.columns)
                    selected_y_col = st.selectbox("Select Y-axis column", data.columns)

                    # Create a scatter plot using Seaborn
                    plt.figure(figsize=(10, 6))
                    sns.scatterplot(data=data_with_anomalies_RobustCovariance, x=selected_x_col, y=selected_y_col, hue='Anomaly', palette={0: 'blue', 1: 'red'})

                    # Get the current legend
                    current_handles, current_labels = plt.gca().get_legend_handles_labels()

                    # Customize the legend
                    legend_labels = ['Not Anomaly', 'Anomaly']
                    legend_title = 'Anomaly'
                    custom_legend = plt.legend(current_handles, legend_labels, title=legend_title, loc='upper right')

                    # Set colors for the legend
                    for handle, label in zip(custom_legend.legendHandles, legend_labels):
                        if label == 'Not Anomaly':
                            handle.set_color('blue')
                        elif label == 'Anomaly':
                            handle.set_color('red')

                    # Show the Seaborn plot
                    st.pyplot()

                    # Save the Seaborn plot as an image file (optional)
                    # plt.savefig("robust_covariance_plot.png")

                    st.write("Download the data with anomaly indicator")
                    st.download_button(
                        label="Download",
                        data=final_data.to_csv(index=False),
                        file_name="RobustCovarianceAnomaly.csv",
                        mime="text/csv"
                    )

                    # Count the number of anomalies
                    num_anomalies = data_with_anomalies_RobustCovariance['Anomaly'].sum()

                    # Total number of data points
                    total_data_points = len(data_with_anomalies_RobustCovariance)

                    # Calculate the percentage of anomalies
                    percentage_anomalies = (num_anomalies / total_data_points) * 100

                    st.write(f"Number of anomalies: {num_anomalies}")
                    st.write(f"Percentage of anomalies: {percentage_anomalies:.2f}%")


        elif selected_anomalyAlgorithm == "One-Class SVM":
                st.markdown(
                "<h2 style='font-size: 24px; color: blue;'>Upload Dataset, Empower Machine Learning Algorithms!</h2>",
                unsafe_allow_html=True)
                data_file = st.file_uploader("Upload File", type=["csv", "xlsx", "XLSX"])

                if data_file is not None:
                    file_extension = data_file.name.split(".")[-1]
                    if file_extension == "csv":
                        data = pd.read_csv(data_file)
                    elif file_extension in ["xlsx", "XLSX"]:
                        data = pd.read_excel(data_file)
                    else:
                        st.error("Unsupported file format. Please upload a CSV or Excel file.")






                    st.write("Dealing with missing values:")
                    threshold = 0.1  # Set the threshold to 10% (0.1)
                    missing_percentages = data.isnull().mean()  # Calculate the percentage of missing values in each column
                    columns_to_drop = missing_percentages[missing_percentages > threshold].index  # Get the columns exceeding the threshold
                    data = data.drop(columns=columns_to_drop)  # Drop the columns
                    st.write(f"Features with more than {threshold*100:.2f}% missing values dropped successfully.")



                    data = drop_features_with_missing_values(data)




                    st.write("Dealing with duplicate values...")
                    num_duplicates = data.duplicated().sum()  # Count the number of duplicate rows
                    data_unique = data.drop_duplicates()  # Drop the duplicate rows
                    st.write(f"Number of duplicate rows: {num_duplicates}")
                    st.write("Dealing done with duplicates.")

                    st.write("Performing categorical feature encoding...")
                    copy_data=data.copy()
                    categorical_features = [feature for feature in data_unique.columns if data_unique[feature].dtype == 'object']
                    data_encoded = data_unique.copy()
                    for feature in categorical_features:
                        labels_ordered = data_unique.groupby([feature]).size().sort_values().index
                        labels_ordered = {k: i for i, k in enumerate(labels_ordered, 0)}
                        data_encoded[feature] = data_encoded[feature].map(labels_ordered)
                    data = data_encoded  # Update the original dataset with encoded features
                    st.write("Categorical features encoded successfully.")

                    st.write("Performing feature scaling...")
                    numeric_columns = data.select_dtypes(include=["int", "float"]).columns

                    if len(numeric_columns) == 0:
                        st.write("No numeric columns found.")
                    else:
                        scaler = MinMaxScaler()
                        data_scaled = data.copy()
                        data_scaled[numeric_columns] = scaler.fit_transform(data_scaled[numeric_columns])
                        data = data_scaled  # Update the original dataset with scaled features
                        st.write("Feature scaling performed successfully.")

                    st.write("Downloading the dataset...")

                    # Save the modified dataset to a file
                    modified_dataset_filename = "modified_dataset.csv"
                    # data.to_csv(modified_dataset_filename, index=False)
                    st.write(data.head())
                    st.write(data.shape)
            


                    # Applying the anomaly detection using One-Class SVM
                    data_with_anomalies_OneClassSVM = apply_anomaly_detection_OneClassSVM(data)
                    AnomalyFeature=data_with_anomalies_OneClassSVM[["Anomaly"]]
                    final_data=pd.concat([copy_data,AnomalyFeature],axis=1)

                    st.subheader("Data with Anomalies")
                    st.write(final_data)

                    selected_x_col = st.selectbox("Select X-axis column", data.columns)
                    selected_y_col = st.selectbox("Select Y-axis column", data.columns)

                    # Create a scatter plot using Seaborn
                    plt.figure(figsize=(10, 6))
                    sns.scatterplot(data=data_with_anomalies_OneClassSVM, x=selected_x_col, y=selected_y_col, hue='Anomaly', palette={0: 'blue', 1: 'red'})

                    # Get the current legend
                    current_handles, current_labels = plt.gca().get_legend_handles_labels()

                    # Customize the legend
                    legend_labels = ['Not Anomaly', 'Anomaly']
                    legend_title = 'Anomaly'
                    custom_legend = plt.legend(current_handles, legend_labels, title=legend_title, loc='upper right')

                    # Set colors for the legend
                    for handle, label in zip(custom_legend.legendHandles, legend_labels):
                        if label == 'Not Anomaly':
                            handle.set_color('blue')
                        elif label == 'Anomaly':
                            handle.set_color('red')

                    # Show the Seaborn plot
                    st.pyplot()

                    # Save the Seaborn plot as an image file (optional)
                    # plt.savefig("one_class_svm_plot.png")

                    st.write("Download the data with anomaly indicator")
                    st.download_button(
                        label="Download",
                        data=final_data.to_csv(index=False),
                        file_name="OneClassSVMAnomaly.csv",
                        mime="text/csv"
                    )

                    # Count the number of anomalies
                    num_anomalies = data_with_anomalies_OneClassSVM['Anomaly'].sum()

                    # Total number of data points
                    total_data_points = len(data_with_anomalies_OneClassSVM)

                    # Calculate the percentage of anomalies
                    percentage_anomalies = (num_anomalies / total_data_points) * 100

                    st.write(f"Number of anomalies: {num_anomalies}")
                    st.write(f"Percentage of anomalies: {percentage_anomalies:.2f}%")

        elif selected_anomalyAlgorithm == "One-Class SVM (SGD)":
                st.markdown(
                "<h2 style='font-size: 24px; color: blue;'>Upload Dataset, Empower Machine Learning Algorithms!</h2>",
                unsafe_allow_html=True)
                data_file = st.file_uploader("Upload File", type=["csv", "xlsx", "XLSX"])

                if data_file is not None:
                    file_extension = data_file.name.split(".")[-1]
                    if file_extension == "csv":
                        data = pd.read_csv(data_file)
                    elif file_extension in ["xlsx", "XLSX"]:
                        data = pd.read_excel(data_file)
                    else:
                        st.error("Unsupported file format. Please upload a CSV or Excel file.")






                    st.write("Dealing with missing values:")
                    threshold = 0.1  # Set the threshold to 10% (0.1)
                    missing_percentages = data.isnull().mean()  # Calculate the percentage of missing values in each column
                    columns_to_drop = missing_percentages[missing_percentages > threshold].index  # Get the columns exceeding the threshold
                    data = data.drop(columns=columns_to_drop)  # Drop the columns
                    st.write(f"Features with more than {threshold*100:.2f}% missing values dropped successfully.")



                    data = drop_features_with_missing_values(data)




                    st.write("Dealing with duplicate values...")
                    num_duplicates = data.duplicated().sum()  # Count the number of duplicate rows
                    data_unique = data.drop_duplicates()  # Drop the duplicate rows
                    st.write(f"Number of duplicate rows: {num_duplicates}")
                    st.write("Dealing done with duplicates.")

                    st.write("Performing categorical feature encoding...")
                    copy_data=data.copy()
                    categorical_features = [feature for feature in data_unique.columns if data_unique[feature].dtype == 'object']
                    data_encoded = data_unique.copy()
                    for feature in categorical_features:
                        labels_ordered = data_unique.groupby([feature]).size().sort_values().index
                        labels_ordered = {k: i for i, k in enumerate(labels_ordered, 0)}
                        data_encoded[feature] = data_encoded[feature].map(labels_ordered)
                    data = data_encoded  # Update the original dataset with encoded features
                    st.write("Categorical features encoded successfully.")

                    st.write("Performing feature scaling...")
                    numeric_columns = data.select_dtypes(include=["int", "float"]).columns

                    if len(numeric_columns) == 0:
                        st.write("No numeric columns found.")
                    else:
                        scaler = MinMaxScaler()
                        data_scaled = data.copy()
                        data_scaled[numeric_columns] = scaler.fit_transform(data_scaled[numeric_columns])
                        data = data_scaled  # Update the original dataset with scaled features
                        st.write("Feature scaling performed successfully.")

                    st.write("Downloading the dataset...")

                    # Save the modified dataset to a file
                    modified_dataset_filename = "modified_dataset.csv"
                    # data.to_csv(modified_dataset_filename, index=False)
                    st.write(data.head())
                    st.write(data.shape)


                    # Applying the anomaly detection using SGD-based One-Class SVM
                    data_with_anomalies_SGDOCSVM = apply_anomaly_detection_SGDOCSVM(data)
                    AnomalyFeature=data_with_anomalies_SGDOCSVM[["Anomaly"]]
                    final_data=pd.concat([copy_data,AnomalyFeature],axis=1)

                    st.subheader("Data with Anomalies (SGD-based One-Class SVM)")
                    st.write(final_data)

                    selected_x_col = st.selectbox("Select X-axis column", data.columns)
                    selected_y_col = st.selectbox("Select Y-axis column", data.columns)

                    # Create a scatter plot using Seaborn
                    plt.figure(figsize=(10, 6))
                    sns.scatterplot(data=data_with_anomalies_SGDOCSVM, x=selected_x_col, y=selected_y_col, hue='Anomaly', palette={0: 'blue', 1: 'red'})

                    # Get the current legend
                    current_handles, current_labels = plt.gca().get_legend_handles_labels()

                    # Customize the legend
                    legend_labels = ['Not Anomaly', 'Anomaly']
                    legend_title = 'Anomaly'
                    custom_legend = plt.legend(current_handles, legend_labels, title=legend_title, loc='upper right')

                    # Set colors for the legend
                    for handle, label in zip(custom_legend.legendHandles, legend_labels):
                        if label == 'Not Anomaly':
                            handle.set_color('blue')
                        elif label == 'Anomaly':
                            handle.set_color('red')

                    # Show the Seaborn plot
                    st.pyplot()

                    # Save the Seaborn plot as an image file (optional)
                    # plt.savefig("sgd_one_class_svm_plot.png")

                    st.write("Download the data with anomaly indicator")
                    st.download_button(
                        label="Download",
                        data=final_data.to_csv(index=False),
                        file_name="SGD_OneClassSVM_Anomaly.csv",
                        mime="text/csv"
                    )

                    # Count the number of anomalies
                    num_anomalies = data_with_anomalies_SGDOCSVM['Anomaly'].sum()

                    # Total number of data points
                    total_data_points = len(data_with_anomalies_SGDOCSVM)

                    # Calculate the percentage of anomalies
                    percentage_anomalies = (num_anomalies / total_data_points) * 100

                    st.write(f"Number of anomalies: {num_anomalies}")
                    st.write(f"Percentage of anomalies: {percentage_anomalies:.2f}%")

























        # starting of visualization side bar over here




        st.sidebar.header("Deep Learning Methods")
        anomaly_options = ["None", "Autoencoder"]
        selected_anomalyAlgorithm = st.sidebar.selectbox("Select deep learning algorithms", anomaly_options)

        if selected_anomalyAlgorithm == "None":
            st.write(" ")

        elif selected_anomalyAlgorithm == "Autoencoder":

            st.markdown(
                "<h2 style='font-size: 24px; color: blue;'>Upload Your Dataset, Fuel Deep Learning!</h2>",
                unsafe_allow_html=True)
            data_file = st.file_uploader("Upload File", type=["csv", "xlsx", "XLSX"])

            if data_file is not None:
                file_extension = data_file.name.split(".")[-1]
                if file_extension == "csv":
                    data = pd.read_csv(data_file)
                elif file_extension in ["xlsx", "XLSX"]:
                    data = pd.read_excel(data_file)
                else:
                    st.error("Unsupported file format. Please upload a CSV or Excel file.")






                st.write("Dealing with missing values:")
                threshold = 0.1  # Set the threshold to 10% (0.1)
                missing_percentages = data.isnull().mean()  # Calculate the percentage of missing values in each column
                columns_to_drop = missing_percentages[missing_percentages > threshold].index  # Get the columns exceeding the threshold
                data = data.drop(columns=columns_to_drop)  # Drop the columns
                st.write(f"Features with more than {threshold*100:.2f}% missing values dropped successfully.")



                data = drop_features_with_missing_values(data)




                st.write("Dealing with duplicate values...")
                num_duplicates = data.duplicated().sum()  # Count the number of duplicate rows
                data_unique = data.drop_duplicates()  # Drop the duplicate rows
                st.write(f"Number of duplicate rows: {num_duplicates}")
                st.write("Dealing done with duplicates.")

                st.write("Performing categorical feature encoding...")
                copy_data=data.copy()
                categorical_features = [feature for feature in data_unique.columns if data_unique[feature].dtype == 'object']
                data_encoded = data_unique.copy()
                for feature in categorical_features:
                    labels_ordered = data_unique.groupby([feature]).size().sort_values().index
                    labels_ordered = {k: i for i, k in enumerate(labels_ordered, 0)}
                    data_encoded[feature] = data_encoded[feature].map(labels_ordered)
                data = data_encoded  # Update the original dataset with encoded features
                st.write("Categorical features encoded successfully.")

                st.write("Performing feature scaling...")
                numeric_columns = data.select_dtypes(include=["int", "float"]).columns

                if len(numeric_columns) == 0:
                    st.write("No numeric columns found.")
                else:
                    scaler = MinMaxScaler()
                    data_scaled = data.copy()
                    data_scaled[numeric_columns] = scaler.fit_transform(data_scaled[numeric_columns])
                    data = data_scaled  # Update the original dataset with scaled features
                    st.write("Feature scaling performed successfully.")

                st.write("Downloading the dataset...")

                # Save the modified dataset to a file
                modified_dataset_filename = "modified_dataset.csv"
                # data.to_csv(modified_dataset_filename, index=False)
                st.write(data.head())
                st.write(data.shape)



                # Assuming 'apply_anomaly_detection_autoencoder' function is defined elsewhere
                # and returns a DataFrame with an 'Anomaly' column (0 for non-anomalies, 1 for anomalies)
                data_with_anomalies_Autoencoder = apply_anomaly_detection_autoencoder(data)
                AnomalyFeature=data_with_anomalies_Autoencoder[["Anomaly"]]
                final_data=pd.concat([copy_data,AnomalyFeature],axis=1)

                st.subheader("Data with Anomalies")
                st.write(final_data)

                selected_x_col = st.selectbox("Select X-axis column", data.columns)
                selected_y_col = st.selectbox("Select Y-axis column", data.columns)

                # Create a scatter plot using Seaborn
                plt.figure(figsize=(10, 6))
                sns.scatterplot(data=data_with_anomalies_Autoencoder, x=selected_x_col, y=selected_y_col, hue='Anomaly', palette={0: 'blue', 1: 'red'})

                # Get the current legend
                current_handles, current_labels = plt.gca().get_legend_handles_labels()

                legend_labels = ['Not Anomaly', 'Anomaly']
                legend_title = 'Anomaly'
                custom_legend = plt.legend(current_handles, legend_labels, title=legend_title, loc='upper right')

                # Set colors for the legend
                for handle, label in zip(custom_legend.legendHandles, legend_labels):
                    if label == 'Not Anomaly':
                        handle.set_color('blue')
                    elif label == 'Anomaly':
                        handle.set_color('red')

                # Show the Seaborn plot
                st.pyplot()

                # Save the Seaborn plot as an image file (optional)
                # plt.savefig("scatter_plot.png")

                st.write("Download the data with anomaly indicator")
                st.download_button(
                    label="Download",
                    data=data_with_anomalies_Autoencoder.to_csv(index=False),
                    file_name="final_data.csv",
                    mime="text/csv"
                )

                # Count the number of anomalies
                num_anomalies = data_with_anomalies_Autoencoder['Anomaly'].sum()

                # Total number of data points
                total_data_points = len(data_with_anomalies_Autoencoder)

                # Calculate the percentage of anomalies
                percentage_anomalies = (num_anomalies / total_data_points) * 100

                st.write(f"Number of anomalies: {num_anomalies}")
                st.write(f"Percentage of anomalies: {percentage_anomalies:.2f}%")













                



















                





         
        # Rest of your Streamlit app code...

        # Place the Time Series Analysis selection code at a different location



        # starting of basic information side bar
        #st.sidebar.header("Categorical Statistical method (WIP)")
        #info_options = ["None", "Chi-Square Test", "ANOVA",]
        #selected_info = st.sidebar.selectbox("Choose an EDA type", info_options)

        #if selected_info == "None":
        #    st.write(" ")
        #elif selected_info == "Chi-Square Test":
        #    st.header("Try other technique we are working on Chi-Square Test.......")
        #elif selected_info == "ANOVA":
        #    st.header("Try other technique we are working on ANOVA.......")







        st.sidebar.header("Time Series Analysis (WIP)")

        #st.sidebar.header("Time Series Analysis",: color = 'blue')

        #"<h2 style='font-size: 24px; color: blue;'>Time Series Analysis</h2>",
        info_options_ts = [
            "None",
            "ARIMA",
            "FBPROPHET",
            "HOLT-WINTER",
            # Add more options here...
        ]



        # Prompt the user to select a time series analysis method
        selected_anomalyAlgorithm = st.sidebar.selectbox("Select Time Series algorithms", info_options_ts)

        if selected_anomalyAlgorithm == "None":
            st.write(" ")

        elif selected_anomalyAlgorithm == "ARIMA":
            st.header("Try other technique we are working on ARIMA.......")

        elif selected_anomalyAlgorithm == "FBPROPHET":
            st.header("Try other technique we are working on FBPROPHET.......")

        elif selected_anomalyAlgorithm == "HOLT-WINTER":
            st.header("Try other technique we are working on HOLT-WINTER.......")










if __name__ == "__main__":
    main()





def UI():
    # Add custom HTML and CSS using Bootstrap
    bootstrap_html = """

        <center>

        <h2 style="margin-bottom:100px;">Empowering Your Data: Unleash the Power of Effortless Querying and Precise Conversion!</h2>
        <h3 style="margin-bottom:100px;"><span style="color: #2b86d9;font-weight:800;text-align:center">InfraBot AI</span>:<span style="color:#000;">Inquire about infrared products with InfraBot AI in this chat.</span></h3>
        <h3 style="margin-bottom:100px;"><span style="color: #2b86d9;font-weight:800;text-align:center">Multiple PDF Query</span>:<span style="color:#000;">Effortlessly conduct precise PDF queries with Multiple PDF Query.</span></h3>
        <h3 style="margin-bottom:100px;"><span style="color: #2b86d9;font-weight:800;text-align:center">Whisper Speech to Text</span>:<span style="color:#000;">Whisper Speech to Text: Transform video audio into PDF for easy querying.</span></h3>
        <h3 style="margin-bottom:100px;"><span style="color: #2b86d9;font-weight:800;text-align:center">Streamlined Excel Query</span>:<span style="color:#000;">Streamlined Excel Query: Effortlessly unravel your messy data files.</span></h3>
        </center>

        

        <div class="cards-list">

        <a href="http://18.182.55.167:8080/">
        <div class="card 1">
        <div class="card_image"> <img src="https://static.wixstatic.com/media/a89add_3d73f7e43cff4f37bdf0af4772ef6595~mv2.gif" /> </div>
        <div class="card_title title-dark">
            <p>InfraBotAI</p>
        </div>
        </div>
        </a>

        <a href="https://infrared-2p52zc9tdhxech2i8ok9pf.streamlit.app/PdfQuery">
        <div class="card 2">
        <div class="card_image">
            <img src="https://www.onlineoptimism.com/wp-content/uploads/2023/03/AI-Guidelines-GIF.gif" />
            </div>
        <div class="card_title title-dark">
            <p>Multiple PDF Query</p>
        </div>
        </div>
        </a>
        


        <a href="https://infrared-2p52zc9tdhxech2i8ok9pf.streamlit.app/Whisper">
        <div class="card 2">
        <div class="card_image">
            <img src="https://thumbs.gfycat.com/EvenJaggedEyas-size_restricted.gif" />
            </div>
        <div class="card_title title-dark">
            <p>Whisper- Speech to Text PDF</p>
        </div>
        </div>
        </a>


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
        .css-e3xfei{
        position: relative;
        bottom:174px;
        }
        .eczjsme9{
        visibility:hidden;
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



