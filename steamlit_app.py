import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# function to display frequency distribution chart
def show_frequency_distribution(df, column_name):
    sns.histplot(data=df, x=column_name)
    st.pyplot()

# function to display most common values chart
def show_most_common_values(df, column_name):
    value_counts = df[column_name].value_counts()
    st.bar_chart(value_counts)

# main function for Streamlit app
def main():
    st.title("CSV Visualization App")
    file = st.file_uploader("Upload CSV", type=["csv"])
    if file is not None:
        df = pd.read_csv(file)
        st.write(df.head())

        # let the user select the type of visualization
        chart_type = st.selectbox("Select chart type:", ["Frequency Distribution", "Most Common Values"])
        column_name = st.selectbox("Select column to visualize:", df.columns)

        if chart_type == "Frequency Distribution":
            show_frequency_distribution(df, column_name)
        elif chart_type == "Most Common Values":
            show_most_common_values(df, column_name)

if __name__ == "__main__":
    main()
