import pandas as pd
import numpy as np
import folium
import folium.plugins as plugins

df = pd.read_csv('abc.csv', encoding='CP949')
df.head()

df.sort_values(by='기준날짜', inplace=True)
df = df.reset_index(drop=True)

new = df[['기준날짜', '카메라명칭']].copy()
new['계수 평균'] = (df['진입계수'] + df['진출계수']) / 2
new.head()

location = pd.DataFrame(new['카메라명칭'].unique(), columns=['카메라명칭'])
location['위도'] = pd.Series([37.57777, 37.581425, 37.581286, 37.580543])
location['경도'] = pd.Series([126.982634, 126.984794, 126.981567, 126.986594])
location

new = pd.merge(new, location, on='카메라명칭')
new = new.sort_values(by='기준날짜')
new.head()

new = new.set_index('기준날짜')
new.to_csv('북촌 유동인구.csv', encoding='EUC-KR')

value = new['계수 평균'].values
minimum = min(value)
maximum = max(value)
new['계수 평균'] = new['계수 평균'].transform(func=lambda x: 300 * (x - minimum) / (maximum - minimum))
new['계수 평균'] = np.ceil(new['계수 평균']).astype(int)
new.head()

date = list(new.index.unique())

matrix = []

for j in date:
    a = []
    temp = new[new.index == j]

    for lat, lon, value in zip(temp['위도'], temp['경도'], temp['계수 평균']):
        [a.append([lat + np.random.normal(0, 0.0003), lon + np.random.normal(0, 0.0003)]) for i in range(value)]

    matrix.append(a)


def change_date(x):
    x = str(x)
    return x[:4] + '-' + x[4:6] + '-' + x[6:]


time_ind = list(map(lambda i: change_date(i), date))
print(time_ind)

m = folium.Map([37.579362, 126.984746], zoom_start=16)
plugins.HeatMapWithTime(matrix, index=time_ind).add_to(m)
m