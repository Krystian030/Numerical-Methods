% Zadanie D
%------------------
clc
clear all
close all

N = [500, 1000, 3000, 6000, 12000];
density = 10;
d = 0.85;
for i = 1:5
    [Edges] = generate_network(N(i),density, 184589);
    B = sparse(Edges(2,:),Edges(1,:),1,N(i),N(i));
    I = speye(N(i));
    L = sparse(1:N(i),1,sum(B),N(i),1);
    A = spdiags(1./L,0,N(i),N(i));
    b(1:N(i),1) = (1-d)/N(i);
    M = sparse(I - d*B*A);
    tic
    r = M\b;
    czas_Gauss(i) = toc;
end
axis equal
plot(N, czas_Gauss);
title("Czas analizy dla algorytmu Gausaa [zadD 184589]")
xlabel("N [Liczba stron]");
ylabel("Czas [s]")
print -dpng zadD_184589.png
%------------------
