%include "msdn_defs.inc"

[bits 32]

struc Student
.last_name resb 20
.first_name resb 20
.age resd 1
.height resd 1
.eye_color resb 15
.size
endstruc

%define MAX_STUDENTS 100
%define NULL 0

section .text 

extern  _printf
extern _exit

extern _fopen
extern _fscanf
extern _strtok
extern _strcpy
extern _scanf
extern _atoi
extern _fclose
extern __open_osfhandle
extern __fdopen
extern CreateFileA

global  _main 

_main: 
		push NULL
		push FILE_ATTRIBUTE_NORMAL
		push OPEN_EXISTING
		push NULL
		push 0
		push GENERIC_READ ; open the file in read mode
		push fileName
		call CreateFileA
		cmp eax,INVALID_HANDLE_VALUE
		je .error
	
		mov [hFile],eax ; the handle of the file will be stored in hFile
		
		; we need a C run-time descriptor in order to open a file stream
		push 0 ; _O_RDONLY
		push dword [hFile]
		call __open_osfhandle
		add esp,4*2
		
		cmp eax,-1
		je .error
		mov [cHandle],eax
		
		; convert the C run-time descriptor to a FILE* structure 
		push readMode
		push dword [cHandle]
		call __fdopen
		add esp,4*2
		
		; we could have just used fopen but the point was to learn how to use CreateFileA
		; and I was curious if there was a way to convert a handle to a file pointer

		; set the file pointer
		mov [filePointer],eax
		
		; read the number of students
		push numStudents
		push intFormat
		push dword [filePointer]
		call _fscanf
		
		mov ecx,[numStudents]
		mov edi,0 ; index in the students array
		
		.read_data:
			push ecx
			
			; read the current line
			push buffer
			push strFormat
			push dword [filePointer]
			call _fscanf
			add esp,12
			
			; parse the line using strtok
			push delim
			push buffer
			call _strtok
			add esp,8
			
			; current value counter
			mov ebx,0
			
			.tokenize:
				; eax contains the token
				mov [token],eax
				inc ebx
				cmp byte [token],NULL
				je .continue_reading
				cmp ebx,1
				je .add_last_name
				cmp ebx,2
				je .add_first_name
				cmp ebx,3
				je .add_age
				cmp ebx,4
				je .add_height
				cmp ebx,5
				je .add_eye_color
			
				.add_last_name:
					; save the edi register
					push edi
					mov eax,token
					lea edi,students[edi + Student.last_name]
					mov esi,[token]
					cld
					.copy:
						lodsb
						stosb
						test al,al
						jnz .copy
					
					; restore edi
					pop edi
					jmp .continue_token
				.add_first_name:
					push edi
					mov eax,token
					lea edi,students[edi + Student.first_name]
					mov esi,[token]
					cld
					.copy_name:
						lodsb
						stosb
						test al,al
						jnz .copy_name
					pop edi
					jmp .continue_token
				.add_age:
					push dword [token]
					call _atoi
					mov students[edi + Student.age],eax
					add esp,4
					jmp .continue_token
				.add_height:
					push dword [token]
					call _atoi
					mov students[edi + Student.height],eax
					add esp,4
					jmp .continue_token
				.add_eye_color:
					push edi
					mov eax,token
					lea edi,students[edi + Student.eye_color]
					mov esi,[token]
					
					.copy_color:
						lodsb
						stosb
						test al,al
						jnz .copy_color
					pop edi
					jmp .continue_token
				
				.continue_token:
					push delim
					push NULL
					call _strtok ; eax will contain the token
					add esp,8
					jmp .tokenize
			.continue_reading:
				pop ecx ; restore ecx
				add edi,Student.size ; increment the index in the students array
				dec ecx
				cmp ecx,0 ; have we read all the students?
				jne .read_data

		.read_command:
			; read the student index
			push command
			push intFormat
			call _scanf
			add esp,4*2
			
			; if it is 0,we should exit
			cmp dword [command],0
			je .finish
			
			; the index should be less or equal to the number of students
			mov eax,[numStudents]
			cmp dword [command],eax
			jg .inexistent_id
			
			; compute the index for the student
			mov bx,Student.size
			mov ax,[command]
			dec ax
			mul bx ; the result in stored in dx:ax
			
			; copy dx:ax into eax
			push dx
			push ax
			pop eax
			
			; pointer to current student structure
			add eax,students ; command *Student.size + students
			
			; print the selected student
			; eye color
			add eax,Student.eye_color
			push eax
			
			; height
			sub eax,Student.eye_color
			add eax,Student.height
			push dword [eax]
			
			; age
			sub eax,Student.height
			add eax,Student.age
			push dword [eax]
			
			; first name
			sub eax,Student.age
			add eax,Student.first_name
			push eax
			
			; last name
			sub eax,Student.first_name
			add eax,Student.last_name
			push eax
			
			push studentFormat
			call _printf
			add esp,4
			
			; index was valid,continue reading
			jmp .read_command
			
			; index invalid,print an error and continue reading
			.inexistent_id:
				push dword [command]
				push invalidIndexError
				call _printf
				add esp,8
				jmp .read_command
		
		jmp .finish
		
		; should only get here if there was an error reading from the file
		.error:
			push errorMessage
			call _printf
			add esp,4
		
		.finish:
		; close the file 
		push filePointer
		call _fclose
		add esp,4
		
        push    0
        call    _exit
        ret 

section .data
	students: times MAX_STUDENTS * Student.size db 0
	buffer: times 100 db 0
	token: times 25 db 0
	fileName: db "students.txt",0
	readMode: db "r",0
	intFormat: db "%d",0
	strFormat: db "%s",0
	studentFormat: db "%s %s %d %d %s",0Ah,0 ; format used to print a student entity
	command : dd 0
	numStudents: dd 0
	cHandle: dd 0
	hFile: dd 0
	filePointer: dd 0
	errorMessage: db "An error has occurred while opening the file.",0
	invalidIndexError: db "Invalid index given: maxmimum index value is %d.",0Ah,0
	delim: db ",",0