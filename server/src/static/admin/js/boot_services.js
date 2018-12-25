var wq = {
        theme:"sk-cube",
        content :'',
        message:'<h2>page will reload after successful operation.</h2>',
        backgroundColor:"rgba(10,10,10,0.3)",
        textColor:"white"
};

function service_operation(data){
    swal({
        text: data.msg,
        type: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'continue',
        showLoaderOnConfirm: true,
        preConfirm: () => {}
    }).then((result) => {
        if (result.value) {
            HoldOn.open(wq);
            send_ajax(data);

    }
});
}

function send_ajax(data){
    $.ajax({
            type : "POST",
            dataType : 'json',
            data : {
                'node_ip': data.node_ip,
                'csrfmiddlewaretoken': data.csrf,
                'server_type':data.server_type,
                'action_type':data.action_type,
                'node_id': data.node_id
            },
            url : data.url,
            success : function(result) {
                if (result.success === 1){
                    setTimeout(function(){ window.location.reload(); },2000);

                }else if (result.success === 2) {
                    HoldOn.close();
                    data.msg="We are unable to gracefully stop request service. We can forcefully stop the node, " +
                        "but it may cause instability in your service. Do you want to stop the service forcefully ?";

                        data.url="/"+data.service_name+"/command/kill/";
                        console.log(data.url);
                    service_operation(data);
                }else{
                    HoldOn.close();
                    console.log(result.msg);
                    swal(result.msg[0]);
                }
            }
        });
}