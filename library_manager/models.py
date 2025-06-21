from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Authors(models.Model):
    author_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=False)

    class Meta:
        indexes = [
                    models.Index(fields=['first_name', 'last_name'], name='author_name'),
                ]
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Publishers(models.Model):
    publisher_id = models.IntegerField(primary_key=True)
    publisher_name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return f"{self.publisher_name}"

# added to store genres for MtM relation between Books and Genres
# Genre names are unique, so can be used for primary_key which removes creating ids and prevents duplicates
class Genres(models.Model):
    genre_name = models.CharField(max_length=255, primary_key=True)

    def __str__(self):
        return f"{self.genre_name}"

class Members(models.Model):
    member_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    email = models.EmailField(null=False, unique=True, db_index=True)
    # remember to add a part to hash passwords before storing
    password = models.TextField(max_length=255, null=False)
    membership_date = models.DateField(null=False, auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.email} | created: {self.membership_date}"

class Books(models.Model):
    isbn = models.CharField(max_length=17, primary_key=True)
    title = models.CharField(max_length=255, null=False, db_index=True)
    genres = models.ManyToManyField(Genres)
    authors = models.ManyToManyField(Authors)
    publishers = models.ManyToManyField(Publishers)
    publication_year = models.IntegerField(
        validators=[MinValueValidator(1970)],
        null=True
    )
    language = models.CharField(max_length=3, null=False)
    total_quantity = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(99)],
        null=False
    )

    def __str__(self):
        return f"{self.isbn}: {self.title} | published: {self.publication_year} | in stock: {self.total_quantity} | language: {self.language}"

class Loans(models.Model):
    member_id = models.ForeignKey(Members, on_delete=models.PROTECT)
    isbn = models.ForeignKey(Books, on_delete=models.CASCADE)
    loan_date = models.DateField(null=False)
    return_date = models.DateField(null=False)

    class Meta():
        unique_together = ('member_id', 'isbn')

    def __str__(self):
        return f"Member: {self.member_id.first_name} {self.member_id.last_name} rented: {self.isbn.title} "



# class BookAuthors(models.Model):    simple MtM - use models.ManytoManyField(otherModel) instead
# class BookPublishers(models.Model): simple MtM - use models.ManytoManyField(otherModel) instead
# adding one for genre so books can have multiple genres