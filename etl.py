import streamlit as st
import pandas as pd
data={
    'Task':['Extract','Transfer','Load'],
    'Status':['Completed','InProgress','Pending']
}
df=pd.DataFrame(data)
st.write('ETL Pipeline execution status',df)