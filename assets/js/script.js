$(document).ready(function(){

    function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                // Only send the token to relative URLs i.e. locally.
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            }
        }
    });


    if ($(".requestsTable").length) {

        function sendViews(requests) {
            $.ajax({
                method: "post",
                url: "/requests/ajaxrequests/",
                data: {'data':JSON.stringify(requests)}
            });
        }

        function fillData(data) {
            var compiledRow = _.template(
                "<tr class=<%=bold_class%>>" +
                "<td><%=date%></td>" +
                "<td><%=method%></td>" +
                "<td><%=path%></td>" +
                "<td><%=server_protocol%></td> " +
                "<td><%=ip_addr%></td> " +
                "</tr>");
            var rows = '';
            data['ajaxrequests'].forEach(function (item) {
                var row = compiledRow({
                    date: item['date'],
                    method: item['method'],
                    path: item['path'],
                    server_protocol: item['server_protocol'],
                    ip_addr: item['ip_addr'],
                    bold_class: item['viewed'] == false ? 'bold-font' : '',
                });
                rows += row;
            });

            $('.requestsTable').html(rows);

            if (data['new_requests']){
                $('.requests').text('(' + data['new_requests'] + ') new requests');
                document.title = '(' + data['new_requests'] + ') new requests';
            }else{
                $('.requests').text('Last 10 Requests');
                document.title = 'Last 10 Requests';
            }
        }

        var requests = [];
        function fillRequests() {

            $.ajax({
                method: "get",
                url: "/requests/ajaxrequests/"
            }).done(function (data) {
                fillData(data);
                requests = data['ajaxrequests'];
                if (wasRequestsViewed()) {
                    sendViews(requests);
                }

            });
        }

        function wasRequestsViewed(){
            return document.visibilityState=='visible';
        }

        fillRequests();
        setInterval(fillRequests, 5000); //5 sec delay

    }


    if ($("#edit_form").length) {

/*
         function managestatusVisible(show){
            var status = $('#message');
            if(show){
               status.show();
            }else{
                status.hide();
            }
         }

         function manageFormStatus(success){
             var status = $('#message');
             if (success){
                managestatusVisible(true);
                status.addClass('alert-success');
                status.text('Data saved done!');

            }else{
                managestatusVisible(true);
                status.addClass('alert-danger');
                status.text('Error saving data!');
             }

         }

         function formElementsEnableDisable(enable){
             if (enable){
                $("#edit_form :input").prop('disabled', false);
             }else{
                $("#edit_form :input").prop('disabled', true);
             }
         }


        managestatusVisible(false);




         function showErrors(responseText, statusText, xhr, $form) {
             manageFormStatus(false);
             formElementsEnableDisable(true);
         }


*/

        var options = {
             //target: '#message',
             success: showSuccess,
             error: showSuccess,
         };




         function formElementsEnableDisable(enable){
             if (enable){
                $("#edit_form :input").prop('disabled', false);
             }else{
                $("#edit_form :input").prop('disabled', true);
             }
         }

         function showSuccess() {
           $("#edit_form :input").prop('disabled', true);

         }

        $('#edit_form').submit(function () {
            $(this).ajaxSubmit();
showSuccess();
            //formElementsEnableDisable(false);
            //$("#submit_button").prop( "disabled", true);
            return false
        });




    }
    
});
