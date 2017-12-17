; 4.
; a) Write a function to return the sum of two vectors.
; b) Write a function to get from a given list the list of all atoms, on any
; level, but on the same order. Example:
; (((A B) C) (D E)) ==> (A B C D E)
; c) Write a function that, with a list given as parameter, inverts only continuous
; sequences of atoms. Example:
; (a b c (d (e f) g h i)) ==> (c b a (d (f e) i h g))
; d) Write a list to return the maximum value of the numerical atoms from a list, at superficial level.

; http://mathworld.wolfram.com/VectorAddition.html
(defun vectorSum (a b)
	(cond
		( (NOT (equal(list-length a)(list-length b))) NIL)
		((OR (NULL a)(NULL b)) NIL)
		(T ( cons ( + (CAR a)(CAR b))(vectorSum(CDR a)(CDR b))))
	)
)

(defun getAtoms(l)
	(cond
		((NULL l) NIL)
		((listp (CAR l)) ( append (getAtoms(CAR l)) (getAtoms(CDR l))))
		((atom (CAR l)) (cons (CAR l) (getAtoms (CDR l))))
	)
)

(defun maxElement(l)
	(cond
		((NULL l) NIL)
		((equal (length l) 1) (CAR l))
		(T(max (CAR l) (maxElement(CDR l))))
	)
)

(defun maxElementSuperficial(l)
	(cond
		((NULL l) NIL)
		(T(maxElement (getAtoms l)))
	)
)

(defun reverseList (l res)
	(cond
		((null l) (reverse res))
		((listp (car l))  (append (reverse res) (cons (reverseList (car l) nil) (reverseList (cdr l) nil))))
		(T (reverseList ( cdr l ) (append res (list (car l)))))
	)
)

(write-line "Vector sum:")
(write (vectorSum '(1 2 3 4) '(1 2 3 4)))
(write-line "")
(write-line "Atoms from list:")
(write (getAtoms '((11 (2(3))) 3 4)))
(write-line "")
(write-line "Max element superficial:")
(write (maxElementSuperficial '((11 (2)) 3 4)))
(write-line "Reverse list:")
(write (reverseList '((a b c (d (e f) g h i))) nil))