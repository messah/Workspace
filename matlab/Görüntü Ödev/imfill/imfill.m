function V = imfill2(bw, esik)
    bw2 = imfill(bw,'holes');
    l = bwlabel(bw2);
    ls = unique(l(l~=0));
    for i=1:length(ls)
        if length(find(l==i)) < esik 
            l(find(l==i)) = 0;
        end
    end
    imshow(l)
