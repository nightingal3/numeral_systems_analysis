function [g,complx,numtype,lgabv] = kyl(plotopt)

if nargin == 0 plotopt = [0 0]; end

addpath treesupp/
addpath @tree/

g.nnodes = zeros(1000,1);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
lgabv = 'kyl';
numtype = 6;

% 1
c = 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('ta-','1'); c = c + 1;

% 2-5
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('na','2'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('so','3'); c = c + 1;
[commandcells,rulecells,numcells,nnodecells,depthcells] = SUC({'so','lwi','ge'},{'4','5'});
for i = 1:length(rulecells) 
	g.rule{c} = rulecells{i}; g.num{c} = numcells{i}; g.command{c} = commandcells{i}; 
	g.depths{c} = depthcells{i}; g.nnodes(c) = nnodecells{i};
	c = c + 1;
end
% 6,8,7,9
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'w',''' swa'''},{'w','na'},'6,8'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MULADD({'w',''' swa ','ta-'''},{'w','na','ta-'},'7,9'); c = c + 1;
% 10
[commandcells,rulecells,numcells,nnodecells,depthcells] = SUC({'lwi swa ta-','cha/'},{'10'});
for i = 1:length(rulecells) 
	g.rule{c} = rulecells{i}; g.num{c} = numcells{i}; g.command{c} = commandcells{i}; 
	g.depths{c} = depthcells{i}; g.nnodes(c) = nnodecells{i};
	c = c + 1;
end

% 20...90
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'u',''' cha-'''},{'u','cha/'},'20...50'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'''cha- ''','v'},{'cha/','v'},'60,80'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'x','''cha-'''},{'x','cha/'},'70,90'); c = c + 1;

% 11...99
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'y ','z'},{'y','v'},'11...99'); c = c + 1;

% 100
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c},t_l,t_r] = POW('je',{'cha/','na'},'100'); c = c + 1;

% Sets w, u, v
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('w',{'so','lwi'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('u',{'na','so','lwi','ge'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('v',{'so swa','lwi swa'});  c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('x',{'so swa ta','lwi swa ta'});  c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('y',{'cha/','na cha-','so cha-','lwi cha-','ge cha-','cha- so swa','so swa tacha-','cha- lwi swa','lwi swa tacha-'});  c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('z',{'ta-','na','so','lwi','ge','so swa','so swa ta-','lwi swa','lwi swa ta-'});  c = c + 1;

% Equivalences
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = EQU('ta','ta-'); 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Compute complexity
g.nnodes(find(g.nnodes==0)) = [];
complx = sum(g.nnodes);

if plotopt(1) == 1
    printGrammar(g,complx,numtype,lgabv)
end