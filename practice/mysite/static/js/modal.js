jQuery('.site-header').on('click', function() {
  jQuery('body').append('<div id="modal-overlay"></div>');
  jQuery('#modal-overlay').fadeIn('1500');
  jQuery('.gnav .gnav__menu').fadeIn('1500');
});

jQuery(document).on('click', '#modal-overlay', function() {
  jQuery('#modal-overlay').fadeOut('1500');
  jQuery('.gnav .gnav__menu').fadeOut('1500');
});
