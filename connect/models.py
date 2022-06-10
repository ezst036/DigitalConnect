from django.db import models
from twilio.rest import Client

# Create your models here.
class ContactConnect(models.Model):
    title=models.CharField(max_length=100)
    body=models.TextField()

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        account_sid = 'TWILIO_ACCOUNT_SID'
        auth_token = 'TWILIO_AUTH_TOKEN'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
                                    body=f'message sent - {self.title} - {self.body}',
                                    from_='+15017122661',
                                    to='+15558675310'
                                )

        print(message.sid)
        return super().save(*args, **kwargs)