from importdata import importdata
from psqldocker import psqldocker_up, psqldocker_down
from mydependencies import install_pandas, install_kaggle_api, install_pyscopg2, install_psql_cli
from psqlconnect import psql_conn, psql_close, create_tables, insert_datedimtable, insert_statedimtable, insert_sellerdimtable, \
    insert_vehicledimtable, insert_salesfacttable, sql_verify_queries
import os

def main():
    print('Installing dependencies')
    install_pandas()
    install_kaggle_api()
    install_pyscopg2()
    install_psql_cli()

    print('Importing data from Kaggle')
    importdata()
    
    print('Performing transformation on the Kaggle dataset')
    import transform

    print('Starting the PSQL instance in Docker')
    psqldocker_up()
    
    print('Connecting to the PSQL instance via psycopg2')
    conn = psql_conn()
    
    print('Creating dimension tables and fact table')
    create_tables(conn)
    
    print('Inserting values from the csv files to the database tables')
    insert_datedimtable()
    insert_statedimtable()
    insert_sellerdimtable()
    insert_vehicledimtable()
    insert_salesfacttable()
    
    print('Querying the database')
    input('Press any key to run the queries: ')
    sql_verify_queries()
    
    
    # Get a user input to proceed to closing the connection and stopping the db instance
    input('Press any key to close the connection and stop the PSQL instance: ')
    
    print('Is PGPASSWORD still in environment vairables?', end=' ')
    print('PGPASSWORD' in os.environ)
    print('Clearing environment variables')
    del os.environ['PGPASSWORD']
    print('Is PGPASSWORD still in environment vairables?', end=' ')
    print('PGPASSWORD' in os.environ) 
    
    print('Closing the connection to the PSQL instance')
    psql_close(conn)
    
    print('Stopping the PSQL instance in Docker')
    psqldocker_down()
    
if __name__ == '__main__':
    main()