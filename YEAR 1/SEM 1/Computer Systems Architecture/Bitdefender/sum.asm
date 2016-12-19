; compute the sum of two numbers represented on 32 bits
[bits 32]

section .text 

extern  _printf
extern _exit

global  _main 

_main: 
		; copy the value of a into eax
        mov eax,[a]
		
		; add b to eax = a + b
		add eax,[b]
		
		mov [rez],eax
		
		; print the result
		push DWORD [res]
		push DWORD [b]
		push DWORD [a]
		push format
		call _printf
		add esp,4*3
        push    0
        call    _exit
        ret 

section .data

a: dd 1
b: dd 2
res: dd 0
format: db "%d + %d = %d",0