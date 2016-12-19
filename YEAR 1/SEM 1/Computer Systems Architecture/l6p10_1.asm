;10. A byte string S is given. Obtain in the string D the set of the elements of S.
;Exemple:
;S: 1, 4, 2, 4, 8, 2, 1, 1
;D: 1, 4, 2, 8

assume cs:code,ds:data

data segment
	s db 1, 4, 2, 4, 8, 2, 1, 1
	len equ $-s
	d db len dup(?)
data ends

code segment
start:

	mov ax,data
	mov ds,ax
	
	mov cx,len ; used for the loop
	jcxz to_end
	
	mov si,0 ; used as offset for s
	mov di,0 ; used as offset for d
	
	operations:
	
	mov al,s[si] ; copy the current element into al
	
	; if there are no elements in d just add the first one
	cmp di,0 
	je add_element
	
	mov bp,0
	; loop over the current elements in d and check if it contains the current element in s
	check:
	cmp d[bp],al
	je continue ; if we already have that element go to the next one in s
	cmp bp,di ; compare current element index with total number of elements in d
	inc bp ; increment the current index
	jb check ; if we haven't looped over all of them yet,continue
	
	; add the element
	add_element:
	mov byte ptr d[di],al ; move current element from s into d
	inc di ; increment the offset for d
	
	continue:
	inc si ; increment the offset for s
	
	loop operations

to_end:
	mov ax,4c00h
	int 21h
code ends
end start