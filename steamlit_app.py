import streamlit as st
import pandas as pd
import altair as alt

@st.cache
def load_data(file):
    df = pd.read_csv(file)
    return df

def create_chart(df, column_name):
    value_counts = df[column_name].value_counts()
    most_common_value = value_counts.index[0]
    chart_df = pd.DataFrame({column_name: [most_common_value, "Other"],
                              "count": [value_counts[most_common_value], 
                                        len(df) - value_counts[most_common_value]]})
    chart = alt.Chart(chart_df).mark_bar().encode(
        x=column_name,
        y='count',
        color=column_name
    ).properties(
        width=500,
        height=300
    ).transform_joinaggregate(
        total='sum(count)',
    ).transform_calculate(
        percentage="datum.count / datum.total"
    ).mark_bar().encode(
        tooltip=['count', alt.Tooltip('percentage', format='.2%')]
    ).properties(
        title=f"Most Common Value in {column_name}"
    ).mark_text(
        align='center',
        baseline='middle',
        dx=0,
        dy=5,
        font={'size': 14}
    ).encode(
        text=alt.condition(
            alt.datum.count > 0,
            alt.datum[column_name],
            alt.value(' ')
        )
    )
    return chart

def main():
    st.title("Upload CSV File")
    file = st.file_uploader("Choose a CSV file")
    if file:
        df = load_data(file)
        st.write(df)
        column_name = st.selectbox("Select a column", df.columns)
        chart = create_chart(df, column_name)
        st.altair_chart(chart, use_container_width=True)

if __name__ == '__main__':
    main()
