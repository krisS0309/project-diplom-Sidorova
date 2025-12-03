# api/order_api.py
# Только HTTP запросы, никакого print()

import requests
import configuration

def post_new_order(order_body):
    """Чистый POST запрос для создания заказа"""
    return requests.post(
        configuration.URL_SERVICE + configuration.CREAT_ORDERS,
        json=order_body
    )

def get_order_by_track(track_number):
    """Чистый GET запрос для получения заказа по треку"""
    get_order_url = f"{configuration.URL_SERVICE}/api/v1/orders/track?t={track_number}"
    return requests.get(get_order_url)