// A $( document ).ready() block.
$( document ).ready(function() {
    var dialog = document.querySelector('dialog');
    var showDialogButton = document.querySelector('#review-dialog');
    if (! dialog.showModal) {
      dialogPolyfill.registerDialog(dialog);
    }
    showDialogButton.addEventListener('click', function() {
      dialog.showModal();
    });
    dialog.querySelector('.close').addEventListener('click', function() {
      dialog.close();
    });
});