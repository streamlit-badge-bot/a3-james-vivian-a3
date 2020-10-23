# Exploring Football Players in FIFA 19

![A screenshot of your application. Could be a GIF.](screenshot.png)


Association football (soccer) is undeniably the most popular sport in the world. In this project, we create interactive 
visualizations that enable users to explore a dataset of players from <i>FIFA 19</i>, a football simulation video game. By 
interacting with our visualizations, users can learn about the attributes that make up a valuable football player, the 
correlations between player attributes (e.g. sport-specific skills, general measures of athletic ability, etc.), and how
players from different countries around the world compare. More detail on these, along with specific sample questions, 
are provided in the Project Goals section below.

## Project Goals

TODO: **A clear description of the goals of your project.** Describe the question that you are enabling a user to answer. The question should be compelling and the solution should be focused on helping users achieve their goals. 

## Design

### Player World Map

<b>How to Interact</b>

Users can select how many markings for the top N countries are shown on the world map, where the player statistic, aggregate function, and order for determining top countries can be configured by interacting with dropdowns on the sidebar. An example configuration might be to show the top 50 countries (player nationalities) based on their average player overall ratings in descending order (highest to lowest). 

When users hover over a country marking on the map, the marking changes from a small green circle to a larger red circle and a tooltip appears next to their cursor that displays the country’s name and additional aggregate player stats that can be selected in the sidebar. Examples of player stats include Age, Overall Rating (0-100, Potential Rating (0-100), and Value. The available aggregate functions to use are mean, min, and max. 

Users can choose to zoom into a specific continent by selecting its name in the dropdown above the world map. This is useful in cases where countries are very small and packed together. For example, Europe is the smallest continent but is also composed of many small countries that produce many top football players. When they select Europe in the dropdown, they zoom into Europe and see which regions produce players that satisfy a specific attribute (e.g. highest Overall Rating or Wage/Week (€))

<b>Design Process and Rationale</b>

Some of our initial exploration questions involved comparisons among players of different nationalities. As a result, we chose to create an interactive world map to allow users to learn about how different countries compare based on different aggregate player statistics.

The design of this interactive map was inspired and created by blending elements from examples on the Altair documentation site, specifically the [World Map](https://altair-viz.github.io/gallery/world_map.html) and the [Locations of US Airports map](https://altair-viz.github.io/gallery/airports.html), which showed tooltips for the airport name, city, and state for airports in the US.

Initially, we chose to show a spherical globe (orthographic) for the world map, but later decided that the equirectangular map would allow users to see all of the countries at once and compare them side-by-side. 

Our initial implementation had marks that changed from small black circles to larger black circles when they were hovered over. However, many small black circles in close proximity produced a cluttered look when showing markings for all of the countries in the dataset. Using the same color on hover also made it difficult to see exactly where the user’s cursor was hovering over on the map. We changed these to small green circles and larger red circles (on hover), respectively. The green is slightly darker than the green used to color in the countries on the map; this allows users to see the small circles marking the different countries but prevents them from becoming too distracting. The large red circle stands out in large contrast against the green on the map, allowing users to clearly see which country they were hovering over.

Lastly, we moved the multiselect dropdown for specifying which player stats to show, the checkboxes for selecting which aggregate functions to use, and the dropdowns to configure how to determine the Top N Countries to the sidebar so they would not take up too much room or be visually overwhelming to the user on the main portion of the screen. This also allows their focus to stay on the world map.


## Development

### Player World Map

To create the interactive Player World Map we used the original FIFA 19 players dataset from Kaggle and a Countries dataset containing geographic information on countries around the world from Google’s Dataset Publishing Language repository. We found that we needed the Countries dataset to plot the data points on the world map since the original dataset did not contain latitude and longitude information for the countries of player’s nationalities.

We needed to do some data cleaning to merge the 2 datasets. The Countries dataset was initially missing 26 countries from the Nationality column in the FIFA 19 dataset. On closer inspection, all but 1 of these discrepancies were due to differences in naming convention (e.g. specifying the individual countries England, Scotland, Wales, and Northern Ireland instead of listing them as United Kingdom or using different symbols and abbreviations). We created a new column in the FIFA 19 dataset ‘Player Nationality’ that was a copy of the ‘Nationality’ column, except it used the Countries dataset naming convention. The only Nationality that we did not have geographic information for was Curaçao; we found its geographic coordinates on Google and added it to the dataset manually.


### Additional Info

<b>Estimated Time Spent Developing App</b>
40 hours

<b>Aspects that took the most time:</b>
* Figuring out how to use Altair and Streamlit
* Finding and integrating the GPS coordinate information for the different countries (data cleaning to get the naming conventions used in both datasets to match)
* Adding the zoom feature that allows users to zoom into a specific continent on the map since Altair’s maps currently do not support the .interactive() function

<b>Division of Work:</b>

We divided our work by taking on different interactive visualizations and meeting regularly to consult each other for feedback and new ideas.

* Correlation Plots and Machine Learning Tool (James)
* Player World Map (Vivian)
