function [g,complx,numtype,lgabv] = eip(plotopt)

if nargin == 0 plotopt = [0 0]; end

addpath treesupp/
addpath @tree/

g.nnodes = zeros(1000,1);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
lgabv = 'eip';
numtype = 2;

% 1
c = 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('ton','1'); c = c + 1;

% 2-25
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('betinye','2'); c = c + 1;
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = ONE('winilye','3'); c = c + 1;
[commandcells,rulecells,numcells,nnodecells,depthcells] = SUC({'winilye','dumbarye','fangobarye','nakobarye','tekbarye','finbarye','toubnebarye','takobarye','koklombarye','obarye','mekbarye','odigin','koklomdigin','takubdigin','toubnedigin','findigin','tekdigin','nakubdigin','famdigin','dumdigin','winilyaba','betinyaba','seselekyaba'},...
    {'4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25'});
for i = 1:length(rulecells) 
	g.rule{c} = rulecells{i}; g.num{c} = numcells{i}; g.command{c} = commandcells{i}; 
	g.depths{c} = depthcells{i}; g.nnodes(c) = nnodecells{i};
	c = c + 1;
end

% Note: the book shows form for 50 but does not specify forms 26-49
% or any other forms, assuming goes up to 25
% 26-100
[g.command{c},g.rule{c},g.num{c},g.nnodes(c),g.depths{c}] = HIG({'seselekyaba','many'},'26-100');


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Compute complexity
g.nnodes(find(g.nnodes==0)) = [];
complx = sum(g.nnodes);

if plotopt(1) == 1
    printGrammar(g,complx,numtype,lgabv)
end