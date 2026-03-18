section .data
    num1 db 3
    num2 db 7
    msg  db "Resultado: "
    tam  equ $-msg

section .bss
    res resb 2          ; IMPORTANTE: Reservar 2 bytes

section .text
    global _start

_start:
    ; 1. Realiza a soma
    mov al, [num1]
    add al, [num2]

    ; 2. Separa os dígitos
    mov ah, 0           ; Limpa AH para a divisão
    mov bl, 10
    div bl              ; Divide AX por 10. Resultado: AL = quociente, AH = resto

    ; 3. Converte para ASCII
    add al, 48
    add ah, 48

    ; 4. Salva na memória
    mov [res], al
    mov [res+1], ah

    ; 5. Imprime "Resultado: "
    mov eax, 4          ; sys_write
    mov ebx, 1          ; stdout
    mov ecx, msg
    mov edx, tam
    int 0x80

    ; 6. Imprime os dois dígitos do resultado
    mov eax, 4
    mov ebx, 1
    mov ecx, res
    mov edx, 2
    int 0x80

    ; 7. Exit
    mov eax, 1          ; sys_exit
    xor ebx, ebx        ; return 0
    int 0x80
