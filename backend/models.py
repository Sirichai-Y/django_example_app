from django.db import models

# Create your models here.
class Province(models.Model):
    province_name = models.CharField(max_length=255)
    province_latitude = models.DecimalField(max_digits=20, decimal_places=10, null=True)
    province_longitude = models.DecimalField(max_digits=20, decimal_places=10, null=True)

    def __str__(self) :
        return self.province_name

class Situation(models.Model):
    situation_name = models.CharField(max_length=255)
    situation_start = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.situation_name

class Message(models.Model):
    message_sentence = models.CharField(max_length=255)
    message_situation = models.ForeignKey(Situation, models.DO_NOTHING, related_name='situations')
    message_from = models.ForeignKey(Province, models.DO_NOTHING, related_name='from_prov')
    message_to = models.ForeignKey(Province, models.DO_NOTHING, related_name='to_prov')
    message_sender = models.CharField(max_length=255, null=True)
    message_like = models.PositiveIntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.situation.name

