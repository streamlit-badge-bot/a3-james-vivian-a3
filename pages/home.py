import streamlit as st
import pandas as pd


@st.cache(allow_output_mutation=True)  # add caching so we load the data only once
def load_data():
    fifa = pd.read_csv("data/fifa19.csv", encoding="UTF-8", index_col=0)
    countries = pd.read_csv("data/countries.csv", encoding="UTF-8")
    return fifa, countries


def write():
    st.header("Overview of the Data")

    fifa, countries = load_data()

    fifa_overview = """This tool allows users to explore a dataset from the video game "FIFA 19",
                        the 2019 version of the popular soccer video game. Below we see the
                        first few rows of the dataset. We see the features include player descriptors such as name, age, 
                        height, weight, and nationality, as well as their skill ratings for several different
                        soccer skills. For an explanation of each of the features, check out the
                        [Kaggle dataset description](https://www.kaggle.com/karangadiya/fifa19/discussion/133113)"""
    st.write(fifa_overview)

    gps_overview = """Since the FIFA 19 dataset did not provide geographic information on the countries listed in the
                      Nationality column, we used a second dataset to collect the GPS coordinates (latitude and 
                      longitude) for those countries. This information was used to generate our Player World Map."""
    st.write(gps_overview)

    st.subheader("Preview of the FIFA 19 Dataset")
    st.write("[source link](https://www.kaggle.com/karangadiya/fifa19)")
    st.write(fifa.head(20))

    st.subheader("Preview of the Countries Dataset")
    st.write("[source link](https://github.com/google/dspl/blob/master/samples/google/canonical/countries.csv)")
    st.write(countries.head(20))
