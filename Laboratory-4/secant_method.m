function [xvect,xdif,fx,it_cnt]=secant_method(a,b,eps,fun)

xvect = [];
xdif = [];
fx = [];
it_cnt = 0;
x0 = a;
x1 = b;

%x = (a + b)/2;
for i = 1:1000

    fx0 = feval(fun,x0);
    fx1 = feval(fun,x1);
       
    c = x1 - (fx1*(x1-x0))/(fx1-fx0);
    
    x0 = x1;
    x1 = c;
    
    fc = feval(fun,c);

    xvect(i) = c;
    fx(i) = abs(fc);
   
    it_cnt = it_cnt + 1;
    xdif(it_cnt) = abs(x1 - x0);
    

    if abs(fc) < eps || abs(b-a) < eps
        return 
    elseif feval(fun,a) * fc < 0
        b = c;
    else 
        a = c;
    end
    
end


end

