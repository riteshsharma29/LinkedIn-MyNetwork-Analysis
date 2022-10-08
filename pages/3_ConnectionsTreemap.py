import streamlit as st
import plotly.express as px
import pandas as pd
import os

st.set_page_config(page_title="Treemap of Company MyConnections Work@")

st.sidebar.success("<Treemap> #  displays hierarchical data as a set of nested rectangles. Each group is represented by a rectangle, where area is proportional to its value.")

connections_df = pd.read_csv(os.path.join(os.getcwd(),"pages/Connections.csv"))
company_groupby = connections_df.groupby(by='Company').count().reset_index().sort_values(by='First Name', ascending=False).reset_index(drop=True)

fig3 = px.treemap(company_groupby[:200], path=['Company', 'Position'],
          values='First Name',
          labels={'First Name': 'Number'})

st.plotly_chart(fig3)

