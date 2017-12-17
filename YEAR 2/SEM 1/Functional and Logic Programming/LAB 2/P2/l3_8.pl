% reverse_list_h(L : list, RC: list,R : list)
% reverse_list_h(in,in,out)
reverse_list_h([],RC,RC).

reverse_list_h([H | T],RC,R):-RC1 = [ H | RC],
			    reverse_list_h(T,RC1,R).

% reverse_list(L : list,R : list)
% reverse_list(in,out)
reverse_list(L,R):-reverse_list_h(L,[],R).

% successor_h( L : list,Carry : number, RC: List,R : list)
% successor_h( in,in,in,out).
successor_h([],0,RC,RC).
successor_h([],1,RC,[1 | RC]).

successor_h([H|T],Carry,RC,R):-Sum is H + Carry,
			       Carry1 is Sum div 10,
			       Sum1 is Sum mod 10,
			       RC1 = [ Sum1 | RC],
			       successor_h(T,Carry1,RC1,R).

% successor(L : list, R : list)
% successor(in,out)
successor(L,R):-reverse_list(L,Rev),
		successor_h(Rev,1,[],R).

% succ_sublist(L : list, R:list)
% succ_sublist(in,out)
succ_sublist([],[]).

succ_sublist([H | T],[Succ | R]):-is_list(H),
			 successor(H,Succ),
			 succ_sublist(T,R).

succ_sublist([H | T],[H | R]):-succ_sublist(T,R).
