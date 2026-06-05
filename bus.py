"""
bus.py
------
The shared 8-bit data bus.

In real hardware, only ONE component can drive the bus at a time
(everything else is in high-impedance state). We simulate that here
with a single value plus a "driver" tag for debugging.
"""


class Bus:
    def __init__(self):
        self._value = 0
        self._driver = None  # who put the value here (for tracing)

    def put(self, value: int, driver: str = "") -> None:
        self._value = value & 0xFF
        self._driver = driver

    def get(self) -> int:
        return self._value

    @property
    def driver(self) -> str | None:
        return self._driver

    def __repr__(self) -> str:
        return f"BUS={self._value:02X} (from {self._driver})"
