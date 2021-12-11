zEGGy  ; reads first number and loads it into accumulator 0
ZEGGY 0
ZEggy  ; clears current memory block

zEGGy  ; read again
ZEGGY 1 ; store num2 to accumulator 1

ZEggy  ; clears current memory block
zEGGy  ; read again

zeGGY 1 ; move to addr 1 if we are subtracting
ZEGGy 0 ; write accumulator 0 to addr 1

Zeggy 1 ; move back to address 0 if at addr 1
ZEGGy 1 ; write accumulator 1 to addr 0

zeggY 1 ; move back to addr 1
ZEGGY 0 ; store to accumulator 0

Zeggy 1 ; move back to address 0
ZegGy 0 ; add accumulator 0

zEggy  ; write output