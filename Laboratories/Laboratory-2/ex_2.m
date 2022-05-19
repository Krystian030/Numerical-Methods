a = 10;
r_max = 5;
n_max = 100;
n = 0;
flag = false;
rand_count = 0;
rand_counts = [];
r = [];
x = [];
y = [];
circle_area = [];
area = 0;

while (n <= n_max)
    while (~flag)
        r_rand = rand()*r_max;
        x_rand = rand()*a;
        y_rand = rand()*a;
        flag = can_plot(x_rand,y_rand,r_rand,a);
        rand_count = rand_count + 1;
        if(flag)
            for i=1:n
                dist = sqrt((x(i)-x_rand)^2+(y(i)-y_rand)^2);
                distCircle = abs(r(i) + r_rand);
                if(dist <= distCircle)
                    flag = false;
                    break;
                end
            end
        end
    end
    axis equal
    plot_circ(x_rand,y_rand,r_rand);
    hold on
    flag = false;
    n = n+1;
    if (n <= n_max)
        r(n) = r_rand;
        x(n) = x_rand;
        y(n) = y_rand;
        rand_counts(n) = rand_count;
        rand_count = 0;
        area = area + pi*r_rand^2;
        circle_area(n) = area;

        fprintf(1, ' %s%5d%s%.3g\r ', 'n =',  n, ' S = ', area)
        pause(0.01)
    end
end

figure("Name","Powierzchnia calkowita");
semilogx(1:n_max,circle_area);
xlabel("n");
ylabel("powierzchnia calkowita");
title("Powierzchnia calkowita");
saveas(gcf,'wykres_powierzchnia_calkowita.png');

figure("Name","Srednia liczba losowan");
fun_rando = cumsum(rand_counts)./(1:numel(rand_counts));
loglog(1:n_max,fun_rando);
xlabel("n");
ylabel("Srednia liczba losowan");
title("Srednia liczba losowan");
saveas(gcf,'wykres_srednia_liczba_losowan.png');