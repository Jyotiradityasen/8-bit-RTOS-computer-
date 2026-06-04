/*
 * memory.h
 * --------
 * 256 bytes of RAM (one byte per 8-bit address).
 */
#ifndef MEMORY_H
#define MEMORY_H

#include <stdint.h>
#include <stddef.h>

#define MEM_SIZE 256

typedef struct {
    uint8_t cells[MEM_SIZE];
} memory_t;

void    mem_init(memory_t *m);
uint8_t mem_read(const memory_t *m, uint8_t addr);
void    mem_write(memory_t *m, uint8_t addr, uint8_t val);
void    mem_load(memory_t *m, const uint8_t *bytes, size_t n, uint8_t start);

#endif
