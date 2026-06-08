"""8-bit computer emulator (SAP-1 inspired)."""

from .register import Register
from .memory import Memory
from .alu import ALU
from .bus import Bus
from .cpu import CPU
from .assembler import assemble, AssemblerError
from . import instructions

__all__ = [
    "Register", "Memory", "ALU", "Bus", "CPU",
    "assemble", "AssemblerError", "instructions",
]
__version__ = "1.0.0"
