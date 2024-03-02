from django.db import models
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError

from user.models import MyBaseModel

User = get_user_model()


# Create Direct message model
class DirectMessageModel(MyBaseModel):
    text_message = models.TextField(blank=True, verbose_name='Text message')
    sender = models.ForeignKey(
        User, blank=False, null=False, on_delete=models.PROTECT,
        verbose_name='Sender', related_name='sender_direct_messages'
    )   # Relate it to a sending user
    receiver = models.ForeignKey(
        User, blank=False, null=False, on_delete=models.PROTECT,
        verbose_name='Receiver', related_name='receiver_direct_messages'
    )   # Relate it to a sending user
    media_file = models.FileField(
        upload_to='message/%Y/%m', blank=True, verbose_name='Media File')
    media_type = models.CharField(
        max_length=10, choices=[('image', 'Image'), ('video', 'Video'), ('audio', 'Audio')],
        verbose_name='Media type', blank=True
    )   # This can include a media or not

    class Meta:
        verbose_name = 'Direct message'
        verbose_name_plural = 'Direct messages'

    def __str__(self):
        return f'{self.sender} sent a message with id {self.id} '

    def clean(self):
        # Check for having at least one type of messages
        if self.text_message is None and self.media_file is None:
            raise ValidationError(
                'A direct message should contain either a text message or a media file.'
            )
