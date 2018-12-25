var options = {
    responsive: true,
    maintainAspectRatio: false,
    scales: {
        xAxes: [{
            ticks: {
                minRotation: 90,
                autoSkip: true,
                maxTicksLimit: 10
            }
        }],
        yAxes: [{
            ticks: {
                beginAtZero: true
            }
        }]
    }, elements: {
        line: {
            fill: false
        }
    }
};

function cpu_usage(date, cpu) {
    $("#cpu_usage").removeClass("hidden");
    var a = new Chart($('#cpu'), {
        type: 'line',
        data: {
            labels: date,
            datasets: cpu,
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                xAxes: [{
                    ticks: {
                        minRotation: 90,
                        autoSkip: true,
                        maxTicksLimit: 10
                    }
                }],
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }, elements: {
                line: {
                    fill: false
                }
            }
        }
    });
}

function shared_memory(date, sm_total, sm_used, sm_free) {
    $("#shared_memory").removeClass("hidden");
    $("#total_swap_memory_text").text("Total swap memory: " + sm_total[0] + " GB");
    new Chart($('#sm'), {
        type: 'line',
        data: {
            labels: date,
            datasets: [
                {
                    "label": "used",
                    "data": sm_used,
                    "hidden": false,
                    "pointRadius": 0,
                    "borderColor": "rgba(" + Math.floor(Math.random() * 255) + "," + Math.floor(Math.random() * 255) + ","
                        + Math.floor(Math.random() * 255) + ",1)"
                },
                {
                    "label": "free",
                    "data": sm_free,
                    "hidden": true,
                    "pointRadius": 0,
                    "borderColor": "rgba(" + Math.floor(Math.random() * 255) + "," + Math.floor(Math.random() * 255) + ","
                        + Math.floor(Math.random() * 255) + ",1)"
                }
            ],
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                xAxes: [{
                    ticks: {
                        minRotation: 90,
                        autoSkip: true,
                        maxTicksLimit: 10
                    }
                }],
                yAxes: [{
                    ticks: {
                        beginAtZero: true,
                        steps: 10,
                        stepValue: 5,
                        max: Math.ceil(sm_total[0])
                    }
                }]
            }
        }
    });
}

function virtual_memory(date, vm_shared, vm_used, vm_free, vm_available, vm_total, vm_buffer, vm_cache) {
    $("#virtual_memory").removeClass("hidden");
    $("#total_virtual_memory_text").text("Total virtual memory: " + vm_total[0] + " GB");
    new Chart($('#vm'), {
        type: 'line',
        data: {
            labels: date,
            datasets: [
                {
                    "label": "shared",
                    "data": vm_shared,
                    "hidden": false,
                    "pointRadius": 0,
                    "borderColor": "rgba(" + Math.floor(Math.random() * 255) + "," + Math.floor(Math.random() * 255) + ","
                        + Math.floor(Math.random() * 255) + ",1)"
                },
                {
                    "label": "used",
                    "data": vm_used,
                    "hidden": true,
                    "pointRadius": 0,
                    "borderColor": "rgba(" + Math.floor(Math.random() * 255) + "," + Math.floor(Math.random() * 255) + ","
                        + Math.floor(Math.random() * 255) + ",1)"
                },
                {
                    "label": "free",
                    "data": vm_free,
                    "hidden": true,
                    "pointRadius": 0,
                    "borderColor": "rgba(" + Math.floor(Math.random() * 255) + "," + Math.floor(Math.random() * 255) + ","
                        + Math.floor(Math.random() * 255) + ",1)"
                },
                {
                    "label": "available",
                    "data": vm_available,
                    "hidden": true,
                    "pointRadius": 0,
                    "borderColor": "rgba(" + Math.floor(Math.random() * 255) + "," + Math.floor(Math.random() * 255) + ","
                        + Math.floor(Math.random() * 255) + ",1)"
                },
                {
                    "label": "buffer",
                    "data": vm_buffer,
                    "hidden": true,
                    "pointRadius": 0,
                    "borderColor": "rgba(" + Math.floor(Math.random() * 255) + "," + Math.floor(Math.random() * 255) + ","
                        + Math.floor(Math.random() * 255) + ",1)"
                },
                {
                    "label": "cache",
                    "data": vm_cache,
                    "hidden": true,
                    "pointRadius": 0,
                    "borderColor": "rgba(" + Math.floor(Math.random() * 255) + "," + Math.floor(Math.random() * 255) + ","
                        + Math.floor(Math.random() * 255) + ",1)"
                }
            ],
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                xAxes: [{
                    ticks: {
                        minRotation: 90,
                        autoSkip: true,
                        maxTicksLimit: 10
                    }
                }],
                yAxes: [{
                    ticks: {
                        beginAtZero: true,
                        steps: 10,
                        stepValue: 5,
                        max: Math.ceil(vm_total[0])
                    }
                }]
            }
        }

    });
}

function network_bandwidth(date, data) {
    $("#network_bandwidth").removeClass("hidden");
    date.shift();
    key = Object.keys(data);
    $('#network_bandwidth').empty();
    max_val = [];

    for (max_lp = 0; max_lp < key.length; max_lp++) {
        max_val.push(Math.max(...data[max_lp][Object.keys(data[max_lp])][0]["data"]));
    }

    for (a = 0; a < key.length; a++) {
        interface_name = Object.keys(data[a]);
        id = interface_name + 'text';
        var cls = 'col-md-6';
        if (data[a].length === 1) {
            cls = 'col-md-12';
        }

        console.log(data[a][interface_name]);
        if(data[a][interface_name] != null) {
            $('#network_bandwidth').append(
                "<div class='" + cls + "'>" +
                "<div class='panel panel-default '>" +
                "<div class='panel-body'><div class='page-header'><h4>" + interface_name + "<p id='" + id + "_text'" +
                "class='pull-right'></p></h4></div>" +
                "<div style='height: 300px;'><canvas id='" + interface_name + "'" +
                "style='width:1024px;height:400px;'></canvas></div></canvas></div></div></div>");
            new Chart($('#' + interface_name), {
                type: 'line',
                data: {
                    labels: date,
                    datasets: data[a][interface_name],
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {
                        xAxes: [{
                            ticks: {
                                minRotation: 90,
                                autoSkip: true,
                                maxTicksLimit: 10
                            }
                        }],
                        yAxes: [{
                            ticks: {
                                beginAtZero: true,
                                steps: 10,
                                stepValue: 5,
                                max: max_val[a]
                            }
                        }]
                    }, elements: {
                        line: {
                            fill: false
                        }
                    }
                }
            });
        }
    }
}

function disk_usage(date, du_disk_free, du_disk_percentage, du_disk_used, du_disk_total) {
    $("#disk_usage").removeClass("hidden");
    $('#total_disk_text').text("Total disk space: " + du_disk_total[0] + " GB");
    new Chart($('#du'), {
        type: 'line',
        data: {
            labels: date,
            datasets: [
                {
                    "label": "free disk",
                    "data": du_disk_free,
                    "hidden": false,
                    "pointRadius": 0,
                    "borderColor": "rgba(" + Math.floor(Math.random() * 255) + "," + Math.floor(Math.random() * 255) + "," +
                        Math.floor(Math.random() * 255) + ",1)"
                },
                {
                    "label": "disk used",
                    "data": du_disk_used,
                    "hidden": true,
                    "pointRadius": 0,
                    "borderColor": "rgba(" + Math.floor(Math.random() * 255) + "," + Math.floor(Math.random() * 255) + "," +
                        Math.floor(Math.random() * 255) + ",1)"
                },
            ],
        }
        ,
        options: options
    });
}

function disk_io(date, dio_write_count, dio_read_count, dio_read_time, dio_write_time) {
    $("#disk_io").removeClass("hidden");
    $("#disk_io_time").removeClass("hidden");
    new Chart($('#dio'), {
        type: 'line',
        data: {
            labels: date,
            datasets: [
                {
                    "label": "write count",
                    "data": dio_write_count,
                    "hidden": false,
                    "pointRadius": 0,
                    "borderColor": "rgba(" + Math.floor(Math.random() * 255) + "," + Math.floor(Math.random() * 255) + "," +
                        Math.floor(Math.random() * 255) + ",1)"
                },
                {
                    "label": "read count",
                    "data": dio_read_count,
                    "hidden": true,
                    "pointRadius": 0,
                    "borderColor": "rgba(" + Math.floor(Math.random() * 255) + "," + Math.floor(Math.random() * 255) + "," +
                        Math.floor(Math.random() * 255) + ",1)"
                }
            ],
        },
        options: options
    });

    new Chart($('#dio_time'), {
        type: 'line',
        data: {
            labels: date,
            datasets: [
                {
                    "label": "write time",
                    "data": dio_read_time,
                    "hidden": false,
                    "pointRadius": 0,
                    "borderColor": "rgba(" + Math.floor(Math.random() * 255) + "," + Math.floor(Math.random() * 255) + ","
                        + Math.floor(Math.random() * 255) + ",1)"
                },
                {
                    "label": "read time",
                    "data": dio_write_time,
                    "hidden": true,
                    "pointRadius": 0,
                    "borderColor": "rgba(" + Math.floor(Math.random() * 255) + "," + Math.floor(Math.random() * 255) + "," +
                        Math.floor(Math.random() * 255) + ",1)"
                }
            ],
        },
        options: options
    });
}

function service_metrices(id, date, label) {
    $("#cpu_usage").removeClass("hidden");
    new Chart($(id + ``), {
        type: 'line',
        data: {
            labels: date,
            datasets: label,
        },
        options: options
    });
}

function processes(proc) {
    $("#processes").removeClass("hidden");
    $("#proc").removeClass("hidden");
    for (i = 0; i < proc.length; i++) {
        var single_row = JSON.parse(proc[i]);
        ioc = single_row["io_counters"];
        if (ioc != null) {
            read_count = ioc[0];
            write_count = ioc[1];
            read_bytes = ioc[2];
            write_bytes = ioc[3];
        } else {
            read_count = write_count = read_bytes = write_bytes = 0;
        }
        row = "<tr>" +
            "<td>" + single_row["name"] + "</td>" +
            "<td>" + single_row["cpu_percent"] + "</td>" +
            "<td>" + parseInt(single_row["memory_percent"]).toFixed(2) + "</td>" +
            "<td>" + read_bytes + "</td>" +
            "<td>" + write_bytes + "</td>" +
            "<td>" + read_count + "</td>" +
            "<td>" + write_count + "</td>" +
            "</tr>";
        $("#proc_table tbody").append(row);
    }
    var table = $("#proc_table").dataTable({
        "order": [[1, "desc"]],
        destroy: true,
        "dom":'ft<"custom-pagin"p>',
        language:{
                    search: "_INPUT_",
                    searchPlaceholder: "Service ..."
                },
    });
}

function hdfs_metrics(date, label) {
    var disk = [];
    for (i = 0; i < label.length; i++) {
        if (['non_dfs_used', 'used_space'].indexOf(label[i].label) >= 0) {
            disk.push(label[i]);
        }
        if (label[i].label === "capacity") {
            capacity = label[i].data[0]
        }
    }
    chart_for_bd_services("hdfs_metrics", date, {"HDFS Disk Usage": disk});
    $('#HDFS_Disk_Usage_text').text("Capacity: " + capacity + " GB");
}

function yarn_metrics(date, label) {
    var memory = [];
    var cpu = [];
    for (i = 0; i < label.length; i++) {
        if (['cpu_used'].indexOf(label[i].label) >= 0) {
            cpu.push(label[i]);
        }
        if (['memory_used'].indexOf(label[i].label) >= 0) {
            memory.push(label[i]);
        }
    }
    chart_for_bd_services("yarn_metrics", date, {"Yarn Memory Usage": memory});
}

function hbase_metrics(date, label) {
    var memory = [];
    var io = [];
    for (i = 0; i < label.length; i++) {
        if (['read_request', 'write_request'].indexOf(label[i].label) >= 0) {
            io.push(label[i]);
        }
        if (['used_heap'].indexOf(label[i].label) >= 0) {
            memory.push(label[i]);
        }
        if (label[i].label === "max_heap") {
            max_heap = label[i].data[0];
        }

    }
    chart_for_bd_services("hbase_metrics", date, {"Hbase Memory Usage": memory, "Hbase IO": io});
    $('#Hbase_Memory_Usage_text').text("Total Memory: " + max_heap + " GB");
}

function spark_metrics(date, label) {
    var memory = [];
    var cpu = [];
    for (i = 0; i < label.length; i++) {
        if (['cores_used'].indexOf(label[i].label) >= 0) {
            cpu.push(label[i]);
        }
        if (['memory_used'].indexOf(label[i].label) >= 0) {
            memory.push(label[i]);
        }
        if (label[i].label === "total_cores") {
            total_cores = label[i].data[0];
        }
        if (label[i].label === "total_memory") {
            total_memory = label[i].data[0];
        }
    }
    chart_for_bd_services("spark_metrics", date, {"Spark Memory Usage": memory});
    $('#Spark_Memory_Usage_text').text("Total Memory: " + total_memory + " GB");
    $('#Spark_CPU_Usage_text').text("Total Cores: " + total_cores);

}

function es_metrics(date, label) {
    var memory = [];
    var swap_memory = [];
    var cpu = [];
    for (i = 0; i < label.length; i++) {
        if (['cpu_percent'].indexOf(label[i].label) >= 0) {
            cpu.push(label[i]);
        }
        if (['free_memory', 'used_memory'].indexOf(label[i].label) >= 0) {
            memory.push(label[i]);
        }
        if (['swap_free_memory', 'swap_used_memory'].indexOf(label[i].label) >= 0) {
            swap_memory.push(label[i]);
        }

        if (label[i].label === "swap_total_memory") {
            swap_total_memory = label[i].data[0] / 1000;
        }
        if (label[i].label === "total_memory") {
            total_memory = label[i].data[0] / 1000;
        }
    }
    chart_for_bd_services("es_metrics", date, {
        "Elasticsearch Memory Usage": memory,
        "Elasticsearch Swap Memory Usage": swap_memory, "Elasticsearch CPU Usage": cpu
    });
    $('#Elasticsearch_Memory_Usage_text').text("Total Memory: " + total_memory + " GB");
    $('#Elasticsearch_Swap_Memory_Usage_text').text("Total Swap Memory: " + swap_total_memory + " GB");

}

function chart_for_bd_services(parent, date, data) {
    k = Object.keys(data);
    var cls = 'col-md-6';
    if (k.length === 1) {
        cls = 'col-md-12';
    }
    $('#' + parent).empty();

    for (q = 0; q < k.length; q++) {
        service_name = k[q];
        id = service_name.split(' ').join('_');
        $('#' + parent).append(
            "<div class='" + cls + "'>" +
            "<div id='" + service_name + "' class='panel panel-default '>" +
            "<div class='panel-body'><div class='page-header'><h4>" + service_name + "<p id='" + id + "_text' " +
            "class='pull-right'></p></h4></div>" +
            "<div style='height: 300px;'><canvas id='" + id + "' " +
            "style='width:1024px;height:400px;'></canvas></div></canvas></div></div></div>");

        new Chart($('#' + id), {
            type: 'line',
            data: {
                labels: date,
                datasets: data[service_name],
            },
            options: options
        });

    }
}

function ajax_call(token, data_type, data_value, id, url) {
    $.ajax({
        type: "POST",
        dataType: 'json',
        data: {'csrfmiddlewaretoken': token, 'data_type': data_type, 'data_value': data_value, 'node_id': id},
        url: url,
        success: function (result) {
            if (result) {
                if (result.success === 0) {
                    HoldOn.close();
                    Swal({
                        title: 'ERROR !!!',
                        html: "<b>" + result.msg[0] + "</b><br /> you can try following steps: <br />" +
                            "1) restart agent. Follow doc [url here] <br />" +
                            "2) report a bug [url here]",
                        type: 'error',
                        showCancelButton: true,
                        confirmButtonColor: '#3085d6',
                        cancelButtonColor: '#d33',
                        confirmButtonText: 'sure'
                    }).then((result) => {
                        if (result.value) {
                            window.location.href = "/nodes/list_nodes/";
                        }
                    });

                } else {
                    shared_memory(result.date, result.sm_total, result.sm_used, result.sm_free);
                    cpu_usage(result.date, result.cpu);
                    virtual_memory(result.date, result.vm_shared, result.vm_used, result.vm_free, result.vm_available,
                        result.vm_total, result.vm_buffer, result.vm_cache);
                    disk_io(result.date, result.dio_write_count, result.dio_read_count, result.dio_read_time,
                        result.dio_write_time);
                    disk_usage(result.date, result.du_disk_free, result.du_disk_percentage, result.du_disk_used,
                        result.du_disk_total);

                    network_bandwidth(result.date, result.network);
                    processes(result.process);
                    ky = Object.keys(result.service_data);
                    for (w = 0; w < ky.length; w++) {
                        a = result.service_data[w];
                        service_name = Object.keys(a)[0];
                        service_value = a[service_name];
                        date = service_value[0];
                        label = service_value[1];
                        if (service_name === "hdfs_hdfs") {
                            hdfs_metrics(date, label);
                        }
                        if (service_name === "yarn_yarn") {
                            yarn_metrics(date, label);
                        }
                        if (service_name === "hbase_hbase") {
                            hbase_metrics(date, label);
                        }
                        if (service_name === "elastic_search_elastic_search") {
                            es_metrics(date, label)
                        }
                        if (service_name === "spark_spark") {
                            spark_metrics(date, label);
                        }
                    }

                    setTimeout(HoldOn.close(), 3000);
                }
            }
        }
    });
}
