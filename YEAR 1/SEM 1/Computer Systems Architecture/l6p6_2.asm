; Problem 6: 
; 				A byte string S is given. Obtain the string D1 which contains all the even numbers of S and the string S2 which contains all the odd numbers of S.
;				Example:
;				S: 1, 5, 3, 8, 2, 9
; 				D1: 8, 2
; 				D2: 1, 5, 3, 9

; Version with string instructions

assume cs:code,ds:data

data segment
	s db 1,5,3,8,2,9
	len EQU $-s 
	
	d1 db len dup(?) ; assume all of the numbers are even
	d2 db len dup(?) ; assume all of the numbers are odd
	two db 2
	
data ends

code segment
start:
	mov ax,data
	mov ds,ax
	
	mov cx,len
	jcxz to_end; make sure the length is not zero
	
	lea si,s ; put the address of the source string in si
	
	cld ; parse string from left to right
	
	mov bp,0 ; offset for d1
	mov ax,data
	mov ES,ax
	lea di,d2 ; destination index is d2
	
	operations:
	lodsb ; load byte into al
	
	mov bl,al ; make a copy of the number as we are going to divide it by two
	
	mov ah,0
	idiv two
	
	; if ah is zero then the number is even
	cmp ah,0
	je even_op
	
	; this will only get executed if the number is odd
	mov al,bl
	stosb
	;mov byte ptr d2[di],bl ; copy the current number into d2
	jmp continue
	
	even_op:
	mov byte ptr d1[bp],bl ; copy the current number into d1
	inc bp ; increment the offset for d1
	
	continue:
	loop operations
	
	to_end:
	mov ax,4c00h
	int 21h
code ends
end start