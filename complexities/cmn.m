function [g,complx,numtype,lgabv] = cmn(plotopt)

if nargin == 0 plotopt = [0 0]; end

addpath treesupp/
addpath @tree/

g.nnodes = zeros(1000,1);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
lgabv = 'cmn';
numtype = 6;

% 1
c = 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('simi','1'); c = c + 1;

% 2-10
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('waha','2'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('pahitI','3'); c = c + 1;
[commandcells,rulecells,numcells,nnodecells,depthcells] = SUC({'pahitI','hayarokwetI','mo?ovekatI','navaitI','tatsikwItI','namegwatsikwItI','wimhinatI','simaRI'},{'4','5','6','7','8','9','10'});
for i = 1:length(rulecells) 
	g.rule{c} = rulecells{i}; g.num{c} = numcells{i}; g.command{c} = commandcells{i}; 
	g.depths{c} = depthcells{i}; g.nnodes(c) = nnodecells{i};
	c = c + 1;
end

% 11...19
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'w',''' ma ','to?ikatI'''},{'w','simaRI'},'11...19'); c = c + 1;

% 20...90
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'u','''maRI'''},{'u','simaRI'},'20,30'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'v',''' simaRI'''},{'v','simaRI'},'40...90'); c = c + 1;

% 21...29
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'''wahamanitI ''','w'},{'wahamaRI','w'},'21...29'); c = c + 1;
% 31...99
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'x ','w ','''ma ','to?ikatI'''},{'x','w'},'31...99'); c = c + 1;

% 100
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c},t_l,t_r] = POW('simatI',{'simaRI','waha'},'100'); c = c + 1;

% Sets w, u, v
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('w',{'simi','wahati','pahitI','hayarokwetI','mo?ovekatI','navaitI','tatsikwItI','namegwatsikwItI','wimhinatI'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('u',{'waha','pahi'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('v',{'hayarokwI','mo?ovetI','navai','tatsakwI','namegwatsikwI','wihminatI'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('x',{'pahimaRI','hayarokwI simaRI','mo?ovetI simaRI','navai simaRI','tatsakwI simaRI','namegwatsikwI simaRI','wihminatI simaRI'}); c = c + 1;

% Equivalences
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = EQU('waha','wahati'); 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Compute complexity
g.nnodes(find(g.nnodes==0)) = [];
complx = sum(g.nnodes);

if plotopt(1) == 1
    printGrammar(g,complx,numtype,lgabv)
end