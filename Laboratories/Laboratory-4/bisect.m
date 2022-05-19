function [xvect,xdif,fx,it_cnt]=bisect(a,b,eps,fun)

xvect = [];
xdif = [];
fx = [];
it_cnt = 0;
prev = a;

%x = (a + b)/2;
    for i = 1:1000
        % bisection algorithm 
        c = (a + b) / 2;
        
        % use feval to obtain the value of the function in 'x' 
        fc = feval(fun,c);
        xvect(i) = c;
        fx(i) = abs(fc);
        it_cnt = it_cnt + 1;
        xdif(it_cnt) = abs(c - prev);
        prev = c;
        
        if abs(fc) < eps || abs(b-a) < eps
            return 
        elseif feval(fun,a) * fc < 0
            b = c;
        else 
            a = c;
        end
    end
end
