from rest_framework import filters


class TipsSearchFilter(filters.SearchFilter):
    """Search filter class"""

    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])