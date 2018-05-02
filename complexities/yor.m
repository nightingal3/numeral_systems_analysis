function [g,complx,numtype,lgabv] = yor(plotopt)

if nargin == 0 plotopt = [0 0]; end

addpath treesupp/
addpath @tree/

g.nnodes = zeros(1000,1);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
lgabv = 'yor';
numtype = 4;

% 1
c = 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('okan','1'); c = c + 1;

% 2-10
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('eji1','2'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('eta','3'); c = c + 1;
[commandcells,rulecells,numcells,nnodecells,depthcells] = SUC({'eta','erin','arun','efa','eje','ejo','esan','ewa'},{'4','5','6','7','8','9','10'});
for i = 1:length(rulecells) 
	g.rule{c} = rulecells{i}; g.num{c} = numcells{i}; g.command{c} = commandcells{i}; 
	g.depths{c} = depthcells{i}; g.nnodes(c) = nnodecells{i};
	c = c + 1;
end

% 11-14
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'w',''' la'''},{'w','ewa'},'11...14'); c = c + 1;

% 20
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'ogun'},{'ewa','eji'},'20'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'ogbon'},{'ewa','eta'},'30'); c = c + 1;

% 40, 60, 80, 100
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'''ogo''','v'},{'ogun','v'},'40...100'); c = c + 1;

% 50, 70, 90
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = SUB({'adota'},{'ogota','ewa'},'50'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = SUB({'adorin'},{'ogorin','ewa'},'70'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = SUB({'adorun'},{'ogorun','ewa'},'90'); c = c + 1;

% 15, 25
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = SUB({'ed','ogun'},{'ogun','arun'},'15'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = SUB({'ed','ogbon'},{'ogbon','arun'},'25'); c = c + 1;

% 35, 45, 55, 65, 75, 85, 95
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = SUB({'''arun','dil''','u'},{'u','arun'},'35...95'); c = c + 1;

% 16-19,21-24,26-29,31-34,36-39,41-44,46-49,51-54,56-59,61-64,66-69,71-74,76-79,81-84,86-89,91-94,96-99
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = SUB({'w','''dil''','z'},{'z','w'},'16-19...96-99'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'w','''lel''','z'},{'z','w'},'21-24...91-94'); c = c + 1;

% Sets w,v,u,z
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('w',{'okan','eji','eta','erin'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('v',{'ji','ta','rin','run'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('u',{'ogoji','adota','ogota','adorin','ogorin','adorun','ogorun'});  c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('z',{'ogun','ogbon','ogoji','adota','ogota','adorin','ogorin','adorun','ogorun'}); c = c + 1;

% Equivalences
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = EQU('ji','eji'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = EQU('ta','eta'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = EQU('rin','erin'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = EQU('run','arun'); 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Compute complexity
g.nnodes(find(g.nnodes==0)) = [];
complx = sum(g.nnodes);

if plotopt(1) == 1
    printGrammar(g,complx,numtype,lgabv)
end