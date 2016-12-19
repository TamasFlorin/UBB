; compute the sum of the absolute values of the given numbers
[bits 32]

section .text 

extern  _printf
extern _exit

global  _main 

_main: 
		mov ecx,0
		mov esi,v
		compute_sum:
			mov eax,[esi]
			; check if the value is greater than 0
			cmp eax,0
			jge add_to_sum ; if it is,we do not have to change the sign
			
			; we have to change the sign of eax
			neg eax
			
			add_to_sum:
			add [sum],eax ; add the value to the sum
			
			add esi,4 ; go to the next element in the vector
			inc ecx
			cmp ecx,[len] ; check if we have looped over all of the elements
			jl compute_sum
		
		; print the sum
		push DWORD [sum]
		push format
		call _printf 
		add esp,4*2
        
		push    0
        call    _exit
        ret 

section .data

v: dd 1, -10, 5, 2, 5, 0, -9, 17
len: dd ($-v)/4
format: db "sum=%d",0
sum: dd 0