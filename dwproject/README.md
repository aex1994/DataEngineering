This project:

1. Installs dependencies such as pandas, psql-client CLI, pyscopg2, kaggle api, and python-dotenv
1. Imports data from Kaggle
2. Transforms the data from Kaggle to dimension tables and fact table and save them to CSV format
3. Sets up a PSQL instance using Docker Compose
4. Creates dimension tables and fact table in the PSQL instance
5. Inserts the values from the CSV files to the appropriate tables in the PSQL instance
6. Queries the PSQL instance to verify the accuracy of the data warehouse

Manual Setup Needed:

1. Manually install Docker Desktop (https://www.docker.com/products/docker-desktop/) in your machine and setup WSL2 integration (https://docs.docker.com/desktop/features/wsl/). Make sure Docker Desktop is running for the duration of the script.
2. All contents of the Data Warehousing Project folder should be in a folder in your home directory called "dwproject". The working directory is "~/dwproject".
3. Rename the temp.env file to .env
4. Create a Kaggle account (https://www.kaggle.com/) and generate your API token. The downloaded API token, kaggle.json, should be copied inside this directory "~/.config/kaggle"
5. Run the mainscript.py
