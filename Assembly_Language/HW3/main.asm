INCLUDE Irvine32.inc

CountMatches proto, ptrArr1: PTR SDWORD, ptrArr2: PTR SDWORD, length: DWORD

CountMatches PROC
    ptrArr1: PTR SDWORD, ptrArr2: PTR SDWORD, FindLargest, length: DWORD
    
    push esi    ; push esi to stack
    push edi    ; push edi to stack
    push ecx    ; push ecx to stack
    
    mov esi, ptrArr1
    mov edi, ptrArr2
    mov ecx, length
    mov eax, 0

    L1:
        cmp [esi], [edi]
        jne Final

    Equal:
        inc eax

    Final:
        add esi, 4
        add edi, 4
        LOOP L1
    
    pop ecx     ; pop ecx from stack
    pop edi     ; pop edi from stack
    pop esi     ; pop esi from stack

    ret

