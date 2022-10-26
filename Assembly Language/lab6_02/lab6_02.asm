INCLUDE Irvine32.inc

.data
result byte 81 DUP(?)

.code
main PROC

mov esi,0		;esi = 0
mov cl,0		;cl = 0

L1:
	inc cl			;++cl
	mov dl,1		;dl = 1
	
	cmp cl,10					
	je L3			;if cl == 10, jump to L3

	L2:
		mov al,cl			;al = cl
		mul dl				;al = al * dl
		mov result[esi],al	;result[esi] = al
		inc esi				;++esi
		inc dl				;++dl
		cmp dl,10		
		je L1				;if dl == 10, jump to L1
		jmp L2				;else, jump to L2

L3:
	exit 
	main ENDP
	END main
		
