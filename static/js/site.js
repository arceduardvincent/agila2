

(function ($) {

    "use strict";

    window.vlmp = {
        init: function() {
            this.renderReviews()
            this.sortableCourses()
            this.createAccordion()
            this.createDropzone()
            this.dialogBox()
            this.courseDifficulty()
        },
        renderReviews: function() {

            if( !$("#progressbar").length ) {
                return
            }

            let i = 5

            /**
             * TODO
             * Replace with actual values from database
             */
            let values = [7, 8, 10, 30, 45]

            for(i=5 ; i>=1; i--) {
                let progress = values[i-1]
                document.querySelector('#progressbar' + i).addEventListener('mdl-componentupgraded', function() {
                    this.MaterialProgress.setProgress( progress )
                });

            }

        },
        sortableCourses: function() {

            if( !$("#sortable").length ) {
                return
            }

            $("#sortable").sortable()

        },
        createAccordion: function() {

            if( !$(".accordion").length ) {
                return
            }

            $(".accordion").accordion({
                icons: {
                    header: 'ui-icon-caret-1-n',
                    // activeHeader: 'ui-icon-caret-1-s'
                }
            })

        },
        createDropzone: function() {

            /**
             * TODO
             */

            $("#dz-thumbnail").dropzone({ url: "/file/post" })


        },
        dialogBox: function(){

            /*
             * This function is used to handle adding courses for Lab Track Page
             */

            if( !$(".dialog-box") ) {
                return
            }

            //Instantiate Dialog Box for Adding Courses
            $('.dialog-box').dialog({
                resizable: false,
                height: 650,
                width: 520,
                modal: true,
                title: "Lab Courses",
                closeOnEscape: true,
                autoOpen: false,
                draggable: false,
                buttons: {
                    "Add Courses to Track": function() {
                        $( this ).dialog( "close" );
                    }
                },
            })

            $(".btn-addCourses").on('click', function(){
                $('.dialog-box').dialog("open")
            })

        },
        courseDifficulty: function(){
            $(".course-difficulty").checkboxradio({
                icon: false
            });
        }

    }

    $(document).ready(function(){

        vlmp.init();

    });

})(jQuery)