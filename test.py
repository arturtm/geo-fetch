import sys
import requests
import csv

# Set api.geonames parametres
geonameuser = 'savchenko.artur90'
url = 'http://api.geonames.org/wikipediaSearchJSON?maxRows=1&'


def run():
    # Try get args from CLI
    try:
        cities = sys.argv[1].replace(' ','')
    except IndexError as e:
        print('Need to input data')

    all_cities = cities.split(',')

    #Search for single city
    for city in all_cities:
        query = city.lower().strip()

        resp = requests.get(url + 'q=' + query + '&username=' + geonameuser)
        cities = resp.json()

        try:
            city = cities['geonames'][0]['countryCode']

            #Open currency csv by country
            with open('country-code-to-currency-code-mapping.csv', mode='r') as csv_file:
                csv_reader = csv.DictReader(csv_file)

                for row in csv_reader:
                    #Check match country for match
                    if row['CountryCode'] == city:
                        print (row['Country'])
                        print (row['Code'])
        except:
            print('City does not found')


if __name__ == '__main__':
    run()
