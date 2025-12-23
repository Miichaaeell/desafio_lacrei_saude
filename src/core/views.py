from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Consultation, Professional
from .serializers import ConsultationSerializer, ProfessionalSerializer


# Views for constultations
class ConsultationListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ConsultationSerializer

    def get_queryset(self):
        qs = Consultation.objects.all()
        professional_id = self.request.query_params.get("professional_id")

        if professional_id:
            qs = qs.filter(professional_id=professional_id)

        return qs


class ConsultationRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer


# Views for professionals


class ProfessionalListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer


class ProfessionalRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer
