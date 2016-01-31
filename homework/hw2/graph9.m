

X=linspace(0,100);
n = 3;

for i=1:100
    Y(i) = X(i).^(1+n.^(-1))+(-1).*(X(i).^(n.^(-1))).^(1+n).*(1+n).^(-1);
end

loglog(X,Y)
xlabel('d range 0-100')
ylabel('Area between curves')
title('n = 3')