clc
clear all
close all

% Problem 1
a = 1;   
b = 60000;

[xvect, xdif, fx, it_cnt] = bisect(a,b,1e-3,@algorithm_input);
feval(@algorithm_input,xvect(it_cnt))
figure("Name","Bisekcja");
semilogy(1:it_cnt,xvect);
xlabel("Numer iteracji");
ylabel("Liczba parametrów wejściowych [N]");
title("Bisekcja - wartości kolejnych przybliżeń [Problem 1]");
print -dpng 1.1_bisekcja_wartosci_kolejnych_przyblizen_184589.png

figure("Name","Bisekcja");
semilogy(1:it_cnt,xdif);
xlabel("Numer iteracji");
ylabel("Różnica pomiędzy wartościami x w kolejnych iteracjach");
title({"Bisekcja - różnica pomiędzy wartościami x", "W kolejnych iteracjach [Problem 1]"});
print -dpng 1.1_bisekcja_roznica_pomiedzy_kolejnymi_wartosciami_184589.png

[xvect, xdif, fx, it_cnt] = secant_method(a,b,1e-3,@algorithm_input);
feval(@algorithm_input,xvect(it_cnt))
figure("Name","Metoda siecznych");
semilogy(1:it_cnt,xvect);
xlabel("Numer iteracji");
ylabel("Liczba parametrów wejściowych [N]");
title("Metoda siecznych - wartości kolejnych przybliżeń [Problem 1]");
print -dpng 1.2_metoda_siecznych_wartosci_kolejnych_przyblizen_184589.png

figure("Name","Metoda siecznych");
semilogy(1:it_cnt,xdif);
xlabel("Numer iteracji");
ylabel("Różnica pomiędzy wartościami x w kolejnych iteracjach");
title({"Metoda siecznych - różnica pomiędzy wartościami x", "W kolejnych iteracjach [Problem 1]"});
print -dpng 1.2_metoda_siecznych_roznica_pomiedzy_kolejnymi_wartosciami_184589.png

% Problem 2
a = 0;   
b = 50;

[xvect, xdif, fx, it_cnt] = bisect(a,b,1e-12,@compute_impedance);

feval(@compute_impedance,xvect(it_cnt))
figure("Name","Bisekcja");
semilogy(1:it_cnt,xvect);
xlabel("Numer iteracji");
ylabel("Częstoltiwość kątowa ω[rad/s]");
title("Bisekcja - wartości kolejnych przybliżeń [Problem 2]");
print -dpng 2.1_bisekcja_wartosci_kolejnych_przyblizen_184589.png

figure("Name","Metoda siecznych");
semilogy(1:it_cnt,xdif);
xlabel("Numer iteracji");
ylabel("Różnica pomiędzy wartościami x w kolejnych iteracjach");
title({"Bisekcja - różnica pomiędzy wartościami x","W kolejnych iteracjach [Problem 2]"});
print -dpng 2.1_bisekcja_roznica_pomiedzy_kolejnymi_wartosciami_184589.png


[xvect, xdif, fx, it_cnt] = secant_method(a,b,1e-12,@compute_impedance);
feval(@compute_impedance,xvect(it_cnt))
figure("Name","Metoda siecznych");
semilogy(1:it_cnt,xvect);
xlabel("Numer iteracji");
ylabel("Częstoltiwość kątowa ω[rad/s]");
title("Metoda siecznych - wartości kolejnych przybliżeń [Problem 2]");
print -dpng 2.2_metoda_siecznych_wartosci_kolejnych_przyblizen_184589.png

figure();
semilogy(1:it_cnt,xdif);
xlabel("Numer iteracji");
ylabel("Różnica pomiędzy wartościami x w kolejnych iteracjach");
title({"Metoda siecznych - różnica pomiędzy wartościami x","W kolejnych iteracjach [Problem 2]"});
print -dpng 2.2_metoda_siecznych_roznica_pomiedzy_kolejnymi_wartosciami_184589.png

% Problem 3
[xvect, xdif, fx, it_cnt] = bisect(a,b,1e-12,@time_flight);

feval(@time_flight,xvect(it_cnt))
figure("Name","Bisekcja");
semilogy(1:it_cnt,xvect);
xlabel("Numer iteracji");
ylabel("Czas t [s]");
title("Bisekcja - wartości kolejnych przybliżeń [Problem 3]");
print -dpng 3.1_bisekcja_wartosci_kolejnych_przyblizen_184589.png

figure();
semilogy(1:it_cnt,xdif);
xlabel("Numer iteracji");
ylabel("Różnica pomiędzy wartościami x w kolejnych iteracjach");
title({"Bisekcja - różnica pomiędzy wartościami x","W kolejnych iteracjach [Problem 3]"});
print -dpng 3.1_bisekcja_roznica_pomiedzy_kolejnymi_wartosciami_184589.png


[xvect, xdif, fx, it_cnt] = secant_method(a,b,1e-12,@time_flight);
feval(@time_flight,xvect(it_cnt))
figure("Name","Metoda siecznych");
semilogy(1:it_cnt,xvect);
xlabel("Numer iteracji");
ylabel("Czas t [s]");
title("Metoda siecznych - wartości kolejnych przybliżeń [Problem 3]");
print -dpng 3.2_metoda_siecznych_wartosci_kolejnych_przyblizen_184589.png

figure();
semilogy(1:it_cnt,xdif);
xlabel("Numer iteracji");
ylabel("Różnica pomiędzy wartościami x w kolejnych iteracjach");
title({"Metoda siecznych - różnica pomiędzy wartościami x", "W kolejnych iteracjach [Problem 3]"});
print -dpng 3.2_metoda_siecznych_roznica_pomiedzy_kolejnymi_wartosciami_184589.png

% === Zadanie 3 === 
options = optimset("Display","iter");
[x,fval,exitflag,output] = fzero(@tan,6, options);
options = optimset("Display","iter");
[x,fval,exitflag,output] = fzero(@tan,4.5, options);