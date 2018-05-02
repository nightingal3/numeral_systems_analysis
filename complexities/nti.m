function [g,complx,numtype,lgabv] = nti(plotopt)

if nargin == 0 plotopt = [0 0]; end

addpath treesupp/
addpath @tree/

g.nnodes = zeros(1000,1);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
lgabv = 'nti';
numtype = 3;

% 1
c = 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('atdi','1'); c = c + 1;

% 2-10
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('oyo','2'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('ibhu','3'); c = c + 1;
[commandcells,rulecells,numcells,nnodecells,depthcells] = SUC({'ibhu','ifo','imbo','aza','arubhu','aru','arugyetdi','idre'},...
    {'4','5','6','7','8','9','10','11','12'});
for i = 1:length(rulecells) 
	g.rule{c} = rulecells{i}; g.num{c} = numcells{i}; g.command{c} = commandcells{i}; 
	g.depths{c} = depthcells{i}; g.nnodes(c) = nnodecells{i};
	c = c + 1;
end

% 12,16,20,24,28,32
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'otsi'},{'ibhu','ifo'},'12'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'opi'},{'ifo','ifo'},'16'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'aba'},{'imbo','ifo'},'20'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'arotsi'},{'aza','ifo'},'24'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'adzoro'},{'arubhu','ifo'},'28'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'wadhi'},{'aru','ifo'},'32'); c = c + 1;

% 11...31
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = SUB({'w','''-','vi'''},{'w','atdi'},'11...31'); c = c + 1;
% 13...30
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'v',''' do ''','u'},{'v','u'},'13...30'); c = c + 1;

% 64
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'oyo ','wadhi'},{'oyo','wadhi'},'64'); c = c + 1;

% 65 - 95 (Note: author left a gap in description of forms - interpolated)
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'''oyo ', 'wadhi ', 'do ''','z'},{'oyo wadhi','z'},'65...95'); c = c + 1;

% 96
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'ibhu ','wadhi'},{'ibhu','wadhi'},'96'); c = c + 1;

% 96 - 100 (Note: author left a gap in description of forms - interpolated)
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'''ibhu ', 'wadhi ', 'do ''','z'},{'ibhu wadhi','z'},'96...100'); c = c + 1;

% Sets w, v, u, z
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('w',{'otsi','opi','aba','arotsi','adzoro','wadhi'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('v',{'otsi','opi','aba','arotsi','adzoro'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('u',{'atdi','oyo'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('z',{'1-[digit for brevity]','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31'}); 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Compute complexity
g.nnodes(find(g.nnodes==0)) = [];
complx = sum(g.nnodes);

if plotopt(1) == 1
    printGrammar(g,complx,numtype,lgabv)
end