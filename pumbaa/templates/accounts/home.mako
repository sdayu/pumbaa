<%inherit file="/base/default.mako"/>

<h1>Hello, ${request.user.username}</h1>

% if request.user.status == 'wait for approval':
This user wait for approval.
% endif