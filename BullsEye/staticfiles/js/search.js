$(document).ready(function(){
    $("#search-input").on('keyup', function(e){
        if (e.key === 'Enter' || e.keyCode === 13) {
            performSearch();
        }
    });

    $("button[type='submit']").click(function(){
        performSearch();
    });

    function performSearch() {
        var query = $("#search-input").val();
        $.ajax({
            url: 'http://127.0.0.1:7000/sample',
            type: 'GET',
            data: { q: query },
            success: function(data) {
                // Redirect to the search result page with data as parameter
                window.location.href = "/search_result?data=" + encodeURIComponent(JSON.stringify(data));
            },
            error: function() {
                alert("Error fetching search results. Please try again later.");
            }
        });
    }
});
