;  Compute e = i - (j/g) + 5 where 1<=i<=255 , 2<=j<=126 , 1<=g<=100
assume cs:code,ds:data
data segment
	i db 255
	j db 126
	g db 100
	e dw 0
data ends

code segment
start:
	mov ax,data
	mov ds,ax
	
	mov al,j ; al:=j
	mov ah,0 ; use the unsigned representation of ax
	div g ; al:=ax/g
	mov ah,0 ; set ax to be an unsigned value
	
	mov bx,ax ; bx:=ax= (j/g)
	mov al,i ; al:=i
	mov ah,0 ; set ax to be an unsigned value
	
	sub ax,bx ; ax:=ax-bx=i - (j/g)
	add ax,5 ; ax:=ax+5 =i- (j/g) + 5
	mov e,ax ; e = i- (j/g) + 5
	
	mov ax,4C00h
	int 21h
code ends
end start