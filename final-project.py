import pandas
import requests
import io
from sklearn.datasets.samples_generator import make_blobs
from matplotlib import pyplot as plt
from matplotlib import style

# NYTimes global deaths data
url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/excess-deaths/deaths.csv'
# load data into pandas DataFrame
data = pandas.read_csv(io.StringIO(requests.get(url).text))

# Countries organized into lists named after their respective continent
europe = ['Austria', 'Belgium','Denmark', 'Finland', 'France', 'Germany', 'Italy',
'Netherlands', 'Norway', 'Portugal', 'Russia', 'Sweden', 'Switzerland', 'United Kingdom']
northam = ['Mexico', 'United States']
southam = ['Brazil', 'Ecuador', 'Peru',]
asia = ['Indonesia', 'Israel', 'South Korea', 'Thailand']
# convert DataFrame to a list for operability
country_list = data.values.tolist()

eu_count = 0
northam_count = 0
southam_count = 0
asia_count = 0
for country in country_list:
    c = str(country[0])
    if c in europe:
        eu_count += int(country[8])
    elif c in northam:
        northam_count += int(country[8])
    elif c in southam:
        southam_count += int(country[8])
    elif c in asia:
        asia_count += int(country[8])

def create_file(europe, northam, southam, asia, eu_count, northam_count,
southam_count, asia_count):
    '''Function to create file with continent information(countries) and total COVID-19 deaths
    PARAMETERS: continemts, total counts of deaths per continent
    RETURNS: file'''
    file = open('continentinfo.txt', 'w')
    file.write('European Countries\n')
    for i in europe:
        file.write(f'{i}\n')
    file.write(f'Total COVID-19 deaths in Europe: {eu_count}\n')
    file.write('North American Countries\n')
    for i in northam:
        file.write(f'{i}\n')
    file.write(f'Total COVID-19 deaths in North America: {northam_count}\n')
    file.write('South American Countries\n')
    for i in southam:
        file.write(f'{i}\n')
    file.write(f'Total COVID-19 deaths in South America: {southam_count}\n')
    file.write('Asian Countries\n')
    for i in asia:
        file.write(f'{i}\n')
    file.write(f'Total COVID-19 deaths in Asia: {asia_count}')
    file.close()


create_file(europe, northam, southam, asia, eu_count, northam_count,
southam_count, asia_count)
# open file
with open('continentinfo.txt', 'r') as allInfo:
    for i in allInfo:
        print(f'{i.rstrip()}')


def visualize(eu_count, northam_count, southam_count, asia_count):
    '''Function to visualize similarities amongst data points from NYTimes excess deaths data
    PARAMETERS: total count of deaths from Asia, Europe, South America, North America
    RETURN: uses matplotlib and sklearn to plot data points'''

    X,y = make_blobs(n_samples = eu_count, center_box = (100.0,10.0), cluster_std =1.0)
    plt.scatter(X[:,0], X[:,1], s=3, color='green')
    X2,y2 = make_blobs(n_samples = northam_count, center_box = (100.0,10.0), cluster_std =1.0)
    plt.scatter(X2[:,0], X2[:,1], s=3, color='red')
    X3,y3 = make_blobs(n_samples = southam_count, center_box = (100.0,10.0), cluster_std =1.0)
    plt.scatter(X3[:,0], X3[:,1], s=3, color='blue')
    X4,y4 = make_blobs(n_samples = asia_count, center_box = (100.0,10.0), cluster_std =1.0)
    plt.scatter(X4[:,0], X4[:,1], s=3, color='magenta')

    plt.xlabel("X")
    plt.ylabel("Y")

    plt.show()
    plt.clf()

visualize(eu_count, northam_count, southam_count, asia_count)
