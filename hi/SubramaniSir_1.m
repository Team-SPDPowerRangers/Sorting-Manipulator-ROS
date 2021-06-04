clc; clear all;

% Question-1
x=-100:100;
y=x;
[x1,x2]=meshgrid(x,y); %will create a 2 by 2 grid
z=(x1-3).^2+(x2-5).^2;
surfc(x,y,z); %Surface contour
shading interp %interpolated shading
xlabel('x');
ylabel('y');
zlabel('z');