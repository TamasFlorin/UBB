; generate a random number

[bits 32]

section .text 

extern  _printf
extern _exit
extern __time32
extern _getchar

global  _main 

_main: 
		push 0 ; NULL
		call __time32 ; the result will be stored in eax
		mov [seed],eax
		add esp,4
		
		generate_random:
		    call _getchar ; the value is sotred in eax
			cmp eax,-1
			je to_end
			
			mov eax,[seed]
			shr eax,8

			; now bx contains bits 8-23 of eax
			mov [rand],ax
			
			; print the random number
			push dword [rand]
			push format
			call _printf
			add esp,4*2
			
			; generate the next seed(seed = rand ^ 2 + k )
			mov ax,[rand]
			mul ax ; dx:ax now contains the seed
			
			; move dx:ax into seed
			mov [seed],ax
			mov [seed+2],dx 
			
			; add k to seed
			mov eax,k
			add [seed],eax
			
			; continue generating
			jmp generate_random
			
		to_end:
			push    0
			call    _exit
			ret 

section .data

format:   db      '%d',0 
seed: dd 0
rand: dw 0
k: equ 66666 ; constant