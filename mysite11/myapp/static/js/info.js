$(document).ready(function(){
	
	$('ul.tabs li').click(function(){
		var tab_id = $(this).attr('data-tab');

		$('ul.tabs li').removeClass('current');
		$('.tab-content').removeClass('current');

		$(this).addClass('current');
		$("#"+tab_id).addClass('current');
	})

})

const activeImage = document.querySelector(".product-image .active");
const productImages = document.querySelectorAll(".image-list img");
const navItem = document.querySelector('a.toggle-nav');
function changeImage(e) {
    activeImage.src = e.target.src;
}

function toggleNavigation(){
  this.nextElementSibling.classList.toggle('active');
}

productImages.forEach(image => image.addEventListener("click", changeImage));
navItem.addEventListener('click', toggleNavigation);

//<![CDATA[
	jQuery(document).ready(function($){ $(".multitab-widget-content-widget-id").hide(); $("ul.multitab-widget-content-tabs-id li:first a").addClass("multitab-widget-current").show(); $(".multitab-widget-content-widget-id:first").show(); $("ul.multitab-widget-content-tabs-id li a").click(function() { $("ul.multitab-widget-content-tabs-id li a").removeClass("multitab-widget-current a"); $(this).addClass("multitab-widget-current"); $(".multitab-widget-content-widget-id").hide(); var activeTab = $(this).attr("href"); $(activeTab).fadeIn(); return false; }); });
	//]]>