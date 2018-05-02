function [g,complx,numtype,lgabv] = sla(plotopt)

if nargin == 0 plotopt = [0 0]; end

addpath treesupp/
addpath @tree/

g.nnodes = zeros(1000,1);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
lgabv = 'sla';
numtype = 6;

% 1
c = 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('lee','1'); c = c + 1;

% 2-10
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('nakee','2'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('tai','3'); c = c + 1;
[commandcells,rulecells,numcells,nnodecells,depthcells] = SUC({'tai','dii','solai','?ehts,etai','lahdii','loto','loto','honeno'},{'4','5','6','7','8','9','10'});
for i = 1:length(rulecells) 
	g.rule{c} = rulecells{i}; g.num{c} = numcells{i}; g.command{c} = commandcells{i}; 
	g.depths{c} = depthcells{i}; g.nnodes(c) = nnodecells{i};
	c = c + 1;
end

% 20...90
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'w',''' horenq'''},{'w','horenq'},'20...90'); c = c + 1;

% 11...99
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'u',''' ?o ''','v'},{'u','v'},'11...99'); c = c + 1;

% 100
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c},t_l,t_r] = POW({'lee ','lako ','ono'},{'honeno','nakee'},'100'); c = c + 1;

% Sets w, u, v
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('w',{'nakee','tai','dii','solai','?ehts,etai','lahdii','?ehtsedii','loto'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('u',{'honeno','nakee honeno','tai honeno','dii honeno','solai honeno','?ehts,etai honeno','lahdii honeno','?ehtsedii honeno','loto honeno'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('v',{'lee','nakee','tai','dii','solai','?ehts,etai','lahdii','?ehtsedii','loto'}); 

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Compute complexity
g.nnodes(find(g.nnodes==0)) = [];
complx = sum(g.nnodes);

if plotopt(1) == 1
    printGrammar(g,complx,numtype,lgabv)
end