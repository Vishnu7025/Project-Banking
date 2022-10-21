
// document.getElementById('district').onchange()/s``
$("#district").change(function () {
    const url1 = $("#branch").attr("branch-queries-url");
    const districtId = $(this).val();                // get the selected district ID from the HTML input
    $.ajax({                                          // initialize an AJAX request
        url: url1,                                    // set the url of the request (= ajax/load-branch-details/ )
        data: { 'district_id': districtId },        // add the district id to the GET parameters
        success: function (data) {
            $("#branch").html(data);
        }
    });
});
