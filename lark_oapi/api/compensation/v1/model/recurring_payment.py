# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class RecurringPayment(object):
    _types = {
        "id": str,
        "unique_id": str,
        "user_id": str,
        "item_id": str,
        "issuance_type": str,
        "each_amount": str,
        "start_date": str,
        "end_date": str,
        "issuance_period": str,
        "currency_id": str,
        "remark": str,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.unique_id: Optional[str] = None
        self.user_id: Optional[str] = None
        self.item_id: Optional[str] = None
        self.issuance_type: Optional[str] = None
        self.each_amount: Optional[str] = None
        self.start_date: Optional[str] = None
        self.end_date: Optional[str] = None
        self.issuance_period: Optional[str] = None
        self.currency_id: Optional[str] = None
        self.remark: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "RecurringPaymentBuilder":
        return RecurringPaymentBuilder()


class RecurringPaymentBuilder(object):
    def __init__(self) -> None:
        self._recurring_payment = RecurringPayment()

    def id(self, id: str) -> "RecurringPaymentBuilder":
        self._recurring_payment.id = id
        return self

    def unique_id(self, unique_id: str) -> "RecurringPaymentBuilder":
        self._recurring_payment.unique_id = unique_id
        return self

    def user_id(self, user_id: str) -> "RecurringPaymentBuilder":
        self._recurring_payment.user_id = user_id
        return self

    def item_id(self, item_id: str) -> "RecurringPaymentBuilder":
        self._recurring_payment.item_id = item_id
        return self

    def issuance_type(self, issuance_type: str) -> "RecurringPaymentBuilder":
        self._recurring_payment.issuance_type = issuance_type
        return self

    def each_amount(self, each_amount: str) -> "RecurringPaymentBuilder":
        self._recurring_payment.each_amount = each_amount
        return self

    def start_date(self, start_date: str) -> "RecurringPaymentBuilder":
        self._recurring_payment.start_date = start_date
        return self

    def end_date(self, end_date: str) -> "RecurringPaymentBuilder":
        self._recurring_payment.end_date = end_date
        return self

    def issuance_period(self, issuance_period: str) -> "RecurringPaymentBuilder":
        self._recurring_payment.issuance_period = issuance_period
        return self

    def currency_id(self, currency_id: str) -> "RecurringPaymentBuilder":
        self._recurring_payment.currency_id = currency_id
        return self

    def remark(self, remark: str) -> "RecurringPaymentBuilder":
        self._recurring_payment.remark = remark
        return self

    def build(self) -> "RecurringPayment":
        return self._recurring_payment