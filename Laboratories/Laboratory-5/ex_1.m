clc
clear all
close all

% punkty
K = [5, 15, 25, 35];

% mapa rozkładu
[XX,YY] = meshgrid(linspace(0,100,101),linspace(0,100,101));

for i = 1:size(K, 2)
    [x,y,f] = lazik(K(i));
    
    % interpolacja wielomianowa
    [p] = polyfit2d(x,y,f);
    [FFW] = polyval2d(XX,YY,p);

    %interpolacja trygonometryczna
    [p] = trygfit2d(x,y,f);
    [FFT] = trygval2d(XX,YY,p);
    
    figure("Name",sprintf("%d_probek.png",K(i)))

    % droga ruchu łazika
    subplot(2,2,1)
    plot(x,y,'-o','linewidth',1, 'markersize', 3)
    xlabel("x [m]")
    ylabel("y [m]")
    title(sprintf("Tor ruchu łazika dla %d próbek",K(i)));
    axis equal

    % wartości zebranych próbek
    subplot(2,2,2)
    plot3(x,y,f,'o')
    xlabel("x [m]")
    ylabel("y [m]")
    zlabel("f(x,y)")
    grid on
    title(sprintf("Zebrane wartości dla %d próbek",K(i)));
    axis tight

    % interpolacja wielomianowa - surf
    subplot(2,2,3)
    surf(XX,YY,FFW)
    shading flat
    xlabel("x [m]")
    xlim([0 100])
    ylabel("y [m]")
    zlabel("f(x,y)")
    title(sprintf("Interpolacja wielomianowa dla %d wartości",K(i)));
    axis tight

    % interpolacja trygonometryczna - surf
    subplot(2,2,4)
    surf(XX,YY,FFT)
    shading flat
    xlabel("x [m]")
    ylabel("y [m]")
    zlabel("f(x,y)")
    title(sprintf("Interpolacja trygonometryczna dla %d wartości",K(i)));
    axis tight

    % zapis png
    set(gcf, 'PaperUnits', 'inches');
    x_width=10;
    y_width=6;
    set(gcf, 'PaperPosition', [0 0 x_width y_width]); 
    saveas(gcf,sprintf("%d_probek.png",K(i)))
end