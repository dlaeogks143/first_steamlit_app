import streamlit
import pandas

streamlit.header('How was your drink? ☕')

coffee_menu = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
coffee_menu = coffee_menu.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
coffee_selected = streamlit.selectbox("Pick some fruits:", list(coffee_menu.index))

fruits_to_show = coffee_menu.loc[coffee_selected]


