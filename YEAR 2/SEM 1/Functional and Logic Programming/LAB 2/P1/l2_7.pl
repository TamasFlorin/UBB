/*
  a) Write a predicate to compute the intersection of two sets
*/

% contains(L:list,X:number,R:number)
% contains(in,in,out)
contains([],_,0).
contains([H|_],H,1).
contains([H|T],X,R):-H=\=X,
		     contains(T,X,R).

% my_append(L1:list,X:number,R:list)
% my_append(in,in,out)
my_append([],X,[X]).
my_append([H|T],X,[H | R]):-my_append(T,X,R).

intersection([],_,[]).
intersection([H|T],S2,[H|R]):-contains(S2,H,C),
			      C=:=1,
			      intersection(T,S2,R).

intersection([H|T],S2,R)    :-contains(S2,H,C),
			      C=\=1,
			      intersection(T,S2,R).
			 

/*
  b)Write a predicate to create a list (m,...,n) of all integer numbers
    from the interval [m,n].
*/

% generate(N:number,M:number,R:list)
% generate(in,in,out)
generate(N,N,[N]).
generate(M,N,[M | R]):-M1 is M + 1,
		       generate(M1,N,R).
