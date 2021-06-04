% NVS PRADYUMNA
% BL.EN.U4AIE19043

%1e is left ; 

clc;
clear all;
close all;

% question 1
% part a
mata1=randi([0,5],9,2)*randi([0,5],2,9)
matb1=mata1 + transpose(mata1)
ans1a=rank(matb1)

% part b
[ans1bEigenVec, ans1bEigen]=eig(matb1);
ans1bEigenVec
ans1bEigenVal=[];
size1=size(ans1bEigen);
for i1=1:1:size1(2)
    for j1=1:1:size1(1)
        if i1==j1
            ans1bEigenVal=[ans1bEigenVal;ans1bEigen(i1,j1)];
        end
    end
end
ans1bEigenVal

% part c
disp('The eigen values are not complex')
disp('Eigen values of real-symmetric matrices are always real')
disp('Eigen values of real matrics can be real or complex')
disp('The matrix B is symmetric, so it only has real values')

% part d     not yet complete
disp('The number of zero eigen values = 4')
disp('This is because, No. of non-zero eigen values=Rank')

% part e HAVE TO CHECK AND VERIFY
disp('For a symmetric matrix, eigen vectors are always orthogonal to eachother')
ans1bEigenVec
check=dot(ans1bEigenVec(:,2),ans1bEigenVec(:,3))

% part f
[rrefOfB,rowVecPivotPosi]=rref(matb1);
rsRowVecLen=length(rowVecPivotPosi);
RowSpace1=rrefOfB(1:rsRowVecLen,:)
ColSpace1=matb1(:,rowVecPivotPosi)
NullSpace1=null(matb1)

% part g
nullityMatSize=size(null(matb1));
nullity1=nullityMatSize(2)


% question 2
a2=randi(5,10,3)*randi(5,3,5)
% part a
s1=a2*transpose(a2)
s2=transpose(a2)*a2

% part b
ans2b1=rank(s1)
ans2b2=rank(s2)

% part c
ans2c1=eig(s1)
ans2c2=eig(s2)
disp('What i noticed is that the non-zero')
disp('eigen values are same for both S1 and S2')
disp('and the no. of eigen values is equal to rank')

% part d
nullSizeA=size(null(a2));
nullSizes1=size(null(s1));
nullSizes2=size(null(s2));
ans2dnullityA=nullSizeA(2)
ans2dnullityS1=nullSizes1(2)
ans2dnullityS2=nullSizes2(2)

% question 3
% part a
v3=randi(5,1,10)
N=null(v3);
for i=1:1:9    
    orthoVec=N(:,i);
end
N

% part b
w3=transpose(v3)*v3

% part c
ans3c1=rank(w3)
ans3c2=eig(w3)

% part d
u3=v3*transpose(v3)

% part e
traceW=trace(w3)
traceU=trace(u3)
euclideanNormV=(norm(v3))^2
disp('Yes, trace of VVT and VTV=(norm(v))^2')
disp('Hence verified')


% question 4
mat4=randi(5,3,2)*randi(5,2,3)
    % for row space
[rsRRform,rscolPosiOfLeadingPivot]=rref(mat4);
rsRowVecLen = length(rscolPosiOfLeadingPivot);
Rspace=rsRRform(1:rsRowVecLen,:)
RSB1=transpose((Rspace(1,:)));% row vec is made into col
RSB2=transpose((Rspace(2,:)));% row vec is made into col
    % for null space
Nspace=null(mat4)
NSB1=Nspace(:,1)
    % for points generation    
RSpoints=[];
NSpoints=[];
for i=1:10000
    % a total of 3 random points
    % 2= row basis, 1= nullbase
 r1=-1+2*rand(1);
 r2=-1+2*rand(1);
 n1=-1+2*rand(1);
 RSpoints=[RSpoints,r1*RSB1+r2*RSB2];
 NSpoints=[NSpoints,n1*NSB1];
end
figure('name','Row and Null space')
title('name','Row and Null space')
scatter3(RSpoints(1,:),RSpoints(2,:),RSpoints(3,:),1);
hold on
scatter3(NSpoints(1,:),NSpoints(2,:),NSpoints(3,:),1);
grid on

% question 5
mat5=randi(5,3,1)*randi(5,1,3)
    % for col space
[csRRform,cscolPosiOfLeadingPivot]=rref(transpose(mat5))
csRowVecLen = length(cscolPosiOfLeadingPivot)
Cspace=csRRform(1:csRowVecLen,:)
CSB1=transpose((Cspace(1,:)));% row vec is made into col
    % for left null space
LNspace=null(transpose(mat5))
LNSB1=LNspace(:,1)
    % generating random points
CSpoints=[];
LNSpoints=[];    
for i=1:10000
    % a total of 2 random points
 c1=-1+2*rand(1);
 ln1=-1+2*rand(1);
 CSpoints=[CSpoints,c1*CSB1];
 LNSpoints=[LNSpoints,ln1*LNSB1];
end
figure('name','Column and left null space')
title('name','Column and left null space')
scatter3(CSpoints(1,:),CSpoints(2,:),CSpoints(3,:),1);
hold on
scatter3(LNSpoints(1,:),LNSpoints(2,:),LNSpoints(3,:),1);
grid on