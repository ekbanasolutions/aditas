var table
$(document).ready(function () {
    table = $("#example").DataTable({
        'columnDefs': [{
            'targets': 0,
            'searchable': false,
            'orderable': false,
            'className': 'dt-body-center'
        }],
        'order': [[1, 'asc']]
    });

    $('#example-select-all').on('click', function () {
        var rows = table.rows({'search': 'applied'}).nodes();
        console.log(rows);
        $('input[type="checkbox"]', rows).prop('checked', this.checked);
    });

    $('#example tbody').on('change', 'input[type="checkbox"]', function () {
        if (!this.checked) {
            var el = $('#example-select-all').get(0);
            if (el && el.checked && ('indeterminate' in el)) {
                el.indeterminate = true;
            }
        }
    });

});

function save_user(data_urls) {
    let selectedArr = [];
    table.rows().nodes().to$().find('input:checkbox[name=selectedBox]:checked').each(function () {
        selectedArr.push($(this).val());
    });

    var data= {
        'csrfmiddlewaretoken': data_urls.csrfmiddlewaretoken,
        'username': $('#id_username').val(),
        'email': $('#id_email').val(),
        'first_name': $('#id_first_name').val(),
        'last_name': $('#id_last_name').val(),
        'is_active': $('#id_is_active:checked').val()?"True":"False",
        'is_superuser': $('#id_is_superuser:checked').val()?"True":"False",
        'groups_id': JSON.stringify(selectedArr),
    };
    $.ajax({
        type: "POST",
        dataType: 'json',
        data: data,
        url: data_urls.post_url,
        success: function (data) {
            if (data.success){
                window.location.href = data_urls.success_url
            }
            else {
                location.reload();
            }
        }
    });
}

function save_group(data_urls){
    let selectedArr = [];
    table.rows().nodes().to$().find('input:checkbox[name=selectedBox]:checked').each(function () {
        selectedArr.push($(this).val());
    });
    $.ajax({
        type: "POST",
        dataType: 'json',
        data: {
            'csrfmiddlewaretoken': data_urls.csrfmiddlewaretoken,
            'group_name': $('#id_groupname').val(),
            'permissions_id': JSON.stringify(selectedArr),
        },
        url: data_urls.post_url,
        success: function (data) {
            if (data.success){
                window.location.href = data_urls.success_url
            }
            else {
                location.reload();
            }
        }
    });
}
