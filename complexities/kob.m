function [g,complx,numtype,lgabv] = kob(plotopt)

if nargin == 0 plotopt = [0 0]; end

addpath treesupp/
addpath @tree/

g.nnodes = zeros(1000,1);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
lgabv = 'kob';
numtype = 2;

% 1
c = 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('wanig nobo','1'); c = c + 1;
% 2-23
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('igwo','2'); c = c + 1;
[commandcells,rulecells,numcells,nnodecells,depthcells] = SUC({'igwo','igwo ag nobo','igwo milo','mamid','kago','mudun','raleb','ajip','sidug','agip','mogan','agip bog','sidug bog','ajip bog','raleb bog','mudun bog','kagol bog','mamid bog','igwo milo','igwo','igwo','wanig nobo'},...
    {'3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23'});
for i = 1:length(rulecells) 
	g.rule{c} = rulecells{i}; g.num{c} = numcells{i}; g.command{c} = commandcells{i}; 
	g.depths{c} = depthcells{i}; g.nnodes(c) = nnodecells{i};
	c = c + 1;
end

% 24-46
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'''nin ','ju-ol ','adog ','da ''','w'},{'wanig nobo','w'},'24...46'); c = c + 1;

% 47...69
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MULADD({'''nin ','ju-ol ','mohop ','adog ','da ''','w'},{'igwo','wanig nobo','w'},'47...69'); c = c + 1;

% Note: numbers beyond 70 are deduced from author's account of grammar

% 70...92
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MULADD({'''nin ','ju-ol ','mohau ','nogag ','adog ','da ''','w'},{'igwo ag nobo','wanig nobo','w'},'70...92'); c = c + 1;

% 93...100
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MULADD({'''nin ','ju-ol ','mohau ','mohau ','adog ','da ''','w'},{'igwo milo','wanig nobo','w'},'93...100'); c = c + 1;

% Set w
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('w',{'wanig nobo','igwo','igwo ag nobo','igwo milo','mamid','kago','mudun','raleb','ajip','sidug','agip','mogan','agip bog','sidug bog','ajip bog','raleb bog','mudun bog','kagol bog','mamid bog','igwo milo','igwo','igwo','wanig nobo'});
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Compute complexity
g.nnodes(find(g.nnodes==0)) = [];
complx = sum(g.nnodes);

if plotopt(1) == 1
    printGrammar(g,complx,numtype,lgabv)
end