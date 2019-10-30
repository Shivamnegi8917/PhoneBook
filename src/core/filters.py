import django_filters
from .models import PhoneBook

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = PhoneBook
        fields = {
            'firstname': ['icontains', ],
            'lastname': ['icontains', ],
            'phone': ['exact', ]
        }