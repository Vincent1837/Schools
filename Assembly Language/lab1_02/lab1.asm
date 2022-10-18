include Irvine32.inc

.data

.code
lab1 PROC
	mov al,00110001b ;al = 00110001b
	mov ah,31		 ;ah = 31
	mov ax,2531h     ;ax = 2531h
	mov dx,0eeeah    ;dx = 0eeeah
	sub dx,ax        ;dx = dx - ax
	exit

lab1 ENDP
END lab1