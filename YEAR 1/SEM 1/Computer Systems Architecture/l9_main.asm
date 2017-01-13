; Name: Tamas Florin
; Group: 917
; Print on the screen, for each number between 32 and 126, the value of the number (in base 10) and the character whose ASCII code the number is.

assume cs:code,ds:data

data segment
    ten dw 10
data ends

code segment

extrn PrintNumbers:proc
start:
    mov ax,data
    mov ds,ax

    call PrintNumbers

    mov ax,4c00h
    int 21h
code ends
end start