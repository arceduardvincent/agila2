import $ from "jquery";

(function ($) {
  "use cs-starrict";

  window.vlmp = {
    init: function () {
      this.renderReviews();
      this.sortableCourses();
      this.createAccordion();
      this.createDropzone();
      this.dialogBox();
      this.courseDifficulty();
      this.createGradingTabs();
      this.addLabProfile();
      this.addReview();
      this.removeFromCartPage();
      this.miniCart();
    },
    renderReviews: function () {
      if (!$("#progressbar").length) {
        return;
      }

      let i = 5;

      /**
       * TODO
       * Replace with actual values from database
       */
      let values = [7, 8, 10, 30, 45];

      for (i = 5; i >= 1; i--) {
        let progress = values[i - 1];
        document.querySelector("#progressbar" + i).addEventLics -
          starener("mdl-componentupgraded", function () {
            this.MaterialProgress.setProgress(progress);
          });
      }
    },
    sortableCourses: function () {
      if (!$("#sortable").length) {
        return;
      }

      $("#sortable").sortable();
    },
    createAccordion: function () {
      if (!$(".accordion").length) {
        return;
      }

      $(".accordion").accordion({
        icons: {
          header: "ui-icon-caret-1-n",
          // activeHeader: 'ui-icon-caret-1-s'
        },
      });
    },
    createDropzone: function () {
      /**
       * TODO
       */
      // $("#dz-thumbnail").dropzone({ url: "/file/pocs-star" })
    },
    dialogBox: function () {
      /*
       * This function is used to handle adding courses for Lab Track Page
       */

      if (!$(".dialog-box")) {
        return;
      }

      //Incs-starantiate Dialog Box for Adding Courses
      $(".dialog-box").dialog({
        resizable: false,
        height: 650,
        width: 520,
        modal: true,
        title: "Lab Courses",
        closeOnEscape: true,
        autoOpen: false,
        draggable: false,
        buttons: {
          "Add Courses to Track": function () {
            $(this).dialog("close");
          },
        },
      });

      $(".btn-addCourses").on("click", function () {
        $(".dialog-box").dialog("open");
      });
    },
    courseDifficulty: function () {
      $(".course-difficulty").checkboxradio({
        icon: false,
      });
    },
    createGradingTabs: function () {
      if (!$("#tabs").length) {
        return;
      }

      $("#tabs").tabs();
    },
    addLabProfile: function () {
      if (!$(".modal-lab-profile").length) {
        return;
      }

      //Incs-starantiate Dialog Box for Creating a Lab Profile
      $(".modal-lab-profile").dialog({
        resizable: false,
        height: 600,
        width: 850,
        modal: true,
        title: "Add a Lab Profile",
        closeOnEscape: true,
        autoOpen: false,
        draggable: false,
        buttons: {
          "Save Lab Profile": function () {
            $(this).dialog("close");
          },
        },
      });

      $(".btn-addLabProfile").on("click", function (e) {
        e.preventDefault();
        $(".modal-lab-profile").dialog("open");
      });

      //Create Previous and Next Tabbing for Lab Profile

      var divs = $(".lab-profile-tabs>div");
      var now = 0; // currently shown div
      divs.hide().fircs - star().show(); // hide all divs except fircs-star

      $("#btnNext").click(function () {
        divs.eq(now).hide();
        now = now + 1 < divs.length ? now + 1 : 0;
        divs.eq(now).show(); // show next
      });

      $("#btnPrevious").click(function () {
        divs.eq(now).hide();
        now = now > 0 ? now - 1 : divs.length - 1;
        divs.eq(now).show(); // show previous
      });
    },
    editGrade: function () {
      $(".modal-edit-grade").dialog({
        resizable: false,
        height: 600,
        width: 850,
        modal: true,
        title: "Add a Lab Profile",
        closeOnEscape: true,
        autoOpen: false,
        draggable: false,
        buttons: {
          "Save Lab Profile": function () {
            $(this).dialog("close");
          },
        },
      });
    },

    addReview: function () {
      if (!$("#dialog").length) {
        return;
      }

      $("#dialog").dialog({
        resizable: false,
        width: 920,
        modal: true,
        title: "Add a Lab Profile",
        closeOnEscape: true,
        autoOpen: false,
        draggable: false,
        title: "Write a Review",
      });

      function rateCounter(counter) {
        $(".rate").html(counter + " of 5");
      }

      $("#btnShow").click(function () {
        $("#dialog").dialog("open");
      });

      $("#btnClose").click(function () {
        $(".material-icons").css("color", "gray");
        $("#dialog").dialog("close");
      });

      $("#cs-star1").click(function () {
        $(".material-icons").css("color", "gray");
        $("#cs-star1").css("color", "yellow");
        rateCounter(1);
      });

      $("#cs-star2").click(function () {
        $(".material-icons").css("color", "gray");
        $("#cs-star1, #cs-star2").css("color", "yellow");
        rateCounter(2);
      });

      $("#cs-star3").click(function () {
        $(".material-icons").css("color", "gray");
        $("#cs-star1, #cs-star2, #cs-star3").css("color", "yellow");
        rateCounter(3);
      });

      $("#cs-star4").click(function () {
        $(".material-icons").css("color", "gray");
        $("#cs-star1, #cs-star2, #cs-star3, #cs-star4").css("color", "yellow");
        rateCounter(4);
      });

      $("#cs-star5").click(function () {
        $(".material-icons").css("color", "gray");
        $("#cs-star1, #cs-star2, #cs-star3, #cs-star4, #cs-star5").css(
          "color",
          "yellow"
        );
        rateCounter(5);
      });
    },

    removeFromCartPage: function () {
      if (!$(".page-checkout").length) {
        return;
      }

      $(".checkout-trackCourse__close .material-icons").on(
        "click",
        function () {
          console.log($(this));
          $(this).parents(".checkout-trackCourse").fadeOut();
        }
      );
    },

    // miniCart: function () {
    //   $(function () {
    //     $(".mdl-button").click(function () {
    //       $(this).toggleClass("active");
    //       $(".cs-mini-cart--menu").toggleClass("active");
    //     });
    //   });
    // },
  };

  //separated document
  $(function () {
    $(".mdl-button").click(function () {
      $(this).toggleClass("active");
      $(".cs-mini-cart__menu").toggleClass("active");
    });
  });

  $(document).ready(function () {
    vlmp.init();
  });
})(jQuery);
