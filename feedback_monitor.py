import streamlit

streamlit.header('How was your drink? ☕')

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM COFFEE_MENU")
my_data_row = my_cur.fetchone()
streamlit.text("HERE IS OUR COFFEE MENU")
streamlit.text(my_data_row)


