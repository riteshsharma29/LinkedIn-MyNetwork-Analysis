import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="MyConnections")

st.sidebar.success("<Connected On> indicates the date I connected to that person. Visualization is represented with Plotly Line chart.")

connections_df = pd.read_csv("Connections.csv")
connections_df ["Connected On"] = pd.to_datetime(connections_df ["Connected On"])
connections_line = px.line(connections_df.groupby(by='Connected On').count().reset_index(),
                           x="Connected On",
                           y="First Name",
                           labels={'First Name': 'Number'},
                           title='My Connections')

st.plotly_chart(connections_line)

