#!/usr/bin/python
import psycopg

import psycopg

# Basic connection using a connection string
conn_string = 'postgresql://baronvice:x1Dk%3EmkR2JSJ@89.169.3.129:5432/transbypg'

# Autocommit mode
try:
    with psycopg.connect(conn_string, autocommit=True) as conn:
        print("Successfully connected in autocommit mode!")
        with conn.cursor() as cur:

            # Execute a command: this creates a new table
            cur.execute("SELECT * FROM public.\"trackStorage_trip\"")
            results = cur.fetchall()
            for res in results:
                print(res)
        # Perform database operations, changes are committed immediately
except psycopg.OperationalError as e:
    print(f"Connection failed: {e}")