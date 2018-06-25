from .models import Plant
import django_filters

class PlantFilter(django_filters.FilterSet):
    print("IN FILTER")
    name = django_filters.CharFilter(name='name', lookup_expr="icontains")

    class Meta:
        model = Plant
        fields = ['name']