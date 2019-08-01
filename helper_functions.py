import json
import pandas as pd
import matplotlib.pyplot as plt

def clean_df(df):
    
    id = []
    latitude = []
    longitude = []
    price = []
    n_bathrooms = []
    n_bedrooms = []
    n_suites = []
    parkingSpaces = []
    totalArea = []
    usableArea = []
    tipo = []

    for i in range(len(df)):

        if 'geoLocation' in df.address[i] \
        and 'price' in df.pricingInfos[i] \
        and not pd.isnull(df['bathrooms'][i]) \
        and not pd.isnull(df['bedrooms'][i]) \
        and not pd.isnull(df['suites'][i]) \
        and not pd.isnull(df['parkingSpaces'][i]) \
        and not pd.isnull(df['totalAreas'][i]) \
        and not pd.isnull(df['usableAreas'][i]) \
        and not pd.isnull(df['unitTypes'][i]):

            id.append(df['id'][i])
            latitude.append(df['address'][i]['geoLocation']['location']['lat'])
            longitude.append(df['address'][i]['geoLocation']['location']['lon'])
            price.append(df['pricingInfos'][i]['price'])
            n_bathrooms.append(df['bathrooms'][i])
            n_bedrooms.append(df['bedrooms'][i])
            n_suites.append(df['suites'][i])
            parkingSpaces.append(df['parkingSpaces'][i])
            totalArea.append(df['totalAreas'][i])
            usableArea.append(df['usableAreas'][i])
            tipo.append(df['unitTypes'][i])

    dataframe = pd.DataFrame({
        
        'id': id,
        'latitude': latitude,
        'longitude': longitude,
        'price': price,
        'n_bathrooms': n_bathrooms,
        'n_bedrooms': n_bedrooms,
        'n_suites': n_suites,
        'parking_spaces': parkingSpaces,
        'total_area': totalArea,
        'usable_area': usableArea,
        'tipo': tipo
    })
    
    return dataframe

def plotCorrelationMatrix(df, graphWidth):
    corr = df.corr()
    plt.figure(num=None, figsize=(graphWidth, graphWidth),
               dpi=80, facecolor='w', edgecolor='k')
    corrMat = plt.matshow(corr, fignum=1)
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
    plt.yticks(range(len(corr.columns)), corr.columns)
    plt.gca().xaxis.tick_bottom()
    plt.colorbar(corrMat)
    plt.title(f'Matriz de Correlacao', fontsize=15)
    plt.show()

    