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
df_ori=raw_data("./data/GP_cash_needs_survey_result_as_of_0208-7-2.xlsx", "Quick 1-minute Survey about you")
         
# Filters
df_1=df_ori
st.sidebar.markdown("## Define **filters:**")

country_choice = st.sidebar.selectbox('Select the country:', ['All', 'India','Canada','Brazil', 'USA','China', 'Thailand','Philippines'])
if country_choice != "All":
  df_1=df_1.query("Country==@country_choice")
CurrencyOutUS_choice = st.sidebar.radio('Pick up category about whether having non-US currencies: ', ['All', 'Yes', 'No'])
if CurrencyOutUS_choice != "All":
  df_1=df_1.query("CurrenciesOutUS==@CurrencyOutUS_choice")
wantUSCurrency_choice = st.sidebar.radio('Pick up category about whether you want US currency: ', ['All', 'Yes', 'No', 'NA'])
if wantUSCurrency_choice != "All":
  df_1=df_1.query("wantUSCurrency==@wantUSCurrency_choice")

# figures display
with col11:  
  title_ch1='Data Visualizaion'
  st.markdown(f'<h3 style="text-aligh: center;color: green;">{title_ch1}</h3>',unsafe_allow_html=True)
  title_ch2='****2D interactive plots********'
  st.markdown(f'<h4 style="text-aligh: center;color: green;">{title_ch2}</h4>',unsafe_allow_html=True)

  with st.expander("Pie Charts:    check global asset currency under country"):    
    fig_3=px.sunburst(df_1, color='wantUSCurrency', path=['CurrenciesOutUS','wantUSCurrency', 'Country'], labels=['CurrenciesOutUS','wantUSCurrency', 'Country'])
    st.plotly_chart(fig_3,   use_container_width=True, height=600)
  with st.expander("Tree Map:    check global asset currency under country"):    
    fig_tree=px.treemap(df_1, color='wantUSCurrency', path=['CurrenciesOutUS','wantUSCurrency', 'Country'])
    st.plotly_chart(fig_tree, use_container_width=True, height=600)    
  title_ch3='****3D interactive plots********'
  st.markdown(f'<h4 style="text-aligh: center;color: green;">{title_ch3}</h4>',unsafe_allow_html=True)
  with st.expander("Check the relationship between CurrenciesOutUS, wantUSCurrency, and Country"): 
    fig_scatter1=px.scatter_3d(df_1, y='CurrenciesOutUS', x='wantUSCurrency', z='Country', color='wantUSCurrency')
    st.plotly_chart(fig_scatter1,  use_container_width=True, height=3000)


