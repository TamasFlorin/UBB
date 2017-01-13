; Author: Tamas Florin group 917
; Date: 29.12.2016
; Problem 8: 
;			    Write a program which reads the name of a file and two characters from the keyboard. 
; 				The program should replace all occurrences of the first character in that file with the 
;				second character given by the user.
assume cs:code,ds:data

data segment
	fileName db 12 dup(0)  ; file name buffer
	maxLength db 12 ; maximum number of characters that the file name can have
	fileNameLength db 0 ; actual file name length
	fileHandle dw 0
	
	; output strings
	errorMessage db 0Ah,"An error has occurred when opening the file.Make sure the file exists.","$"
	success: db 0Ah,"Program successfully executed.","$"
	fileNameMsg db 0Ah,"File name:","$"
	toReplaceMsg db 0Ah,"character to replace:","$"
	replaceWithMsg db 0Ah,"replace with:","$"
	
	; characters read from the user
	to_replace db 0
	replace_with db 0
	char db 0
	
	; some constants
	readWrite equ 2
	fromCurrentLocation equ 1
	EOF equ 0
data ends

code segment
start:
	mov ax,data
	mov ds,ax
	
	; print file name message
	mov ah,09h
	lea dx,fileNameMsg
	int 21h
	
	; read a string from the keyboard
	lea dx,fileName
	mov al,maxLength
	mov byte ptr fileName,al ; first byte might contain the maximum length
	mov ah,0Ah ; use service 0Ah
	int 21h ; with intrerrupt 21h
	
	; second byte of the buffer will contain the actual length
	mov al,byte ptr fileName + 1
	mov fileNameLength,al

	mov bh,0
	mov bl,fileNameLength	
	mov si,bx
	
	; in order to open a file we need the asciiz format,so our string needs to end with 0
	mov fileName[si + 2],0
	
	lea dx,fileName+ 2 ; fileName starts at buffer+2
	mov ah,3Dh ; we are using service 30h
	mov al,readWrite; read/write access
	int 21h
	jc .error ; if the carry flag is set then there was an error opening the file
	
	; ax contains the file handle
	mov fileHandle,ax
	
	; now we can also read the characters since the fileName is valid
	mov ah,09h
	lea dx,toReplaceMsg
	int 21h
	
	mov ah,01h
	int 21h
	mov to_replace,al
	
	mov ah,09h
	lea dx,replaceWithMsg
	int 21h
	
	mov ah,01h
	int 21h
	mov replace_with,al
	
	; let's read from the file
	.read_file:
		mov ah,3Fh ; we will be using service 3Fh
		mov bx,fileHandle
		mov cx,1 ; we only want to read one character at a time
		lea dx,char ; char will be our buffer
		int 21h
		cmp ax,EOF ; check if we are at the end of the file 
		je .success ;if so,we can stop
		
		; check if the char matches the character given by the user
		mov bl,to_replace
		cmp char,bl
		je .replace_char
		jmp .read_file
		
		.replace_char:
			; we have to move the file pointer to the left
			mov ah,42h
			mov bx,fileHandle
			mov cx,-1
			mov dx,-1
			mov al,fromCurrentLocation ; move pointer from current location
			int 21h
			
			; write the character
			mov ah,40h
			mov bx,fileHandle
			mov cx,1
			lea dx,replace_with
			int 21h
			
			; continue reading
			jmp .read_file
	
	; if an error has occurred print a message
	.error:
		mov ah,09h
		lea dx,errorMessage
		int 21h
		jmp .finish
	
	; let the user know that everything went as expected and close the file handle
	.success:
		; close file handle
		mov ah,3Eh
		mov bx,fileHandle
		int 21h
		; print success message
		mov ah,09h
		lea dx,success
		int 21h
	.finish:
		mov ax,4c00h
		int 21h
code ends
end start