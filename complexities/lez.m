function [g,complx,numtype,lgabv] = lez(plotopt)

if nargin == 0 plotopt = [0 0]; end

addpath treesupp/
addpath @tree/

g.nnodes = zeros(1000,1);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
lgabv = 'lez';
numtype = 5;

% 1
c = 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('sad','1'); c = c + 1;

% 2-10
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('q,wed','2'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('pud','3'); c = c + 1;
[commandcells,rulecells,numcells,nnodecells,depthcells] = SUC({'pud','q,ud','wad','rugud','irid','muzud','k,ud','c,ud'},{'4','5','6','7','8','9','10'});
for i = 1:length(rulecells) 
	g.rule{c} = rulecells{i}; g.num{c} = numcells{i}; g.command{c} = commandcells{i}; 
	g.depths{c} = depthcells{i}; g.nnodes(c) = nnodecells{i};
	c = c + 1;
end

% 11,14...16
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'''c,u''','w'},{'c,ud','w'},'11,14...16'); c = c + 1;
% 12,13
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'''c,i''','v'},{'c,ud','v'},'12,13'); c = c + 1;
% 17...19
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'''c,e''','u'},{'c,ud','u'},'17...19'); c = c + 1;

% 20
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'qad'},{'c,ud','q,wed'},'20'); c = c + 1;

% 40
[commandcells,rulecells,numcells,nnodecells,depthcells] = SUC({'qad-ni c,ek,ud','jaxc,ur'},{'40'});
for i = 1:length(rulecells) 
	g.rule{c} = rulecells{i}; g.num{c} = numcells{i}; g.command{c} = commandcells{i}; 
	g.depths{c} = depthcells{i}; g.nnodes(c) = nnodecells{i};
	c = c + 1;
end

% 60,80
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'x',''' qad'''},{'x','qad'},'60,80'); c = c + 1;

% 21...99
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'y','''-','ni ''','z'},{'y','z'},'21...99'); c = c + 1;

% 100
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = POW('wis',{'c,ud','q,wed'},'100'); c = c + 1;

% Sets w,v,u
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('w',{'sad','q,ud','wad','rugud'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('v',{'q,wed','pud'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('u',{'rid','muzud','k,ud'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('x',{'pud','q,ud'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('y',{'qad','jaxc,ur','pudqad','q,udqad'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('z',{'1-[digit for brevity]','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19'}); c = c + 1;

% Equivalence
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = EQU('rid','irid');
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Compute complexity
g.nnodes(find(g.nnodes==0)) = [];
complx = sum(g.nnodes);

if plotopt(1) == 1
    printGrammar(g,complx,numtype,lgabv)
end