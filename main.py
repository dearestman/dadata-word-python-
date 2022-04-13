import json
import requests as requests

from docxtpl import DocxTemplate

API_KEY = '9d8df37c8b44353cfe3b44444a341ddf848d4a35'
API_SECRET = 'deb1fc67310bd7d2ba818b7b89d7494b7471de96'

BASE_URL = 'https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/'

def find_INN(resource, query):
    url = BASE_URL + resource
    headers = {
        'Authorization': 'Token ' + API_KEY,
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    data = {
        'query': query
    }
    res = requests.post(url, data=json.dumps(data), headers=headers)
    return res.json()

def testWord():
    doc = DocxTemplate("Шаблон.doc")
    context = {'name': 'ООО Ромашка', 'director': 'г. Москва, ул. Долгоруковская, д. 0'}
    doc.render(context)
    doc.save("шаблон-final.docx")


if __name__ == '__main__':
    testWord()
    data = find_INN('party', '0278101668')
    # название компании
    print('Название: ' + data['suggestions'][0]['value'])
    # Полное название
    print('Полное название: ' + data['suggestions'][0]['data']['name']['full_with_opf'])
    # КПП
    print('КПП: ' + data['suggestions'][0]['data']['kpp'])
    # ОГРН
    print('ОГРН: ' + data['suggestions'][0]['data']['ogrn'])
    # Должность + ФИО
    print(data['suggestions'][0]['data']['management']['post'] + ": " + data['suggestions'][0]['data']['management'][
        'name'])
    # юр.адрес
    print('Юр.адрес: ' + data['suggestions'][0]['data']['address']['value'])
