INCLUDE Irvine32.inc
main EQU start@0

.stack 4096

ExitProcess proto, dwExitCode: DWORD
FindLargest proto, aPtr: PTR SDWORD, arraySize: DWORD               ; declare prototype of FindLargest

.data
Ex1Array SDWORD 105522063, 110502531, 110502567                     ; initialize Ex1Array
Ex2Array SDWORD -105522063, -110502531, -110502567                  ; initialize Ex2Array

.code
main PROC
    invoke FindLargest, OFFSET Ex1Array, LENGTHOF Ex1Array    
    invoke FindLargest, OFFSET Ex2Array, LENGTHOF Ex2Array          ; call FindLargest
    call WaitMsg                                                    ; pause the current program
    invoke ExitProcess, 0
main ENDP

FindLargest PROC,
    aPtr:PTR SDWORD, arraySize:DWORD
    push esi                ; push esi to stack
    push ecx                ; push ecx to stack
    mov eax, 80000000h      ; eax = smallest possible 32bit signed integer
    mov esi, aPtr           ; point to the first element
    mov ecx, arraySize      ; set iteration times

L1:
    cmp eax, [esi]          ; compare the current value and current maximum 
    jg L2                   ; if smaller than max, jump to L2
    mov eax, [esi]          ; update max value

L2:
    add esi, 4              ; esi += 4
    loop L1

    call WriteInt           ; print out the largest value
    call Crlf               ; nextline

    pop ecx                 ; pop ecx from stack
    pop esi                 ; pop esi from stack

    ret                     ; return from subroutine
FindLargest ENDP
    
END main