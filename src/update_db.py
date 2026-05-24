import sqlite3
import pandas as pd

def update_db(pandas_df, connection):
    """ Upload pandas dataframe to sql database, skip duplicates
    """
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM Weather WHERE dt = ?", (pandas_df.index[0],))
    exists = cursor.fetchone()[0]
    
    if exists == 0:
        pandas_df.to_sql('Weather', connection, if_exists='append', index=True)
        print("Uploaded to database!")
    else:
        print("Duplicate entry skipped!")

if __name__ == "__main__":
    import doctest
    doctest.testmod()