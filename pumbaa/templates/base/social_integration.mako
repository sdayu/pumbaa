<section title="social">
## facebook
<span>
	<div id="fb-root"></div>
	<script>(function(d, s, id) {
	  var js, fjs = d.getElementsByTagName(s)[0];
	  if (d.getElementById(id)) return;
	  js = d.createElement(s); js.id = id;
	  js.src = "//connect.facebook.net/th_TH/all.js#xfbml=1&appId=${request.registry.settings.get('velruse.facebook.consumer_key')}";
	  fjs.parentNode.insertBefore(js, fjs);
	}(document, 'script', 'facebook-jssdk'));</script>
	<div class="fb-like" data-href="${request.current_route_url()}" data-width="100" data-height="50" data-colorscheme="light" data-layout="button_count" data-action="like" data-show-faces="true" data-send="false"></div>
</span>
## twitter
<span>
    <a href="http://twitter.com/share" class="twitter-share-button" data-count="horizontal" data-via="pumbaa">Tweet</a><script type="text/javascript" src="http://platform.twitter.com/widgets.js"></script>
</span>
## google plus
<span>
	<script type="text/javascript" src="http://apis.google.com/js/plusone.js"></script>
	<g:plusone></g:plusone>
</span>
</section>