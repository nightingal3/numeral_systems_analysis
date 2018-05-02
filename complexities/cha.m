function [g,complx,numtype,lgabv] = cha(plotopt)

if nargin == 0 plotopt = [0 0]; end

addpath treesupp/
addpath @tree/

g.nnodes = zeros(1000,1);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
lgabv = 'cha';
numtype = 6;
% 1
c = 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('unu','1'); c = c + 1;

% 2-15
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('dos','2'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('tres','3'); c = c + 1;
[commandcells,rulecells,numcells,nnodecells,depthcells] = SUC({'tres','kuatro','sinko','sais','siete','ocho','nuebe','diez','onse','dosse','trese','katotse','kinse'},{'4','5','6','7','8','9','10','11','12','13','14','15'});
for i = 1:length(rulecells) 
	g.rule{c} = rulecells{i}; g.num{c} = numcells{i}; g.command{c} = commandcells{i}; 
	g.depths{c} = depthcells{i}; g.nnodes(c) = nnodecells{i};
	c = c + 1;
end

% 16...19
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'''dies',' i ''','w'},{'dies','w'},'16...19'); c = c + 1;

% 20
[commandcells,rulecells,numcells,nnodecells,depthcells] = SUC({'dies i nuebe','bente'},{'20'});
for i = 1:length(rulecells) 
	g.rule{c} = rulecells{i}; g.num{c} = numcells{i}; g.command{c} = commandcells{i}; 
	g.depths{c} = depthcells{i}; g.nnodes(c) = nnodecells{i};
	c = c + 1;
end

% 30...90
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'v','''nta'''},{'v','dies'},'30...90'); c = c + 1;

% 21...99
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'x',''' i ''','u'},{'x','u'},'21...99'); c = c + 1;

% 100
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c},t_l,t_r] = POW('siento',{'dies','dos'},'100'); c = c + 1;

% Sets w, u, v, x
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('w',{'sais','siete','ocho','nuebe'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('u',{'unu','dos','tres','kuatro','sinko','sais','siete','ocho','nuebe'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('v',{'tre','kuare','sinkue','sise','site','oche','nube'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('x',{'bente','trenta','kuarenta','sinkuenta','sisenta','sitenta','ochenta','nubenta'}); c = c + 1;

% Equivalences
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = EQU('tre','tres'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = EQU('kuare','kuatro'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = EQU('sinkue','sinko'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = EQU('sise','sais'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = EQU('site','siete'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = EQU('oche','ocho'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = EQU('nube','nuebe');

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Compute complexity
g.nnodes(find(g.nnodes==0)) = [];
complx = sum(g.nnodes);

if plotopt(1) == 1
    printGrammar(g,complx,numtype,lgabv)
end