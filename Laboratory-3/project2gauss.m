% Zadanie E
%------------------
clc
clear all
close all

% przykład działania funkcji tril, triu, diag:
N = [989];
density = 10;
d = 0.85;

for i = 1:2
  
%     N = 989;
    N = 941
    d1(1,1:N) = 13;  
    d2(1,1:(N-1)) = -1; 
    d3(1,1:(N-2)) = -1;
    M = zeros(N,N) + diag(d1,0) + diag(d2,1) + diag(d3,2) + diag(d2,-1) + diag(d3,-2);

    b(1:N,1) = 0;
    for i = 0:N-1
        n = sin(i*(4+1));
        b(i+1,1) = n;
    end

    M = full(M);
    L = tril(M,-1);
    U = triu(M,1);
    D = diag(diag(M,0));    
    iter(i) = 0;
    r(1:N,1) = 0; % r^0
    
    var1 = -(D+L);  % -(D+L)
    var2= (D+L)\b;  % (D+L)^(-1) * b
    
    val = 10^(-9);
    norm_res = norm(M*r-b);
    iters = 0
    tic
    while(norm_res > val)
        iters = iters + 1;
        r = var1\(U*r)+ var2;
        norm_res = norm(M*r-b);
        
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
