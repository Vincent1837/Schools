INCLUDE Irvine32.inc
.data
consoleHandle    DWORD ?
xyInit COORD <32,8> ; starting coordinate
xyBound COORD <80,25> ; Border
xyPos COORD <32,8> ; position of cursor 

main EQU start@0
.code
main PROC

; Get the Console standard output handle:
	INVOKE GetStdHandle, STD_OUTPUT_HANDLE
	mov consoleHandle,eax
	
; set the starting position 
INITIAL:
	mov ax,xyInit.x
	mov xyPos.x,ax
	mov ax,xyInit.y
	mov xyPos.y,ax
START:
	call ClrScr
	INVOKE SetConsoleCursorPosition, consoleHandle, xyPos
	call ReadChar
	.IF ax == 4800h ;UP
		sub xyPos.y,1
	.ENDIF
	.IF ax == 5000h ;DOWN
		add xyPos.y,1
	.ENDIF
	.IF ax == 4B00h ;LEFT
		sub xyPos.x,1
	.ENDIF
	.IF ax == 4D00h ;RIGHT
		add xyPos.x,1
	.ENDIF
	.IF ax == 011Bh ;ESC
		jmp END_FUNC
	.ENDIF
	
	; examine if each directions are over the border.
	.IF xyPos.x == 0h ;x lowerbound
		jmp INITIAL ; if over the border then stay at the original position.
	.ENDIF
	mov ax,xyBound.x ; p.s. when comparing can¡¦t use two-address, so we turn one of them into register.
	.IF xyPos.x == ax ;x upperbound
		jmp INITIAL ; if over the border then stay at the original position.
	.ENDIF
	
	.IF xyPos.y == 0h ;y lowerbound
		jmp INITIAL ; if over the border then stay at the original position.
	.ENDIF
	mov ax,xyBound.y
	.IF xyPos.y == ax ;y upperbound
		jmp INITIAL ; if over the border then stay at the original position.
	.ENDIF
	
	jmp START
END_FUNC:
	exit
main ENDP

END main
