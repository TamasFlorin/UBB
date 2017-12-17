% reverse_list_h(L : list, RC: list,R : list)
% reverse_list_h(in,in,out)
reverse_list_h([],RC,RC).

reverse_list_h([H | T],RC,R):-RC1 = [ H | RC],
			    reverse_list_h(T,RC1,R).

% reverse_list(L : list,R : list)
% reverse_list(in,out)
reverse_list(L,R):-reverse_list_h(L,[],R).

% product_h(L : list,Digit : int,Carry : int,RC : list, R :list)
% product_h(in,in,in,in,out)
product_h([],_,0,RC,RC).
product_h([],_,Carry,RC,[Carry | RC]).

product_h([H|T],Digit,Carry,RC,R):-Prod is H * Digit + Carry,
				    Carry1 is Prod div 10,
				    Prod1 is Prod mod 10,
				    RC1 = [Prod1 | RC],
				    product_h(T,Digit,Carry1,RC1,R).

% product(L : list, Digit: int, R : list)
% product(in,in,out)
product(L,Digit,R):-reverse_list(L,Rev),
		product_h(Rev,Digit,0,[],R).

% prod_sublist(L : list, R:list)
% prod_sublist(in,out)
prod_sublist([],_,[]).

prod_sublist([H | T],Digit,[Prod | R]):-is_list(H),
			 product(H,Digit,Prod),
			 prod_sublist(T,Digit,R).

prod_sublist([H | T],Digit,[H | R]):-prod_sublist(T,Digit,R).


