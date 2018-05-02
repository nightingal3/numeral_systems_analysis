function [g,complx,numtype,lgabv] = hzb(plotopt)

if nargin == 0 plotopt = [0 0]; end

addpath treesupp/
addpath @tree/

g.nnodes = zeros(1000,1);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
lgabv = 'hzb';
numtype = 6;

% 1
c = 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('has','1'); c = c + 1;

% 2-10
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('q,an.u','2'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('la.na','3'); c = c + 1;
[commandcells,rulecells,numcells,nnodecells,depthcells] = SUC({'la.na','oq,e.n','li.no','il.no','al.no','bel.no','uc,i.n','ac,a.n'},{'4','5','6','7','8','9','10'});
for i = 1:length(rulecells) 
	g.rule{c} = rulecells{i}; g.num{c} = numcells{i}; g.command{c} = commandcells{i}; 
	g.depths{c} = depthcells{i}; g.nnodes(c) = nnodecells{i};
	c = c + 1;
end

% 11...19
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'''ac,a.n ''','w'},{'ac,a.n','w'},'11...19'); c = c + 1;

% 20...90
[commandcells,rulecells,numcells,nnodecells,depthcells] = SUC({'ac,a.n uc,i.n','qo.no'},{'20'});
for i = 1:length(rulecells) 
	g.rule{c} = rulecells{i}; g.num{c} = numcells{i}; g.command{c} = commandcells{i}; 
	g.depths{c} = depthcells{i}; g.nnodes(c) = nnodecells{i};
	c = c + 1;
end
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'u','''=rig'''},{'u','ac,a.n'},'30...90'); c = c + 1;

% 21...99
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MULADD({'u','''=rig','no''','w'},{'u','ac,a.n','w'},'21...99'); c = c + 1;

% 100
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c},t_l,t_r] = POW({'has','=c,it'},{'ac,a.n','q,an.u'},'100'); c = c + 1;

% Sets w, u, v
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('w',{'has','q,an.u','la.na','oq,e.n','li.no','il.no','al.no','bel.no','uci.n'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('u',{'la.na','oq,e.n','li.no','il.no','al.no','bel.no','uci.n'}); 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Compute complexity
g.nnodes(find(g.nnodes==0)) = [];
complx = sum(g.nnodes);

if plotopt(1) == 1
    printGrammar(g,complx,numtype,lgabv)
end