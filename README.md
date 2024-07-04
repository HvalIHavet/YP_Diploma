# Практический блок: вторая часть
_____
## Работа с базой данных
### *Задание 1*
Представь: тебе нужно проверить, отображается ли созданный заказ в базе данных.
Для этого: выведи список логинов курьеров с количеством их заказов в статусе «В доставке»
### *Задание 2*
Нужно убедиться, что в базе данных статусы заказов записываются корректно.
Для этого: выведи все трекеры заказов и их статусы. 
### Технические особенности:
- Доступ к базе осуществляется с помощью команды psql -U morty -d scooter_rent. Пароль: smith.
- У psql есть особенность: если таблица в базе данных с большой буквы, то её в запросе нужно брать в кавычки. Например, select * from “Orders”.
---

## Автоматизация теста к API
### *Задание*
Автоматизируй сценарий:
 - Клиент создает заказ.
 - Проверяется, что по треку заказа можно получить данные о заказе.
 
**Шаги автотеста:**
1. Выполнить запрос на создание заказа.
2. Сохранить номер трека заказа.
3. Выполнить запрос на получения заказа по треку заказа.
4. Проверить, что код ответа равен 200.

# Требования
- Для запуска тестов должны быть установлены пакеты pytest и requests
- Запуск всех тестов выполянется командой pytest
_____