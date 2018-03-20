$(document).ready(function() {

    $('#submit_btn').click(function(){

            var data = {};
            data.first_name = $('#firstname').val();
            data.last_name = $('#lastname').val();
            data.email = $('#email').val();
            data.password = $('#password').val();


            $.ajax({
                type: "POST",
                url: "user/<int:pk>",
                data: data,
                cache: false,
                success: function (response) {
                  alert("success")
                }
            });
                return false;
        });

    });