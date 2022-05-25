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
        # UseSecuredConnection = request.POST.get('UseSecuredConnection')
        # Useauthentication = request.POST.get('Useauthentication')

        ''' Email message'''
        import smtplib

        sender_mail = email_from
        sender_mail_pass = password
        receiver_mail = email_to
        port = port
        login = login
        host = host
        # UseSecuredConnection = UseSecuredConnection
        # Useauthentication = Useauthentication

        # creates SMTP session
        s = smtplib.SMTP(host, port)
        # s = smtplib.SMTP('smtp.gmail.com', port)
        s.ehlo()
        # start TLS for security
        s.starttls()
        s.ehlo()
        #
        # if UseSecuredConnection == true:
        #     if Useauthentication == true:

        # Authentication
        s.login(sender_mail, sender_mail_pass)
        # else:
        #     return "error"
        # message to be sent

        subject = 'SMTP email test'
        message = 'Subject: {}\n\n{}'.format(subject, 'mail is working fine')

        # sending the mail
        s.sendmail(sender_mail, receiver_mail, message)

        # terminating the session
        s.quit()

        return render(request, 'home.html')
