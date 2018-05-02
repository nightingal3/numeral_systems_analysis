function [g,complx,numtype,lgabv] = dag(plotopt)

if nargin == 0 plotopt = [0 0]; end

addpath treesupp/
addpath @tree/

g.nnodes = zeros(1000,1);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
lgabv = 'dag';
numtype = 4;

% 1
c = 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('daiton','1'); c = c + 1;

% 2-5
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('dere','2'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('yampo','3'); c = c + 1;
[commandcells,rulecells,numcells,nnodecells,depthcells] = SUC({'yampo','bayabayapa',{'nani ','yamunaet'}},{'4','5'});
for i = 1:length(rulecells) 
	g.rule{c} = rulecells{i}; g.num{c} = numcells{i}; g.command{c} = commandcells{i}; 
	g.depths{c} = depthcells{i}; g.nnodes(c) = nnodecells{i};
	c = c + 1;
end

% 6-9
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'''nani ','yamu ''','w'},{'nani yamunaet','w'},'6...9'); c = c + 1;

% 10
[commandcells,rulecells,numcells,nnodecells,depthcells] = SUC({'nani yamu bayabayapa','aonagaet'},{'10'});
for i = 1:length(rulecells) 
	g.rule{c} = rulecells{i}; g.num{c} = numcells{i}; g.command{c} = commandcells{i}; 
	g.depths{c} = depthcells{i}; g.nnodes(c) = nnodecells{i};
	c = c + 1;
end

% 11-14
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'''aonagaet ','pusinawan ''','w'},{'aonagaet','w'},'11...14'); c = c + 1;

% 15
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'''aonagaet ','pusin ','yamunaet'''},{'aonagaet','nani yamunaet'},'15'); c = c + 1;

% 16-19
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'''aonagaet ','pusin ','yamu ''','w'},{'aonagaet pusin yamunaet','w'},'16...19'); c = c + 1;

% 20,40,60,80
[commandcells,rulecells,numcells,nnodecells,depthcells] = SUC({'aonagaet pusin yamu bayabayapa','apane'},{''});
for i = 1:length(rulecells) 
	g.rule{c} = rulecells{i}; g.num{c} = numcells{i}; g.command{c} = commandcells{i}; 
	g.depths{c} = depthcells{i}; g.nnodes(c) = nnodecells{i};
	c = c + 1;
end
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'''apane ''','w'},{'apane','w'},'20...80'); c = c + 1;

% 21...99 (excl. 31-34,51-54,71-74,91-94)
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MULADD({'''apane ''','w',''' apan ','da ''','v'},{'apane','w','v'},'21...99 (excl. 31-34,51-54,71-74,91-94)'); c = c + 1;

% 31-34,51-54,71-74,91-94
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MULADDADD({'''apane ''','w',''' apan ','da ','aonagaet ','pusin ','yamu ''','w'},{'apane','w','aonagaet','w'},'31-34,51-54,71-74,91-94'); c = c + 1;

% 100
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'apane ','nani ', 'yamunaet'},{'apane','nani yamunaet'},'100'); c = c + 1;

% Sets w, v
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('w',{'daiton','dere','yampo','bayabayapa'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('v',{'1-[digit for brevity]','2','3','4','5','6','7','8','9','10','15','16','17','18','19'}); c = c + 1;

% Equivalence
%[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = EQU('pusinawan','pusinawan'); c = c + 1;
%[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = EQU('pusin yamu','pusinawan');
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Compute complexity
g.nnodes(find(g.nnodes==0)) = [];
complx = sum(g.nnodes);

if plotopt(1) == 1
    printGrammar(g,complx,numtype,lgabv)
end