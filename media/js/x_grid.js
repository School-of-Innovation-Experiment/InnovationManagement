$(function(){
  $.fn.editable.defaults.url = '/post';
  $.fn.editable.defaults.mode = 'inline';


  $('#testusername').editable(
    {
      url:'/post',
      type:'text',
      pk:1,
      name:'testusername',
      title:'enter username'
  });

});
