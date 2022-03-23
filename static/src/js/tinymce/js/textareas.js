tinymce.init({
    selector: 'textarea',  // change this value according to your HTML
    images_upload_url: '/upload_image/', // Image upload address in Django route
    height: 500,
  plugins: [
      'advlist autolink link image lists charmap print preview hr anchor pagebreak',
      'searchreplace wordcount visualblocks visualchars code fullscreen insertdatetime media nonbreaking',
      'table emoticons template paste help'
    ],
    menubar: 'favs file edit view insert format tools table help',
    toolbar: 'undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | ' +
      'bullist numlist outdent indent | link image | print preview media fullpage | ' +
      'forecolor backcolor emoticons | help',
}
);