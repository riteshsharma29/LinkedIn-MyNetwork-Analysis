import streamlit as st
import plotly.express as px
import pandas as pd
import os

st.set_page_config(page_title="Top Common Positions in my Network")

st.sidebar.success("Top Common Positions of the people in my Network.Majority being Software Engineers.")

connections_df = pd.read_csv(os.path.join(os.getcwd(),"pages/Connections.csv"))

# lower the words because people tend to write the same titles with different cases
connections_df['Position'] = connections_df['Position'].str.title()

# Extract the position with frequency greater than 0.5%
# connections_df['Position'].value_counts()[connections_df['Position'].str.lower().value_counts()/len(connections_df) * 100 > 0.5]

fig6 = px.bar(connections_df.groupby(by='Position').count().sort_values(by='First Name', ascending=False)[:10].reset_index(),
       x='Position',
       y='First Name',
       labels={'First Name': 'Number'},
        title= 'Positions in my LinkedIn Network'
      )

st.plotly_chart(fig6)
