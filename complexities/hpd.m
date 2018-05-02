function [g,complx,numtype,lgabv] = hpd(plotopt)

if nargin == 0 plotopt = [0 0]; end

addpath treesupp/
addpath @tree/

g.nnodes = zeros(1000,1);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
lgabv = 'hpd';
numtype = 1;

c = 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('?ayup','1'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('ko?ap','2'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('mora?ap','3'); c = c + 1;
[commandcells,rulecells,numcells,nnodecells,depthcells] = SUC({'mora?ap','babni','?aedapuh'},...
    {'4','5'});
for i = 1:length(rulecells) 
	g.rule{c} = rulecells{i}; g.num{c} = numcells{i}; g.command{c} = commandcells{i}; 
	g.depths{c} = depthcells{i}; g.nnodes(c) = nnodecells{i};
	c = c + 1;
end

[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'cap ','cob ','popog'},{'?aedapuh','?ayup'},'6'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'u',''' cob ','cakget '''},{'?u','?aedapuh'},'7...9'); c = c + 1;

[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'cob ','ni-','hu?'},{'?aedapuh','ko?ap'},'10'); c = c + 1;

[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'v',''' jib ','cakget '''},{'v','cob ni-hu?'},'11...14,16...19'); c = c + 1;

[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'?ayup ','jib ','hu?'},{'?aedapuh','mora?ap'},'15'); c = c + 1;

[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'jib ','ni-','hu?'},{'?aedapuh','babni'},'20'); c = c + 1;

[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = HIG({'jib ni-hu?','many'},'21-100');c = c + 1;

[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('u',{'ko?ap','mora?ap','babni'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('v',{'form(another)','ko?ap','mora?ap','babni'}); c = c + 1;

[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = EQU('form(another)','?ayup'); 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Compute complexity
g.nnodes(find(g.nnodes==0)) = [];
complx = sum(g.nnodes);

if plotopt(1) == 1
    printGrammar(g,complx,numtype,lgabv)
end