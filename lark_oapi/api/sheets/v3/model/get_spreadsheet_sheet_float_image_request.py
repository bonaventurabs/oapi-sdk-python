# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class GetSpreadsheetSheetFloatImageRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.spreadsheet_token: Optional[str] = None
        self.sheet_id: Optional[str] = None
        self.float_image_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetSpreadsheetSheetFloatImageRequestBuilder":
        return GetSpreadsheetSheetFloatImageRequestBuilder()


class GetSpreadsheetSheetFloatImageRequestBuilder(object):

    def __init__(self,
                 get_spreadsheet_sheet_float_image_request: GetSpreadsheetSheetFloatImageRequest = GetSpreadsheetSheetFloatImageRequest()) -> None:
        get_spreadsheet_sheet_float_image_request.http_method = HttpMethod.GET
        get_spreadsheet_sheet_float_image_request.uri = "/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/float_images/:float_image_id"
        get_spreadsheet_sheet_float_image_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._get_spreadsheet_sheet_float_image_request: GetSpreadsheetSheetFloatImageRequest = get_spreadsheet_sheet_float_image_request

    def spreadsheet_token(self, spreadsheet_token: str) -> "GetSpreadsheetSheetFloatImageRequestBuilder":
        self._get_spreadsheet_sheet_float_image_request.spreadsheet_token = spreadsheet_token
        self._get_spreadsheet_sheet_float_image_request.paths["spreadsheet_token"] = spreadsheet_token
        return self

    def sheet_id(self, sheet_id: str) -> "GetSpreadsheetSheetFloatImageRequestBuilder":
        self._get_spreadsheet_sheet_float_image_request.sheet_id = sheet_id
        self._get_spreadsheet_sheet_float_image_request.paths["sheet_id"] = sheet_id
        return self

    def float_image_id(self, float_image_id: str) -> "GetSpreadsheetSheetFloatImageRequestBuilder":
        self._get_spreadsheet_sheet_float_image_request.float_image_id = float_image_id
        self._get_spreadsheet_sheet_float_image_request.paths["float_image_id"] = float_image_id
        return self

    def build(self) -> GetSpreadsheetSheetFloatImageRequest:
        return self._get_spreadsheet_sheet_float_image_request