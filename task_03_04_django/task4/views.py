from django.shortcuts import render
from datetime import date, timedelta

def task4_view(request):
    return render(request, "task4/task4.html")
WEEKDAYS_RU = {
    0: "понедельник",
    1: "вторник",
    2: "среда",
    3: "четверг",
    4: "пятница",
    5: "суббота",
    6: "воскресенье",
}

MONTHS_RU_GEN = {
    1: "января",
    2: "февраля",
    3: "марта",
    4: "апреля",
    5: "мая",
    6: "июня",
    7: "июля",
    8: "августа",
    9: "сентября",
    10: "октября",
    11: "ноября",
    12: "декабря",
}

def day_of_programmer(year: int) -> date:
    # 256-й день года = 1 января + 255 дней
    return date(year, 1, 1) + timedelta(days=255)

def task4_view(request):
    context = {"result": None}

    if request.method == "GET":
        return render(request, "task4/task4.html", context)

    # POST
    year_raw = (request.POST.get("year") or "").strip()
    context["year"] = year_raw

    # Проверка, что год — число
    if not year_raw.isdigit():
        context["error"] = "Введите год числом (например, 2021)."
        return render(request, "task4/task4.html", context)

    year = int(year_raw)

    # Разумные ограничения (чтобы не ловить экзотические ошибки)
    if year < 1 or year > 9999:
        context["error"] = "Введите год в диапазоне 1–9999."
        return render(request, "task4/task4.html", context)

    d = day_of_programmer(year)
    weekday_ru = WEEKDAYS_RU[d.weekday()]
    month_ru = MONTHS_RU_GEN[d.month]

    context["result"] = f"{d.day} {month_ru} ({weekday_ru})"
    return render(request, "task4/task4.html", context)