# ETL-Project

Police Shootings ETL Project

Instructions: Run the jupyter notebook named Police-Shooting-Analysis.ipynb, which can be found in DF_Cleanup folder.

This project's objective was to Extract, Transform, and Load 2 different data sources related to US Police Shootings. Since there's not one source for this type of data,  this process explores the idea of combining different datasets in an uniform way to load to a database where persistent data about this shootings can live. This exemplifies using 2 sources of data, but it could be extended to include more.


Extract: Data was obtained Kaggle.com 
	- We extracted two .csv files from Kaggle.com related to Police Shootings in the US:	
		1. Police_killings_new.csv		
		2. Datasets_2647_4395_PoliceKillingsUS.csv
	- Given the fact that Kaggle.com does not provide a clean link to their .csv files, our attempt to use pandas to read from url was not successful (df=pd.read_csv(url))
	For example, this is the typical Kaggle way to display their .csv files: https://www.kaggle.com/jpmiller/police-violence-in-the-us?select=police_killings.csv . 
	- We explored other options to obtain the .csv in a more automated way, however given the time for this project we couldn’t get the alternate code ready in time.
	- We proceeded to download both of the .csv files to the local repository and worked from there. 

Transform: This step was performed in Jupyter notebook and then converted to a Python script using the nbconvert application within Anaconda
	- The 2 datasets had differences in the amount of columns, the data types, and the content of each column in rows. This made it challenging and therefore we decided that it needed clean up before it could be loaded to a persistent database.
	- The first step in the transformation was to rename the columns from both datasets the same, then cast mixed data types, such as float and strings and booleans to strings. After that we proceeded to concatenate both datasets and remove duplications based on 3 factors:
		1. Name
		2. City
		3. State
	- Once the duplications were removed, then we proceeded to normalize the rest of the information in each column to have homogenized categories. This presented several challenges, for example Age was expected to be a numeric value, however some rows had "unknown" values instead of numbers. This took some data exploration of each column and respective clean up.
	- We decided to drop columns that added little to no value such as "url to images".
	- Finally we had a clean dataframe that had the right columns with the correct data types ready to be loaded into Postgress SQL database.

Load:
	Using pandas, we created SQLpostgres database using pandas.DataFrame.to_sql. We ran a few query tests, we querried race totals to test our database. Data was successfully queried. 
	

