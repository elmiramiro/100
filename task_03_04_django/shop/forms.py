from django import forms

class RegistrationForm(forms.Form):
    first_name = forms.CharField(label="Имя", max_length=50)
    last_name = forms.CharField(label="Фамилия", max_length=50)
    age = forms.IntegerField(label="Возраст", min_value=1, max_value=120)
    email = forms.EmailField(label="Email")
    gender = forms.ChoiceField(
        label="Пол",
        choices=[("M", "Мужской"), ("F", "Женский")],
        widget=forms.RadioSelect
    )
    address = forms.CharField(
        label="Адрес для доставки товара",
        widget=forms.Textarea(attrs={"rows": 3})
    )
    subscribe = forms.BooleanField(
        label="Хотите ли подписаться на новости нашего интернет-магазина?",
        required=False
    )
