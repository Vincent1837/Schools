##
## Write Euclidean algorithm by MIPS instruction
##


#############################
#  data segment  #
#############################

    .data
inputa:	.asciiz	"Input a:"
inputb:	.asciiz	"Input b:"
output:	.asciiz "GCD(a,b):"
error:	.asciiz "a and b need > 0\n"


#############################
#  text segment  #
#############################

    .text
# INPUT
main:
    # Get input a = $s0
    li	$v0, 4
    la	$a0, inputa
    syscall
    li $v0, 5
    syscall
    move $s0, $v0

    # Get input b = $s1
    li	$v0, 4
    la	$a0, inputb
    syscall
    li $v0, 5
    syscall
    move $s1, $v0

# CHECK IF INPUT > 0
L1:
    # Check if a > 0
    blez $s0, Error
    # Check if b > 0
    blez $s1, Error

# EUCLIDEAN ALGORITHM
    # While b != 0, keep looping
L2: beqz $s1, L3 # if b == 0, go to output
    # Divide a by b, keeping the remainder in a
    div $s0, $s1
    mfhi $s0
    # Swap a and b
    move $t0, $s0
    move $s0, $s1
    move $s1, $t0
    # Go back to the start of the loop
    j L2

# OUTPUT
L3:
    # Print output and GCD(a,b)
    li	$v0, 4
    la	$a0, output
    syscall
    li $v0, 1
    move $a0, $s0
    syscall

#EXIT
Exit:
    # Exit program
    li $v0, 10
    syscall

#ERROR
Error:
    # Print error and back to main
    li	$v0, 4
    la	$a0, error
    syscall
    b main
