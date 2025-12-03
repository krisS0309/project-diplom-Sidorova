# Сидорова Кристина, 38-я когорта — Дипломный проект. Инженер по тестированию плюс
# autotest.py
# Точка входа с логированием, можно оставить print() только здесь

import logging
import sys
from tests.test_order_flow import test_full_order_flow

# Настраиваем логирование
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('test_results.log')
    ]
)

logger = logging.getLogger(__name__)

def run_autotest():
    """Запуск автотеста"""
    logger.info("=" * 50)
    logger.info("ЗАПУСК АВТОТЕСТА API ЗАКАЗОВ")
    logger.info("=" * 50)
    
    try:
        # Логируем начало теста
        logger.info("Шаг 1: Тест создания и получения заказа")
        
        # Запускаем тест
        test_full_order_flow()
        
        # Если дошли сюда - тест пройден
        logger.info("✅ Тест пройден успешно!")
        return True
        
    except AssertionError as e:
        logger.error(f"❌ Тест не пройден: {e}")
        return False
    except Exception as e:
        logger.error(f"⚠️ Неожиданная ошибка: {e}")
        return False

def main():
    """Основная функция"""
    print("=" * 50)
    print("АВТОТЕСТ ДИПЛОМНОГО ПРОЕКТА")
    print("Сидорова Кристина, 38-я когорта")
    print("=" * 50)
    
    success = run_autotest()
    
    if success:
        print("\n✅ АВТОТЕСТ ПРОЙДЕН УСПЕШНО!")
        print("Результаты сохранены в test_results.log")
        sys.exit(0)
    else:
        print("\n❌ АВТОТЕСТ НЕ ПРОЙДЕН")
        print("Проверьте лог test_results.log для деталей")
        sys.exit(1)

if __name__ == "__main__":
    main()