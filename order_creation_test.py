import sender_stand_request
import data

# Кулигина Екатерина, 18-я когорта — Финальный проект. Инженер по тестированию плюс
# Тестирование
def test_order_creation():
    track = sender_stand_request.create_order(data.order_body).json()['track']
    response = sender_stand_request.get_order(track)
    assert response.status_code == 200