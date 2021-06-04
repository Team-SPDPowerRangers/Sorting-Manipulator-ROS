% NVS PRADYUMNA
% BL.EN.U4AIE19043

clc;
clear all;

% question 1
ans1mat=randi(5,10);
[eigenVectors1,eigenValues1]=eig(ans1mat);
eigenVectors1
ans1EigenVal=[];
size1=size(eigenValues1);
for i1=1:1:size1(2)
    for j1=1:1:size1(1)
        if i1==j1
            ans1EigenVal=[ans1EigenVal;eigenValues1(i1,j1)];
        end
    end
end
ans1EigenVal


% question 2
% part a
a2=randi(5,3);
[rightEigen2a,eigenValues2a,leftEigen2a]=eig(a2);
rightEigen2a
leftEigen2a
ans2EigenVal=[];
size1=size(eigenValues2a);
for i1=1:1:size1(2)
    for j1=1:1:size1(1)
        if i1==j1
            ans2EigenVal=[ans2EigenVal;eigenValues2a(i1,j1)];
        end
    end
end
ans2EigenVal

% part b
syms x;
ans2b=charpoly(a2,x)
charpolyCoeff=charpoly(a2);

% part c 
ans2c = polyvalm(charpolyCoeff,a2)
    % polyvalm means substitute matrix in place of variable
disp('Since the output is a zero matrix')
disp('It means that the matrix satisfies it characteristic polynomial ')
disp('It satisfies the cayley-hamiston theorem')
disp('Hence verified')


% question 3
a3=randi(5,5,3)
a3aaT=a3*transpose(a3)
a3aaTEigen=eig(a3aaT)
a3aTa=transpose(a3)*a3
a3aTaEigen=eig(a3aTa)
disp('Yes, the non-zero eigen values')
disp('of ATA and AAT are same')

 
% question 4
e41=3;
e42=5;
e43=7;
e44=11;
ev41=[1;1;2;2];
ev42=[1;0;1;0];
ev43=[2;1;2;0];
ev44=[0;1;1;0];
diag4=diag([e41,e42,e43,e44])
eVectors4=[ev41,ev42,ev43,ev44]
ans4=eVectors4*diag4*inv(eVectors4)
 

% question 5
e1=5;
e2=9;
eV1=[1;1];
eV2=[1;-1];
D5=diag([e1,e2])
v5=[eV1,eV2]
ans5=v5*D5*inv(v5)