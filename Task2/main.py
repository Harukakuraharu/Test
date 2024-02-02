import os
import requests


def put_folder(folder_name): 

    headers = {'Content-Type': 'application/json',
                       'Authorization': os.getenv('TOKEN')}
    url_folder = 'https://cloud-api.yandex.net/v1/disk/resources/'       
    params = {'path': folder_name}
    responce = requests.put(url_folder, headers=headers, params=params) 
    return responce.status_code




# if __name__ == '__main__':
#     put_folder('папка')

