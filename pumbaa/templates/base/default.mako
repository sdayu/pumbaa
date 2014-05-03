<%inherit file="/base/base.mako"/>
<%block name="keywords">CoE, PSU, Computer Engineering, Prince of Songkla University, Community</%block>
<%block name="description">This site is for people in CoE</%block>
<%include file="/base/navigator_bar.mako"/>
    <div class="container">
      <div class="jumbotron">
        <h1 style="font-style: italic;"><a href="#">Hello, pumbaa.CoE!</a></h1>
        <div ng-controller="pumbaaTimeCtrl" class="pull-right">
            <div class="pull-right">
            <label class="label label-default">{{ptime | date:'hh'}}</label> :
            <label class="label label-default">{{ptime | date:'mm'}}</label> :
            <label class="label label-default">{{ptime | date:'ss'}}</label>
            </div>
            <br> Today is {{ptime | date:'MMM d, yyyy'}}
        </div>
	  </div>

${next.body()}
<%include file="/base/footer.mako"/>
	</div>
