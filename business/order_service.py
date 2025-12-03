# business/order_service.py
# Бизнес-логика, без print()

from api.order_api import post_new_order, get_order_by_track

def create_order_and_get_track(order_body):
    """Создание заказа и возврат трек-номера"""
    response = post_new_order(order_body)
    
    if response.status_code != 201:
        return None, response.status_code
    
    try:
        track_number = response.json()["track"]
        return track_number, response.status_code
    except (KeyError, ValueError):
        return None, response.status_code

def get_order_and_validate(track_number):
    """Получение заказа по треку и валидация"""
    response = get_order_by_track(track_number)
    return response.status_code == 200, response.status_code, response.json() if response.status_code == 200 else None