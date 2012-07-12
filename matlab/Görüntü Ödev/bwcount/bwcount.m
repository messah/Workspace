function V = bwcount(I)
[R, C] = size(I);
I = imfill(I, 'holes');
j = 2;
I = double(I);
for r = 1:R
	for c = 1:C
		if (I(r, c) == 1)
			i = 1;
			n = [];
			if(r >= 1)
				if (c + 1 >= 1 && c + 1 <= C)
					n(i) = I(r, c + 1);
					i = i + 1;
				end
				if (c - 1 >= 1)
					n(i) = I(r, c - 1);
					i = i + 1;
				end
			end
			if(c >= 1)
				if (r + 1 >= 1 && r + 1 <= R)
					n(i) = I(r + 1, c);
					i = i + 1;
				end
				if (r - 1 >= 1)
					n(i) = I(r - 1, c);
					i = i + 1;
				end
			end
			neigh = n(n ~= 0 & n ~= 1);
			if (~isempty(neigh))
				labels = unique(neigh);
				count = [];
				for i = 1:length(labels)
					count(i) = length(find(neigh == labels(i)));
				end
				deger = labels(find(count == max(count)));
				if (length(deger) > 1)
					s = min(labels);
					b = max(labels);
					I(r, c) = s;
					I(I == b) = s;
				else
					I(r, c) = deger;
				end
			else
				I(r, c) = j;
				j = j + 1;
			end
		end
	end
end
neigh = I(I ~= 0);
labels = unique(neigh);
    
fprintf(' label adedi:%4d\n', length(labels));
    
for i = 1:length(labels)
	fprintf('\n%3d  numaralı etiket adedi %4d\n', i, length(I(I == labels(i))));
end  
    
for i = 1:length(labels)
	I(I == labels(i)) = i;
end
    
    

