<section title="social" style="display: inline;">
## facebook
<span>
	<div id="fb-root"></div>
	<script>(function(d, s, id) {
	  var js, fjs = d.getElementsByTagName(s)[0];
	  if (d.getElementById(id)) return;
	  js = d.createElement(s); js.id = id;
	  js.src = "//connect.facebook.net/us_US/all.js#xfbml=1&appId=${request.registry.settings.get('velruse.facebook.consumer_key')}";
	  fjs.parentNode.insertBefore(js, fjs);
	}(document, 'script', 'facebook-jssdk'));
	</script>
	<div class="fb-like" data-href="https://developers.facebook.com/docs/plugins/" data-width="450" data-height="26" data-colorscheme="light" data-layout="standard" data-action="like" data-show-faces="true" data-send="true"></div>
</span>
## twitter
<span>
    <a href="http://twitter.com/share" class="twitter-share-button" data-count="horizontal" data-via="pumbaa">Tweet</a><script type="text/javascript" src="http://platform.twitter.com/widgets.js"></script>
</span>

## google plus
<span>
<div class="g-plusone" data-annotation="inline" data-width="300"></div>
<script type="text/javascript">
  (function() {
    var po = document.createElement('script'); po.type = 'text/javascript'; po.async = true;
    po.src = 'https://apis.google.com/js/plusone.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(po, s);
  })();
</script>
</span>


</section>