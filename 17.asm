.model small

.data                                      
    arr1 db 1,2,3,4,5,6,7,8,9,10 
    arr2 dw 1000,1005,1010,1015,1020,1025,1030,1035,1040,1045
    len dw 10
    sum_arr1 db 1 dup(?)
    sum_arr2 dw 1 dup(?)

.code                
    mov dx, data
    mov ds, dx
    mov dx, 0
    
    mov cx, len
    mov di, 0
    mov al, 0
    ARR_LOOP:
        add al, arr1[di]  
        add bx, arr2[di]  
        inc di
    loop ARR_LOOP
    
    mov sum_arr1, al
    mov sum_arr2, bx
    hlt