from rest_framework import serializers
from .models import *

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'bio']

    # Since we have to put validation logic in create and update, we use save to make it easier
    def save(self, **kwargs):
        validated_data = self.validated_data
        dupe_authors = self.Meta.model.objects.filter(name = validated_data.get('name')).count()
        if dupe_authors:
            raise serializers.ValidationError({
                "Detail": "Author already exists!"
            })
        author = Author(**validated_data)
        author.save()
        return author
        

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'category', 'description']

    def save(self, **kwargs):
        validated_data = self.validated_data
        dupe_genre = self.Meta.model.objects.filter(category = validated_data.get('category')).count()
        if dupe_genre:
            raise serializers.ValidationError({
                "Detail": "Genre already exists!"
            })
        genre = Genre(**validated_data)
        genre.save()
        return genre

class BookSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='name', queryset=Author.objects.all())
    genre = serializers.SlugRelatedField(slug_field='category', queryset=Genre.objects.all())

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_date', 'genre', 'available_copies']

    # this function is run when we do serializer.is_valid
    # we have to check if the book has same title as well as author before raising error
    def validate(self, attrs):
        title = attrs.get('title')
        author = attrs.get('author')
        if Book.objects.filter(title=title, author=author).exists():
            raise serializers.ValidationError({
                "Detail": "A book with this title by the same author already exists."
            })
        return attrs

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    book = serializers.SlugRelatedField(slug_field='title', queryset=Book.objects.all())

    class Meta:
        model = Review
        fields = ['id', 'user', 'book', 'rating', 'rating_text']
    
class ReserveSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    book = serializers.SlugRelatedField(slug_field='title', queryset=Book.objects.all())

    class Meta:
        model = Reserve
        fields = ['id', 'user', 'book' ,'reserve_date', 'status']
    
class BorrowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    book = serializers.SlugRelatedField(slug_field='title', queryset=Book.objects.all())
    
    # fine is gonne be shown with difference to time so its not in the db
    fine = serializers.SerializerMethodField()

    class Meta:
        model = Borrow
        fields = ['id', 'user', 'book' ,'borrow_date', 'return_date', 'fine']
        read_only_fields = ['borrow_date', 'return_date', 'fine']

    def create(self, validated_data):
        # Set return_date automatically: 14 days after borrow_date (today)
        borrow_date = datetime.date.today()
        return_date = borrow_date + timezone.timedelta(days=14)

        # borrow date and return data are not set by borrower
        return Borrow.objects.create(
            user=validated_data['user'],
            book=validated_data['book'],
            borrow_date=borrow_date,
            return_date=return_date,
        )
    
    def get_fine(self, borrow:Borrow):
        # Get today's date (only date part)
        today = datetime.date.today()
        # Access the return_date from the borrow object since we passed the Borrow class to it
        return_date = borrow.return_date
        fine_per_day = 10
        
        if today > return_date:
            days_exceeded = (today-return_date).days
            fine = fine_per_day*days_exceeded
            return fine
        else:
            return 0
