
clc
clear all
close all


% N = 989;
%N = 10;
N = 20;
d1(1,1:N) = 3;  
d2(1,1:(N-1)) = -1; 
d3(1,1:(N-2)) = -1;
M = zeros(N,N) + diag(d1,0) + diag(d2,1) + diag(d3,2) + diag(d2,-1) + diag(d3,-2);
[L, U, P] = lu(M);

b(1:N,1) = 0;
    for i = 0:N-1
        n = sin(i*(4+1));
        b(i+1,1) = n;
    end

y = L\(P*b);
x = U\y;
norm_res = norm(M*x-b);