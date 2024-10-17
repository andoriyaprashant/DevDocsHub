from django.db import models

class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=100)
    official_website = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.name

class Documentation(models.Model):
    language = models.ForeignKey(ProgrammingLanguage, on_delete=models.CASCADE)
    doc_title = models.CharField(max_length=200)
    content = models.TextField()
    doc_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.doc_title

