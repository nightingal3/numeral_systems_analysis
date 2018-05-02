function [g,complx,numtype,lgabv] = iri(plotopt)

if nargin == 0 plotopt = [0 0]; end

addpath treesupp/
addpath @tree/

g.nnodes = zeros(1000,1);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
lgabv = 'iri';
numtype = 5;

% 1
c = 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('aon','1'); c = c + 1;

% 2-10
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('do','2'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('tri','3'); c = c + 1;
[commandcells,rulecells,numcells,nnodecells,depthcells] = SUC({'tri','ceathair','cuig','se','seacht','ocht','naoi','deich'},{'4','5','6','7','8','9','10'});
for i = 1:length(rulecells) 
	g.rule{c} = rulecells{i}; g.num{c} = numcells{i}; g.command{c} = commandcells{i}; 
	g.depths{c} = depthcells{i}; g.nnodes(c) = nnodecells{i};
	c = c + 1;
end

% 11,13...19
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'w','''deag'''},{'w','deich'},'11,13...19'); c = c + 1;

% 12
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'do','dheag'},{'do','deich'},'12'); c = c + 1;

% 20
[commandcells,rulecells,numcells,nnodecells,depthcells] = SUC({'naoideag','fiche'},{'20'});
for i = 1:length(rulecells) 
	g.rule{c} = rulecells{i}; g.num{c} = numcells{i}; g.command{c} = commandcells{i}; 
	g.depths{c} = depthcells{i}; g.nnodes(c) = nnodecells{i};
	c = c + 1;
end

% 30
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'deich','fichead'},{'deich','fiche'},'30'); c = c + 1;

% 31...39
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'v',''' ar',' fhichid'''},{'v','fiche'},'31...39'); c = c + 1;

% 40
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'dai','chead'},{'dod','fiche'},'40'); c = c + 1;

% 50
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'deich ','is ','dai','chead'},{'deich','daichead'},'50'); c = c + 1;

% 60,80
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'u',''' fichid'''},{'u','fiche'},'60,80'); c = c + 1;

% 70,90
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MULADD({'''deich ','is ''','u',''' fichid'''},{'u','fiche','deich'},'70,90'); c = c + 1;

% 21...29,41...99 (interpolated; 21-29 present in author's account)
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'x',''' is ''','y'},{'x','y'},'21...29,41...99'); c = c + 1;

% 100
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = POW('cead',{'deich','do'},'100'); c = c + 1;

% Sets w,v,u,x,y
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('w',{'aon','tri','ceathair','cuig','se','seacht','ocht','naoi'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('v',{'aondeag','dodheag','trideag','ceathairdeag','cuigdeag','sedeag','seachtdeag','ochtdeag','naoideag'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('u',{'tri','cheithre'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('x',{'aon','do','tri','ceathair','cuig','se','seacht','ocht','naoi'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('y',{'fiche','daichead','deich is daichead','tri fichid','deich is tri fichid','cheithre fichid','deich is cheithre fichid'}); c = c + 1;

% Equivalence
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = EQU('cheithre','ceathair'); 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Compute complexity
g.nnodes(find(g.nnodes==0)) = [];
complx = sum(g.nnodes);

if plotopt(1) == 1
    printGrammar(g,complx,numtype,lgabv)
end