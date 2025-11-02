.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 15, 0	sdk_version 15, 5
	.globl	_sort_numbers                   ## -- Begin function sort_numbers
	.p2align	4, 0x90
_sort_numbers:                          ## @sort_numbers
	.cfi_startproc
## %bb.0:
                                        ## kill: def $esi killed $esi def $rsi
	xorl	%eax, %eax
	cmpl	$2, %esi
	jl	LBB0_10
## %bb.1:
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	pushq	%r15
	pushq	%r14
	pushq	%rbx
	.cfi_offset %rbx, -40
	.cfi_offset %r14, -32
	.cfi_offset %r15, -24
	leal	-1(%rsi), %ecx
	movl	%esi, %edx
	xorl	%esi, %esi
	movl	$1, %r8d
	xorl	%eax, %eax
	jmp	LBB0_2
	.p2align	4, 0x90
LBB0_8:                                 ##   in Loop: Header=BB0_2 Depth=1
	incq	%r8
	cmpq	%rcx, %rsi
	je	LBB0_9
LBB0_2:                                 ## =>This Loop Header: Depth=1
                                        ##     Child Loop BB0_3 Depth 2
	movq	%rsi, %r9
	incq	%rsi
	movq	%r8, %r10
	movl	%r9d, %ebx
	jmp	LBB0_3
	.p2align	4, 0x90
LBB0_5:                                 ##   in Loop: Header=BB0_3 Depth=2
	incq	%r10
	movl	%r11d, %ebx
	cmpq	%r10, %rdx
	je	LBB0_6
LBB0_3:                                 ##   Parent Loop BB0_2 Depth=1
                                        ## =>  This Inner Loop Header: Depth=2
	movl	(%rdi,%r10,4), %r14d
	movslq	%ebx, %r15
	movl	%r10d, %r11d
	cmpl	(%rdi,%r15,4), %r14d
	jl	LBB0_5
## %bb.4:                               ##   in Loop: Header=BB0_3 Depth=2
	movl	%ebx, %r11d
	jmp	LBB0_5
	.p2align	4, 0x90
LBB0_6:                                 ##   in Loop: Header=BB0_2 Depth=1
	movl	%r11d, %r10d
	cmpq	%r10, %r9
	je	LBB0_8
## %bb.7:                               ##   in Loop: Header=BB0_2 Depth=1
	movl	(%rdi,%r9,4), %r10d
	movslq	%r11d, %r11
	movl	(%rdi,%r11,4), %ebx
	movl	%ebx, (%rdi,%r9,4)
	movl	%r10d, (%rdi,%r11,4)
	incl	%eax
	jmp	LBB0_8
LBB0_9:
	popq	%rbx
	popq	%r14
	popq	%r15
	popq	%rbp
LBB0_10:
	retq
	.cfi_endproc
                                        ## -- End function
.subsections_via_symbols