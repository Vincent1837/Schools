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
	mov eax,[esi]
	add eax,17
	mov [esi],eax
	inc esi
	LOOP L1
	ret
Convert ENDP

Convert2 PROC
;	Convert a char array by the rules of 0 to A, 1 to B and so on.
;	Receives: esi,eax,ecx
;	Returns: nothing
;	Requires: nothing
;------------------------------------------------------------------

push eax
L1:
	mov eax,[esi]
	add eax,17
	mov [esi],eax
	inc esi
	LOOP L1
pop eax	
ret
Convert2 ENDP


main PROC 

mov eax,9999h
mov ebx,9999h
mov ecx,9999h

mov esi,OFFSET myID
mov ecx,LENGTHOF myID
call Convert

mov esi,OFFSET myID2
mov ecx,LENGTHOF myID2
call Convert2

exit
main ENDP 
END main
