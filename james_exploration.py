import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

st.title("Fifa 2019 Dataset Analysis")

dataset_pverview = """Below we see the first few rows of the dataset.
					We see the features include player descriptors such as name, age, height,
					weight, and nationality, as well as their skill ratings for several different
					soccer skills. For an explantion of each of the features, check out the
					[Kaggle dataset description](https://www.kaggle.com/karangadiya/fifa19/discussion/133113)"""
st.write(dataset_pverview)

@st.cache(allow_output_mutation=True)  # add caching so we load the data only once
def load_data():
    return pd.read_csv("fifa19.csv", encoding = "UTF-8")

df = load_data()
st.write(df.head())

st.header("Feature Correlation Analysis")
st.write("""Let's explore the relationships between some of the quantitative
	variables in the dataset. Select an independent (x-axis) and a dependent
	(y-axis) variable below and see a scatter plot of these two variables with
	a fitted 5th degree polynomial line, and see their correlation coefficient
	as well. Note that noise has been added to the variables in the plot due to
	the high number of overlapping points in the dataset, but the correlation
	coefficient is calculated using the original data.""")

# Here, we remove the extra text around the wage to get it as an integer
wage_array = df["Value"].to_numpy()
fixed_wages = []
for wage in wage_array:
    if wage[-1]=="M":
        wage = float(wage[1:-1])*1000000
    elif wage[-1]=="K":
        wage = float(wage[1:-1])*1000
    else:
        wage=0
    fixed_wages.append(wage)
df["Player_Wage"] = fixed_wages
df = df[df.Player_Wage!='']
df["Player_Wage"] = df["Player_Wage"].astype(np.int64)*1000

# Now add a column of 'Age' with some noise to make visualizations more clear
#df["Age_Noise"] = df["Age"] + np.random.normal(0,.3,len(df))

correlation_options = ['Age', 'Overall', 'Potential', 'Player_Wage', 'International Reputation', 
				       'Skill Moves', 'Crossing','Finishing', 'HeadingAccuracy', 'ShortPassing',
				       'Volleys', 'Dribbling', 'Curve', 'FKAccuracy', 'LongPassing',
				       'BallControl', 'Acceleration', 'SprintSpeed', 'Agility', 'Reactions',
				       'Balance', 'ShotPower', 'Jumping', 'Stamina', 'Strength', 'LongShots',
				       'Aggression', 'Interceptions', 'Positioning', 'Vision', 'Penalties',
				       'Composure', 'Marking', 'StandingTackle', 'SlidingTackle', 'GKDiving',
				       'GKHandling', 'GKKicking', 'GKPositioning', 'GKReflexes']
df_quant = df[correlation_options]
noise = np.random.normal(0,0.3,df_quant.shape)
df_quant_noise = df_quant + noise
st.write(df_quant_noise.head())

x_var = st.selectbox("Independent Variable", options = correlation_options, index=0)
y_var = st.selectbox("Dependent Variable", options = correlation_options, index=1)

correlation = np.corrcoef(df[x_var],df[y_var])[0][1]
st.write("Correlation: %.2f" % correlation)
chart = alt.Chart(df_quant_noise).mark_circle(color="#000000",size=10,opacity=.3).encode(
    x=alt.X(x_var, scale=alt.Scale(zero=False)),
    y=alt.Y(y_var, scale=alt.Scale(zero=False))#,
    #color=alt.Y("species")
)
chart = chart + chart.transform_regression(x_var,y_var,method="poly",order=5).mark_line(color="#0000FF")
chart = chart.properties(
    width=800, height=500
).interactive()

st.write(chart)
