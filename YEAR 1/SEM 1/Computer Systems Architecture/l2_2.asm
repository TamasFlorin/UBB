;  Compute E = (64+c+b) - (a+d) where a,d-byte and b,c-word
assume ds:data,cs:code

data segment
	a db 100
	d db 4
	
	b dw 100
	c dw 100
	
	e dw ?
data ends

code segment
start:
	mov ax,data
	mov ds,ax
	
	mov al,a ; al:=a 
	cbw ; convert byte to signed word
	
	mov bx,ax ; bx: = ax = a
	
	mov al,d ; al:=d
	cbw ; convert byte to signed word
	
	add bx,ax ; bx:=bx + ax = a + d
	
	mov ax,64 ; ax:=64
	add ax,c ; ax:=ax+c = 64 + c
	add ax,b ; ax:=ax + b = 64 + c + b
	
	sub ax,bx ; ax:= ax - bx
	
	mov e,ax ; e:= (64+c+b)-(a+d)
	
	mov ax,4c00h
	int 21h

code ends
end start