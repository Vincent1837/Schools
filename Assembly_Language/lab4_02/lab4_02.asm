INCLUDE Irvine32.inc
.data 

MyID BYTE "110502531"
MyID2 BYTE "110502567"

.code

Convert PROC USES eax
;	Convert a char array by the rules of 0 to A, 1 to B and so on.
;	Receives: esi,eax,ecx
;	Returns: nothing
;	Requires: nothing
;------------------------------------------------------------------

L1:
	mov al,[esi]		;move [esi] to al
	add al,17			;al = al + 17
	mov [esi],al		;move al to [esi]
	inc esi				;++esi
	LOOP L1				;--ecx, if ecx != 0 then jumpt to L1
	ret
Convert ENDP

Convert2 PROC
;	Convert a char array by the rules of 0 to A, 1 to B and so on.
;	Receives: esi,eax,ecx
;	Returns: nothing
;	Requires: nothing
;------------------------------------------------------------------

push eax				;push eax to stack
L1:
	mov al,[esi]		;move [esi] to al
	add al,17			;al = al + 17
	mov [esi],al		;move al to [esi]
	inc esi				;++esi
	LOOP L1				;--ecx, if ecx != 0 then jumpt to L1
pop eax					;pop eax from stack
ret
Convert2 ENDP


main PROC 

mov eax,9999h			;eax = 9999h
mov ebx,9999h			;ebx = 9999h
mov edx,9999h			;edx = 9999h

mov esi,OFFSET MyID		;esi = position of MyID
mov ecx,LENGTHOF MyID	;ecx = length of MyID
call Convert

mov esi,OFFSET MyID2	;esi = position of MyID2
mov ecx,LENGTHOF MyID2	;ecx = length of MyID2
call Convert2

exit
main ENDP 
END main



