function [g,complx,numtype,lgabv] = geo(plotopt)

if nargin == 0 plotopt = [0 0]; end

addpath treesupp/
addpath @tree/

g.nnodes = zeros(1000,1);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
lgabv = 'geo';
numtype = 5;

% 1
c = 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('ert-i','1'); c = c + 1;

% 2-10
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('or-i','2'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('sam-i','3'); c = c + 1;
[commandcells,rulecells,numcells,nnodecells,depthcells] = SUC({'sam-i','otx-i','xut-i','ekvs-i','svid-i','rva','cxra','at-i'},{'4','5','6','7','8','9','10'});
for i = 1:length(rulecells) 
	g.rule{c} = rulecells{i}; g.num{c} = numcells{i}; g.command{c} = commandcells{i}; 
	g.depths{c} = depthcells{i}; g.nnodes(c) = nnodecells{i};
	c = c + 1;
end

% 11-18 excl 13,17
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'''t','-''','w','''met,'''},{'w','at-i'},'11-18excl13,17'); c = c + 1;

% 13,17,19
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'ca','-','met,','-i'},{'sam-i','at-i'},'13'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'cvid','-','met,','-i'},{'svid-i','at-i'},'17'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'cxra','-','met,','-i'},{'cxra','at-i'},'19'); c = c + 1;

% 20
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'oc-i'},{'or-i','at-i'},'20'); c = c + 1;

% 40,60,80
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'or','-','m','-','oc-i'},{'or-i','oc-i'},'40'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'sam','-','oc-i'},{'sam-i','oc-i'},'60'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MUL({'otx','-','m','-','oc-i'},{'otx-i','oc-i'},'80'); c = c + 1;

% 21 - 99
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ADD({'v','''da','-''','u'},{'v','u'},'21...99'); c = c + 1;

% 100
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = POW({'as-i'},{'at-i','or-i'},'100'); c = c + 1;

% Sets w,v,u
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('w',{'ert -i','or -i','otx -i','xut -i','ekvs -i','vra -i'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('v',{'oc-','or-m-oc-','sam-oc-','otx-m-oc-'}); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = MEM('u',{'1-[digit for brevity]','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19'}); c = c + 1;

% Equivalences
%[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = EQU('ert -i','ert-i'); c = c + 1;
%[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = EQU('or -i','or-i'); c = c + 1;
%[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = EQU('otx -i','otx-i'); c = c + 1;
%[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = EQU('xut -i','xut-i'); c = c + 1;
%[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = EQU('ekvs -i','ekvs-i'); c = c + 1;
%[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = EQU('vra -i','rva-i'); c = c + 1;
%[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = EQU('oc-','oc-i'); c = c + 1;
%[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = EQU('or-m-oc-','or-m-oc-i'); c = c + 1;
%[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = EQU('sam-oc-','sam-oc-i'); c = c + 1;
%[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = EQU('sam-oc-','otx-m-oc-i'); 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Compute complexity
g.nnodes(find(g.nnodes==0)) = [];
complx = sum(g.nnodes);

if plotopt(1) == 1
    printGrammar(g,complx,numtype,lgabv)
end