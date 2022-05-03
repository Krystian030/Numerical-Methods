%% Metody numeryczne - Laboratorium nr 2 
% Zadanie 1
% Krystian Jandy s184589

% === Zadanie A ===               
Edges = sparse([4,6,3,4,5,5,6,7,5,6,4,6,4,7,6 ...%i
                1,1,2,2,2,3,3,3,4,4,5,5,6,6,7]); %j


% === Zadanie B === 
d = 0.85;
N = 7;

B = sparse(Edges(1:15),Edges(16:30),1,N,N);
I = speye(N);

A = sparse(N,N);

b = zeros(N,1);
b(:,1) = (1-d)/N;

for i=1:N
    A(i,i) = 1/sum(B(:,i));
end 

M = sparse(I-d*B*A);

r = M\b;
bar(r);
