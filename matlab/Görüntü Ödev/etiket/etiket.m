function E = etiket(I)
[R,C] = size(I);
E = double(I);
label = 2;
for j=1:R
    for i=1:C
        if j==1 & i==1
            if E(j,i) == 1
                E(j,i) = label;
                label = label + 1;
            end
        elseif j==1
            if E(j,i) == 1
                if E(j,i-1) > 1
                    E(j,i) = E(j,i-1);
                else
                    E(j,i) = label;
                    label = label + 1;
                end
            end
        elseif i==1    
            if E(j,i) == 1
                if E(j-1,i) > 1
                    E(j,i) = E(j-1,i);
                else
                    E(j,i) = label;
                    label = label + 1;
                end
            end   
        else
            if E(j,i) == 1
                if (E(j-1,i) > 1) & (E(j,i-1) > 1)
                    if E(j-1,i) > E(j,i-1)
                        E(j,i) = E(j,i-1);
                        E(E == E(j-1,i)) = E(j,i-1);
                    else
                        E(j,i) = E(j-1,i);
                        E(E == E(j,i-1)) = E(j-1,i);
                    end
                elseif E(j-1,i) > 1
                    E(j,i) = E(j-1,i);
                elseif E(j,i-1) > 1
                    E(j,i) = E(j,i-1);
                else
                    E(j,i) = label;
                    label = label + 1;
                end
            end
        end 
    end
end
A = unique(E(:));
for i=2:length(A)
    E(E==A(i)) = i-1;
end

end
