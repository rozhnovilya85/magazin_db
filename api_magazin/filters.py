from datetime import datetime

import django_filters as filters
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Q

from api_magazin.models import Magazine


class ShopFilter(filters.FilterSet):
    city = filters.CharFilter(field_name='city__name')
    street = filters.CharFilter(field_name='street__name')
    open = filters.NumberFilter(method='is_open_filter', validators=[MinValueValidator(0), MaxValueValidator(1)])

    class Meta:
        model = Magazine
        fields = ['city', 'street', 'open']

    def is_open_filter(self, queryset, name, value):
        now = datetime.now().time()

        if int(value) == 0:
            return queryset.filter(Q(time_open__gte=now) | Q(time_close__lte=now))
        else:
            return queryset.filter(time_open__lte=now, time_close__gte=now)