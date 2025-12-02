# Сидорова Кристина, 38-я когорта — Дипломный проект. Инженер по тестированию плюс

import config
import requests
import data

# Создание заказа
def post_new_order(order_body):
	return requests.post(config.URL_SERVICE + config.CREATE_ORDER_PATH,
	                     json = order_body,
	                     headers = data.headers)

# Получение заказа по номеру трекера
def get_order_from_track(track):
	return requests.get(config.URL_SERVICE + config.FIND_ORDER_FROM_TRACK_PATH + str(track),
	                    headers = data.headers)

# Выполнить запрос на получения заказа по треку заказа.
def assertion_code_200():
	response_pno = post_new_order(data.order_body)
	track = response_pno.json()["track"]
	return get_order_from_track(track).status_code

# Проверить, что код ответа равен 200.
def test_get_order_from_track_code_200():
	assert assertion_code_200() == data.status_code_200