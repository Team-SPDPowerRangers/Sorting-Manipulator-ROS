clc,clear all;

% Question-1
matSize=2
a=randi(9,matSize,matSize)
b=randi(9,matSize,matSize)
c=randi(9,matSize,matSize)
d=randi(9,matSize,matSize)

akronb=kron(a,b)
ckrond=kron(c,d)

% 1. (A kron B)' = A' kron B'
akronbTranspose=transpose(akronb)
aTkronbT=kron(transpose(a),transpose(b))
ans1a=akronbTranspose==aTkronbT

% 2. (A kron B)(c kron D) = AC kron BD
akronbIntockrond=akronb*ckrond
ackronbd=kron(a*c,b*d)
ans1b=akronbIntockrond==ackronbd

% 3. (A kron B)(inv(A)kron inv(B)) = I kron I
akronbIntoainvkronbinv=round(akronb*(kron(inv(a),inv(b))))
ikroni=kron(eye(matSize),eye(matSize))
ans1c=akronbIntoainvkronbinv==ikroni

% Question-2
colSize=4
U=randi(9,colSize,1)
V=randi(9,colSize,1)
UkronV=kron(U,V)
as1=reshape((transpose(U*transpose(V))),[],1)
as2=reshape(V*transpose(U),[],1)
ans2=as1==as2

% Question-3
A=randi(20,9,1)
ans3=transpose(reshape(A,3,3))

% Question-4
ab=fft(4)