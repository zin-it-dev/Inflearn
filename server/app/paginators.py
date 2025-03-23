class PageNumberPagination:
    def __init__(self, page_size):
        self.page_size = page_size


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 20


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10


class ExtraLargeResultsSetPagination(PageNumberPagination):
    page_size = 50
