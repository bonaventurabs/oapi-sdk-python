# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class OnboardingTaskChange(object):
    _types = {
        "after_status": str,
        "task_code": str,
    }

    def __init__(self, d=None):
        self.after_status: Optional[str] = None
        self.task_code: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "OnboardingTaskChangeBuilder":
        return OnboardingTaskChangeBuilder()


class OnboardingTaskChangeBuilder(object):
    def __init__(self) -> None:
        self._onboarding_task_change = OnboardingTaskChange()

    def after_status(self, after_status: str) -> "OnboardingTaskChangeBuilder":
        self._onboarding_task_change.after_status = after_status
        return self

    def task_code(self, task_code: str) -> "OnboardingTaskChangeBuilder":
        self._onboarding_task_change.task_code = task_code
        return self

    def build(self) -> "OnboardingTaskChange":
        return self._onboarding_task_change
