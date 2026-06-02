
# 8-Bit Breadboard Computer

> A fully functional 8-bit computer built from scratch using discrete 7400-series logic chips — no microprocessor, no shortcuts. Includes a custom assembler and an automated build-and-flash toolchain.

<p align="center">
<img width="1532" height="1047" alt="computer" src="https://github.com/user-attachments/assets/754e1403-2a4e-4a62-a347-70813aec3319" /></p>

<p align="center">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=flat-square" alt="C++">
  <img src="https://img.shields.io/badge/Language-C-A8B9CC?style=flat-square" alt="C">
  <img src="https://img.shields.io/badge/Tooling-Python-3776AB?style=flat-square" alt="Python">
  <img src="https://img.shields.io/badge/Automation-Shell-4EAA25?style=flat-square" alt="Shell">
  <img src="https://img.shields.io/badge/Build-PlatformIO-FF7F00?style=flat-square" alt="PlatformIO">
  <img src="https://img.shields.io/badge/Logic-7400%20Series%20TTL-CC0000?style=flat-square" alt="7400 TTL">
</p>

---

## What this is

This is a working computer that I designed and wired by hand on breadboards. Instead of using a single off-the-shelf processor chip, it is built from individual logic gates, registers, and counters — the same building blocks that real CPUs are made of. The goal was to understand a computer from the transistor up: how it fetches an instruction, decodes it, does math, stores results, and shows output.

It runs real programs that I write in my own assembly language, assemble into machine code with a custom tool, and load onto the hardware with a single command.

---

## Highlights

- **Built from discrete logic** — clock, registers, arithmetic unit, RAM, program counter, instruction register, and a microcoded control unit, all wired by hand.
- **Custom assembler** — written in Python, it turns human-readable assembly into the machine code the hardware understands.
- **Automated build & flash pipeline** — a single shell command assembles a program, builds the firmware, and flashes the memory chips, replacing a slow and error-prone manual process.
- **Firmware in C++ / C** — written and uploaded through PlatformIO to program the memory chips that drive the control logic and the display.
- **Live visual debugging** — LED indicators on every bus and register make the machine's internal state visible in real time, which is how I traced and fixed wiring and timing bugs.

---

## How it works

The computer follows a classic fetch–decode–execute cycle:

1. **Fetch** — the program counter points to the next instruction in RAM, which is loaded into the instruction register.
2. **Decode** — the control unit reads the instruction and activates the right set of control signals for that step.
3. **Execute** — data moves across the shared bus between registers, the arithmetic unit performs the operation, and the result is stored or sent to the output display.

The control signals for every instruction are stored as **microcode** on memory chips, so adding or changing an instruction means updating the microcode rather than rewiring the board.

---

## Architecture

| Module | What it does |
|---|---|
| Clock | Drives the whole machine; supports single-step and continuous modes for debugging |
| Program Counter | Tracks the address of the next instruction |
| Registers (A / B) | Hold the values the arithmetic unit works on |
| Arithmetic Unit | Performs addition and subtraction |
| RAM | Stores the program and its data |
| Instruction Register | Holds the current instruction being executed |
| Control Unit | Microcode-driven; generates the control signals for each step |
| Output | Drives the display so results are human-readable |


---

## Toolchain

The software side is what turns a pile of logic chips into something programmable:

```
program.asm  ──►  assembler (Python)  ──►  machine code  ──►  flash script (shell)  ──►  memory chips
```

- **Assembler** — parses my assembly language and emits the binary machine code.
- **Firmware** — C++ / C built with PlatformIO, responsible for programming the memory chips.
- **Build script** — one shell command runs the whole flow end to end so testing a change is fast and repeatable.

---

## Repository layout

```
.
├── asm/            # Custom assembler (Python)
├── firmware/       # C++ / C firmware (PlatformIO project)
├── programs/       # Example assembly programs
├── scripts/        # Build & flash automation (shell)
├── docs/           # Photos and documentation
└── README.md
```
---

## Getting started

```bash
# 1. Assemble a program into machine code
./scripts/build.sh programs/example.asm

# 2. Flash it onto the hardware
./scripts/flash.sh
```

---

## What I learned

- How a CPU actually works at the level of individual gates and control signals.
- Reading datasheets and reasoning about propagation delay, timing, and bus contention.
- Designing an instruction set and writing the assembler that targets it.
- Building automation so the slow parts of the workflow happen with one command.
- Systematic hardware debugging — isolating a single faulty wire among hundreds.

---

## Built with

`C++` · `C` · `Python` · `Shell scripting` · `PlatformIO` · `7400-series TTL logic`

---

<p align="center">
  <em>Designed, wired, and programmed by Jyotiraditya Sen.</em>
</p>
