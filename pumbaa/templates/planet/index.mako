<%inherit file="/base/default.mako"/>
<%!
	from velruse import login_url
%>
<%block name="addition_header">
<link rel="stylesheet" href="/public/libs/holderjs/holder.js">
<style type="text/css">
.published{
	font-size:18px;
}
</style>
</%block>
<h1>${project}</h1>
<div class="row">
	<div class="col-sm-6 col-md-8">
	% for result in results:

		<div class="row">


			<div class="col-sm-6 col-md-12">
				<div class="thumbnail">

					<div class="row">
						<div class="col-sm-6 col-md-4">
					  		<img src="${result['img_src']}" width="100%">
					  	</div>
					  	<div class="col-sm-6 col-md-8">
							<div class="caption">
								<span class="pull-right">
									<span class="label label-primary published">${result['published_year']}</span>&nbsp;
									<span class="label label-info published">${result['published_month']}</span>&nbsp;
							    	<span class="label label-default">${result['published_day']}</span>&nbsp;
							    </span><br/>
							    <h3>${result['title'] | n}</h3>
							    <p>${result['content'] | n}</p>

								
							    <br/>
							    <p class="pull-right"><a href="#" class="btn btn-primary" role="button">Read more >></a> 
							    </p>
							</div>
					  	</div>
					</div>
				</div>
			</div>


		</div>

	% endfor
	</div>
	<div class="col-sm-6 col-md-4">
	Test menu
	</div>
</div>

