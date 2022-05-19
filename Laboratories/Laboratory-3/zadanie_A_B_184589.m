%diary('log_184589_lab3')

clc
clear all
close all

% odpowiednie fragmenty kodu można wykonać poprzez znazaczenie i wciśnięcie F9
% komentowanie/ odkomentowywanie: ctrl+r / ctrl+t

% Zadanie A
%------------------
N = 10;
density = 3; % parametr decydujący o gestosci polaczen miedzy stronami
[Edges] = generate_network(N, density,184589);
%-----------------

% Zadanie B
%------------------
% generacja macierzy I, A, B i wektora b
d = 0.85;
%A = sparse(A);  % macierze A, B i I muszą być przechowywane w formacie sparse (rzadkim)
B = sparse(Edges(2,:),Edges(1,:),1,N,N);
I = speye(N);
L = sparse(1:N,1,sum(B),N,1);
A = spdiags(1./L,0,N,N);
b(1:N,1) = (1-d)/N;
save zadB_184589 A B I b
%-----------------