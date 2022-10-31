INCLUDE Irvine32.inc

.data
ChStrs BYTE "################      ##      ##      ##      ##      ##      ##"
BitStrs BYTE 8 DUP(?)

.code

change PROC
	mov edi, 0						; edi = 0
	L3:	
		cmp ChStrs[esi], '#'		
		je L2						; jump to L2 if char is '#'
		mov BitStrs[edi], '0'		; else write '0' if blank
		jmp L4						; jump to L4
		L2:
			mov BitStrs[edi], '1'	; write '1'
		L4:
			inc esi					; ++esi
			inc edi					; ++edi
			cmp edi, 8				
			jne L3					; loop L3 if edi != 8
	mov edx, OFFSET BitStrs			; move the address to edx
	CALL writestring				; print to console
	CALL Crlf						; new line
	RET								; return
change ENDP

main PROC
	
	mov esi, 0						; esi = 0
	mov ecx, 8						; ecx = 8
	L1:
		CALL change					; invoke process 'change'
		LOOP L1						;ecx = ecx - 1, if ecx != 0, jump to L1
	
	exit

main ENDP
END main