from django import forms
from sms.tasks import send_sms


class SendSMSForm(forms.Form):
    phone_number = forms.CharField(label='Номер телефону', max_length=14)
    message = forms.CharField(label='Меседж', max_length=160)

    def send_sms(self):
        send_sms.delay(self.cleaned_data['phone_number'], self.cleaned_data['message'])
