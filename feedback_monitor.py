import streamlit

streamlit.header('How was your drink? ☕')

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM COFFEE_MENU")
my_data_row = my_cur.fetchall()
streamlit.text("HERE IS OUR COFFEE MENU")
streamlit.dataframe(my_data_row)

import pandas

my_coffee_list = my_cur.execute("SELECT Item FROM COFFEE_MENU")
my_coffee_list = my_coffee_list.set_index('Coffee')

# Let's put a pick list here so they can pick the fruit they want to include 
Item_selected = streamlit.selectbox("Pick your item:", list(my_coffee_list.index))

Items_to_show = my_coffee_list.loc[fruits_selected]
