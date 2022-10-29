INCLUDE Irvine32.inc
.data 

Value1 SBYTE 03h
Value2 SBYTE 02h
Value3 SBYTE 8fh
Result SDWORD ?

.code 
main PROC 

movsx eax,Value1	; eax = Value1
movsx ebx,Value2	; ebx = Value2
add eax,ebx			; eax = eax + ebx = Value1 + Value2

mov ebx,eax			; ebx = eax = Value1 + Value2
shl eax,4			; eax = eax * 16 = (Value1 + Value2) * 16
shl ebx,1			; ebx = ebx * 2 = (Value1 + Value2) * 2

sub eax,ebx			; eax = eax - ebx = (16 - 2) * (Value1 + Value2);
movsx ecx,Value3	; ecx = Value3
sub ecx,eax			; ecx = ecx - eax = Value3 - 14 * (Value1 + Value2)
neg ecx				; ecx = -ecx = -(Value3 - 14 * (Value1 + Value2))

mov Result,ecx		; Result

exit

main ENDP 
END main

