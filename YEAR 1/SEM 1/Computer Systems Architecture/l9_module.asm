; Name: Tamas Florin
; Group: 917
; Print on the screen, for each number between 32 and 126, the value of the number (in base 10) and the character whose ASCII code the number is.

assume cs:code,ds:data

data segment public
    ten dw 10
data ends

code segment public

public PrintBase10
PrintBase10:
    push bp
    mov bp,sp
    push ax
    push cx
    push dx

    ; the number that we want to print
    mov ax,[bp +4]

    cmp ax,0
    jge positive

    ; the number is not positive,print the '-' sign
    push ax ; save the ax register

    ; print '-'
    mov ah,02h
    mov dl,'-'
    int 21h
    
    pop ax ; restore the ax register

    neg ax

    positive:
        mov cx,0 ; number of digits
        push_digits:
            ; push each digit of the number onto the stack
            mov dx,0
            div ten
            push dx
            inc cx
            cmp ax,0 
            ja push_digits
        
        ; pop the digits from the stack and print them
        pop_digits:
            pop dx
            add dl,'0'
            mov ah,02h
            int 21h
        loop pop_digits

    pop dx
    pop cx
    pop ax
    pop bp
    ret 2

public PrintChar
PrintChar:
    push bp
    mov bp,sp

    push ax
    push dx
    
    ; ax will contain the ascii code of the character
    mov ax,[bp+4]

    ; dl will contain the character to be printed
    mov dl,al
    mov ah,02h
    int 21h

    pop dx
    pop ax
    pop bp

    ret 2

public PrintNumbers
PrintNumbers:
    push bp
    mov bp,sp

    push cx

    mov cx,32

    print:
        ; print the number in base 10
        push cx
        call PrintBase10

        ; leave a space between the number and the ascii code
        push ' '
        call PrintChar

        ; print the ascii code
        push cx
        call PrintChar

        ; print new line
        push 0Ah
        call PrintChar
        
        inc cx
        cmp cx,126
        jbe print

    pop cx
    pop bp
    ret 
code ends
end