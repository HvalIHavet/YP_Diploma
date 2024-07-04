import configuration
import requests
import data

# Создание заказа
def create_order(order_body):
   return requests.post (configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=order_body)

# Получение данных заказа по номеру трекера
def get_order(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_INFO + str(track_number))

# Кулигина Екатерина, 18-я когорта — Финальный проект. Инженер по тестированию плюс
# Тестирование
def test_order_creation():
    track = create_order(data.order_body).json()['track']
    response = get_order(track)
    assert response.status_code == 200