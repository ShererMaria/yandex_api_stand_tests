import requests
import configuration
import data


def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)


response = get_docs()


def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH,
                        params={"count": 20})


response = get_logs()


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)


response = post_new_user(data.user_body);


def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)


response = get_users_table()


def post_products_kits(products_ids):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                         json=products_ids,  # Тело запроса содержит ID продуктов в формате JSON
                         headers=data.headers)  # Использование заголовков из файла data.py


response = post_products_kits(data.product_ids)
