from django.db import models
from twilio.rest import Client

messagetypes = [
    ('newmember', 'New member'),
    ('prayer', 'Prayer request'),
]

# Create your models here.
class ContactConnect(models.Model):
    title=models.CharField(max_length=100)
    body=models.TextField()
    messagetype = models.CharField(max_length=24, choices=messagetypes, default='newmember')
    first_name = models.CharField(verbose_name="First Name", max_length=255, blank=True)
    last_name = models.CharField(verbose_name="Last Name", max_length=255, blank=True)
    userAccountid = models.IntegerField(verbose_name="Account number",default=0)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        
        account_sid = 'TWILIO_ACCOUNT_SID'
        auth_token = 'TWILIO_AUTH_TOKEN'

        # or self.messagetype == 'prayer'

        #Should not send notifications for new member Connect messages
        #Confirm default sid and token information to prevent errors
        if self.messagetype == 'prayer':

            if not (account_sid == 'TWILIO_ACCOUNT_SID' or 
                auth_token == 'TWILIO_AUTH_TOKEN'):
            
                client = Client(account_sid, auth_token)
                message = client.messages.create(
                                            body=f'message sent - {self.title} - {self.body}',
                                            from_='+15017122661',
                                            to='+15558675310'
                                        )

                print(message.sid)

        return super().save(*args, **kwargs)