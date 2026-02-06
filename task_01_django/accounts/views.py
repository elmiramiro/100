from django.shortcuts import render, redirect

# Учебная "база" пользователей: логин -> (пароль, роль)
USERS = {
    "admin": ("1234", "Администратор"),
    "user": ("1111", "Пользователь"),
}

def login_view(request):
    # 1) Если просто открыли страницу — показать форму
    if request.method == "GET":
        return render(request, "accounts/login.html")

    # 2) Если нажали "Войти" — проверить введённые данные
    if request.method == "POST":
        login_input = request.POST.get("login", "").strip()
        password_input = request.POST.get("password", "").strip()

        # Проверка логина
        if login_input in USERS:
            real_password, role = USERS[login_input]
            # Проверка пароля
            if password_input == real_password:
                # Успех: сохраняем в сессии и ведём на страницу приветствия
                request.session["login"] = login_input
                request.session["role"] = role
                return redirect("welcome")
            else:
                return render(request, "accounts/login.html", {"error": "Неверный пароль."})
        else:
            return render(request, "accounts/login.html", {"error": "Такого пользователя нет."})

    # На всякий случай
    return render(request, "accounts/login.html", {"error": "Некорректный метод запроса."})


def welcome_view(request):
    # Берём данные из сессии
    login_value = request.session.get("login")
    role = request.session.get("role")

    # Если зашли на /welcome/ без авторизации — отправляем на логин
    if not login_value or not role:
        return redirect("login")

    return render(request, "accounts/welcome.html", {"login": login_value, "role": role})
