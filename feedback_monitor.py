import streamlit

streamlit.header('How was your drink? ☕')

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM COFFEE_MENU")
my_data_row = my_cur.fetchall()
streamlit.text("HERE IS OUR COFFEE MENU")
streamlit.dataframe(my_data_row)

import pandas as pd

# Use read_sql_query to execute the query and create a DataFrame
my_coffee_list = pd.read_sql_query("SELECT Item FROM COFFEE_MENU", my_cur)

# Set the index of the DataFrame to the "Item" column
my_coffee_list = my_coffee_list.set_index('Item')

# Let's put a pick list here so they can pick the item they want to include 
item_selected = streamlit.selectbox("Pick your item:", list(my_coffee_list.index))

# Get the row of the selected item from the DataFrame
item_to_show = my_coffee_list.loc[item_selected]
