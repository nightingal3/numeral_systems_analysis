function printGrammar(g,complx,numtype,lgabv,printopt)

if nargin < 5 printopt = 0; end

disp(['Language: ',lgabv])

if numtype == 0
    disp('Type: restricted approximate')
elseif numtype == 1
    disp('Type: restricted exact')
elseif numtype == 2
    disp('Type: body-part')
elseif numtype == 3
    disp('Type: other base')
elseif numtype == 4
    disp('Type: vigesimal')
elseif numtype == 5
    disp('Type: hybrid')
else
    disp('Type: decimal')
end

disp('Number,   Rule,   Decomposition,  Length')
for i = 1:length(g.nnodes)
    disp([g.num{i},',   ',g.command{i},',   ',g.rule{i},',  ',num2str(g.nnodes(i))])
end

disp(['c = ',num2str(complx)])
