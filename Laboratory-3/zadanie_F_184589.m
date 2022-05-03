% Zadanie E
%------------------
clc
clear all
close all

% przykład działania funkcji tril, triu, diag:
N = [500, 1000, 3000, 6000, 12000];
density = 10;
d = 0.85;

for i = 1:5
    [Edges] = generate_network(N(i),density,184589);
    B = sparse(Edges(2,:),Edges(1,:),1,N(i),N(i));
    I = speye(N(i));
    L = sparse(1:N(i),1,sum(B),N(i),1);
    A = spdiags(1./L,0,N(i),N(i));
    b(1:N(i),1) = (1-d)/N(i);
    M = sparse(I - d*B*A);
    
    L = tril(M,-1);
    U = triu(M,1);
    D = spdiags(spdiags(M,0),0,N(i),N(i));
    
    iter(i) = 0;
    r(1:N(i),1) = 1; % r^0
    
    var1 = -(D+L);  % -(D+L)
    var2= (D+L)\b;  % (D+L)^(-1) * b
    
    val = 10^(-14);
    norm_res = norm(M*r-b);

    tic
    while(norm_res > val)
        iter(i) = iter(i) + 1;
        r = var1\(U*r)+ var2;
        norm_res = norm(M*r-b);
        if N(i) == 1000
            residuums(iter(i)) = norm_res;
        end
    end
    czas_Gaussa_Seidla(i) = toc*1000;
    
end
% wykres nr 1
axis equal
plot(N, czas_Gaussa_Seidla)
title("Czas analizy dla algorytmu Gausaa-Seidla [zadE_1 184589]")
xlabel("N [Liczba stron]");
ylabel("Czas [ms]")
print -dpng zadF_184589_1.png

% wykres nr 2
axis equal
plot(N,iter)
title("Liczba iteracji [zadE_2 184589]")
xlabel("N [Liczba stron]");
ylabel("Iteracje [Liczba iteracji]")
print -dpng zadF_184589_2.png

% wykres nr 3 
axis equal
semilogy(residuums);
title("Norma z residuum dla kolejnych iteracji [zadE_3 184589]")
xlabel("Numer iteracji");
ylabel("Norma z residuum")
print -dpng zadF_184589_3.png
%------------------
