;10. A byte string S is given. Obtain in the string D the set of the elements of S.
;Exemple:
;S: 1, 4, 2, 4, 8, 2, 1, 1
;D: 1, 4, 2, 8
; String operations version

assume cs:code,ds:data

data segment
	s db 1, 4, 2, 4, 8, 2, 1, 1
	len equ $-s
	d db len dup(?)
	count db 0
data ends

code segment
start:
	mov ax,data
	mov ds,ax
	
	mov cx,len ; we will use cx for loop
	
	jcxz to_end ; make sure cx isn't zero
	
	cld ; clear direction flag
	
	lea si,s ; source index is s
	
	; prepare destination string
	mov es,ax
	lea di,d ; destination index is d
	
	operations:
	lodsb ; load current element of s into al
	
	cmp count,0 ; if the current number of elements in d is zero just add the first element from s
	je add_element
	
	mov bl,count ; store the count variable into bl
	mov bp,0 ; offset used to loop over d
	
	check:
	cmp d[bp],al ; check if the current string from s is already in d
	je continue ; if it is go to the next element in s
	inc bp ; increment current index in d
	dec bl ; decrement the number of elements left in d
	cmp bl,0 ; if bl is zero then we have looped over all of the elements in d
	jne check
	
	add_element:
	stosb ; store current element in d
	inc count ; increment the element count
	
	continue:
	loop operations
	
to_end:
	mov ax,4c00h
	int 21h
code ends
end start