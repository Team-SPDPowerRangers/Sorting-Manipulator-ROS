clear all;
close all;
clc;
imageFile='highimage1.PNG';
%imageFile='highimage2.PNG';
%imageFile='highimage2.PNG';

A = imread(imageFile);
B=rgb2gray(A);
figure(1)
imagesc(A)
%set(gcf,'Position',[1500 100 size(A,2) size(A,1)])

%fft
Bt=fft2(B);
Blog=log(abs(fftshift(Bt))+1);
figure(2)
imshow(mat2gray(Blog),[]);
%set(gcf,'Position',[1500 100 size(A,2) size(A,1)])

%zero out all small coefficient and inverse transform
Btsort = sort(abs(Bt(:)));
counter =1;
figure(3)
for keep=[0.01 0.005 0.002 0.001];
    subplot(2,2,counter)
    thresh = Btsort(floor((1-keep)*length(Btsort)));
    ind=abs(Bt)>thresh;
    Atlow=Bt.*ind;
    Alow=uint8(ifft2(Atlow));
    imshow(Alow)
    title(['',num2str(keep*100),'%'],'FontSize',36)    
    imwrite(Alow,strcat(int2str(counter),'_HighImage1.PNG'))
    counter=counter+1;
end

figure(4)
surf(Alow(10:10:end,10:10:end))
map = hsv(256);
rgb = ind2rgb(Alow,map);
disp(size(rgb))
figure(5)
surf(rgb(10:10:end,10:10:end))

