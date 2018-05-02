function [g,complx,numtype,lgabv] = yaq(plotopt)

if nargin == 0 plotopt = [0 0]; end

addpath treesupp/
addpath @tree/

g.nnodes = zeros(1000,1);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
lgabv = 'yaq';
numtype = 5;

% 1
c = 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE({'wepul'},'1'); c = c + 1;

% 2-6
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE({'wooi'},'2'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE({'bahi'},'3'); c = c + 1;
[commandcells,rulecells,numcells,nnodecells,depthcells] = SUC({'bahi','naiki','mamni','busani',{'woo','-','busani'}},{'4','5','6','7'});
for i = 1:length(rulecells) 
	g.rule{c} = rulecells{i}; g.num{c} = numcells{i}; g.command{c} = commandcells{i}; 
	g.depths{c} = depthcells{i}; g.nnodes(c) = nnodecells{i};
	c = c + 1;
end

% 8,9,10
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'woh','-','naiki'},{'wooi','naiki'},'8'); c = c + 1;
[commandcells,rulecells,numcells,nnodecells,depthcells] = SUC({'woh-naiki','batani'},{'9'});
for i = 1:length(rulecells) 
	g.rule{c} = rulecells{i}; g.num{c} = numcells{i}; g.command{c} = commandcells{i}; 
	g.depths{c} = depthcells{i}; g.nnodes(c) = nnodecells{i};
	c = c + 1;
end
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'woh','-','mamni'},{'wooi','mamni'},'10'); c = c + 1;

% 11...19
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'''woh','-','mamni ',',ama ''','w'},{'woh-mamni','w'},'11...19'); c = c + 1;

% 20
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'senu','-','takaa'},{'wooi','woh-mamni'},'20'); c = c + 1;

% 40,60,80,100
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'v','''-','takaa'''},{'v','senu-takaa'},'40...100'); c = c + 1;

% 21...99 (interpolated; author account missing but shows example for 21)
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'ux'},{'u','x'},'21...99'); c = c + 1;

% Sets w,v,u
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('w',{'wepu,ulai','wooi','bahi','naiki','mamni','busani','woo-busani','woh-naiki','batani'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('v',{'woi','bahi','naiki','mamni'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('u',{'senu-takaa','woi-takaa','bahi-takaa','naiki-takaa'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('x',{'1-[digit for brevity]','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19'}); c = c + 1;

% Equivalence
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = EQU('wepu,ulai','wepul'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = EQU('woi','wooi');
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Compute complexity
g.nnodes(find(g.nnodes==0)) = [];
complx = sum(g.nnodes);

if plotopt(1) == 1
    printGrammar(g,complx,numtype,lgabv)
end