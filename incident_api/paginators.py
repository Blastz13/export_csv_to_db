from rest_framework.pagination import PageNumberPagination


class IncidentListPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'limit'
    page_query = 'page'
    max_page_size = 1000
