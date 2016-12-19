; Problem 6: 
; 				A byte string S is given. Obtain the string D1 which contains all the even numbers of S and the string S2 which contains all the odd numbers of S.
;				Example:
;				S: 1, 5, 3, 8, 2, 9
; 				D1: 8, 2
; 				D2: 1, 5, 3, 9

; Version without string instructions

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
	
	; offsets have to be 0 in the beginning(as we want to start from the first element)
	mov si,0 ; offset for s
	mov bx,0 ; offset for d1
	mov di,0 ; offset for d2
	
	operations:
	mov ah,0
	mov al,byte ptr s[si] ; divide 
	
	; check if al contains an even number
	idiv two ; divide al by two and store the result into ax=> ah:=al % two,al:=al / two
	
	cmp ah,0 ; if ah is zero then s[si] contains an even number
	je even_op ; perform the operations related to the even number
	
	; this will only get executed if the number is odd
	mov al,byte ptr s[si] ; copy the current element from si into al
	mov byte ptr d2[di],al ; copy the element from al into the current position in d2
	inc di ; increment the offset for d2
	jmp checks ; perform the checks
	
	;this will only get executed if the number is even
	even_op:
	mov al,byte ptr s[si] ; copy the current element from si into al
	mov byte ptr d1[bx],al ; copy the element from al into the current in d1
	inc bx ; increment the offset for d1
	
	; check if we haven't gone through the whole array
	; if so,end the execution
	checks:
	inc si ; increment the offset for s
	cmp si,len ; compare the offset to the length of s
	je to_end ; if they are equal we can stop as we have checked each element
	jmp operations ; we are not done,continue
	
	to_end:
	mov ax,4c00h
	int 21h
code ends
end start