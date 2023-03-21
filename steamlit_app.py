import streamlit as st
import pandas as pd
import altair as alt

@st.cache
def load_data(file):
    df = pd.read_csv(file)
    return df

def create_chart(df):
    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X('column_name', type='nominal'),
        y='count()'
    )
    return chart

def main():
    st.title("Upload CSV File")
    file = st.file_uploader("Choose a CSV file")
    if file:
        df = load_data(file)
        st.write(df)
        chart = create_chart(df)
        st.altair_chart(chart, use_container_width=True)

if __name__ == '__main__':
    main()
