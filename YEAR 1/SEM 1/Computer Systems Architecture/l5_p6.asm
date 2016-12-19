; Problem:6. The word A is given. Obtain the integer number n represented on the bits 0-2 of A. Then obtain the word B by rotating A n 
;				  positions to the right (without carry flag). 
assume cs:code,ds:data

data segment
	A dw 0000000000001111b
	B dw 0
	n db 0
	
data ends

code segment
start:
	mov ax,data
	mov ds,ax
	
	mov ax,A; ax:=A=0000000000001111b=Fh
	
	; we only care about the first 3 bits 
	and ax,00000000000000111b;ax:=0000000000000111b=7h
	
	mov ah,0 ; ah:=0h
	
	; n is represented by the value stored in al
	mov n,al ; n:=al=0000000000000111b=7h
	
	mov cl,n ; cl:=al=7h
	
	; we shift the bits to the right without carry flag
	shr ax,cl;ax:=0h
	
	mov B,ax; B:=ax=0h
	
	mov ax,4c00h
	int 21h
code ends
end start