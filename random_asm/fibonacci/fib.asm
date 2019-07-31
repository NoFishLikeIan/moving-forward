; NOTES
; EAX 32bit: is the primary registry used for input/output
; ESP: stack pointer
; jb: jump if condition is met
; dec: decrement by one
; push: pushes onto the stack

_fibonacci:
  mov eax, [esp + 4]    ; -> eax = n
  cmp eax, 2            ; -> if n < 2
  jb _endFiboFunc       ; ...... break
  dec eax               ; -> push n-1
  push eax
  call _fibonacci        ; calls eax = fib(n-1)
  xchg eax, [esp]       ; eax = n - 1, [esp] = fib(n-1)
  dec eax               ; push n-2
  push eaxs
  call _fibonacci        ; returns eax = fib(n-1)
  add eax, [esp+4]      ; eax = fib(n-1)+fib(n-2)
  add esp, 8

_endFiboFunc:
  ret                   ; exit the function!