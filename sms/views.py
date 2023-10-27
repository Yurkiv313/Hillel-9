from django.shortcuts import render

from .forms import SendSMSForm
from .tasks import send_sms


def main(request):
    form = SendSMSForm(request.POST)
    if form.is_valid():
        phone_number = form.cleaned_data['phone_number']
        message = form.cleaned_data['message']
        send_sms.delay(phone_number, message)
    return render(request, 'main.html')
