% Determine the position of the maximal element in a linear list

% max_element_h(L : list,MaxElem : number,Res : Number).
% max_element(i,i,o)
max_element_h([],MaxElem,MaxElem).
max_element_h([H|T],MaxElem,Res):-H > MaxElem,
				max_element_h(T,H,Res).

max_element_h([H|T],MaxElem,Res):-H =< MaxElem,
				max_element_h(T,MaxElem,Res).

% max_element(L : list, R : number)
% max_element(i,o)
max_element([H|T],R):-max_element_h(T,H,R).

% max_pos_h(L : list,MaxElem : number,Pos : number,R : list)
% max_pos_h(i,i,i,o)
max_pos_h([],_,_,[]).

max_pos_h([H|T],MaxElem,Pos,[Pos|R]):-H =:= MaxElem,
			            Pos1 is Pos + 1,
				    max_pos_h(T,MaxElem,Pos1,R).
max_pos_h([H|T],MaxElem,Pos,R):- H =\= MaxElem,
			       Pos1 is Pos + 1,
			       max_pos_h(T,MaxElem,Pos1,R).

% max_pos(L : list, R : list)
% max_pos(i,o)
max_pos(L,R):-max_element(L,MaxElement),
	      max_pos_h(L,MaxElement,1,R).

% replace the sublists with the positions of the maximum element
% replace_sub(L : list, R : list)
% replace_sub(i,o)
replace_sub([],[]).
replace_sub([H|T],[Pos |R ]):-is_list(H),
			      max_pos(H,Pos),
			      replace_sub(T,R).

replace_sub([H | T],[H | R]):- replace_sub(T,R).	       
