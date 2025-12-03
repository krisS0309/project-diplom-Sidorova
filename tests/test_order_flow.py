# tests/test_order_flow.py
# Только тесты с assert, без print()

import data
from business.order_service import create_order_and_get_track, get_order_and_validate

def test_create_order_success():
    """Тест успешного создания заказа"""
    track_number, status_code = create_order_and_get_track(data.order_body)
    
    # Проверяем с помощью assert
    assert status_code == 201, f"Ожидался код 201, получен {status_code}"
    assert track_number is not None, "Трек номер не был получен"
    assert isinstance(track_number, int), f"Трек номер должен быть числом, получен {type(track_number)}"

def test_get_order_success():
    """Тест успешного получения заказа по треку"""
    # Создаем заказ
    track_number, create_status = create_order_and_get_track(data.order_body)
    assert create_status == 201, "Не удалось создать заказ"
    assert track_number is not None, "Трек номер не получен"
    
    # Получаем заказ
    success, get_status, order_data = get_order_and_validate(track_number)
    
    # Проверяем с помощью assert
    assert success is True, f"Не удалось получить заказ, код: {get_status}"
    assert get_status == 200, f"Ожидался код 200, получен {get_status}"
    assert order_data is not None, "Данные заказа не получены"

def test_full_order_flow():
    """Полный тестовый сценарий"""
    # 1. Создание заказа
    track_number, create_status = create_order_and_get_track(data.order_body)
    
    # Проверка создания
    assert create_status == 201, f"Ошибка создания заказа: {create_status}"
    assert track_number is not None, "Трек номер не получен"
    
    # 2. Получение заказа по треку
    success, get_status, order_data = get_order_and_validate(track_number)
    
    # Проверка получения
    assert success is True, f"Ошибка получения заказа: {get_status}"
    assert get_status == 200, f"Код ответа не 200: {get_status}"
    assert "order" in order_data if order_data else False, "Ключ 'order' отсутствует в ответе"