from django.db import models

NULLABLE = {"blank": True, "null": True}


class Product(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Имя продукта", help_text="Введите Имя продукта"
    )
    description = models.TextField(
        verbose_name="Описание продукта", help_text="Введите Описание продукта"
    )
    image = models.ImageField(
        upload_to="index/images", verbose_name="Изображение товара", help_text="Загрузите изображение товара"
    )
    category = models.ForeignKey(
        "Category", on_delete=models.SET_NULL, verbose_name="Категория", help_text="Введите название категории",
        related_name="products", **NULLABLE
    )
    price = models.IntegerField(
        verbose_name="Цена товара", help_text="Введите цену"
    )
    created_at = models.DateTimeField(
        verbose_name="Дата создания", help_text="Введите дату создания", auto_now_add=True
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["category", "name"]

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Имя категории", help_text="Введите имя категории"
    )
    description = models.TextField(
        verbose_name="Описание категории", help_text="Введите описание категории"
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class SpecialOffers(Product):
    discounted_price = models.IntegerField(
        verbose_name="Цена товара со скидкой", help_text="Введите цену"
    )

    class Meta:
        verbose_name = "Специальное предложение"
        verbose_name_plural = "Специальные предложения"

    def __str__(self):
        return self.name
