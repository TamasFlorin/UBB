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
	
	mov al,a; al:=a=04h
	imul a ; ax:=al * a=10h
	
	idiv b ; ax:= ax / b,dx:=ax % b => ax=8h
	
	mov bx,ax ; bx:=ax=a*a/b = 8h
	
	mov ax,b; ax:=b=2h
	imul b ; ax:dx:=ax*b=b*b => ax=4h,dx=0h
	
	add ax,bx ; ax:=ax + bx = (a*a/b + b*b) = Ch
	
	mov bx,b ; bx:=b=2h
	add bx,2 ;bx:=bx+2=4h
	
	idiv bx ; ax:=dx:ax/bx,dx:=dx:ax % bx => ax:=(a*a/b + b*b) / (2+b) = 4h
	
	add ax,word ptr e ; ax:=ax + e = 4h
	adc dx,word ptr e+2; dx:=dx +(e+2) = 0h
	
	mov ax,4c00h
	int 21h
code ends
end start