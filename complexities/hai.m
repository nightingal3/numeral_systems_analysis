function [g,complx,numtype,lgabv] = hai(plotopt)

if nargin == 0 plotopt = [0 0]; end

addpath treesupp/
addpath @tree/

g.nnodes = zeros(1000,1);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
lgabv = 'hai';
numtype = 6;

% 1
c = 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('srwaansang','1'); c = c + 1;

% 2-8
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('sdang','2'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('hlrun.ahl','3'); c = c + 1;
[commandcells,rulecells,numcells,nnodecells,depthcells] = SUC({'hlrun.ahl','stansang','tleehl','tluwan.ahl','jagwa.a','sdaansaangaa'},{'4','5','6','7','8'});
for i = 1:length(rulecells) 
	g.rule{c} = rulecells{i}; g.num{c} = numcells{i}; g.command{c} = commandcells{i}; 
	g.depths{c} = depthcells{i}; g.nnodes(c) = nnodecells{i};
	c = c + 1;
end
% 10
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'tlaa.ahl'},{'sdang','tleehl'},'10'); c = c + 1;
% 9
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = SUB({'tlaa.ahl ','srwaansang ','gaw'},{'tlaa.ahl','srwaansang'},'9'); c = c + 1;

% 11...18
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'''tlaa.ahl ','7waaga ''','w'},{'tlaa.ahl','w'},'11...18'); c = c + 1;

% 20...90
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'''tlaa.ahl ''','u'},{'tlaa.ahl','u'},'20...90'); c = c + 1;
% 19
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = SUB({'tlaa.alii ','sdang ','srwaansang ','gaw'},{'tlaa.alii sdang','srwaansang'},'19'); c = c + 1;

% 21...99
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MULADD({'''tlaa.ahl ''','u',' 7waaga ''','v'},{'tlaa.ahl','u','v'},'21...99'); c = c + 1;

% 100
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c},t_l,t_r] = POW('bai3',{'shi2','er4'},'100'); c = c + 1;

% Sets w, u, v
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('w',{'srwaansang','sdang','hlrun.ahl','stansang','tleehl','tluwan.ahl'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('u',{'sdang','hlrun.ahl','stansang','tleehl','tluwan.ahl','jagwa.a'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('v',{'srwaansang','sdang','hlrun.ahl','stansang','tleehl','tluwan.ahl','jagwa.a','sdaansaangaa','tlaa7ahllng srwaansing gaw'}); 

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Compute complexity
g.nnodes(find(g.nnodes==0)) = [];
complx = sum(g.nnodes);

if plotopt(1) == 1
    printGrammar(g,complx,numtype,lgabv)
end