var ajax_call = function() {

};

var interval = 1000 * 60 * X; // where X is your every X minutes




function fetchData(data){
    $.ajax({
            type : "POST",
            dataType : 'json',
            data : {
                'node_ip': data.node_ip,
                'csrfmiddlewaretoken': data.csrf
            },
            url : data.url,
            success : function(result) {
                if (result.success){

                }else{
                    HoldOn.close();

                }
            }
        });
    setInterval(this, interval);
}