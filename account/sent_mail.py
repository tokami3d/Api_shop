from django.core.mail import  send_mail

def send_confirmation_email(user, code):
    full_link = f'http://localhost:8000/api/v1/accounts/activate/{code}/'
    send_mail(
        'Здравстуйте! активируйте ваш аккаунт если это вы!',f'чтобы активировать ваш аккаунт нужно пререйти по ссылке:\n{full_link}'
                                                            
        'dzholdoshev1@gmail.com'
        [user],
        fail_silently=False
    )
