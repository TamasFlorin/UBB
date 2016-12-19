; Problem : lab 7 ex 8
; Being given a string of bytes, build a string of words which contains in the low bytes of 
; the words the set of distinct characters from the given string and in the high byte of a 
; word it contains the number of occurrences of the low byte of the word in the given byte string.
; Ex: given the string: sir DB 2, 4, 2, 5, 2, 2, 4, 4 
; we should have the result: rez DW 0402h, 0304h, 0105h

data segment
    str db 2,4,2,5,2,2,4,4
    len equ $-sir ; the length of the string of bytes
    res dw len dup(?) ; assume we'll have len unique elements
    unique db 0 ; the number of unique elements in the source string 
ends


code segment
start:
; set segment registers:
    mov ax, data
    mov ds, ax
    mov es,ax
    
    lea si,str ; this is the source string 
    lea di,res ; this is the destination string 
    
    mov cx,len ; cx will be used by the loop instruction
    
    ; clear the destination flag(we parse the string from left to right)
    cld
    
    perform_check:
        ; load the current element
        lodsb ; he loaded string will be stored in al  
        
        ; check if we already have this element in our destination string
        cmp unique,0
        je add_element
        
        mov bx,0
        mov ah,0
        check_existent:
            cmp al,byte ptr res[bx]
            je duplicate ; if the element is already in our dest string then go to the next element in str
            inc bx
            cmp bl,unique
            jne check_existent
        
        ; add the current element to the destination string
        add_element:
            ; count the number of times that the current element appeares in str
            mov ah,0 ; ah will contain the result
            mov bx,0
            
            count:
                cmp al,str[bx] ; compare al with the current element
                jne continue
                inc ah 
                continue:
                inc bx
                cmp bx,len
                jne count ; keep counting
                
            ; now that al contains the current element
            ; and ah the count we can load it in our dest string
            stosw ; load a word into res
            inc unique
            
        
        duplicate:    
    loop perform_check
    
    
    mov ax, 4c00h ; exit to operating system.
    int 21h    
ends

end start ; set entry point and stop the assembler.
