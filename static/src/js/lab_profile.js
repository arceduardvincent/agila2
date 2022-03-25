// A $( document ).ready() block.
$( document ).ready(function() {
      imgInp.onchange = evt => {
      const [file] = imgInp.files
      if (file) {
        labPreview.src = URL.createObjectURL(file)
      }}
});