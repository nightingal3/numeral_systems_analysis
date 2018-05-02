function [g,complx,numtype,lgabv] = kty(plotopt)

if nargin == 0 plotopt = [0 0]; end

addpath treesupp/
addpath @tree/

g.nnodes = zeros(1000,1);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
lgabv = 'kty';
numtype = 6;

% 1
c = 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('ej','1'); c = c + 1;

% 2-10
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('kaat','2'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('koolam','3'); c = c + 1;
[commandcells,rulecells,numcells,nnodecells,depthcells] = SUC({'koolam','njela','wat','kuut','laapat','njiilar'},{'4','5','6','7','8'});
for i = 1:length(rulecells) 
	g.rule{c} = rulecells{i}; g.num{c} = numcells{i}; g.command{c} = commandcells{i}; 
	g.depths{c} = depthcells{i}; g.nnodes(c) = nnodecells{i};
	c = c + 1;
end
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'jeegw'},{'kaat','wat'},'10'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = SUB({'iir','jeegw'},{'jeegw','ej'},'9'); c = c + 1;

% 20...90
[commandcells,rulecells,numcells,nnodecells,depthcells] = SUC({'jeegw+orakk+iir+jeegw','koos'},{'20'});
for i = 1:length(rulecells) 
	g.rule{c} = rulecells{i}; g.num{c} = numcells{i}; g.command{c} = commandcells{i}; 
	g.depths{c} = depthcells{i}; g.nnodes(c) = nnodecells{i};
	c = c + 1;
end
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'w','''+','jeegw'''},{'w','jeegw'},'30...80'); c = c + 1;
% 100
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c},t_l,t_r] = POW('saat',{'jeegw','kaat'},'100'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = SUB({'iir','+','saat'},{'saat','jeegw'},'90'); c = c + 1;

% 11...19
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = SUB({'''jeegw','-','orakk','-''','u'},{'jeegw','u'},'11...18'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'jeegw','+','orakk','+','iir','+','jeegw'},{'jeegw','irrjeegw'},'19'); c = c + 1;

% 21...99
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'v','''-','orakk','-''','x'},{'v','x'},'21...99'); c = c + 1;

% Sets w, u, v
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('w',{,'koolam','njela','wat','kuut','laapat','njiilar'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('u',{'ej','kaat','koolam','njela','wat','kuut','laapat','njiilar'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('v',{'koos','koolam+jeegw','njela+jeegw','wat+jeegw','kuut+jeegw','laapat+jeegw','njiilar+jeegw','iirjeegw+jeegw'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('x',{'ej','kaat','koolam','njela','wat','kuut','laapat','njiilar','iirjeegw'}); 

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Compute complexity
g.nnodes(find(g.nnodes==0)) = [];
complx = sum(g.nnodes);

if plotopt(1) == 1
    printGrammar(g,complx,numtype,lgabv)
end