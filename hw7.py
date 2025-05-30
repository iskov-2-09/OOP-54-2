# Имитация базы данных — список пользователей
users_db = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com"}
]

def get_user_by_id(user_id):
    for user in users_db:
        if user["id"] == user_id:
            return user
    # Пользователь не найден
    return None

# Пример использования:
if __name__ == "__main__":
    user = get_user_by_id(2)
    if user:
        print("Найден пользователь:", user)
    else:
        print("Пользователь не найден")
