from rest_framework import serializers
from library import models


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model       =   models.Book
        fields      =   '__all__'


class CususerSerializer(serializers.ModelSerializer):
    class Meta:
        model       =   models.Cususer
        fields      =   ('first_name',
                        'last_name',
                        'profile',
                        'username',
                        
                        )




class IssuedbooksSerializer(serializers.ModelSerializer):
    class Meta:
        model      =   models.Issuedbooks
        fields      =   '__all__'



