% Zadanie G
%------------------
clc
clear all
close all

load Dane_Filtr_Dielektryczny_lab3_MN.mat

N = size(M,1);
% Metoda Gaussa
tic
r_gauss = M\b;
czas_Gauss = toc
%------------------

% Metoda Jacobiego
L = tril(M,-1);
U = triu(M,1);
D = spdiags(spdiags(M,0),0,N,N);
iter = 0;
r_jacobi(1:N,1) = 1; % r^0
var1 = -D\(L+U); % -D^(-1) * (L+U)
var2 = D\b;  % D^(-1) * b
val = 10^(-14);
norm_res = norm(M*r_jacobi-b);
tic
while(norm_res > val)
    iter = iter + 1;
    r_jacobi = var1 * r_jacobi + var2;
    norm_res = norm(M*r_jacobi-b);
    residuums_jacobi(iter) = norm_res;
    if norm_res > 100000
        break;
    end
end
czas_Jacobi = toc
%------------------

% Metoda Gaussa-Seidla
L = tril(M,-1);
U = triu(M,1);
D = spdiags(spdiags(M,0),0,N,N);

iter= 0;
r_gaussa_seidla(1:N,1) = 1; % r^0

var1 = -(D+L);  % -(D+L)
var2= (D+L)\b;  % (D+L)^(-1) * b

val = 10^(-14);
norm_res = norm(M*r_gaussa_seidla-b);
while(norm_res > val)
    iter = iter + 1;
    r_gaussa_seidla = var1\(U*r_gaussa_seidla)+var2;
    norm_res = norm(M*r_gaussa_seidla-b);
    residuums_gauss_seidla(iter) = norm_res;
    if norm_res > 10000
        break;
    end
end
czas_Gaussa_Seidla = toc

figure("Name","Norma z residuum dla kolejnych iteracji - Gauss Seidel ");
title("Norma z residuum dla kolejnych iteracji - Gauss Seidel")
xlabel("Numer iteracji");
ylabel("Norma z residuum")
plot(residuums_gauss_seidla)

figure("Name","Norma z residuum dla kolejnych iteracji - Jacobi");
title("Norma z residuum dla kolejnych iteracji - Jacobi")
xlabel("Numer iteracji");
ylabel("Norma z residuum")
plot(residuums_jacobi)
%------------------