% helper predicate to compute sum of a list
% sum_helper(L : list,LC : list,LR : list)
% sum_helper(in,in,out)
sum_helper([],S,S).
sum_helper([H|T],S,Res):-S1 is S + H,
		  sum_helper(T,S1,Res).

% predicate to compute sum of a list
% sum(L : list,R : integet)
% sum(in,out)
sum(L,R):-sum_helper(L,0,R).

% helper predicate to compute len of a list
% len_helper(L : list,LR: list,LC : list)
% len_helper(in,in,out)

len_helper([],LC,LC).
len_helper([H|T],LC,LR):-LC1 is LC + 1,
	      len_helper(T,LC1,LR).

% predicate to compute the len of a list
% len(L : List, R : integer)
% len(in,out)
len(L,R):-len_helper(L,0,R).

% check if a given sublist is a solution
% solution(L : list,InitLen : integer)
% solution(in,in)
solution(L,InitLen):-sum(L,Suma),
	     Suma > 0,
	     InitLen > 0,
	     Res1 is Suma mod InitLen,
	     Res1 =:= 0.

% generate all the subsets of a given list
% subset(L : list,R : list)
% subset(in,out)
subset([],[]).
subset([H|T],[H|TR]):-subset(T,TR).
subset([_|T],TR):-subset(T,TR).

% check the subsets of a list that have the sum divisible by the length of the entire list
% solve_subsets(L : list,R : list,InitLen:integer)
% solve_subsets(in,out,in)
solve_subsets([],[],_).
solve_subsets([H|T],[H|TR],InitLen):-solution(H,InitLen),
				     solve_subsets(T,TR,InitLen).
solve_subsets([H|T],R,InitLen):-solve_subsets(T,R,InitLen).

% solve the given problem
% solve( L : list, R : list)
% solve(in,out)
solve(L,R):-len(L,Length),
	    findall(RP,subset(L,RP),RF),
	    solve_subsets(RF,R,Length).
