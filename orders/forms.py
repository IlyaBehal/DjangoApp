import re
from django import forms



class CreateOrderFrom(forms.Form):

    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    requires_delivery = forms.ChoiceField(choices=[
        ("0", False), 
        ("1", True)
        ],)
    delivery_address = forms.CharField(required=False)
    payment_on_get = forms.ChoiceField(choices=[
        ("0", "False"), 
        ("1", "True")
        ],)

    def clean_phone_number(self):
        data = self.cleaned_data['phone_number']
        
        if not data.isdigit():
            raise forms.ValidationError("Номер телефону повинен містити тільки цифри!")
        
        pattern = re.compile(r'^\d{10}$')

        if not pattern.match(data):
            raise forms.ValidationError("Неправильний формат номеру телефону!")
        
        return data



    # firts_name = forms.CharField(widget=forms.TextInput(
    #     attrs={
    #         'class': 'from-control',
    #         'placeholder': "Введіть ім'я"
    #     }
    # ))
    # last_name = forms.CharField(widget=forms.TextInput(
    #     attrs={
    #         'class': 'from-control',
    #         'placeholder': "Введіть прізвище"
    #     }
    # ))
    # phone_number = forms.CharField(widget=forms.TextInput(
    #     attrs={
    #         'class': 'from-control',
    #         'placeholder': "Номер телефону"
    # }))
    # requires_delivery = forms.ChoiceField(widget=forms.RadioSelect(),
    #                                     choices=[
    #                                         ('0', False),
    #                                         ('1', True)],
    #                                     initial=0)

    # delivery_address = forms.CharField(widget=forms.Textarea(
    #     attrs={
    #         'class': 'from-control',
    #         'placeholder': "Введіть адресу доставки",
    #         'id': 'delivery_address',
    #         'rows': 2
    #     }
    # ))

    # payment_on_get = forms.ChoiceField(widget=forms.RadioSelect(),
    #                                     choices=[
    #                                         ('0', 'False'),
    #                                         ('1', 'True')],
    #                                     initial="card")
