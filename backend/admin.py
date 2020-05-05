from django.contrib import admin
from .models import Province, Situation, Message, Comment

class ProvinceAdmin(admin.ModelAdmin):
    model = Province
    list_display = ['id', 'province_name', 'province_latitude', 'province_longitude',]
    search_fields = ['province_name']

    def get_ordering(self, request):
        return ['id']

    def get_form(self, request, obj=None, **kwargs):
        form = super(ProvinceAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['province_latitude'].required = False
        form.base_fields['province_longitude'].required = False
        return form

class SituationAdmin(admin.ModelAdmin):
    model = Situation
    list_display = ['id', 'situation_name', 'situation_start',]

    def get_ordering(self, request):
        return ['id']

class MessageAdmin(admin.ModelAdmin):
    model = Message
    list_display = ['id', 'message_sentence', 'message_sender', 'message_like',  'message_situation', 'message_from', 'message_to',]
    
    def get_ordering(self, request):
        return ['id']

    def get_form(self, request, obj=None, **kwargs):
        form = super(MessageAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['message_sender'].required = False
        return form

class CommentAdmin(admin.ModelAdmin):
    model = Message
    list_display = ['id', 'message_id', 'message_comment', 'comment_sender', 'create_at',]
    
    def get_ordering(self, request):
        return ['id']

    def get_form(self, request, obj=None, **kwargs):
        form = super(MessageAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['comment_sender'].required = False
        return form

# Register your models here.
admin.site.register(Province, ProvinceAdmin)
admin.site.register(Situation, SituationAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Comment, CommentAdmin)