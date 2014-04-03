<%page args="page, pages" />
<%! from urllib.parse import urlparse %>
<%
show_pagination = 5
start_page = page - (show_pagination//2) if page - (show_pagination//2) > 0 else 1
end_page = page + (show_pagination//2) if page + (show_pagination//2) <= pages  else pages

path = urlparse(request.current_route_path()).path
%>

% if pages > 1:
<ul class="pagination">
  <li${' class=disabled' if start_page <= 1 else ''}><a href="${path}?page=${start_page-1}">&laquo;</a></li>
  % for i in range(start_page, end_page+1):
  <li${' class=active' if i==page else ''}><a href="${path}?page=${i}">${i}</a></li>
  % endfor
  <li${' class=disabled' if end_page <= pages else ''}><a href="${path}?page=${end_page+1}">&raquo;</a></li>
</ul>
% endif