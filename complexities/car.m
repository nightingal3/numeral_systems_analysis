function [g,complx,numtype,lgabv] = car(plotopt)

if nargin == 0 plotopt = [0 0]; end

addpath treesupp/
addpath @tree/

g.nnodes = zeros(1000,1);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
lgabv = 'car';
numtype = 4;

% 1
c = 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('o:win','1'); c = c + 1;

% 2-3
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('o:ko','2'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('o:ruwa','3'); c = c + 1;

% 4
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'o:ko','paime'},{'o:ko','o:ko'},'4'); c = c + 1;

% 5
[commandcells,rulecells,numcells,nnodecells,depthcells] = SUC({'o:kopaime','aiyato:ne'},{'5'});
for i = 1:length(rulecells) 
	g.rule{c} = rulecells{i}; g.num{c} = numcells{i}; g.command{c} = commandcells{i}; 
	g.depths{c} = depthcells{i}; g.nnodes(c) = nnodecells{i};
	c = c + 1;
end

% 10
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'aiya','pato:ro'},{'aiyato:ne','o:ko'},'10'); c = c + 1;

% 6,7,8
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'o:win','tuwo:piima'},{'o:win','aiyato:ne'},'6'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'o:ko','tuwo:piima'},{'o:ko','aiyato:ne'},'7'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'o:ruwa','tuwo:piima'},{'o:ruwa','aiyato:ne'},'8'); c = c + 1;

% 9
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = SUB({'o:win','apo:siki:ri'},{'aiyapato:ro','o:win'},'9'); c = c + 1;

% 11...19
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'''aiyapato:ro ','ku:pona:ka ''','w'},{'aiyapato:ro','w'},'11...19'); c = c + 1;

% 20
[commandcells,rulecells,numcells,nnodecells,depthcells] = SUC({'aiyapato:ro ku:pona:ka o:winapo:siki:ri','o:wingari?na'},{'20'});
for i = 1:length(rulecells) 
	g.rule{c} = rulecells{i}; g.num{c} = numcells{i}; g.command{c} = commandcells{i}; 
	g.depths{c} = depthcells{i}; g.nnodes(c) = nnodecells{i};
	c = c + 1;
end

% 40...100
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'v','''kari?na'''},{'v','o:wingari?na'},'40...100'); c = c + 1;

% 21...99
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'v',''' ku:pona:ka ''','u'},{'v','u'},'21...99'); c = c + 1;

% Sets w,v,u
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('w',{'o:win','o:ko','o:ruwa','o:kopaime','aiyato:ne','o:wintuwo:piima','o:kotuwo:piima','o:ruwatuwo:piima','o:winapo:siki:ri','aiyapato:ro'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('v',{'o:ko','o:ruwa','o:kopaime','aiyato:ne'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('u',{'1-[digit for brevity]','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19'}); 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Compute complexity
g.nnodes(find(g.nnodes==0)) = [];
complx = sum(g.nnodes);

if plotopt(1) == 1
    printGrammar(g,complx,numtype,lgabv)
end