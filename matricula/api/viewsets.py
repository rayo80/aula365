
from rest_framework import viewsets
import matricula.api.serializers as mas


class TeacherViewSet(viewsets.ModelViewSet):
    serializer_class = mas.TeacherSerializer
    queryset = mas.TeacherSerializer.Meta.model


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = mas.StudentSerializer
    queryset = mas.StudentSerializer.Meta.model


class InscriptionViewSet(viewsets.ModelViewSet):
    serializer_class = mas.InscriptionsSerializer
    queryset = mas.InscriptionsSerializer.Meta.model


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = mas.CourseSerializer
    queryset = mas.CourseSerializer.Meta.model
