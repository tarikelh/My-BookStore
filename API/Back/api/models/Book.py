from django.db import models

class Book(models.Model):
    ISBN = models.CharField(max_length=50)
    product = models.OneToOneField('Product', on_delete=models.CASCADE)
    editor = models.ForeignKey('Editor', on_delete=models.CASCADE)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    book_type = models.ForeignKey('BookType', on_delete=models.CASCADE)

    def to_json(self):
        return {
            'ISBN': self.ISBN,
            'product_id': self.product.id,
            'editor_id': self.editor.id,
            'author_id': self.author.id,
            'book_type_id': self.book_type.id,
        }
