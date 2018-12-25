function browse_directory_hdfs(data_var){
        var name = data_var.clicked_directory;
        var previous_directory = data_var.directory_id.val();
        var after_directory = previous_directory + '/' + name;
        data_var.directory_id.val(after_directory);


        $.ajax({
                type : "GET",
                dataType : 'json',
                data : {
                    'directory_name': after_directory,
                    'csrfmiddlewaretoken': '{{ csrf_token }}',
                    'master_ip': data_var.master_ip,
                },
                url : data_var.browse_url,
                success : function(data) {
                    var datas = data.FileStatus;
                    var content = '';
                    data_var.table_id.DataTable().destroy();
                    for(var i=0; i<datas.length; i++){
                        console.log(datas[i].permission, datas[i].owner, datas[i].group, datas[i].length, datas[i].pathSuffix);
                        content += '<tr role="row" class="odd">';
                        content += '<td class="sorting_0"><input type="checkbox" name="selectedBox" class="selectedBox" value="'+datas[i].pathSuffix+'"></td>';
                        content += '<td class="sorting_1">' + datas[i].permission + '</td>';
                        content += '<td class="sorting_2">' + datas[i].owner + '</td>';
                        content += '<td class="sorting_3">' + datas[i].group + '</td>';
                        content += '<td class="sorting_4">' + datas[i].length + '</td>';
                        if(datas[i].type === 'FILE'){
                            content += '<td class="sorting_5">' + datas[i].pathSuffix + '</td>';
                        }
                        else {
                            content += '<td class="sorting_6"><a style="display: block" class="directory_class">' + datas[i].pathSuffix + '</a></td>';
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

                }
            });
}


function back_directory_hdfs(data_var) {
    $.ajax({
                type : "GET",
                dataType : 'json',
                data : {
                    'directory_name': data_var.directory_id.val(),
                    'csrfmiddlewaretoken': data_var.csrf,
                    'master_ip': data_var.master_ip,
                },
                url : data_var.back_url,
                success : function(data) {
                    var datas = data.FileStatus;
                    var content = '';
                    data_var.table_id.DataTable().destroy();
                    for(var i=0; i<datas.length; i++){
                        console.log(datas[i].permission, datas[i].owner, datas[i].group, datas[i].length, datas[i].pathSuffix);
                        content += '<tr role="row" class="odd">';
                        content += '<td class="sorting_0"><input type="checkbox" name="selectedBox" class="selectedBox" value="'+datas[i].pathSuffix+'"></td>';
                        content += '<td class="sorting_1">' + datas[i].permission + '</td>';
                        content += '<td class="sorting_2">' + datas[i].owner + '</td>';
                        content += '<td class="sorting_3">' + datas[i].group + '</td>';
                        content += '<td class="sorting_4">' + datas[i].length + '</td>';
                        if(datas[i].type === 'FILE'){
                            content += '<td class="sorting_5">' + datas[i].pathSuffix + '</td>';
                        }
                        else {
                            content += '<td class="sorting_6"><a style="display: block" class="directory_class">' + datas[i].pathSuffix + '</a></td>';
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
                    data_var.directory_id.val(data.back_directory);
                }
                });
}


function browse_eachnode_local(data_var){
    if (data_var.clicked_directory !== ""){
            var modal_name = data_var.clicked_directory;
            var modal_previous_directory = data_var.directory_id.val();
            var modal_after_directory = modal_previous_directory + modal_name;
    }
    else {
        modal_after_directory = data_var.directory_id.val();
    }
            // data_var.directory_id.val(modal_after_directory);

            $.ajax({
                type : "POST",
                dataType : 'json',
                data : {
                    'directory_name': modal_after_directory,
                    'node_ip': data_var.node_ip,
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
                        content += '<td class="sorting_1">' + datas[i].permission + '</td>';
                        content += '<td class="sorting_2">' + datas[i].owner + '</td>';
                        content += '<td class="sorting_3">' + datas[i].group + '</td>';
                        content += '<td class="sorting_4">' + datas[i].size + '</td>';
                        if(datas[i].type === 'file'){
                            content += '<td class="sorting_5">' + datas[i].name + '</td>';
                        }
                        else {
                            content += '<td class="sorting_6"><a style="display: block" class="directory_class">' + datas[i].name + '</a></td>';
                        }
                        content += '</tr>';
                    }
                    data_var.table_id.find("tbody").html(content);
                    data_var.table_id.DataTable();
                    data_var.directory_id.val(data.path);
                }
        });
}


function back_eachnode(data_var) {
    $.ajax({
                type : "POST",
                dataType : 'json',
                data : {
                    'directory_name': data_var.directory_id.val(),
                    'node_ip': data_var.node_ip,
                    'csrfmiddlewaretoken': data_var.csrf
                },
                url : data_var.back_url,
                success : function(data) {
                    var datas = data.folder_details;
                    var content = '';
                    data_var.table_id.DataTable().destroy();
                    for(var i=0; i<datas.length; i++){
                        content += '<tr role="row" class="odd">';
                        content += '<td class="sorting_1">' + datas[i].permission + '</td>';
                        content += '<td class="sorting_2">' + datas[i].owner + '</td>';
                        content += '<td class="sorting_3">' + datas[i].group + '</td>';
                        content += '<td class="sorting_4">' + datas[i].size + '</td>';
                        if(datas[i].type === 'file'){
                            content += '<td class="sorting_5">' + datas[i].name + '</td>';
                        }
                        else {
                            content += '<td class="sorting_6"><a style="display: block" class="directory_class">' + datas[i].name + '</a></td>';
                        }
                        content += '</tr>';
                    }
                    data_var.table_id.find("tbody").html(content);
                    data_var.table_id.DataTable();
                    data_var.directory_id.val(data.path);
                }
                });
}