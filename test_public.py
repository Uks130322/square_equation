import dataclasses

import pytest

from sq_equat import sq_equat


@dataclasses.dataclass
class Case:
    parameters: tuple[int, int, int]
    result: list

    def __str__(self) -> str:
        return f"{self.parameters[0]} * x ** 2 + {self.parameters[1]} * x + {self.parameters[2]} = 0"


TEST_CASES = [
    Case(parameters=(0, 0, 0), result=["Any number is a root"]),
    Case(parameters=(1, 2, 7), result=["No roots"]),
    Case(parameters=(1, -4, 4), result=[2.0]),
    Case(parameters=(1, 6, 5), result=[-7.0, 1.0]),
    Case(parameters=(1, 11, 8), result=[-27.75, 16.75])

]


@pytest.mark.parametrize("t", TEST_CASES, ids=str)
def test_norm_phone(t: Case) -> None:
    assert sq_equat(*t.parameters) == t.result



