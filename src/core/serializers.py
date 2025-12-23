from datetime import timedelta
from django.utils import timezone
from rest_framework import serializers
from .models import Professional, Consultation


class ProfessionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professional
        fields = "__all__"

    def validate(self, attrs):
        phone = (
            attrs.get("phone")
            if "phone" in attrs
            else (self.instance.phone if self.instance else "")
        ) or ""
        email = (
            attrs.get("email")
            if "email" in attrs
            else (self.instance.email if self.instance else "")
        ) or ""

        phone = phone.strip()
        email = email.strip()

        if not phone and not email:
            raise serializers.ValidationError(
                {
                    "contact": "É necessário fornecer pelo menos um meio de contato: telefone ou email."
                }
            )

        attrs["phone"] = phone
        attrs["email"] = email
        return attrs


class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = "__all__"

    def validate_scheduled_at(self, value):
        if value < timezone.now() - timedelta(minutes=1):
            raise serializers.ValidationError(
                "A data e hora de agendamento não pode ser menor que a data e hora atual."
            )
        return value
