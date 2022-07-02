import streamlit as st
import pandas as pd
import plotly 
import plotly.express as px
     
#@st.cache
def raw_data(input_file, sheetname):
  df=pd.read_excel(open(input_file, 'rb'), sheet_name=sheetname )
  return df

#######################glabal variables

#define functions

##############################
st.set_page_config(layout="wide", initial_sidebar_state="auto")
col11, col12 = st.columns((3,1))
with col11:
  title_1="Survey Data exploration for GP"
  st.markdown(f'<h1 style="text-align: center;color: green;">{title_1}</h1>',unsafe_allow_html=True)
  subj_1="-- CapStone project"
  st.markdown(f'<h2 style="text-align: center;color: green;">{subj_1}</h2>',unsafe_allow_html=True) 
  st.markdown ("Team 5")
  st.markdown("Data are collected from ALM 2022 Capstone class. ")
   
with col12:
  title_11="Hello! I am Henry. Can I help you?"
  st.markdown(f'<h2 style="text-align: center;color: purple;">{title_11}</h2>',unsafe_allow_html=True)
  user_input =''
  user_input = st.text_area("Type your questions here (enter 'contrl+enter' to finish your questions)", value="", max_chars=5000)
  if user_input.lower().find('no question') != -1:
    st.write ("Great! Have a nice day!")
  else:
    if user_input.lower().find('item level plots') != -1:
      st.write ("At this point, only Spokane data are provided.")
    else: 
      if user_input.lower()!='': 
        st.write ("Sorry, I am not sure! Please contact xix294@g.harvard.edu")
         
# read in data: hourly break down
df_ori=raw_data("./data/GP cash needs survey result as of 0208-7-2.xlsx", "survey")
         
# Filters
df_1=df_ori
st.sidebar.markdown("## Define **filters:**")

country_choice = st.sidebar.selectbox('Select the range of order counts:', ['All', 'India','Canada','Brazil', 'USA','China', 'Thailand','Philippines'])
if country_choice != "All":
  df_1=df_1.query("country==@country_choice")
CurrencyOutUS_choice = st.sidebar.radio('Pick up month(s) you are interested:', ['All', 'Yes', 'No'])
if CurrencyOutUS_choice != "All":
  df_1=df_1.query("CurrenciesOutUS==@CurrencyOutUS_choice")
wantUSCurrency_choice = st.sidebar.radio('Pick up month(s) you are interested:', ['All', 'Yes', 'No'])
if wantUSCurrency_choice != "All":
  df_1=df_1.query("wantUSCurrency==@wantUSCurrency_choice")

# figures display
#rt_diff = (df_1["rt_total"].max() - df_1["rt_total"].min()) / 10
#df_1["rt_scale"] = (df_1["rt_total"] - df_1["rt_total"].min()) / rt_diff + 1
#df_1["rt_scale"] = pow(df_1["rt_scale"],2)
with col11:  
  title_ch1='Data Visualizaion'
  st.markdown(f'<h3 style="text-aligh: center;color: green;">{title_ch1}</h3>',unsafe_allow_html=True)
  title_ch2='****2D interactive plots for hourly breakdown********'
  st.markdown(f'<h4 style="text-aligh: center;color: green;">{title_ch2}</h4>',unsafe_allow_html=True)
     
  with st.expander("Animation:    display the net sales across all hours and the relationship with Month"):  
    fig_ani2=px.scatter(df_1, y='Net_Sales', x='Hour', animation_frame='Month', color='Hour', size='Net_Sales', size_max=60)
    fig_ani2.update_layout(transition = {'duration': 100000})
    st.plotly_chart(fig_ani2,  use_container_width=True, height=600)   

  title_ch3='****3D interactive plots for hourly breakdown********'
  st.markdown(f'<h4 style="text-aligh: center;color: green;">{title_ch3}</h4>',unsafe_allow_html=True)
  with st.expander("Check the relationship between Month, hour and net sales in an interactive 3D way"): 
    fig_scatter1=px.scatter_3d(df_1, y='Month', x='Hour', z='Guest_Count', color='Month', size='Guest_Count', size_max=50)
    st.plotly_chart(fig_scatter1,  use_container_width=True, height=3000)

     
#plots for weekday breakdown
with col11:  
  title_ch2='****2D interactive plots for weekday breakdown********'
  st.markdown(f'<h4 style="text-aligh: center;color: green;">{title_ch2}</h4>',unsafe_allow_html=True)
     
  with st.expander("Animation:    display the net sales across all Weekdays and the relationship with Month"):  
    fig_ani22=px.scatter(df_2, y='Net_Sales', x='Weekday', animation_frame='Month', color='Weekday', size='Net_Sales', size_max=60)
    fig_ani22.update_layout(transition = {'duration': 100000})
    st.plotly_chart(fig_ani22,  use_container_width=True, height=600)   

  title_ch3='****3D interactive plots for weekday breakdown********'
  st.markdown(f'<h4 style="text-aligh: center;color: green;">{title_ch3}</h4>',unsafe_allow_html=True)
  with st.expander("Check the relationship between Month, hour and net sales in an interactive 3D way"): 
    fig_scatter11=px.scatter_3d(df_2, y='Weekday', x='Month', z='Guest_Count', color='Weekday', size='Guest_Count', size_max=50)
    st.plotly_chart(fig_scatter11,  use_container_width=True, height=3000)
