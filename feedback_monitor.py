import streamlit

streamlit.header('How was your drink? ☕')

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM COFFEE_MENU")
my_data_row = my_cur.fetchall()
streamlit.text("HERE IS OUR COFFEE MENU")
streamlit.dataframe(my_data_row)


