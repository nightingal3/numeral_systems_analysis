function [g,complx,numtype,lgabv] = wra(plotopt)

if nargin == 0 plotopt = [0 0]; end

addpath treesupp/
addpath @tree/

g.nnodes = zeros(1000,1);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
lgabv = 'wra';
numtype = 4;

% 1
c = 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('isaka','1'); c = c + 1;

% 2-5
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE({'mana','mo'},'1'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE({'dihana','mo'},'1'); c = c + 1;
[commandcells,rulecells,numcells,nnodecells,depthcells] = SUC({'dihanamo',{'oro','baka','ya'},{'moho','basi'}},{'4','5'});
for i = 1:length(rulecells) 
	g.rule{c} = rulecells{i}; g.num{c} = numcells{i}; g.command{c} = commandcells{i}; 
	g.depths{c} = depthcells{i}; g.nnodes(c) = nnodecells{i};
	c = c + 1;
end

% 6-9
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'''moho ','matana ''','w'},{'mohobasi','w'},'6...9'); c = c + 1;

% 10
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'moho ','reko'},{'mohobasi','manamo'},'10'); c = c + 1;

% 11-19
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'''moho ','reko ','arai ''','v'},{'mohoreko','v'},'11...19'); c = c + 1;

% 20,40,60,80
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'warao'},{'mohoreko','orobakaya'},''); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'''warao ''','w'},{'warao','w'},'20...80'); c = c + 1;

% 21...99 (Note: interpolated from author's description)
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MULADD({'''warao ''','w',''' arai ''','v'},{'warao','w','v'},'21...99'); c = c + 1;

% 100
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'warao ','mahobasi'},{'warao','mahobasi'},'100'); c = c + 1;

% Sets w,v
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('w',{'isaka','manamo','rihanamo','orobakaya'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('v',{'1-[digit for brevity]','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19'}); c = c + 1;

% Equivalence
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = EQU('rihanamo','dihanamo'); 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Compute complexity
g.nnodes(find(g.nnodes==0)) = [];
complx = sum(g.nnodes);

if plotopt(1) == 1
    printGrammar(g,complx,numtype,lgabv)
end