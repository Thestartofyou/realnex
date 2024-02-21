import requests
import pandas as pd
import matplotlib.pyplot as plt

class RealNexAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.realnex.com'

    def get_property_listings(self, filters=None):
        headers = {'Authorization': f'Bearer {self.api_key}'}
        params = filters if filters else {}
        response = requests.get(f'{self.base_url}/listings', headers=headers, params=params)
        return response.json()

def analyze_property_listings(listings):
    df = pd.DataFrame(listings)
    average_lease_rate = df['lease_rate'].mean()
    vacancy_rate = (df['vacancy'] == 'Vacant').mean()
    return average_lease_rate, vacancy_rate

def visualize_data(average_lease_rate, vacancy_rate):
    labels = ['Average Lease Rate', 'Vacancy Rate']
    values = [average_lease_rate, vacancy_rate]
    plt.bar(labels, values)
    plt.xlabel('Metric')
    plt.ylabel('Value')
    plt.title('Property Analysis Metrics')
    plt.show()

def main():
    # Initialize RealNex API client with your API key
    api_key = 'YOUR_API_KEY'
    realnex_api = RealNexAPI(api_key)

    # Retrieve property listings from RealNex
    filters = {'property_type': 'Office', 'city': 'New York'}
    listings = realnex_api.get_property_listings(filters=filters)

    # Analyze property listings data
    average_lease_rate, vacancy_rate = analyze_property_listings(listings)

    # Visualize analysis results
    visualize_data(average_lease_rate, vacancy_rate)

if __name__ == '__main__':
    main()

