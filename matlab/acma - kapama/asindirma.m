function BW = asindirma(BW)
%I = imread('cameraman.tif');
%BW = im2bw(I);
[R C] = size(BW);
J = ones(R+2,C+2);
J(2:R+1,2:C+1) = BW;
K = J;
for r=2:R+1
    for c=2:C+1
        if J(r,c) && (~J(r-1,c-1) || ~J(r-1,c) || ~J(r-1,c+1) || ~J(r,c-1) || ~J(r,c+1) || ~J(r+1,c-1) || ~J(r+1,c) || ~J(r+1,c+1))
            K(r,c) = 0;
        end
    end
end
BW = K(2:R+1,2:C+1);