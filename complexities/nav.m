function [g,complx,numtype,lgabv] = nav(plotopt)

if nargin == 0 plotopt = [0 0]; end

addpath treesupp/
addpath @tree/

g.nnodes = zeros(1000,1);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
lgabv = 'nav';
numtype = 6;

% 1
c = 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('t,aala,i','1'); c = c + 1;

% 2-10
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('naaki','2'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('taa','3'); c = c + 1;
[commandcells,rulecells,numcells,nnodecells,depthcells] = SUC({'taa','dii',',ashdla','hastaah','tsosts,id','tseebii','nahast,ei','neeznaa'},{'4','5','6','7','8','9','10'});
for i = 1:length(rulecells) 
	g.rule{c} = rulecells{i}; g.num{c} = numcells{i}; g.command{c} = commandcells{i}; 
	g.depths{c} = depthcells{i}; g.nnodes(c) = nnodecells{i};
	c = c + 1;
end

% 11...19
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'w',''',aadah'''},{'w','''neeznaa'''},'11...19\excl15,16'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'u','''ts,aadah'''},{'u','''neeznaa'''},'15,16'); c = c + 1;

% 20...90
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'v','''diin'''},{'v','neeznaa'},'20...90'); c = c + 1;

% 21...99
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MULADD({'v','''diin ','doo ','ba ''','x'},{'v','neeznaa','x'},'21...99'); c = c + 1;

% 100
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c},t_l,t_r] = MUL({'neezna','diin'},{'neeznaa','neeznaa'},'100'); c = c + 1;

% Sets w, u, v, x
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('w',{'la,','naaki','taa','dii,','tsosts,id','tseebii','nahast,ei'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('u',{',ashdla,','hasta'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('v',{'naa','ta','diz',',ashdla','hasta','tsosts,i','tseebi','nahast,e'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('x',{'t,aala,i','naaki','taa','dii',',ashdla','hastaah','tsosts,id','tseebii','nahast,ei'}); c = c + 1;

% Equivalences
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = EQU('la,','t,laa,ii'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = EQU('hasta','hastaah');  c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = EQU('naa','naaki');  c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = EQU('ta','taa');  c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = EQU('diz','dii');  c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = EQU(',ashdla',',ashdla');  c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = EQU('tsosts,i','tsosts,id');  c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = EQU('tseebi','tseebii');  c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = EQU('nahast,e','nahast,ei'); 

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Compute complexity
g.nnodes(find(g.nnodes==0)) = [];
complx = sum(g.nnodes);

if plotopt(1) == 1
    printGrammar(g,complx,numtype,lgabv)
end