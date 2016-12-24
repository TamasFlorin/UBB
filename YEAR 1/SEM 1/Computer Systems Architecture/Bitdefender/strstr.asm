[bits 32]

section .text 

extern  _printf
extern _exit

global  _main

; stdcall(char *str)
; we will store the result in ebx
; note that we are only storing the result in ebx for convenience(it should be stored in eax)
_strlen:
	push ebp
	mov ebp,esp
	
	; take the string from the stack
	mov esi,[ebp+8]
	
	mov ebx,0
	
	count:
		mov dl,byte [esi]
		cmp dl,0
		je end_
		inc ebx
		inc esi
		jmp count
	
	end_:
	pop ebp
	ret 4
	
; stdcall(char *haystack,char*needle)
; we will be using esi and edi and the result will be stored in eax
_strstr:
	push ebp
	mov ebp,esp
	
	push esi 
	push edi
	
	mov esi,[ebp+8] ; haystack
	mov edi,[ebp+12] ; needle
	
	mov ebx,esi
	mov eax,edi
	
	search:
		mov esi,ebx; will hold current haystack value
		mov edi,eax ; will hold current needle value
		
		mov dl,byte [esi]
		cmp dl,0
		je not_found
	loop_needle:
			mov dl,byte [esi]
			mov dh,byte [edi]
			cmp dl,dh
			jne continue_search
			inc esi
			inc edi
			mov dl,byte [edi]
			cmp dl,0
			je found
			jmp loop_needle
		continue_search:
			inc ebx
			jmp search
		not_found:
			mov eax,0
			jmp to_end
		found:
			mov eax,ebx
	to_end:
	
	pop edi
	pop esi
	
	pop ebp
	ret 2*4 ; also clean the stack
_main:
		push needle
		push haystack
		call _strstr
		cmp eax,0
		je print_not_found
		
		push needle
		call _strlen
		
		push ebx
		; the result is stored in eax
		sub eax,haystack
		push eax
		push format
		call _printf
		add esp,8
		jmp to_exit
		
		print_not_found:
			push message
			call _printf
			add esp,4
		to_exit:
        push    0
        call    _exit
        ret 

section .data
message: db 'substring not found',0
format: db '[%d,%d]',0
haystack: db 'banana',0
needle: db 'ana',0