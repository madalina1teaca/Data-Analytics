#importing libraries
import mysql.connector
import pandas as pd
import os

# mysql database connection
conn = mysql.connector.connect(
    host = 'localhost',
    user = '',
    password
)