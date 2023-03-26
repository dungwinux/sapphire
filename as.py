# Inspired by https://github.com/corkami/docs/blob/master/x86/x86.md#switching-between-32b-and-64b-modes

# pip install keystone-engine
from keystone import *

# Address are placeholder here. Will be replaced at runtime
# Part of the assembly use codegolf techniques.
# See https://codegolf.stackexchange.com/questions/132981/tips-for-golfing-in-x86-x64-machine-code
CODE = b"""
    mov     eax, 0x30A95DCA
    sub     eax, 0x2f
    test    eax, eax
    jne     loop_end
    mov     r8, 0x22C73994A5390DB2
    mov     r9, 0x17DDBA9051227F8F
    xor     esi, esi
    lea     rdx, [rsi + 0x3c]
    lea     rcx, [rsi + 0x41]
    lea     r10, [rsi + 0xD3]
    lea     r11, [rsi + 0xF7]
loop:
    cmp     rsi, 0x2f
    jae     loop_end
    mov     al, [r9 + rsi]
    ror     al, 1
    xor     al, [r8 + rsi]
    xor     al, dl
    test    al, al
    xchg    edx, ecx
    xchg    ecx, r10d
    xchg    r10d, r11d
    jnz     loop_end
    lea     rsi, [rax + rsi + 1]
    jmp     loop
loop_end:
    mov     rdx, 0x2E3325CF3A909908
    mov     [rdx], rax
"""

try:
    ks = Ks(KS_ARCH_X86, KS_MODE_64)
    encoding, count = ks.asm(CODE)
    print("%s = %s (number of statements: %u)" %(CODE, encoding, count))
    print("Formatted string: {}".format(bytes(encoding)))
    print("Bytes: {}".format(" ".join([hex(x)[2:].rjust(2, "0") for x in encoding])))
    print("C-style: {}".format(",".join(["0x" + hex(x)[2:].rjust(2, "0") for x in encoding])))
    print("Length {}".format(hex(len(encoding))))
except KsError as e:
    print("ERROR: %s" %e)
