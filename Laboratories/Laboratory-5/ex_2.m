clc
clear all
close all

[XX,YY] = meshgrid(linspace(0,100,101),linspace(0,100,101));

div_poly = [];
div_tryg = [];


% pierwszy pomiar
[x, y, f] = lazik(5);
[p] = polyfit2d(x,y,f);
[FFP_prev] = polyval2d(XX,YY,p);

[p] = trygfit2d(x,y,f);
[FFT_prev] = trygval2d(XX,YY,p);


for i = 2:41
    K = i + 4;
    [x,y,f] = lazik(K);
    
    [p] = polyfit2d(x,y,f);
    [FFP] = polyval2d(XX,YY,p);
    div_poly(i-1) = max(max(abs(FFP-FFP_prev)));
    FFP_prev = FFP;

    [p] = trygfit2d(x,y,f);
    [FFT] = trygval2d(XX,YY,p);
    div_tryg(i-1) = max(max(abs(FFT-FFT_prev)));
    FFT_prev = FFT;
end

plot(6:45, div_poly);
xlabel("Liczba punktów pomiarowych [K]")
ylabel("Maksymalna wartość różnicy interpolowanych funkcji")
title("Zbieżność interpolacji wielomianowej")
saveas(gcf,"zbieznosc_interpolacji_wielomianowej.png")

plot(6:45, div_tryg);
xlabel("Liczba punktów pomiarowych [K]")
ylabel("Maksymalna wartość różnicy interpolowanych funkcji")
title("Zbieżność interpolacji trygonometrycznej")
saveas(gcf,"zbieznosc_interpolacji_trygonometrycznej.png")