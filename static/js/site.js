

(function ($) {

    "use strict";

    window.vlmp = {
        init: function() {
            this.renderReviews()
        },
        renderReviews: function() {

            let i = 5

            /**
             * TODO
             * Replace with actual values from database
             */
            let values = [7, 8, 10, 30, 45]

            for(i=5 ; i>=1; i--) {
                let progress = values[i-1];
                document.querySelector('#progressbar' + i).addEventListener('mdl-componentupgraded', function() {
                    this.MaterialProgress.setProgress( progress )
                });

            }

        }

    } 

    $(document).ready(function(){

        vlmp.init();

    });

})(jQuery)