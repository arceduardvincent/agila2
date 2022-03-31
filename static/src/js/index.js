
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
            this.createGradingTabs()
            this.addLabProfile()
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
        courseDifficulty: function() {
            $(".course-difficulty").checkboxradio({
                icon: false
            });
        },
        createGradingTabs: function() {

            if ( !$('#tabs').length ) {
                return
            }

            $('#tabs').tabs()
        },
        addLabProfile: function() {

            if ( !$('.modal-lab-profile').length ) {

                return
            }


            //Instantiate Dialog Box for Creating a Lab Profile
            $('.modal-lab-profile').dialog({
                resizable: false,
                height: 600,
                width: 850,
                modal: true,
                title: "Add a Lab Profile",
                closeOnEscape: true,
                autoOpen: false,
                draggable: false,
                buttons: {
                    "Save Lab Profile": function() {
                        $( this ).dialog( "close" );
                    }
                },
            })

            $('.btn-addLabProfile').on('click', function(e){
                e.preventDefault()
                $('.modal-lab-profile').dialog("open")
            })


            //Create Previous and Next Tabbing for Lab Profile

            var divs = $('.lab-profile-tabs>div');
            var now = 0; // currently shown div
            divs.hide().first().show(); // hide all divs except first

            $("#btnNext").click(function() {
                divs.eq(now).hide();
                now = (now + 1 < divs.length) ? now + 1 : 0;
                divs.eq(now).show(); // show next
            });

            $("#btnPrevious").click(function() {
                divs.eq(now).hide();
                now = (now > 0) ? now - 1 : divs.length - 1;
                divs.eq(now).show(); // show previous
            });

        }

    }

    $(document).ready(function(){

        vlmp.init();

    });

})(jQuery)