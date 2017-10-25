/*
   a. Write a predicate to test if a list is a set.
*/

% count_h(L:list,X:number,C:umber,R:number)
% count_h(in,in,in,out)
% C is used as a counter variable
count_h([],_,C,C).
count_h([H|T],X,C,R):-H=:=X,
		  C1 is C+1,
		  count_h(T,X,C1,R).
count_h([H|T],X,C,R):-H=\=X,
		  count_h(T,X,C,R).

% just a helper function so we do not have to pass 0 to the counter
% count(L:list,X:number,R:number)
% count(in,in,out)
count(L,X,R):-count_h(L,X,0,R).

% is_set_h(S:list,S1:list,R:number)
% is_set_h(in,in,out)
is_set_h([],_,1).

is_set_h([H|T],S,R):-count(S,H,C),
		     C=:=1,
		     is_set_h(T,S,R).

is_set_h([H|_],S,0):-count(S,H,C),
		     C=\=1.
% is_set(S:list,R:number)
% is_set(in,out)
is_set(S,R):-is_set_h(S,S,R).

/*
  b. Write a predicate to remove the first three occurrences of an 
  element in a list. If the element occurs less
  than three times, all occurrences will be removed.
*/
% remove_3_h(L:list,E:numberr,Removed:nr,Temp:list,R:list)
% remove_3_h(in,in,in,out)

remove_3_h([],_,_,[]).
remove_3_h([H|T],E,Removed,[ H | R]):-H=\=E,
				      remove_3_h(T,E,Removed,R).

remove_3_h([H|T],E,Removed,[H|R]):-H=:=E,
			       Removed >= 3,
			       remove_3_h(T,E,Removed,R).

remove_3_h([H|T],E,Removed,R):-H=:=E,
			       Removed < 3,
			       Removed1 is Removed + 1,
			       remove_3_h(T,E,Removed1,R).

% remove_3(L:list,E:number,R:list)
% remove_3(in,in,out)
remove_3(L,E,R):-remove_3_h(L,E,0,R).

