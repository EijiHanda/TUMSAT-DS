import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="Demand Forecasting", page_icon=":chart_with_upwards_trend:", layout="wide")

@st.cache
def load_data(file):
    data = pd.read_csv(file)
    return data

def main():
    st.title("Demand Forecasting")
    file = st.file_uploader("Upload your data file", type=["csv"])
    if file is not None:
        data = load_data(file)
        st.dataframe(data.head())
        model = LinearRegression()
        model.fit(data[['x1', 'x2', 'x3']], data['y'])
        st.write("Model intercept: ", model.intercept_)
        st.write("Model coefficient: ", model.coef_)

if __name__=="__main__":
    main()
