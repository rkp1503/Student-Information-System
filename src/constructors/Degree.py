"""
Author: Rayla Kurosaki

GitHub: https://github.com/rkp1503

File: Degree.py
"""


class Degree:
    def __init__(self, plan_code: str, name: str):
        self.plan_code: str = plan_code
        self.name: str = name
        pass

    def get_plan_code(self) -> str:
        return self.plan_code

    def get_name(self) -> str:
        return self.name

    pass
