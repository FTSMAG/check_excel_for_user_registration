import pandas as pd
import requests
import urllib
from templates import link


def current_template():
    #urllib.urlretrieve(link,'out.xlsx')
    print(link)
    rezult = requests.get(link)
    with open('templete.xlsx','wb')as file:
        file.write(rezult.content)




#execel = pd.read_excel('./Сибирь Заведение_новых_пользователей_ЦУП-ЕДГ-ЕГЭ (004).xlsx')

#print(execel.head())


current_template()