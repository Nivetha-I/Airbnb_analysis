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
    select= option_menu("Main Menu", ["Home", "Data Exploration"])
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
if select == "Data Exploration":
    tab1, tab2, tab3, tab4= st.tabs(["***PRICE BASED ANALYSIS***","***AVAILABILITY BASED ANALYSIS***","***LOCATION BASED ANALYSIS***", "***GEOLOGICAL VISUALIZATION***"])
    with tab1:
        st.title("**PRICE DIFFERENCE**")
        col1,col2= st.columns(2)

        with col1:
            
            
            country= st.selectbox("Select the Country",df["country"].unique())

            df1= df[df["country"] == country]
            df1.reset_index(drop= True, inplace= True)

            room_ty= st.selectbox("Select the Room Type",df1["room_type"].unique())
            
            df2= df1[df1["room_type"] == room_ty]
            df2.reset_index(drop= True, inplace= True)

            df_bar= pd.DataFrame(df2.groupby("property_type")[["price","number_of_reviews"]].sum())
            df_bar.reset_index(inplace= True)

            fig_bar= px.bar(df_bar, x='property_type', y= "price", title= "PRICE FOR PROPERTY TYPES",hover_data=["number_of_reviews"],color_discrete_sequence=px.colors.sequential.Redor_r, width=600, height=500)
            st.plotly_chart(fig_bar)

        
        
    with tab2:

        def datafr():
            df_a= pd.read_csv("C:/Users/admin/Desktop/Airbnb_Analysis_project/Airbnb_analysis.csv")
            return df_a

        df_a= datafr()

        st.title("**AVAILABILITY ANALYSIS**")
        col1,col2= st.columns(2)

        with col1:
            
            
            country_a= st.selectbox("Select the Country_a",df_a["country"].unique())

            df1_a= df[df["country"] == country_a]
            df1_a.reset_index(drop= True, inplace= True)

            property_ty_a= st.selectbox("Select the Property Type",df1_a["property_type"].unique())
            
            df2_a= df1_a[df1_a["property_type"] == property_ty_a]
            df2_a.reset_index(drop= True, inplace= True)

            df_a_sunb_30= px.sunburst(df2_a, path=["room_type"], values="availability_365",width=600,height=500,title="Availability_365",color_discrete_sequence=px.colors.sequential.Peach_r)
            st.plotly_chart(df_a_sunb_30)
        
        

    with tab3:

        st.title("LOCATION ANALYSIS")
        st.write("")

        def datafr():
            df= pd.read_csv("C:/Users/admin/Desktop/Airbnb_Analysis_project/Airbnb_analysis.csv")
            return df

        df_l= datafr()

        country_l= st.selectbox("Select the Country_l",df_l["country"].unique())

        df1_l= df_l[df_l["country"] == country_l]
        df1_l.reset_index(drop= True, inplace= True)

        proper_ty_l= st.selectbox("Select the Property type",df1_l["property_type"].unique())

        df2_l= df1_l[df1_l["property_type"] == proper_ty_l]
        df2_l.reset_index(drop= True, inplace= True)

        st.write("")

        def select_the_df(sel_val):
            if sel_val == str(df2_l['price'].min())+' '+str('to')+' '+str(differ_max_min*0.30 + df2_l['price'].min())+' '+str("(30% of the Value)"):

                df_val_30= df2_l[df2_l["price"] <= differ_max_min*0.30 + df2_l['price'].min()]
                df_val_30.reset_index(drop= True, inplace= True)
                return df_val_30

            elif sel_val == str(differ_max_min*0.30 + df2_l['price'].min())+' '+str('to')+' '+str(differ_max_min*0.60 + df2_l['price'].min())+' '+str("(30% to 60% of the Value)"):
            
                df_val_60= df2_l[df2_l["price"] >= differ_max_min*0.30 + df2_l['price'].min()]
                df_val_60_1= df_val_60[df_val_60["price"] <= differ_max_min*0.60 + df2_l['price'].min()]
                df_val_60_1.reset_index(drop= True, inplace= True)
                return df_val_60_1
            
            elif sel_val == str(differ_max_min*0.60 + df2_l['price'].min())+' '+str('to')+' '+str(df2_l['price'].max())+' '+str("(60% to 100% of the Value)"):

                df_val_100= df2_l[df2_l["price"] >= differ_max_min*0.60 + df2_l['price'].min()]
                df_val_100.reset_index(drop= True, inplace= True)
                return df_val_100
            
        differ_max_min= df2_l['price'].max()-df2_l['price'].min()

        val_sel= st.radio("Select the Price Range",[str(df2_l['price'].min())+' '+str('to')+' '+str(differ_max_min*0.30 + df2_l['price'].min())+' '+str("(30% of the Value)"),
                                                    
                                                    str(differ_max_min*0.30 + df2_l['price'].min())+' '+str('to')+' '+str(differ_max_min*0.60 + df2_l['price'].min())+' '+str("(30% to 60% of the Value)"),

                                                    str(differ_max_min*0.60 + df2_l['price'].min())+' '+str('to')+' '+str(df2_l['price'].max())+' '+str("(60% to 100% of the Value)")])
                                          
        df_val_sel= select_the_df(val_sel)

        st.dataframe(df_val_sel)

        
    with tab4:

        st.title("GEOLOGICAL VISUALIZATION")
        st.write("")

        fig_4 = px.scatter_mapbox(df, lat='latitude', lon='longitude', color='price', size='number_of_reviews',
                        color_continuous_scale= "rainbow",hover_name='name',range_color=(0,49000), mapbox_style="carto-positron",
                        zoom=1)
        fig_4.update_layout(width=1150,height=800,title='Geospatial Distribution of Listings')
        st.plotly_chart(fig_4)   


    