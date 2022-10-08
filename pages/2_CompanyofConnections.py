import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Company Connections Work@")

st.sidebar.success("<Connected On> indicates Which organizations do the people in my network work at. Visualization is represented with Plotly Bar chart.")

connections_df = pd.read_csv("Connections.csv")
company_groupby = connections_df.groupby(by='Company').count().reset_index().sort_values(by='First Name', ascending=False).reset_index(drop=True)

fig = px.bar(company_groupby[:100],
      x='First Name',
      y='Company',
      labels={'First Name': 'Number'})

st.plotly_chart(fig)

