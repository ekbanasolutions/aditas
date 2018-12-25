
function sync(csrf,url) {
    swal({
        title: 'Are you sure want to synchronize user to backup configuration?',
        type: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'continue',
        showLoaderOnConfirm: true,
    }).then((result) => {
        if (result.value) {
            swal.showLoading();
            $.ajax({
                type : "POST",
                dataType : 'json',
                data : {
                    'csrfmiddlewaretoken': csrf
                },
                url : url,
                success : function(data) {
                    if(data.success){
                        swal("configuration synced successful");
                    }
                    else {
                        swal(data.msg);
                    }
                }
            });
        }
    })
}

function revert(csrf,url) {
    swal({
  title: 'Are you sure want to synchronize backup to user configuration?',
  type: 'warning',
  showCancelButton: true,
  confirmButtonColor: '#3085d6',
  cancelButtonColor: '#d33',
  confirmButtonText: 'continue',
  showLoaderOnConfirm: true,
}).then((result) => {
  if (result.value) {
      swal.showLoading()
        $.ajax({
            type : "POST",
            dataType : 'json',
            data : {
                'csrfmiddlewaretoken': csrf
            },
            url : url,
            success : function(data) {
                if(data.success){
                    swal("configuration reverted successful");
                }
                else {
                    swal(data.msg);
                }
            }
        });
  }
})


}