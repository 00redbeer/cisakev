
import streamlit as st
import pandas as pd

@st.cache
def load_data(file):
    df = pd.read_csv(file)
    return df

def main():
    st.title("Upload CSV File")
    file = st.file_uploader("Choose a CSV file")
    if file:
        df = load_data(file)
        st.write(df)

if __name__ == '__main__':
    main()
