<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title><%block name="title">Welcome to Pumbaa community</%block></title>
    <script src="/public/libs/jquery/jquery-2.0.3.js"></script>
    <link rel="stylesheet" href="/public/libs/bootstrap/3.0.0/css/bootstrap.min.css">
	<link rel="stylesheet" href="/public/libs/bootstrap/3.0.0/css/bootstrap-theme.min.css">
	<script src="/public/libs/bootstrap/3.0.0/js/bootstrap.min.js"></script>

    <%block name="addition_header"></%block>
</head>

<body>
${next.body()}
</body>

</html>