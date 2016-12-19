; compute the gcd of two values represented on 32 bits
[bits 32]

section .text 

extern  _printf
extern _exit

global  _main 

_main: 
		repeat_op:
			mov eax,[x] ; eax stores the value of x
			cmp eax,[y] ; we now compare x with y
			jg dec_x ; if x is greater we have to decrement it
			
			; decrement y
			mov ebx,[x]
			sub [y],ebx
			jmp check
			; decrement x's value
			dec_x:
			mov ebx,[y]
			sub [x],ebx
			
			; check if x==y,if so we can stop
			check:
			mov eax,[x]
			cmp eax,[y]
			je to_end
			jmp repeat_op
			
		
		to_end:
		push DWORD [x]
		push format
		call _printf
		add esp,2*4
		
        push    0
        call    _exit
        ret 

section .data

x: dd 15
y: dd 40
format: db 'cmmdc=%d'