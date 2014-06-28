<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="keywords" content="<%block name='keywords'></%block>" />
	<meta name="description" content="<%block name='description'></%block>" />
    <title><%block name="title">Welcome to Pumbaa community</%block></title>
    <script src="/public/bower_components/jquery/dist/jquery.js"></script>
    <link rel="stylesheet" href="/public/bower_components/bootstrap-css/css/bootstrap.min.css">
	<link rel="stylesheet" href="/public/bower_components/bootstrap-css/css/bootstrap-theme.min.css">
    <link rel="stylesheet" type="text/css" href="/public/css/topicinfo.css" />
	<script src="/public/bower_components/bootstrap-css/js/bootstrap.min.js"></script>
	<script src="/public/bower_components/MathJax/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
	
	<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
	<link rel="alternate" type="application/atom+xml" title="Pumbaa Atom" href="${request.route_url('forums.feeds')}">
    <%block name="addition_header"></%block>
</head>

<body>
${next.body()}
</body>

</html>
