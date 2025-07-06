from rest_framework import serializers
from .models import Books, Members

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'
        # read_only_fields = []

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = '__all__'
        # read_only_fields = []