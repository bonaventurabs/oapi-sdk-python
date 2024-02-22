# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .country_region_subdivision import CountryRegionSubdivision


class SearchBasicInfoCountryRegionSubdivisionResponseBody(object):
    _types = {
        "items": List[CountryRegionSubdivision],
        "page_token": str,
        "has_more": bool,
    }

    def __init__(self, d=None):
        self.items: Optional[List[CountryRegionSubdivision]] = None
        self.page_token: Optional[str] = None
        self.has_more: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SearchBasicInfoCountryRegionSubdivisionResponseBodyBuilder":
        return SearchBasicInfoCountryRegionSubdivisionResponseBodyBuilder()


class SearchBasicInfoCountryRegionSubdivisionResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._search_basic_info_country_region_subdivision_response_body = SearchBasicInfoCountryRegionSubdivisionResponseBody()

    def items(self,
              items: List[CountryRegionSubdivision]) -> "SearchBasicInfoCountryRegionSubdivisionResponseBodyBuilder":
        self._search_basic_info_country_region_subdivision_response_body.items = items
        return self

    def page_token(self, page_token: str) -> "SearchBasicInfoCountryRegionSubdivisionResponseBodyBuilder":
        self._search_basic_info_country_region_subdivision_response_body.page_token = page_token
        return self

    def has_more(self, has_more: bool) -> "SearchBasicInfoCountryRegionSubdivisionResponseBodyBuilder":
        self._search_basic_info_country_region_subdivision_response_body.has_more = has_more
        return self

    def build(self) -> "SearchBasicInfoCountryRegionSubdivisionResponseBody":
        return self._search_basic_info_country_region_subdivision_response_body