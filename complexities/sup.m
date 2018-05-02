function [g,complx,numtype,lgabv] = sup(plotopt)

if nargin == 0 plotopt = [0 0]; end

addpath treesupp/
addpath @tree/

g.nnodes = zeros(1000,1);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
lgabv = 'sup';
numtype = 3;

% 1
c = 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('nigkin','1'); c = c + 1;

% 2-5
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('kshuunni','2'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('taanre','3'); c = c + 1;
[commandcells,rulecells,numcells,nnodecells,depthcells] = SUC({'taanre','sicyeere','kagkuro'},{'4','5'});
for i = 1:length(rulecells) 
	g.rule{c} = rulecells{i}; g.num{c} = numcells{i}; g.command{c} = commandcells{i}; 
	g.depths{c} = depthcells{i}; g.nnodes(c) = nnodecells{i};
	c = c + 1;
end

% 6-9
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'''baa','-''','w'},{'kagkuro','w'},'6...9'); c = c + 1;

% 10
[commandcells,rulecells,numcells,nnodecells,depthcells] = SUC({{'baa','-','ricyeere'},'ke'},{'10'});
for i = 1:length(rulecells) 
	g.rule{c} = rulecells{i}; g.num{c} = numcells{i}; g.command{c} = commandcells{i}; 
	g.depths{c} = depthcells{i}; g.nnodes(c) = nnodecells{i};
	c = c + 1;
end

% 11-19
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'ke ','na ','v'},{'ke','v'},'11...19'); c = c + 1;

% 20
[commandcells,rulecells,numcells,nnodecells,depthcells] = SUC({{'ke na baaricyeere'},'begjaaga'},{'20'});
for i = 1:length(rulecells) 
	g.rule{c} = rulecells{i}; g.num{c} = numcells{i}; g.command{c} = commandcells{i}; 
	g.depths{c} = depthcells{i}; g.nnodes(c) = nnodecells{i};
	c = c + 1;
end

% 21-29
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'begjaaga ','na ','v'},{'begjaaga','v'},'21...29'); c = c + 1;

% 30
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'begjaaga ','na ','ke'},{'begjaaga','ke'},'30'); c = c + 1;

% 31-39
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'''begjaaga ','na ','ke ''','na ''','v'},{'begjaaga  na ke','v'},'31...39'); c = c + 1;

% 40
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'bee','-','shuunni'},{'begjaaga','shuunni'},'40'); c = c + 1;

% 41-49
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'''bee','-','shuunni ','na ''','v'},{'bee-shuunni','v'},'41...49'); c = c + 1;

% 50
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'bee','-','shuunni ','na ','ke'},{'bee-shuunni na','ke'},'50'); c = c + 1;

% 51-59
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'''bee','-','shuunni ','na ','ke ','na ''','v'},{'bee-shuunni na ke','v'},'51...59'); c = c + 1;

% 60
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'bee','-','taanre'},{'begjaaga','taanre'},'60'); c = c + 1;

% 61-69
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'''bee','-','taanre ','na ''','v'},{'bee-taanre','v'},'61...69'); c = c + 1;

% 70
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'bee','-','taanre ','na ','ke'},{'bee-taanre','ke'},'70'); c = c + 1;

% 71-79
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'''bee','-','taanre ','na ','ke ','na ''','v'},{'bee-taanre na ke','v'},'71...79'); c = c + 1;

% 80
[commandcells,rulecells,numcells,nnodecells,depthcells] = SUC({'bee-taanre na ke na baaricyeere','gkuu'},{'80'});
for i = 1:length(rulecells) 
	g.rule{c} = rulecells{i}; g.num{c} = numcells{i}; g.command{c} = commandcells{i}; 
	g.depths{c} = depthcells{i}; g.nnodes(c) = nnodecells{i};
	c = c + 1;
end

% 81-89
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'''gkuu ','na ''','v'},{'gkuu','v'},'81...89'); c = c + 1;

% 90
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'gkuu ','na ','ke'},{'gkuu','ke'},'90'); c = c + 1;

% 91-99
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'''gkuu ','na ','ke ','na ''','v'},{'gkuu na ke','v'},'91...99'); c = c + 1;

% 100
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'gkuu ','na ','begaaga'},{'gkuu','begaaga'},'100'); c = c + 1;


% Sets w, v
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('w',{'ni','shuunni','taanre','ricyeere'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('v',{'nigkin','shuunni','taanre','ricyeere','kagkuro','baani','baashuunni','baataanre','baaricyeere'}); c = c + 1;

% Equivalences
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = EQU('ni','nigkin'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = EQU('ricyeere','sicyeere'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = EQU('baani','baa-ni'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = EQU('baashuunni','baa-shuunni'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = EQU('baataanre','baa-taanre'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = EQU('baaricyeere','baa-ricyeere'); 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Compute complexity
g.nnodes(find(g.nnodes==0)) = [];
complx = sum(g.nnodes);

if plotopt(1) == 1
    printGrammar(g,complx,numtype,lgabv)
end