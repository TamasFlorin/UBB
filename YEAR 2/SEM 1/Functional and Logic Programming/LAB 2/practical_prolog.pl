; [1,[2,3,4],5,6,[7,8]]
; => [1,2,3,4,5,6,7,8]
insert([],E,[E]).
insert([H|T],E,[H|R]):-insert(T,E,R).

replace([],E,L1,[]).
replace([H|T],E,L1,[L1 |R ]):-H=:=E,
			      replace(T,E,L1,R).
replace([H|T],E,L1,[H|R]):-replace(T,E,L1,R).

insert_list([],LC,LC).
insert_list([H|T],LC,LR):-insert(LC,H,Res),
			  insert_list(T,Res,LR).

solve([],E,L1,RC,RC).
solve([H|T],E,L1,RC,R):-is_list(H),
			insert_list(H,RC,Res),
			solve(T,E,L1,Res,R).
solve([H|T],E,L1,RC,R):-insert(RC,H,Res),
			solve(T,E,L1,Res,R).
			
solve_final(L,E,L1,R):-replace(L,E,L1,Res),
		       solve(Res,E,L1,[],R).
