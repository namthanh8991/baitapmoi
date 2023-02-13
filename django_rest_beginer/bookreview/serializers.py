from rest_framework import serializers
from .models import Author, book


class bookSerializer(serializers.ModelSerializer):
    search_url = serializers.SerializerMethodField('get_search_url')
    class Meta:
        model = book
        fields = ['title','isbn','author','id','search_url']


    def get_search_url(self, obj):
        return "http://www.isbnsearch.org/isbn/{}".format(obj.isbn)

class AuthorSerializer(serializers.ModelSerializer):
    books = bookSerializer(read_only=True, many=True, source="book_set")
    class Meta:
        model = Author
        fields = ['id','first_name','last_name','books']




