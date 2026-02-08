from django.shortcuts import render

def task2_view(request):
    context = {"result": None, "action": "min"}

    if request.method == "GET":
        return render(request, "task2/task2.html", context)

    # POST
    a_raw = request.POST.get("a", "").strip()
    b_raw = request.POST.get("b", "").strip()
    c_raw = request.POST.get("c", "").strip()
    action = request.POST.get("action", "").strip()

    # сохраняем введённые значения, чтобы при ошибке не пропали
    context.update({"a": a_raw, "b": b_raw, "c": c_raw, "action": action})

    # 1) преобразование к числам
    try:
        a = float(a_raw.replace(",", "."))
        b = float(b_raw.replace(",", "."))
        c = float(c_raw.replace(",", "."))
    except ValueError:
        context["error"] = "Введите три числа (можно с точкой или запятой)."
        return render(request, "task2/task2.html", context)

    # 2) вычисление по выбранной радиокнопке
    if action == "min":
        result = min(a, b, c)
    elif action == "max":
        result = max(a, b, c)
    elif action == "avg":
        result = (a + b + c) / 3
    else:
        context["error"] = "Выберите действие: минимум / максимум / среднее."
        return render(request, "task2/task2.html", context)

    context["result"] = result
    return render(request, "task2/task2.html", context)
