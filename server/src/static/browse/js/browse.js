function move_file(data_var) {

    let selectedArr4 = [];
    $('#example_wrapper table tbody').find('input:checkbox[name=selectedBox]:checked').each(function() {
        selectedArr4.push($(this).val());
    });
    console.log(selectedArr4);

    if (selectedArr4.length >= 1){
        $("#copy_move_Modal").modal('show');
        $("#copy_move_modal_table").DataTable();

        $("#copy_move_modal_select").click(function () {

            var source = $("#directory").val();
            var files_list = selectedArr4;
            var destination = $("#copy-move-modal-directory").val();
            console.log(source , files_list, destination);
            $.ajax({
                type : "POST",
                dataType : 'json',
                data : {
                    'files': JSON.stringify(files_list),
                    'source': source,
                    'destination': destination,
                    'node_id': data_var.node_id,
                    'csrfmiddlewaretoken': data_var.csrf
                },
                url : data_var.move_url,
                success: function (data) {
                    if (data.success === 1){
                        alert("successfully moved");
                        location.reload()
                    }
                    else {
                        alert(data.msg);
                    }
                    var data_click = {
                        'table_id': $("#copy_move_modal_table"),
                        'directory_id': $("#copy-move-modal-directory"),
                        'clicked_directory': "",
                        'node_id': data_var.node_id,
                        // 'browse_url': "{% url 'browse_directory_ajax' %}",
                        'browse_url': data_var.browse_url,
                        'checkbox': false,
                        'no_file': true,
                        'csrf': '{{ csrf_token }}'
                    }
                    browse_directory_local(data_click);
                }

            });

        });
    }
    else {
        alert("please select at least one file or folder");
    }
}

function rename_file(data_var) {
    let selectedArr5 = [];
    $('#example_wrapper table tbody').find('input:checkbox[name=selectedBox]:checked').each(function() {
        selectedArr5.push($(this).val());
    });
    console.log(selectedArr5);

    if (selectedArr5.length === 1){
        $("#renameModal").modal('show');
        $("#rename-modal-directory").val(selectedArr5[0]);
        $("#rename_file").click(function () {
            $.ajax({
                type : "POST",
                dataType : 'json',
                data : {
                    'files': JSON.stringify(selectedArr5),
                    'source': $("#directory").val(),
                    'new_name': $("#rename-modal-directory").val(),
                    'node_id': data_var.node_id,
                    'csrfmiddlewaretoken': data_var.csrf
                },
                url : data_var.rename_url,
                success: function (data) {
                    if (data.success === 1){
                        alert("successfully renamed");
                        $('#renameModal').modal('hide');
                    }
                    else {
                        alert(data.msg);
                    }
                    var data_click = {
                        'table_id': $("#example"),
                        'directory_id': $("#directory"),
                        'clicked_directory': "",
                        'node_id': data_var.node_id,
                        // 'browse_url': "{% url 'browse_directory_ajax' %}",
                        'browse_url': data_var.browse_url,
                        'checkbox': true,
                        'csrf': '{{ csrf_token }}'
                    }
                    browse_directory_local(data_click);
                }
            });

        });
    }
    else {
        alert("please select only one file or folder");
    }

}

function delete_file(data_var) {
    let selectedArr6 = [];
    $('#example_wrapper table tbody').find('input:checkbox[name=selectedBox]:checked').each(function() {
        selectedArr6.push($(this).val());
    });
    console.log(selectedArr6);

    if (selectedArr6.length >= 1) {
        var user_response = confirm("Are you sure, you want to delete the selected files?");
        if (user_response === true) {
            $.ajax({
                type: "POST",
                dataType: 'json',
                data: {
                    'files': JSON.stringify(selectedArr6),
                    'source': $("#directory").val(),
                    'node_id': data_var.node_id,
                    'csrfmiddlewaretoken': data_var.csrf
                },
                url: data_var.delete_url,
                success: function (data) {
                    if (data.success === 1) {
                        alert("successfully deleted");
                        location.reload()
                    }
                    else {
                        alert(data.msg);
                    }
                    var data_click = {
                        'table_id': $("#example"),
                        'directory_id': $("#directory"),
                        'clicked_directory': "",
                        'node_id': data_var.node_id,
                        // 'browse_url': "{% url 'browse_directory_ajax' %}",
                        'browse_url': data_var.browse_url,
                        'checkbox': true,
                        'csrf': '{{ csrf_token }}'
                    }
                    browse_directory_local(data_click);
                }

            });
        }}

    else {
        alert("please select at least one file or folder");
    }
}

function make_directory(csrf, url1, url2, node_ip, node_id) {

    $('#mkdirModal').modal('show');

    $("#mkdir-create").click(function () {
        if ($("#mkdir-modal-directory").val() === "") {
            alert("please fill the input box to create folder")
        }
        else {
            console.log($("#mkdir-modal-directory").val());
            $.ajax({
                type: "GET",
                dataType: 'json',
                data: {
                    'root_folder': $("#directory").val(),
                    'folder_name': $("#mkdir-modal-directory").val(),
                    'node_ip': node_ip,
                    'csrfmiddlewaretoken': csrf
                },
                url: url1,
                success: function (result) {
                    if (result.success) {
                        $("#mkdirModal").modal('hide');
                        location.reload();
                    }
                    else {
                        alert(result.msg);
                    }
                    var data_click = {
                        'table_id': $("#example"),
                        'directory_id': $("#directory"),
                        'clicked_directory': "",
                        'node_id': node_id,
                        // 'browse_url': "{% url 'browse_directory_ajax' %}",
                        'browse_url': url2,
                        'checkbox': true,
                        'csrf': csrf
                    }
                    browse_directory_local(data_click);
                }
            });

        }
    });
}

function back_local(data_var) {
    // var directory = $('#directory').val();
    // console.log(data_var);
    // var current = data_var.table_id;
    data_var.table_id.DataTable();
    $.ajax({
        type : "GET",
        dataType : 'json',
        data : {
            'directory_name': data_var.directory_id.val(),
            'node_id': data_var.node_id,
            'csrfmiddlewaretoken': data_var.csrf
        },
        url : data_var.back_url,
        success : function(data) {
            var datas = data.folder_details;
            var content = '';
            data_var.table_id.DataTable().destroy();
            for(var i=0; i<datas.length; i++){
                console.log(datas[i].permission, datas[i].owner, datas[i].group, datas[i].size, datas[i].name);
                content += '<tr role="row" class="odd">';
                if (data_var.checkbox){
                    content += '<td class="sorting_0"><input type="checkbox" name="selectedBox" class="selectedBox" value="' + datas[i].name + '"></td>';
                }
                content += '<td class="sorting_1">' + datas[i].permission + '</td>';
                content += '<td class="sorting_2">' + datas[i].owner + '</td>';
                content += '<td class="sorting_3">' + datas[i].group + '</td>';
                content += '<td class="sorting_4">' + datas[i].size + '</td>';
                if(datas[i].type === 'file'){
                    content += '<td class="sorting_5"><a class="file_class">' + datas[i].name + '</a></td>';
                }
                else {
                    content += '<td class="sorting_6"><a style="display: block" class="directory_class">' + datas[i].name + '</a></td>';
                }
                content += '</tr>';
            }

            data_var.table_id.find("tbody").html(content);
            // console.log($("#example tbody").html());
            data_var.table_id.DataTable({
                'columnDefs': [{
                    'targets': 0,
                    'searchable': false,
                    'orderable': false,
                    'className': 'dt-body-center'
                }],
                'order': [[1, 'asc']]
            });
            data_var.directory_id.val(data.back_directory);
        }
    });

}


function browse_directory_local(data_var) {
    var checkbox = data_var.checkbox;
    var current =data_var.table_id;
    var directory = "";
    if (data_var.clicked_directory !== "") {
        var name = data_var.clicked_directory;
        var previous_directory = data_var.directory_id.val();
        var after_directory = previous_directory + name ;
        // if (previous_directory === "/"){
        //     after_directory = previous_directory + "/" + name;
        // }

        var directory = after_directory;
        data_var.directory_id.val(after_directory);
    }
    else {
        if (data_var.hasOwnProperty('root')){
            directory = data_var.root;
        }
        else {
            directory = data_var.directory_id.val();
        }
    }

    // data_var.table_id.DataTable();

    $.ajax({
        type : "GET",
        dataType : 'json',
        data : {
            'directory_name': directory,
            'node_id': data_var.node_id,
            'csrfmiddlewaretoken': data_var.csrf
        },
        url : data_var.browse_url,
        success : function(data) {
            var datas = data.folder_details;
            var content = '';
            data_var.table_id.DataTable().destroy();
            for(var i=0; i<datas.length; i++){
                console.log(datas[i].permission, datas[i].owner, datas[i].group, datas[i].size, datas[i].name);

                content += '<tr role="row" class="odd">';
                if (checkbox){
                    content += '<td class="sorting_0"><input type="checkbox" name="selectedBox" class="selectedBox" value="'+datas[i].name+'"></td>';
                }
                content += '<td class="sorting_1">' + datas[i].permission + '</td>';
                content += '<td class="sorting_2">' + datas[i].owner + '</td>';
                content += '<td class="sorting_3">' + datas[i].group + '</td>';
                content += '<td class="sorting_4">' + datas[i].size + '</td>';
                if(datas[i].type === 'file'){
                    content += '<td class="sorting_5"><a class="file_class">' + datas[i].name + '</a></td>';
                }
                else {
                    content += '<td class="sorting_6"><a style="display: block" class="directory_class">' + datas[i].name + '</a></td>';
                }
                content += '</tr>';
            }
            data_var.table_id.find('tbody').html(content);
            data_var.table_id.DataTable({
                'columnDefs': [{
                    'targets': 0,
                    'searchable': false,
                    'orderable': false,
                    'className': 'dt-body-center'
                }],
                'order': [[1, 'asc']]
            });
            data_var.directory_id.val(data.path);

        }
    });
}

function head_tail(data_var){

    $.ajax({
        type : "POST",
        dataType : 'json',
        data : {
            'file_name': $("#head_tailModalLabel").text(),
            'source': $("#directory").val(),
            'node_id': data_var.node_id,
            'csrfmiddlewaretoken': data_var.csrf
        },
        url : data_var.head_tail_url,
        success : function(data) {
            if (data.success === 1) {
                var data_array = data.result;
                console.log($("#head_tailModalLabel").text());
                $(".head_tail_text").val(Array.prototype.join.call(data_array, "\n"));
            }
            else {
                alert(data.msg);
            }
        }
    });
}

