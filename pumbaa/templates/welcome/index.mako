<%inherit file="/base/default.mako"/>
<div class="row">
	<div class="col-md-6 col-lg-6">
		<div style="font-size: larger;" class="well">
			<p>
				ยินดีต้อนรับสู่สังคมพุมบ้า พวกเราต้องการที่จะนำชุมชนของเรากลับคืนมา หากคุณยังจดจำคืนวันอันแสนงดงามและต้องการมีส่วนร่วมในการพัฒนาสังคมแห่งนี้,กรุณาแจ้งความจำนงมาที่ <a href="mailto:burawich@gmail.com?Subject=Pumbaa%20Volunteer">Burawich Pamornnak</a> (CoE18).
				ขอเชิญทุกคนมาร่วมแบ่งปันความคิดเห็น เพื่อที่จะทำให้สังคมแห่งนี้น่าอยู่เช่นเดิม
			</p>
			<p>
				ขอบคุณครับ
			</p>
		</div>
	</div>
	<div class="col-md-6 col-lg-6">
		<section>
		<ul class="list-inline">
		% for forum in forums:
		<li><button type="button" class="btn btn-default navbar-btn""><a href="${request.route_path('forums.view', name=forum.name)}">${forum.name}</a></button></li>
		% endfor
		</ul>
		</section>
		<div class="panel panel-info">
		  <div class="panel-heading">
		    <h3 class="panel-title">Recent Topics <a href="${request.route_path('feeds')}"><img alt="Atom feed" src="/public/images/feed-icon.svg" width=15px/></a></h3>
		  </div>
		  <div class="panel-body">
		  	<ul class="list-unstyled">
		    % for topic in topics:
		    	<li><a href="${request.route_path('forums.topics.view', title=topic.title, topic_id=topic.id)}">${topic.title}</a></li>
		    % endfor
		    </ul>
		  </div>
		</div>
	</div>
</div>

