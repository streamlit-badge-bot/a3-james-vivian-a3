import streamlit as st
import pandas as pd


@st.cache(allow_output_mutation=True)  # add caching so we load the data only once
def load_data():
    return pd.read_csv("data/fifa19.csv", encoding="UTF-8", index_col=0)


def write():
    st.header("Fifa 2019 Dataset Analysis")

    dataset_overview = """This tool allows users to explore a dataset from the video game "Fifa 19",
                        the 2019 version of the popular soccer video game. Below we see the
                        first few rows of the dataset. We see the features include player descriptors such as name, age, 
                        height, weight, and nationality, as well as their skill ratings for several different
                        soccer skills. For an explanation of each of the features, check out the
                        [Kaggle dataset description](https://www.kaggle.com/karangadiya/fifa19/discussion/133113)"""

    st.write(dataset_overview)

    st.subheader("Preview of the Original Dataset")
    df = load_data()
    st.write(df.head(20))
