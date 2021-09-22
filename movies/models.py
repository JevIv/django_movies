from datetime import date

from django.db import models


class Category(models.Model):
    """Categories"""
    name = models.CharField("Category", max_length=150)
    description = models.TextField("Description")
    url = models.SlugField(max_length=160)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Actor(models.Model):
    """Actors and directors"""
    name = models.CharField("Name", max_length=100)
    age = models.PositiveSmallIntegerField("Age", default=0)
    image = models.ImageField("Image", upload_to="actors/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Actors and directors"
        verbose_name_plural = "Actors and directors"


class Genre(models.Model):
    """Genres"""
    name = models.CharField("Name", max_length=150)
    description = models.TextField("Description")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"


class Movies(models.Model):
    """Movies"""
    title = models.CharField("Name", max_length=100)
    tagline = models.CharField("Tags", max_length=100, default="")
    description = models.TextField("Description")
    poster = models.ImageField("poster", upload_to="movies/")
    year = models.PositiveSmallIntegerField("Release year", default=2019)
    country = models.CharField("Country", max_length=30)
    directors = models.ManyToManyField(Actor, verbose_name="director", related_name="film_director")
    actors = models.ManyToManyField(Actor, verbose_name="actors", related_name="film_actor")
    genres = models.ManyToManyField(Genre, verbose_name="genres")
    world_premiere = models.DateField("Premiere", default=date.today)
    budget = models.PositiveSmallIntegerField("Budget", default=0, help_text="Add value in dollars")
    fees_in_usa = models.PositiveSmallIntegerField("Box office in USA", default=0, help_text="Add value in dollars")
    fees_in_usa = models.PositiveSmallIntegerField("Box office in the world",
                                                   default=0, help_text="Add value in dollars")
    category = models.ForeignKey(Category, verbose_name="Category", on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField("Draft", default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"
