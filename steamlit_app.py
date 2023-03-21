import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data():
    file = st.file_uploader("Upload CSV file", type=["csv"])
    if file is not None:
        data = pd.read_csv(file)
        return data
def display_bar_chart(df, x, y):
    fig, ax = plt.subplots()
    sns.barplot(x=x, y=y, data=df)
    st.pyplot(fig)
def show_dashboard(data):
    st.title("CSV Dashboard")

    if data is not None:
        # display basic info about the data
        st.write("Shape of the data:", data.shape)
        st.write("Columns:", data.columns)

        # display data table
        st.write("Data Table")
        st.write(data)

        # display visualization options
        st.sidebar.title("Visualization Options")
        chart_type = st.sidebar.selectbox("Select Chart Type", ["Bar Chart"])
        x_column = st.sidebar.selectbox("Select X Axis", data.columns)
        y_column = st.sidebar.selectbox("Select Y Axis", data.columns)

        # display visualization
        if chart_type == "Bar Chart":
            display_bar_chart(data, x_column, y_column)
def main():
    data = load_data()
    show_dashboard(data)
if __name__ == "__main__":
    main()
