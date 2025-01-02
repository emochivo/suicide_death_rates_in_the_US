# SUICIDE DEATH RATES IN THE US 

"Suicide Death Rates in the US" was written by Chi Vo and was finished on Jan 1, 2025.

This is my small project aiming to report the suicide death rates in the US based on biological sex or race (or both). The project requires using Python and PostgreSQL. My data (the .csv file) was downloaded from the data catalog of the US government (data.gov). From this project, I learn how to use psycopg2, which is a tool used to establish a connection between Python applications and PostgreSQL databases :)

To run the code, make sure you already installed Python and PostgreSQL before. You can also change the database, user, password, or options from the 'connect()' function (menu_option.py) to match with your current settings. For 'options,' since I named my schema as "suicide_death_rates_us," I assigned it to the search_path field; it should be the schema into which you put the .csv file. 

After that, you can run the main code in your favorite code editor. 
