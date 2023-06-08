#!/usr/bin/python3
"""2-setup_datadog"""
import requests
import os


# Define Datadog API credentials
api_key = os.environ['DD_API_KEY']
app_key = os.environ['DD_APP_KEY']

# dashboard name
name_dashboard = 'Alx Dashboard'

# Datadog API endpoint
url = 'https://api.datadoghq.com/api/v1/dashboard'

# Headers for the Datadog
headers = {
        'Content-Type': 'application/json',
        'DD-API-KEY': api_key,
        'DD-APPLICATION-KEY': app_key
        }

# Datadog API Query
params = {
    'filter': name_dashboard
}

# Get request to Datadog API to get dashboards
response = requests.get(url, headers=headers, params=params)

# Check if the request was a success or fail
if response.status_code != 200:
    print(f'Request failed with status code {response.status_code}.')

# Extract the ID of the first dshboard matching the specified name
data = response.json()
if 'dashboards' not in data or not data['dashboards']:
    print(f'No dash board found with name: "{name_dashboard}".')
    exit(1)

dashboard_id = data['dashboards'][0]['id']

# print the ID of Dashboard
print(f'dashboard: "{name_dashboard}" id: {dashboard_id}')
