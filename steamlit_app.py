import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# function to create pie chart
def create_pie_chart(df):
    # Count the number of CVEs for each product
    product_counts = df['product'].value_counts()

    # Create the pie chart
    fig, ax = plt.subplots()
    ax.pie(product_counts.values, labels=product_counts.index, autopct='%1.1f%%')
    ax.set_title('CVEs by Product')
    st.pyplot(fig)

# main function for Streamlit app
def main():
    st.title("CVE Analysis App")
    file = st.file_uploader("Upload CSV", type=["csv"])
    if file is not None:
        df = pd.read_csv(file)
        st.write(df.head())

        # Create the pie chart
        create_pie_chart(df)

        # Show recent entry and total number of CVEs
        st.subheader("CVE Analysis Results")
        st.write("Recent Entry: ", df.iloc[-1]['cve_id'])
        st.write("Total Number of CVEs: ", len(df))

if __name__ == "__main__":
    main()
