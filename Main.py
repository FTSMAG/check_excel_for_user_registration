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


def parser():
    df_parse = pd.read_excel('templete.xlsx')
    #print(df_parse.head(0))
    for i in df_parse.head(0):
        print(i)
    if 'Логин' and 'Пароль' in df_parse.head(0):
        print("ДАДАДА")







#current_template()
parser()