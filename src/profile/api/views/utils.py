from django.core.mail import EmailMessage


class Util:
    @staticmethod
    def send_email(data):
        email = (
            EmailMessage(
                sunject=data["email_subject"],
                body=data["email_body"],
                to=data["email_user"],
            ),
        )
        email.send()
