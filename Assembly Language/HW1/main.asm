INCLUDE Irvine32.inc

.data 
MyID DWORD ?
Digit0 BYTE 2
Digit1 BYTE 5
Digit2 BYTE 6
Digit3 BYTE 7

.code 
Main PROC 
	movzx edx, Digit0
	shl edx, 24		; 00000002 -> 02000000
	mov MyID, edx

	movzx edx, Digit1
	shl edx, 16		;00000005 -> 00050000
	add MyID, edx

	movzx edx, Digit2
	shl edx, 8		;00000006 -> 00000600
	add MyID, edx

	movzx edx, Digit3
	add MyID, edx
	exit 
Main ENDP 
END main
