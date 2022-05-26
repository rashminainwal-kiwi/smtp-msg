from django.shortcuts import render
from django.views import View


class sender(View):
    def get(self, request):
        return render(request, 'home.html')

    def post(self, request, true=None):
        port = request.POST.get('port')
        login = request.POST.get('login')
        password = request.POST.get('password')
        email_from = request.POST.get('email_from')
        email_to = request.POST.get('email_to')
        host = request.POST.get('host')

        ''' Email message'''
        import smtplib

        sender_mail = email_from
        sender_mail_pass = password
        receiver_mail = email_to
        port = port
        login = login
        host = host

        # creates SMTP session
        s = smtplib.SMTP(host, port)

        s.ehlo()
        # start TLS for security
        s.starttls()
        s.ehlo()

        # Authentication
        s.login(sender_mail, sender_mail_pass)

        # message to be sent
        subject = 'SMTP email test'
        message = 'Subject: {}\n\n{}'.format(subject, 'mail is working fine')

        # sending the mail
        s.sendmail(sender_mail, receiver_mail, message)

        # terminating the session
        s.quit()

        return render(request, 'home.html')
