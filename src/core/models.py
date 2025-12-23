from django.db import models


class Professional(models.Model):
    social_name = models.CharField(max_length=124)
    profession = models.CharField(max_length=124)
    phone = models.CharField(max_length=15, blank=True)
    email = models.EmailField(max_length=124, blank=True)
    street = models.CharField(max_length=124)
    number = models.CharField(max_length=10)
    complement = models.CharField(max_length=124, blank=True, null=True)
    neighborhood = models.CharField(max_length=124)
    city = models.CharField(max_length=124)

    def __str__(self):
        return self.social_name

    class Meta:
        verbose_name = "Professional"
        verbose_name_plural = "Professionals"
        ordering = ["social_name"]


class Consultation(models.Model):
    professional = models.ForeignKey(
        Professional,
        on_delete=models.CASCADE,
        related_name="consultations",
    )
    client_name = models.CharField(max_length=124)
    scheduled_at = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.client_name} - {self.scheduled_at}"

    class Meta:
        verbose_name = "Consultation"
        verbose_name_plural = "Consultations"
        ordering = ["scheduled_at"]
