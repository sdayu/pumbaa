<div class="row">
	<style type="text/css">
	.head-footer {
		background-image: linear-gradient(to bottom,#bce8f1 0,#d9edf7 100%); 
		border: 1px solid #bce8f1;
		font-weight: bold;
		color: #3a87ad;
	}
	</style>
	<div class="col-sm-3 col-md-3 col-lg-3">
		<section title="About Pumbaa">
			<div class="well well-sm head-footer">
				About Pumbaa
			</div>
			<ul class="list-unstyled">
			  <li><a href="${request.route_path('pages.view', title='about')}">เกี่ยวกับ Pumbaa</a></li>
			  <li><a href="${request.route_path('pages.view', title='history')}">ประวัติ Pumbaa</a></li>
			  <li><a href="${request.route_path('pages.view', title='contact')}">ติดต่อเรา</a></li>
			  <li><a href="${request.route_path('pages.view', title='writing guideline')}">แนะนำการเขียน</a></li>
			  <li><a href="${request.route_path('pages.view', title='become member')}">จะมาเป็นสมาชิกได้อย่างไร</a></li>
			</ul>
		</section>
	</div>
	<div class="col-sm-3 col-md-3 col-lg-3">
		<section title="Other">
			<div class="well well-sm head-footer">
				Other
			</div>
			<ul class="list-unstyled">
			  <li><a href="${request.route_path('forums.index')}">กระดานข่าว</a></li>
			  <li><a href="${request.route_path('forums.topics.index')}">กระทู้ทั้งหมด</a></li>
			  <li><a href="${request.route_path('forums.tags.index')}">ป้ายกำกับ</a></li>
			  <li><a href="${request.route_path('forums.feeds')}">Atom</a></li>
			  <li><a href="https://www.facebook.com/groups/115299811878766">Pumbaa on Facebook</a></li>
			</ul>
		</section>
	</div>
	<div class="col-sm-3 col-md-3 col-lg-3">
		<section title="CoE Eng PSU">
			<div class="well well-sm head-footer">
				เว็บไซต์
			</div>
			<ul class="list-unstyled">
			  <li><a href="http://www.coe.psu.ac.th">Department of Computer Engineering</a></li>
			  <li><a href="http://www.eng.psu.ac.th">Faculty of Engineering</a></li>
			  <li><a href="http://www.psu.ac.th">Prince of Songkla University</a></li>
			</ul>
		</section>
	</div>
	<div class="col-sm-3 col-md-3 col-lg-3">
		<section title="Development">
			<div class="well well-sm head-footer">
				Development
			</div>
			<ul class="list-unstyled">
			  <li><a href="https://github.com/sdayu/pumbaa">Pumbaa on GitHub</a></li>
			  <li><a href="https://github.com/sdayu/pumbaa/issues">แจ้งข้อผิดพลาด</a></li>
			  <li><a href="${request.route_path('forums.view', name='Development')}">พูดคุยเกี่ยวกับการพัฒนา Pumbaa</a></li>
			</ul>
		</section>
	</div>
</div>