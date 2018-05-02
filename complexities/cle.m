function [g,complx,numtype,lgabv] = cle(plotopt)

if nargin == 0 plotopt = [0 0]; end

addpath treesupp/
addpath @tree/

g.nnodes = zeros(1000,1);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
lgabv = 'cle';
numtype = 5;

% 1
c = 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('ka:3','1'); c = c + 1;

% 2-10
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('tu4','2'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('ni3','3'); c = c + 1;
[commandcells,rulecells,numcells,nnodecells,depthcells] = SUC({'ni3','kyu3','na3','hnu:3','gya:4','hna4','nu4','gya4'},{'4','5','6','7','8','9','10'});
for i = 1:length(rulecells) 
	g.rule{c} = rulecells{i}; g.num{c} = numcells{i}; g.command{c} = commandcells{i}; 
	g.depths{c} = depthcells{i}; g.nnodes(c) = nnodecells{i};
	c = c + 1;
end

% 11...19
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'''gya4''','w'},{'gya4','w'},'11...19'); c = c + 1;

% 20
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'gya:3'},{'tu4','gya4'},'20'); c = c + 1;

% 30
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'gya4','gya3'},{'gya4','gya:3'},'30'); c = c + 1;

% 40,60,80 (60,80 interpolated)
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'v','''la:3'''},{'v','gya:3'},'40,60,80'); c = c + 1;

% 50 (70,90 interpolated)
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MULADD({'v','''na4','gya3'''},{'v','gya:3','gya4'},'50,70,90'); c = c + 1;

% 21...99 interpolated
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'u','''zi32''','w'},{'u','w'},'21...99'); c = c + 1;

% 100
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'ka:3','na','la:3'},{'na3','gya:3'},'100'); c = c + 1;

% Sets w,v,u
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('w',{'ka:3','tu4','ni3','kyu3','na3','hnu:3','gya:4','hna4','nu4','gya4'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('v',{'tu4','ni3','kyu3'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('u',{'gya:3','gya4gya3','tu4la:3','tu4na4gya3','ni3la:3','ni3na4gya3','kyu3la:3','kyu3na4gya3'}); c = c + 1;

% Equivalence
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = EQU('cheithre','ceathair'); 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Compute complexity
g.nnodes(find(g.nnodes==0)) = [];
complx = sum(g.nnodes);

if plotopt(1) == 1
    printGrammar(g,complx,numtype,lgabv)
end