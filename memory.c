/*
 * memory.c
 * --------
 * 256-byte RAM. Address truncates to 8 bits via uint8_t so we
 * never index out of bounds.
 */
#include <string.h>
#include "memory.h"

void mem_init(memory_t *m) {
    memset(m->cells, 0, MEM_SIZE);
}

uint8_t mem_read(const memory_t *m, uint8_t addr) {
    return m->cells[addr];
}

void mem_write(memory_t *m, uint8_t addr, uint8_t val) {
    m->cells[addr] = val;
}

void mem_load(memory_t *m, const uint8_t *bytes, size_t n, uint8_t start) {
    /* Copy up to MEM_SIZE bytes, starting at `start`. Wraps on overflow
     * (matches what the Python side does). */
    for (size_t i = 0; i < n; i++) {
        m->cells[(uint8_t)(start + i)] = bytes[i];
    }
}
