# Сидорова Кристина, 38-я когорта — Дипломный проект. Инженер по тестированию плюс

import config
import requests
import data  # исправлено с dat на data

# Создание заказа
def post_new_order(order_body):
    return requests.post(config.URL_SERVICE + config.CREATE_ORDER_PATH,
                         json=order_body,
                         headers=data.headers)

# Получение заказа по номеру трекера
def get_order_from_track(track):
    return requests.get(config.URL_SERVICE + config.FIND_ORDER_FROM_TRACK_PATH + str(track),
                        headers=data.headers)

# Выполнить запрос на получения заказа по треку заказа.
def assertion_code_200():
    response_pno = post_new_order(data.order_body)
    track = response_pno.json()["track"]
    print(f"Заказ создан. Трек номер: {track}")
    return get_order_from_track(track).status_code

# Проверить, что код ответа равен 200.
def test_get_order_from_track_code_200():
    status_code = assertion_code_200()
    print(f"Код ответа при получении заказа: {status_code}")
    assert status_code == data.status_code_200
    print("✓ Тест пройден успешно! Код ответа равен 200.")
    return True

# Точка входа для запуска скрипта
if __name__ == "__main__":
    print("=" * 50)
    print("Запуск автотеста API заказов")
    print("=" * 50)
    
    try:
        # Проверяем наличие необходимых модулей
        import config
        import data
        
        print("1. Инициализация завершена")
        print(f"2. Базовый URL: {config.URL_SERVICE}")
        print(f"3. Путь создания заказа: {config.CREATE_ORDER_PATH}")
        print(f"4. Путь поиска заказа: {config.FIND_ORDER_FROM_TRACK_PATH}")
        
        # Запускаем тест
        print("\n5. Запуск теста...")
        result = test_get_order_from_track_code_200()
        
        if result:
            print("\n" + "=" * 50)
            print("✅ ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО!")
            print("=" * 50)
        else:
            print("\n" + "=" * 50)
            print("❌ ТЕСТ НЕ ПРОЙДЕН")
            print("=" * 50)
            
    except ImportError as e:
        print(f"\n❌ Ошибка импорта: {e}")
        print("Проверьте наличие файлов config.py и data.py")
    except Exception as e:
        print(f"\n⚠️  Произошла ошибка: {e}")
        print("Проверьте настройки и доступность API сервера")
    
    # Пауза для просмотра результата
    input("\nНажмите Enter для выхода...")