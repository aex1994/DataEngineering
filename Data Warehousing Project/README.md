This project:

1. Installs dependencies such as pandas, psql-client CLI, pyscopg2, kaggle api, and python-dotenv
1. Imports data from Kaggle
2. Transforms the data from Kaggle to dimension tables and fact table and save them to CSV format
3. Sets up a PSQL instance using Docker Compose
4. Creates dimension tables and fact table in the PSQL instance
5. Inserts the values from the CSV files to the appropriate tables in the PSQL instance
6. Queries the PSQL instance to verify the accuracy of the data warehouse

Manual Setup Needed:

1. Manually install docker desktop in your machine and setup WSL2 integration
2. All content of the Data Warehosing Project Folder should be in a folder in your home directory, called "dwproject" (~/dwproject)
3. Rename the temp.env file to .env
4. Run the mainscript.py
