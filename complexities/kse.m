function [g,complx,numtype,lgabv] = kse(plotopt)

if nargin == 0 plotopt = [0 0]; end

addpath treesupp/
addpath @tree/

g.nnodes = zeros(1000,1);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
lgabv = 'kse';
numtype = 6;

% 1
c = 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('foo','1'); c = c + 1;

% 2-10
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('higka','2'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('hinza','3'); c = c + 1;
[commandcells,rulecells,numcells,nnodecells,depthcells] = SUC({'hinza','taaci','guu','iddu','iiye','yaaha','yagga','woy'},{'4','5','6','7','8','9','10'});
for i = 1:length(rulecells) 
	g.rule{c} = rulecells{i}; g.num{c} = numcells{i}; g.command{c} = commandcells{i}; 
	g.depths{c} = depthcells{i}; g.nnodes(c) = nnodecells{i};
	c = c + 1;
end

% 20...90
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'''wara''','w'},{'woy','w'},'20,30'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'''woy','-''','u'},{'woy','u'},'40...90'); c = c + 1;

% 11...99
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'v','''-','cindi','-''','x'},{'v','x'},'11...99'); c = c + 1;

% 100
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c},t_l,t_r] = POW('zaggu',{'woy','higka'},'100'); c = c + 1;

% Sets w, u, v
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('w',{'gka','nza'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('u',{'taaci','guu','iddu','iiye','yaaha','yagga'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('v',{'woy','waragka','waranza','woy-taaci','woy-guu','woy-iddu','woy-iiye','woy-yaaha','woy-yagga'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('x',{'foo','higka','hinza','taaci','guu','iddu','iiye','yaaha','yagga'}); c = c + 1;

% Equivalences
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = EQU('gka','higka'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = EQU('nza','hinza');

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Compute complexity
g.nnodes(find(g.nnodes==0)) = [];
complx = sum(g.nnodes);

if plotopt(1) == 1
    printGrammar(g,complx,numtype,lgabv)
end