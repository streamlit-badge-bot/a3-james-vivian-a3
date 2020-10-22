import pandas as pd
import streamlit as st
import altair as alt
from vega_datasets import data


@st.cache(allow_output_mutation=True)  # add caching so we load the data only once
def load_data(csv_filepath):
    return pd.read_csv(csv_filepath, index_col=0)


@st.cache(allow_output_mutation=True)
def load_player_stats():
    dictionary = {
        'Age': 'Age',
        'Height (in)': 'Height',
        'Weight (lb)': 'Weight',
        'Overall Rating (0-100)': 'Overall',
        'Potential Rating (0-100)': 'Potential',
        'International Reputation (1-5)': 'International Reputation',
        'Wage (€/week)': 'Wage',
        'Value (€)': 'Value',
        'Release Clause Value (€)': 'Release Clause'
    }
    labels = []
    columns = []
    for label, column in dictionary.items():
        labels.append(label)
        columns.append(column)

    return dictionary, labels, columns


def write():
    st.header("FIFA Players Across the World")
    st.write("""Let's explore the distribution of footballers around the world.
                Hover over the map to see player stats for different countries
                grouped by player nationality.""")

    # Load in the data
    fifa_country_agg = load_data('data/clean_fifa_country_aggs.csv')

    # Add sliders and checkboxes for users to configure visualization
    player_stats_dict, player_stats_labels, player_stats_columns = load_player_stats()
    agg_functions = ['Mean', 'Min', 'Max']

    # Show results for top N countries
    num_countries = fifa_country_agg.shape[0]
    st.markdown('### Show Top N Countries')
    top_countries_count = st.slider('N', 0, num_countries, 50)

    # Select which player stats to show
    st.sidebar.markdown('### Show Player Stats')
    show_player_stats = st.sidebar.multiselect('Show in Tooltip', options=player_stats_labels, default=['Age',
                                                                                         'Overall Rating (0-100)',
                                                                                         'Potential Rating (0-100)'])

    # Select which aggregate functions to include
    st.sidebar.markdown('### Show Aggregate Functions')
    agg_functions_checkbox = {}
    for a in agg_functions:
        agg_functions_checkbox[a] = st.sidebar.checkbox(a, value=a in ['Mean'])

    # Select how to determine top N countries
    st.sidebar.markdown('### Top N Countries Based On')
    top_countries_attr = st.sidebar.selectbox('Player Stat', options=player_stats_labels, index=3)
    top_countries_agg = st.sidebar.selectbox('Using', options=agg_functions)
    top_countries_order = st.sidebar.selectbox('Order', options=['Ascending', 'Descending'], index=1)

    # Draw the world map of FIFA 19 player nationalities
    # source: https://altair-viz.github.io/gallery/index.html#maps

    # Data to show based on user selections
    show_df = fifa_country_agg.sort_values(by='%s_%s' % (player_stats_dict.get(top_countries_attr),
                                                         top_countries_agg.lower()),
                                           ascending=top_countries_order == 'Ascending').head(top_countries_count)

    # Data generators for the background
    sphere = alt.sphere()
    graticule = alt.graticule()

    # Source of land data
    source = alt.topo_feature(data.world_110m.url, 'countries')

    # Layering and configuring the components
    background = alt.layer(
        alt.Chart(sphere).mark_geoshape(fill='lightblue'),
        alt.Chart(graticule).mark_geoshape(stroke='white', strokeWidth=0.2),
        alt.Chart(source).mark_geoshape(fill='#9eb5a8', stroke='black')
    ).project(
        type='equirectangular',

    ).properties(width=800, height=400).configure_view(stroke=None)

    hover = alt.selection(type='single', on='mouseover', nearest=True, fields=['Latitude', 'Longitude'])

    # Get fields to show in tooltip
    tooltip_info = ['Nationality Country']
    for player_stat_label in show_player_stats:
        player_stat_column = player_stats_dict.get(player_stat_label)
        for agg_function, function_checked in agg_functions_checkbox.items():
            if function_checked:
                tooltip_info.append("%s_%s" % (player_stat_column, agg_function.lower()))

    base = alt.Chart(show_df).encode(
        longitude='Longitude:Q',
        latitude='Latitude:Q',
        tooltip=tooltip_info
    )

    points = base.mark_point().encode(
        color=alt.condition(~hover, alt.value('#014600'), alt.value('red')),
        size=alt.condition(~hover, alt.value(30), alt.value(100))
    ).add_selection(hover)

    st.write(background + points)

    st.subheader("Data Shown on Map")
    st.write(show_df)

