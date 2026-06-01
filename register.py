"""
register.py
-----------
8-bit register implementation.

A register holds a single 8-bit value (0-255). The CPU uses several:
  - A and B: general purpose / ALU operands
  - IR: Instruction Register (holds current opcode + operand)
  - MAR: Memory Address Register (which RAM cell to access)
  - PC: Program Counter (which instruction is next)
  - OUT: Output register (what is "displayed")
"""


class Register:
    def __init__(self, name: str, bits: int = 8):
        self.name = name
        self.bits = bits
        self.mask = (1 << bits) - 1   # 0xFF for 8-bit
        self._value = 0

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, v: int) -> None:
        # Wrap on overflow, just like real hardware.
        self._value = v & self.mask

    def increment(self) -> None:
        self.value = self._value + 1

    def reset(self) -> None:
        self._value = 0

    def __repr__(self) -> str:
        return f"{self.name}={self._value:0{self.bits//4}X}h ({self._value:08b})"
