    ; -------- Ex1 --------
    section .data
    num1 db 4
    msg db "Ex1: "
    tam equ $-msg
    section .bss
    res resb 1
    section .text
    global _start

    _start:
        mov al, [num1]
        inc al
        inc al

        add al, 48
        mov [res], al

        mov eax,4
        mov ebx,1
        mov ecx,msg
        mov edx,tam
        int 0x80

        mov eax,4
        mov ebx,1
        mov ecx,res
        mov edx,1
        int 0x80

        mov eax,1
        int 0x80

    ; -------- Ex2 --------
    ; -------- A --------
    section .data
        msg db "Ex2 A: "
        tam equ $-msg

    section .bss
        dez resb 1
        uni resb 1

    section .text
        global _start

    _start:
        mov al, 5
        mov bl, 6
        mul bl

        mov bl, 10
        div bl

        mov [dez], al
        mov [uni], ah

        add byte [dez], 48
        add byte [uni], 48

        mov eax,4
        mov ebx,1
        mov ecx,msg
        mov edx,tam
        int 0x80

        mov eax,4
        mov ebx,1
        mov ecx,dez
        mov edx,1
        int 0x80

        mov eax,4
        mov ebx,1
        mov ecx,uni
        mov edx,1
        int 0x80

        mov eax,1
        int 0x80

    ; -------- B --------
    section .data
        msg db "Ex2 B: "
        tam equ $-msg

    section .bss
        quo resb 1
        res resb 1

    section .text
        global _start

    _start:
        mov al, 8
        mov bl, 3
        div bl

        mov [quo], al
        mov [res], ah

        add byte [quo], 48
        add byte [res], 48

        mov eax,4
        mov ebx,1
        mov ecx,msg
        mov edx,tam
        int 0x80

        mov eax,4
        mov ebx,1
        mov ecx,quo
        mov edx,1
        int 0x80

        mov eax,4
        mov ebx,1
        mov ecx,esp
        mov edx,1
        int 0x80

        mov eax,4
        mov ebx,1
        mov ecx,res
        mov edx,1
        int 0x80

        mov eax,1
        int 0x80

    ; -------- C --------
    section .data
        msg db "Ex2 C: "
        tam equ $-msg

    section .bss
        dez resb 1
        uni resb 1

    section .text
        global _start

    _start:
        mov al, 7
        mov bl, 8
        mul bl

        mov bl, 10
        div bl

        mov [dez], al
        mov [uni], ah

        add byte [dez], 48
        add byte [uni], 48

        mov eax,4
        mov ebx,1
        mov ecx,msg
        mov edx,tam
        int 0x80

        mov eax,4
        mov ebx,1
        mov ecx,dez
        mov edx,1
        int 0x80

        mov eax,4
        mov ebx,1
        mov ecx,uni
        mov edx,1
        int 0x80

        mov eax,1
        int 0x80

; -------- D --------
section .data
    msg db "Ex2 D: "
    tam equ $-msg

section .bss
    dez resb 1
    uni resb 1

section .text
    global _start

_start:
    mov al, 12
    mov bl, 7
    add al, bl

    mov bl, 10
    div bl

    mov [dez], al
    mov [uni], ah

    add byte [dez], 48
    add byte [uni], 48

    mov eax,4
    mov ebx,1
    mov ecx,msg
    mov edx,tam
    int 0x80

    mov eax,4
    mov ebx,1
    mov ecx,dez
    mov edx,1
    int 0x80

    mov eax,4
    mov ebx,1
    mov ecx,uni
    mov edx,1
    int 0x80

    mov eax,1
    int 0x80
