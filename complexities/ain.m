function [g,complx,numtype,lgabv] = ain(plotopt)

if nargin == 0 plotopt = [0 0]; end

addpath treesupp/
addpath @tree/

g.nnodes = zeros(1000,1);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
lgabv = 'ain';
numtype = 4;

% 1
c = 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('sine','1'); c = c + 1;

% 2-5
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('tu','2'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('re','3'); c = c + 1;
[commandcells,rulecells,numcells,nnodecells,depthcells] = SUC({'re','ine','asikne'},{'4','5'});
for i = 1:length(rulecells) 
	g.rule{c} = rulecells{i}; g.num{c} = numcells{i}; g.command{c} = commandcells{i}; 
	g.depths{c} = depthcells{i}; g.nnodes(c) = nnodecells{i};
	c = c + 1;
end

% 10
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'wan'},{'tu','asikne'},'10'); c = c + 1;

% 6-9
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = SUB({'i','wan'},{'wan','ine'},'6'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = SUB({'ar','wan'},{'wan','re'},'7'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = SUB({'tu','pesan'},{'wan','tu'},'8'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = SUB({'sine','pesan'},{'wan','sine'},'9'); c = c + 1;

% 20
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'hotne'},{'tu','wan'},'20'); c = c + 1;

% 30,50,70,90
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MULSUB({'''wan ','e ','w',''' hotne '''},{'w','hotne','wan'},'30...90'); c = c + 1;

% 40,60,80,100
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'w',''' hotne'''},{'w','hotne'},'40...100'); c = c + 1;

% 11...99
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'v',''' ikasma ''','u'},{'v','u'},'11...99'); c = c + 1;

% Sets w,v,u
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('w',{'tu','re','ine','asikne'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('v',{'sine','tu','re','ine','asikne','iwan','arwan','tupesan','sinepesan'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('u',{'wan','hotne','wan e tu hotne','tu hotne','wan e re hotne','re hotne','wan e ine hotne','ine hotne','wan e asikne hotne'}); 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Compute complexity
g.nnodes(find(g.nnodes==0)) = [];
complx = sum(g.nnodes);

if plotopt(1) == 1
    printGrammar(g,complx,numtype,lgabv)
end