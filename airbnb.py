import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
pd.set_option('display.max_columns', None)
import plotly.express as px
import warnings
warnings.filterwarnings("ignore")
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

# Streamlit part

st.set_page_config(layout= "wide")
st.title(" :red[AIRBNB DATA ANALYSIS]")
st.write("")


def datafr():
    df= pd.read_csv("C:/Users/admin/Desktop/Airbnb_Analysis_project/Airbnb_analysis.csv")
    return df

df= datafr()

with st.sidebar:
    select= option_menu("Main Menu", ["Home", "Data Exploration", "About"])
    logoimage = Image.open("C:/Users/admin/Desktop/Airbnb_Analysis_project/airbnblogo_new.jpg")
    st.image(logoimage)

if select == "Home":

    image1= Image.open("C:/Users/admin/Desktop/Airbnb_Analysis_project/airbnblogo_with_house.jpg")
    st.image(image1)
    st.write("")
    st.write('''***Airbnb, Inc. is an American San Francisco-based company operating an online marketplace for short- and long-term homestays and experiences.
                The company acts as a broker and charges a commission from each booking.
                The company was founded in 2008 by Brian Chesky, Nathan Blecharczyk, and Joe Gebbia. Airbnb is a shortened version of its original name, AirBedandBreakfast.com.
                Airbnb is the most well-known company for short-term housing rentals.
                  Unique stays, Experiences, Adventures, and more.
                  24/7 support***''')
    