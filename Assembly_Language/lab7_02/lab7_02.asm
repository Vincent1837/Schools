INCLUDE Irvine32.inc

divide MACRO dividend, divisor, quotient, remainder
	push ax				; push ax to stack
	push dx				; push dx to stack
	IFB <dividend>
		EXITM
	ENDIF
	IFB <divisor>
		EXITM
	ENDIF				; check if there exist empty parameters
	mov dx,0			; clear dx
	mov ax,dividend		; ax = dividend
	idiv divisor		; perform division
	mov quotient,ax		; quotient = ax
	mov remainder,dx	; remainder = dx
	pop dx				; pop dx from stack
	pop ax				; pop ax from stack

ENDM

.data
dividend WORD 2531
divisor WORD 100
quotient WORD 1 DUP(?)
remainder WORD 1 DUP(?)

.code
main PROC
	movsx eax,dividend
	call WriteDec
	call Crlf			; print dividend

	divide dividend, divisor, quotient, remainder

	movsx eax,quotient
	call WriteDec
	call Crlf			; print quotient

	movsx eax,remainder
	call WriteDec
	call Crlf			; print remainder

	exit
main ENDP
END main