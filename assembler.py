"""
assembler.py
------------
A tiny two-pass assembler so you can write programs like:

    LDI 5
    STA 15
    LDA 15
    ADD 15
    OUT
    HLT

Supports labels:

    start:  LDI 1
            OUT
            JMP start

And raw data with `.byte`:

    counter: .byte 0
"""

import re
from . import instructions as ins


class AssemblerError(Exception):
    pass


def assemble(source: str) -> list[int]:
    """Take assembly text and return a list of machine code bytes."""
    lines = source.splitlines()

    # Pass 1: figure out addresses for each label
    labels: dict[str, int] = {}
    cleaned: list[tuple[str, str]] = []   # (label_or_empty, instruction_text)
    address = 0

    for raw in lines:
        # Strip comments and whitespace
        line = raw.split(";", 1)[0].strip()
        if not line:
            continue

        # Label?
        m = re.match(r"^([A-Za-z_]\w*):\s*(.*)$", line)
        if m:
            label, rest = m.group(1), m.group(2).strip()
            if label in labels:
                raise AssemblerError(f"duplicate label: {label}")
            labels[label] = address
            if not rest:
                continue
            line = rest

        cleaned.append(line)
        address += 1
        if address > 256:
            raise AssemblerError("program too large (>256 bytes)")

    # Pass 2: emit bytes
    output: list[int] = []
    for line in cleaned:
        parts = line.split()
        mnemonic = parts[0].upper()
        arg = parts[1] if len(parts) > 1 else None

        # Raw data
        if mnemonic == ".BYTE":
            if arg is None:
                raise AssemblerError(".byte needs a value")
            output.append(_parse_number(arg, labels) & 0xFF)
            continue

        # Opcode lookup
        opcode_map = {name: code for code, name in ins.OPCODE_NAMES.items()}
        if mnemonic not in opcode_map:
            raise AssemblerError(f"unknown mnemonic: {mnemonic}")
        opcode = opcode_map[mnemonic]

        operand = 0
        if arg is not None:
            operand = _parse_number(arg, labels) & 0xF

        output.append(ins.encode(opcode, operand))

    return output


def _parse_number(token: str, labels: dict[str, int]) -> int:
    """Parse a number or label reference."""
    if token in labels:
        return labels[token]
    if token.lower().startswith("0x"):
        return int(token, 16)
    if token.lower().startswith("0b"):
        return int(token, 2)
    try:
        return int(token)
    except ValueError:
        raise AssemblerError(f"can't parse token: {token!r}")
