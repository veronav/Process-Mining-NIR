#!/usr/bin/env python
# coding: utf-8


import requests
import json

api_token = '****'


# Общий запрос для того, чтобы узнать метрики
url='https://****/v1/modules/5/stats/metrics'

headers = {
    "Content-Type": "text/csv", 
    "Authorization": api_token
}

r = requests.get(url, headers=headers)
r.text


# Гугл-выгрузка
url='https://****/v1/modules/5/stats/csv'

params = {
    "dateFrom": "2021-04-01",
    "dateTo": "2021-04-30",
    "metrics": json.dumps(["user"]),
    "breakdown[]": ["date","client_id","category"]
}

headers = {
    "Content-Type": "text/csv", 
    "Authorization": api_token
}

r = requests.get(url=url, params=params, headers=headers)


it = iter(list(r.text.replace('\n',',').split(',')))
data_list=list(map(list, zip(it, it, it)))

import pandas as pd
data_frame=pd.DataFrame(data_list)

data_frame.to_csv('JC_google_id5_api.csv', index=False, encoding='utf-8', header=False)

