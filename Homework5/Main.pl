sum(0, []).
sum(Total, [Head|Tail]) :- sum(Sum, Tail), Total is Head + Sum.

?- sum(Total, [1, 2, 3, 4]).