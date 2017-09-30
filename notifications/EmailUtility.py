from django.core.mail import send_mail


class EmailUtility():
    @staticmethod
    def send(subject, messaage, to_emails):
        send_mail(
            subject,
            messaage,
            AppConstants.from_email(),
            to_emails,
            fail_silently=False,
        )
