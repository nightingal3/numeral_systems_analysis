function [g,complx,numtype,lgabv] = ndy(plotopt)

if nargin == 0 plotopt = [0 0]; end

addpath treesupp/
addpath @tree/

g.nnodes = zeros(1000,1);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
lgabv = 'ndy';
numtype = 6;

% 1
c = 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('wan','1'); c = c + 1;

% 2-10
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('tu','2'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('dii','3'); c = c + 1;
[commandcells,rulecells,numcells,nnodecells,depthcells] = SUC({'dii','fo','feifi','sigisi','seibi','aiti','neigi','tin','elufu','twalufu'},{'4','5','6','7','8','9','10','11','12'});
for i = 1:length(rulecells) 
	g.rule{c} = rulecells{i}; g.num{c} = numcells{i}; g.command{c} = commandcells{i}; 
	g.depths{c} = depthcells{i}; g.nnodes(c) = nnodecells{i};
	c = c + 1;
end

% 13...20
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'''tina''','w'},{'tin','w'},'13...19'); c = c + 1;
[commandcells,rulecells,numcells,nnodecells,depthcells] = SUC({'tinaneigi','twenti'},{'20'});
for i = 1:length(rulecells) 
	g.rule{c} = rulecells{i}; g.num{c} = numcells{i}; g.command{c} = commandcells{i}; 
	g.depths{c} = depthcells{i}; g.nnodes(c) = nnodecells{i};
	c = c + 1;
end

% 30...90
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'w','''tenti'''},{'w','tin'},'30...90'); c = c + 1;

% 21...99
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'u','''-','a','-''','v'},{'u','v'},'21...99'); c = c + 1;

% 100
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c},t_l,t_r] = POW('ondoo',{'tin','tu'},'100'); c = c + 1;

% Sets w, u, v
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('w',{'dii','fo','feifi','sigisi','seibi','aiti','neigi'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('u',{'twenti','diitenti','fotenti','feifitenti','sigisitenti','seibitenti','aititenti','neigitenti'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('v',{'wan','tu','dii','fo','feifi','sigisi','seibi','aiti','neigi'}); 

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Compute complexity
g.nnodes(find(g.nnodes==0)) = [];
complx = sum(g.nnodes);

if plotopt(1) == 1
    printGrammar(g,complx,numtype,lgabv)
end