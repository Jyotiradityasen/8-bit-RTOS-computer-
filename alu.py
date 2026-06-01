"""
alu.py
------
Arithmetic Logic Unit.

Operates on two 8-bit inputs (A and B) and produces an 8-bit result
plus flags:
  - Z (zero)  : set when result == 0
  - C (carry) : set when an add overflows or a sub borrows
"""

from .register import Register


class ALU:
    def __init__(self, reg_a: Register, reg_b: Register):
        self.a = reg_a
        self.b = reg_b
        self.zero_flag = False
        self.carry_flag = False

    # ------------------------------------------------------------------ #
    # Core operations
    # ------------------------------------------------------------------ #
    def add(self) -> int:
        result = self.a.value + self.b.value
        self.carry_flag = result > 0xFF
        result &= 0xFF
        self.zero_flag = (result == 0)
        return result

    def sub(self) -> int:
        # Two's complement subtraction: A + (~B + 1)
        result = self.a.value - self.b.value
        self.carry_flag = result < 0          # "borrow"
        result &= 0xFF
        self.zero_flag = (result == 0)
        return result

    def and_(self) -> int:
        result = self.a.value & self.b.value
        self.zero_flag = (result == 0)
        self.carry_flag = False
        return result

    def or_(self) -> int:
        result = self.a.value | self.b.value
        self.zero_flag = (result == 0)
        self.carry_flag = False
        return result

    def xor(self) -> int:
        result = self.a.value ^ self.b.value
        self.zero_flag = (result == 0)
        self.carry_flag = False
        return result

    def not_a(self) -> int:
        result = (~self.a.value) & 0xFF
        self.zero_flag = (result == 0)
        self.carry_flag = False
        return result
