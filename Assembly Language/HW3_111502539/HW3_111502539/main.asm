include Irvine32.inc
.data 
String byte "Hello World!",0 
.code 
main PROC 
mov edx,offset String 
call writestring 
invoke ExitProcess,0 
main ENDP 
END main
