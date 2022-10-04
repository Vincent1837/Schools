INCLUDE Irvine32.inc
.data 

Result BYTE 9 DUP(?)

.code 
main PROC 
	mov ecx,LENGTHOF Result		;ecx = 9
	mov eax,9					;eax = 9
	mov esi,OFFSET Result	    ;esi = &Result

	L1:
		mov [esi],eax			;*esi = eax
		add eax,9				;eax += 9
		inc esi					;esi += 1
		LOOP L1					;ecx = ecx - 1, if ecx != 0, jump to L1

exit

main ENDP 
END main