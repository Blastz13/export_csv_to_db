from rest_framework import filters


class ReportDateFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        date_from = request.GET.get("date_from")
        date_to = request.GET.get("date_to")

        if date_from:
            queryset = queryset.filter(report_date__gte=date_from)
        if date_to:
            queryset = queryset.filter(report_date__lte=date_to)
        return queryset
