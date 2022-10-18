INCLUDE Irvine32.inc

.data 
myID BYTE "110502531"
myID2 BYTE "110502567"
result BYTE 9 DUP(?)
size_ID BYTE 9

.code
main PROC

	mov esi,0			; esi = 0
	movzx ecx,size_ID	; ecx = 9

L1:
	mov al,myID[esi]	; al = myID[esi]
	mov bl,myID2[esi]	; bl = myID2[esi]
	cmp al,bl			; compare al with bl 
	ja L2				; jump tp L2 if al > bl
	jb L3				; jump to L3 if al < bl
	
	mov result[esi],'A'	; move 'A' to result[esi] if not jumped
	jmp L4				; jump to L4

L2:
	mov result[esi],'B'	; move 'B' to result[esi]
	jmp L4				; jump to L4

L3:
	mov result[esi],'C'	; move 'C' to result[esi]

L4:
	inc esi				; ++esi
	LOOP L1				; ecx = ecx - 1, if ecx != 0, jump to L1
	exit				
main ENDP
END main

