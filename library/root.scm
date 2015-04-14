(define (abs a)(if (< a 0)
		  (- 0 a)
		  a)
)

(define (solve f st en)(if (> (* (f st) (f en)) 0)
			   (display "error")
			   (if (< (f en) 0)
			       (solve f en st)
			       (if (> (abs (- en st)) 0.000000001)
				    (if (> (f (/ (+ en st) 2) ) 0)
					(solve f st (/ (+ en st) 2))
					(solve f (/ (+ en st) 2) en)
					)
				    st
))))

(define (fx x)(- (- 0 (* x x)) (* 2 x)))

(solve fx -.2 10)



