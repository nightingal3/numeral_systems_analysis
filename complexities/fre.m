function [g,complx,numtype,lgabv] = fre(plotopt)

if nargin == 0 plotopt = [0 0]; end

addpath treesupp/
addpath @tree/

g.nnodes = zeros(1000,1);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
lgabv = 'fre';
numtype = 6;

% 1
c = 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('un','1'); c = c + 1;

% 2-16
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('deux','2'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('trois','3'); c = c + 1;
[commandcells,rulecells,numcells,nnodecells,depthcells] = SUC({'trois','quatre','cinq','six','sept','huit','neuf','dix','onze','douze','treize','quatorze','quinze','seize'},{'4','5','6','7','8','9','10','11','12','13','14','15','16'});
for i = 1:length(rulecells) 
	g.rule{c} = rulecells{i}; g.num{c} = numcells{i}; g.command{c} = commandcells{i}; 
	g.depths{c} = depthcells{i}; g.nnodes(c) = nnodecells{i};
	c = c + 1;
end

% 17...19
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'''dix','-''','w'},{'dix','w'},'17...19'); c = c + 1;

% 20...60,80
[commandcells,rulecells,numcells,nnodecells,depthcells] = SUC({'dix-neuf','wingt'},{'20'});
for i = 1:length(rulecells) 
	g.rule{c} = rulecells{i}; g.num{c} = numcells{i}; g.command{c} = commandcells{i}; 
	g.depths{c} = depthcells{i}; g.nnodes(c) = nnodecells{i};
	c = c + 1;
end
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'trente'},{'trois','dix'},'30'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'quarante'},{'quatre','dix'},'40'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'cinquante'},{'cinq','dix'},'50'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'soixante'},{'six','dix'},'60'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'quatre','-','vingt','s'},{'quatre','vingt'},'80'); c = c + 1;

% 21...61,81
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'u','''-','et','-''','un'},{'u','un'},'21...61'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'quatre','-','vingt','-','un'},{'quatre-vingts','un'},'81'); c = c + 1;

% 22...69
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'u','''-''','v'},{'u','v'},'22...69'); c = c + 1;
% 82...89
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'''quatre','-','vingt','-''','v'},{'quatre-vingts','v'},'82...89'); c = c + 1;

% 70...79excl71,90...99excl91
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'x','''-''','y'},{'x','y'},'70...79,90...99excl71,91'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'soixante','-','et','-','onze'},{'soixante','onze'},'71'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'quatre','-','vingt','-','onze'},{'quatre-vingts','onze'},'91'); c = c + 1;

% 100
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c},t_l,t_r] = POW('cent',{'dix','deux'},'100'); c = c + 1;

% Sets w, u, v, x, y
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('w',{'sept','huit','neuf'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('u',{'vingt','trente','quarante','cinquante','soixante'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('v',{'deux','trois','quatre','cinq','six','sept','huit','neuf'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('x',{'soixante','quatre-vingt'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('y',{'dix','douze','treize','quatorze','quinze','seize','dix-sept','dix-huit','dix-neuf'}); 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Compute complexity
g.nnodes(find(g.nnodes==0)) = [];
complx = sum(g.nnodes);

if plotopt(1) == 1
    printGrammar(g,complx,numtype,lgabv)
end