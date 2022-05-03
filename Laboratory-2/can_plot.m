function flag = can_plot(X,Y,R,A)
    if ((X-R>0) && (Y-R)>0 && (X+R)<A && (Y+R)<A)
        flag = true;
        return
    else
        flag = false;
        return
    end
end