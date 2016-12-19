; Compute (a*a/b+b*b)/(2+b)+e where a-byte; b-word; e-doubleword

assume cs:code,ds:data

data segment
	a db 4
	b dw 2
	e dd 1
data ends

code segment
start:
	mov ax,data
	mov ds,ax
	
	mov ah,0 ; use the unsigned value
	mov al,a; al:=a=04h
	mul a ; ax:=al * a=10h
	
	div b ; ax:= ax / b,dx:=ax % b => ax=8h
	
	mov bh,0
	mov bx,ax ; bx:=ax=a*a/b = 8h
	
	mov ah,0
	mov ax,b; ax:=b=2h
	mul b ; ax:dx:=ax*b=b*b => ax=4h,dx=0h
	
	mov ah,0
	add ax,bx ; ax:=ax + bx = (a*a/b + b*b) = Ch
	
	mov bx,b ; bx:=b=2h
	mov bh,0
	add bx,2 ;bx:=bx+2=4h
	
	div bx ; ax:=dx:ax/bx,dx:=dx:ax % bx => ax:=(a*a/b + b*b) / (2+b) = 4h
	
	mov ah,0
	add ax,word ptr e ; ax:=ax + e = 4h
	mov dh,0
	adc dx,word ptr e+2; dx:=dx +(e+2) = 0h
	
	mov ax,4c00h
	int 21h
code ends
end start