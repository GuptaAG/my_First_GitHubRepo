import streamlit
import pandas
import snowflake.connector

streamlit.title('Good, Mornig dear 🥗 🐔 🥑🍞')
streamlit.header('Ready Fast for BreakFast !!')
streamlit.text('Manue')
streamlit.text('South Indian')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Honeydew','Orange'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page.
streamlit.dataframe(fruits_to_show)

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected1=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Mango'])
fruits_to_show1 = my_fruit_list.loc[fruits_selected1]
# Display the table on the page.
streamlit.dataframe(fruits_to_show1)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("My Fruit List Contains:")
streamlit.dataframe(my_data_rows)
