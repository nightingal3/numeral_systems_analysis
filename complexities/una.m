function [g,complx,numtype,lgabv] = una(plotopt)

if nargin == 0 plotopt = [0 0]; end

addpath treesupp/
addpath @tree/

g.nnodes = zeros(1000,1);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
lgabv = 'una';
numtype = 2;

% 1
c = 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('ton','1'); c = c + 1;

% 2-27
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('bitinyi','2'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('wiyniyji','3'); c = c + 1;
[commandcells,rulecells,numcells,nnodecells,depthcells] = SUC({'wiyniyji','dumbaji','amubaji','nabaji','tabaji','iynbaji','towbnabaji','takobaji','koklombaji','amolbaji','kakubmikin','kiysok lubaji','dina kakubmikbaji','dina amolbaji','dina koklombaji','dina takobaji','dina towbnabaji','dina iynbaji','dina tabaji','dina nabaji','dina amubaji','dina dumbaji','wiyniyjaba','bitinyaba','selselekca'},...
    {'2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27'});
for i = 1:length(rulecells) 
	g.rule{c} = rulecells{i}; g.num{c} = numcells{i}; g.command{c} = commandcells{i}; 
	g.depths{c} = depthcells{i}; g.nnodes(c) = nnodecells{i};
	c = c + 1;
end

% 28-100
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = HIG({'selselekca','weyk'},'28-100');


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Compute complexity
g.nnodes(find(g.nnodes==0)) = [];
complx = sum(g.nnodes);

if plotopt(1) == 1
    printGrammar(g,complx,numtype,lgabv)
end