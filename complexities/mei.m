function [g,complx,numtype,lgabv] = mei(plotopt)

if nargin == 0 plotopt = [0 0]; end

addpath treesupp/
addpath @tree/

g.nnodes = zeros(1000,1);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
lgabv = 'mei';
numtype = 5;

% 1
c = 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE({'a','ma'},'1'); c = c + 1;

% 2-7
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE({'a','ni'},'2'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE({'a','hum'},'3'); c = c + 1;
[commandcells,rulecells,numcells,nnodecells,depthcells] = SUC({'ahum',{'ma','ri'},{'ma','ga'},{'ta','ruk'},{'ta','ret'}},{'4','5','6','7'});
for i = 1:length(rulecells) 
	g.rule{c} = rulecells{i}; g.num{c} = numcells{i}; g.command{c} = commandcells{i}; 
	g.depths{c} = depthcells{i}; g.nnodes(c) = nnodecells{i};
	c = c + 1;
end

% 10,8,9
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'tara'},{'ani','maga'},'10'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = SUB({'ni','pan'},{'tara','ani'},'8'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = SUB({'ma','pan'},{'tara','ama'},'9'); c = c + 1;

% 11...13
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'tara','ma','thoy'},{'tara','ama'},'11'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'tara','ni','thoy'},{'tara','ani'},'12'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'tara','hum','thoy'},{'tara','ahum'},'13'); c = c + 1;
% 14...19
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'''tara''','w'},{'tara','w'},'14...19'); c = c + 1;

% 20
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'kun'},{'ani','tara'},'20'); c = c + 1;

% 30 
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'kun','tra'},{'kun','tara'},'30'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MULADD({'hum','phu','tara'},{'ahum','kun','tara'},'70'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MULADD({'mari','phu','tara'},{'mari','phu','tara'},'90'); c = c + 1;

% 20,40,60,80
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'ni','phu'},{'ani','kun'},'40'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'hum','phu'},{'ahum','kun'},'60'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'mari','phu'},{'mari','kun'},'80'); c = c + 1;

% 100
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = POW('cama',{'tara','ani'},'100'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = DIV({'yag','khay'},{'cama','ani'},'50'); c = c + 1;

% 21...99 (interpolated; author account missing)
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'vu'},{'v','u'},'21...99'); c = c + 1;

% Sets w,v,u
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('w',{'mari','maga','taruk','taret'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('v',{'kun','kuntra','niphu','yagkhay','humphu','humphutara','mariphu','mariphutara'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('u',{'1-[digit for brevity]','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19'}); 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Compute complexity
g.nnodes(find(g.nnodes==0)) = [];
complx = sum(g.nnodes);

if plotopt(1) == 1
    printGrammar(g,complx,numtype,lgabv)
end