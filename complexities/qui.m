function [g,complx,numtype,lgabv] = qui(plotopt)

if nargin == 0 plotopt = [0 0]; end

addpath treesupp/
addpath @tree/

g.nnodes = zeros(1000,1);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
lgabv = 'qui';
numtype = 6;

% 1
c = 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('wel','1'); c = c + 1;

% 2-10
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('lawe','2'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('qwa,le','3'); c = c + 1;
[commandcells,rulecells,numcells,nnodecells,depthcells] = SUC({'qwa,le','bayas','tasi','teilasi','lawaqt,sisi','lawet,ali','wilt,ali','t,opa'},{'4','5','6','7','8','9','10'});
for i = 1:length(rulecells) 
	g.rule{c} = rulecells{i}; g.num{c} = numcells{i}; g.command{c} = commandcells{i}; 
	g.depths{c} = depthcells{i}; g.nnodes(c) = nnodecells{i};
	c = c + 1;
end

% 11...19
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'w','''t,siyo,'''},{'w','t,opa'},'11...19'); c = c + 1;

% 20...90
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'u','''s.ta'''},{'u','t,opa'},'20...90'); c = c + 1;

% 21...99
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MULADD({'u','''s.ta ','he,xat ''','v'},{'u','t,opa','v'},'21...99'); c = c + 1;

% 100
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c},t_l,t_r] = POW('tcilta,s.ta',{'t,opa','lawe'},'100'); c = c + 1;

% Sets w, u, v
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('w',{'wi,l','lawe','qwa,le','bayas','tasi','teilasi','lawaqt,sisi','lawet,ali','wilt,ali'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('u',{'lawa','qwa,la','baya','tasi','teilasi','lawaqt,sisi','lawet,ali','wilt,ali'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('v',{'we,l','la,u','qwa,le','bayas','tasi','teilasi','lawaqt,sisi','lawet,ali','wilt,ali'}); 


% Equivalences
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = EQU('wi,l','wel'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = EQU('lawa','lawe'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = EQU('qwa,la','qwa,le'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = EQU('baya','bayas'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = EQU('la,u','lawe'); 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Compute complexity
g.nnodes(find(g.nnodes==0)) = [];
complx = sum(g.nnodes);

if plotopt(1) == 1
    printGrammar(g,complx,numtype,lgabv)
end