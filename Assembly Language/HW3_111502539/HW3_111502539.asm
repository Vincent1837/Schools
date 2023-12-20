INCLUDE Irvine32.inc

CountMatches proto, aptr1: PTR SDWORD, aptr2: PTR SDWORD, arraySize: DWORD


.data
    array1 SDWORD 10, 5, 4, -6, 2, 11, 12
    array2 SDWORD 10, 5, 3, 1, 4, 2, -6

.code
MAIN PROC
    call DumpRegs       ; print registers

    invoke CountMatches, OFFSET array1, OFFSET array2, LENGTHOF array1
    call WriteInt       ; print eax
    call Crlf           ; new line

    call DumpRegs       ; print registers
    
    call WaitMsg        ; wait for input
    exit

MAIN ENDP

CountMatches PROC,
    aptr1: PTR SDWORD, aptr2: PTR SDWORD, arraySize: DWORD
    
    push esi    ; push esi to stack
    push edi    ; push edi to stack
    push ebx    ; push ebx to stack
    push ecx    ; push ecx to stack
    
    mov esi, aptr1
    mov edi, aptr2
    mov ecx, arraySize
    mov eax, 0

    L1:
        mov ebx, [esi]      ; ebx = elements in array1
        cmp ebx, [edi]      ; compare ebx with elements in array2
        jne Final           ; jump to Final if not equal

    Equal:      
        inc eax             ; eax += 1 if equal

    Final:
        add esi, 4          ; esi += 4
        add edi, 4          ; edi += 4
        LOOP L1
    
    pop ecx     ; pop ecx from stack
    pop ebx     ; pop ebx from stack
    pop edi     ; pop edi from stack
    pop esi     ; pop esi from stack

    ret
CountMatches ENDP

END main