"""
Share of Active Users

Interview Question Date: January 2021
Meta/Facebook
EasyID 2005
37
Data Engineer
Data Scientist
BI Analyst
Data Analyst

Output share of US users that are active. Active users are the ones with an "open" status in the table.
DataFrame: fb_active_users
Expected Output Type: pandas.DataFrame

fb_active_users
user_id:int
name:varchar
status:varchar
country:varchar
"""

# Import your libraries
import pandas as pd

# Start writing code
us = fb_active_users[fb_active_users['country'] == 'USA']
result = len(us[us['status'] == 'open']) / len(us)
