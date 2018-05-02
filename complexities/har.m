function [g,complx,numtype,lgabv] = har(plotopt)

if nargin == 0 plotopt = [0 0]; end

addpath treesupp/
addpath @tree/

g.nnodes = zeros(1000,1);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
lgabv = 'har';
numtype = 2;

% 1
c = 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('aglg','1'); c = c + 1;

% 2-12
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('agnobo rol-yobo','2'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('woloml','3'); c = c + 1;
[commandcells,rulecells,numcells,nnodecells,depthcells] = SUC({'woloml','kono ng-b','momd','wrap ck-g-b','mj','amnab','mac','moyb','gadloy','mol'},...
    {'4','5','6','7','8','9','10','11','12'});
for i = 1:length(rulecells) 
	g.rule{c} = rulecells{i}; g.num{c} = numcells{i}; g.command{c} = commandcells{i}; 
	g.depths{c} = depthcells{i}; g.nnodes(c) = nnodecells{i};
	c = c + 1;
end

% 13-18
[commandcells,rulecells,numcells,nnodecells,depthcells] = SUC({'mol',{'ado=k-yobo ','rcb'},{'ado=k-yobo ','rfs'},{'ado=k-yobo ','rb'},{'ado=k-yobo ','rie'},{'ado=k-yobo ','rif'},{'ado=k-yobo ','rwb'}},...
    {'13','14','15','16','17','18'});
for i = 1:length(rulecells) 
	g.rule{c} = rulecells{i}; g.num{c} = numcells{i}; g.command{c} = commandcells{i}; 
	g.depths{c} = depthcells{i}; g.nnodes(c) = nnodecells{i};
	c = c + 1;
end

% 19-30
[commandcells,rulecells,numcells,nnodecells,depthcells] = SUC({'ado=k-yobo wrap ck-g-b','rlf','rrf','rmf','rff','rt','rwb','rif','rie','rb','rfs','rcb','rh'},...
    {'19','20','21','22','23','24','25','26','27','28','29','30'});
for i = 1:length(rulecells) 
	g.rule{c} = rulecells{i}; g.num{c} = numcells{i}; g.command{c} = commandcells{i}; 
	g.depths{c} = depthcells{i}; g.nnodes(c) = nnodecells{i};
	c = c + 1;
end

% 31-36
[commandcells,rulecells,numcells,nnodecells,depthcells] = SUC({'rh',{'howoyl-b ','rcb'},{'howoyl-b ','rfs'},{'howoyl-b ','rb'},{'howoyl-b ','rie'},{'howoyl-b ','rif'},{'howoyl-b ','rwb'}},...
    {'31','32','33','34','35','36'});
for i = 1:length(rulecells) 
	g.rule{c} = rulecells{i}; g.num{c} = numcells{i}; g.command{c} = commandcells{i}; 
	g.depths{c} = depthcells{i}; g.nnodes(c) = nnodecells{i};
    c = c + 1;
end

% 37-100
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = HIG({'howoyl-b rwb','many'},'37-100');

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Compute complexity
g.nnodes(find(g.nnodes==0)) = [];
complx = sum(g.nnodes);

if plotopt(1) == 1
    printGrammar(g,complx,numtype,lgabv)
end