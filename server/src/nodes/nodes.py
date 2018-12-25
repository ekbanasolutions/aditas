import ast
import json
from datetime import datetime, timedelta
from operator import itemgetter
from random import randint

import requests
from administer import context_processors
from administer.helper import helper
from administer.models import Nodes, Clusters
from django.contrib import messages
from django.db import connection
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View


class Nodes_status(View):

    def get(self, request):

        if 'user' in request.session:
            context = context_processors.base_variables_all(request)
            all_nodes = Nodes.objects.filter(approved=1).all()
            nodes = []
            data = {}

            if all_nodes:
                for node in all_nodes:
                    url = 'http://%s:%s/system/total/space/' % (node.ip, node.port)
                    response = CreateConnection.connect(request, url)
                    if response:
                        try:
                            data = response.json()
                        except ValueError as e:
                            data = ast.literal_eval(response.content.decode())
                        except Exception as e:
                            messages.error(request, e)
                        print(data)
                        if data and "success" not in data:
                            print("if")
                            nodes.append({"memory": data["total_memory"], "name": node.name,
                                          "approved": node.approved, "disk": data["total_disk"], "ip": node.ip,
                                          "hostname": node.hostname, "fqdn": node.fqdn, "id": node.id})

                        else:
                            print("first else")
                            offline = True
                            nodes.append({"name": node.name, "approved": node.approved, "ip": node.ip,
                                          "hostname": node.hostname, "fqdn": node.fqdn, "id": node.id, "offline": offline})
                    else:
                        print("second else")
                        offline = True
                        nodes.append({"name": node.name, "approved": node.approved, "ip": node.ip,
                                      "hostname": node.hostname, "fqdn": node.fqdn, "id": node.id, "offline": offline})
                context["nodes"] = nodes
                return render(request, 'nodes/approved_index.html', context)
            else:
                context["not_a_single_client"] = True
                messages.error(request, "no client detected.Did you forget to approve them ??? Go to settings->Unapproved "
                                        "nodes to approve them")
                return render(request, 'nodes/approved_index.html', context)
        else:
            return redirect('login')


    def post(self, request):
        pass


class Realtime_graphs(View):
    def get(self, request, id):
        nodes = Nodes.objects.filter(id=id).values(
            "ip", "hostname", "fqdn", "id", "port").first()
        context = context_processors.base_variables_all(request)
        context["node"] = nodes
        context["ip"] = nodes["ip"]
        if request.is_ajax():
            try:
                url = 'http://%s:%s/system/statistics' % (nodes["ip"], nodes["port"])
                response = CreateConnection.connect(request, url)
                djson = response.json()
            except ValueError as e:
                djson = ast.literal_eval(response.content.decode())
            except Exception as e:
                return JsonResponse(e)

            return JsonResponse(djson)
        else:
            try:
                url = 'http://%s:%s/system/statistics' % (nodes["ip"], nodes["port"])
                data = CreateConnection.connect(request, url)
                djson = data.json()
            except ValueError as e:
                djson = ast.literal_eval(data.content.decode())
            except Exception as e:
                return render(request, 'nodes/realtime_graphs.html', context)

            context["data"] = djson
            context["cpu_num"] = len(djson["cpu_usage"])
            return render(request, 'nodes/realtime_graphs.html', context)


class Node_detail(View):
    def get(self, request, id):
        context = context_processors.base_variables_all(request)
        context["id"] = id
        context["metrics_nodes"] = Nodes.objects.filter(id=id).values("name","ip").first()
        return render(request, 'nodes/node_details.html', context)

    def post(self, request):
        cluster_id = str(request.session[str(request.session['user'])])
        nodes = Nodes.objects.filter(id=request.POST["node_id"]).values("ip", "hostname", "fqdn", "id", "port").first()
        ip = nodes["ip"]
        context = context_processors.base_variables_all(request)
        context["node"] = nodes
        context["ip"] = ip
        url = 'http://%s:%s/system/statistics/history/' % (ip, nodes["port"])
        current_time = datetime.now().replace(microsecond=0)
        # current_time = datetime.today().replace(microsecond=0)

        format = "%b-%d %H:%M"
        if request.POST['data_type'] == 'day':
            date = request.POST['data_value']
            start_date = current_time - timedelta(days=int(date))

            payload = {'days': date}
        else:
            time = request.POST['data_value']
            start_date = current_time - timedelta(hours=int(time))
            payload = {'time': request.POST['data_value']}
            format = "%H:%M %p"

        data = CreateConnection.connect(request, url, payload, True)
        try:
            djson = data.content.decode()
            djson = ast.literal_eval(djson)
        except ValueError as e:
            djson = data.json()
        except Exception as e:
            return JsonResponse(
                {"success": 0, "msg": ["We encountered some problem connecting to client on this node"]}, safe=False)

        if "success" in djson and djson["success"] == 0:
            return JsonResponse(djson, safe=False)

        e, d, h, sm, vm, nbw, diol, dul, p, dt = [], [], [], [], [], [], [], [], [], []

        vm_shared, vm_used, vm_free, vm_available, vm_total, vm_buffer, vm_cache = [], [], [], [], [], [], []
        sm_total, sm_used, sm_free = [], [], []
        dio_write_count, dio_read_count, dio_read_time, dio_write_time = [], [], [], []
        du_disk_free, du_disk_percentage, du_disk_used, du_disk_total = [], [], [], []
        n_bytes_sent, n_packet_sent, n_packet_received, n_bytes_received, n_d_list = [], [], [], [], []

        data = sorted(djson["final_data"], key=itemgetter('time'))
        for a in data:
            abcd = datetime.utcfromtimestamp(a["time"])
            category = abcd.strftime(format)
            if abcd >= start_date:
                p = a["data"]["processes"]
                dt.append(category)
                d = a["data"]["cpu_usage"]
                r = a["data"]["memory_usage"]["swap_memory_usage"]
                t = a["data"]["memory_usage"]["virtual_memory_usage"]
                n_d_list.append(a["data"]["network_bandwidth"])
                dio_d = a["data"]["disk_io"]
                du_d = a["data"]["disk_usage"]
                vm_shared.append(t["shared"])
                vm_used.append(t["used"])
                vm_free.append(t["free"])
                vm_available.append(t["available"])
                vm_total.append(t["total"])
                vm_buffer.append(t["buffer"])
                vm_cache.append(t["cached"])

                sm_total.append(r["total"])
                sm_used.append(r["used"])
                sm_free.append(r["free"])

                dio_write_count.append(dio_d["write_count"] / 1000000)
                dio_read_count.append(dio_d["read_count"] / 1000000)
                dio_read_time.append(dio_d["read_time"]/600000)
                dio_write_time.append(dio_d["write_time"]/600000)

                du_disk_free.append(du_d["disk_free"])
                du_disk_percentage.append(du_d["disk_percentage"])
                du_disk_used.append(du_d["disk_used"])
                du_disk_total.append(du_d["disk_total"])
                e.append(d)

# code for network starts here
        r = []
        l1 = n_d_list
        if l1:
            len_l1 = len(l1)
            len_inf = len(l1[0])
            x = [[[] * len_l1, [] * len_l1] for i in range(len_inf)]
            q = []
            i = 0
            for a in range(0, len(l1)):
                for b in range(0, len(l1[a])):
                    for k, v in l1[a][b].items():# Interface
                        if k not in q:
                            q.append(k)
                        x[i][0].append(v["bytes_sent"])
                        x[i][1].append(v["bytes_recv"])
                    i = i + 1
                i = 0

            n_bytes_sent_diff, n_bytes_received_diff = [], []
            dividend = 1000
            for i in range(0, len(x)):
                for j in range(1, len(x[i][0])):
                    if j < len(x[i][0]):
                        dtl = abs((x[i][0][j] - x[i][0][j - 1]))
                        if dtl >= 1000 and dtl <= 1000000:
                            dividend = 1000
                        elif dtl >= 3000000:
                            dividend = 3000000
                        n_bytes_sent_diff.append(dtl/dividend)
                for j in range(1, len(x[i][1])):
                    if j < len(x[i][1]):
                        dtl = abs((x[i][1][j] - x[i][1][j - 1]))
                        if dtl >= 1000 and dtl <= 1000000:
                            dividend = 1000
                        elif dtl >= 3000000:
                            dividend = 3000000
                        n_bytes_received_diff.append(dtl/dividend)

                g = [{
                    "label": "bytes_sent",
                    "data": n_bytes_sent_diff,
                    "pointRadius": 0,
                    "borderColor": "rgba(" + str(randint(0, 255)) + "," + str(randint(0, 255)) + "," + str(
                        randint(0, 255)) + ",1)"
                },
                    {
                        "label": "bytes_recv",
                        "data": n_bytes_received_diff,
                        "pointRadius": 0,
                        "borderColor": "rgba(" + str(randint(0, 255)) + "," + str(randint(0, 255)) + "," + str(
                            randint(0, 255)) + ",1)"
                    }]

                r.append({q[i]: g})
                n_bytes_sent_diff, n_bytes_received_diff = [], []
# code for network ends here

        z = []
        hidden = False
        for a in range(len(d)):
            for c in range(len(e)):
                z.append(e[c][a])
            g = {
                "label": "CPU " + str(a),
                "data": z,
                "hidden": hidden,
                "pointRadius": 0,
                "borderColor": "rgba(" + str(randint(0, 255)) + "," + str(randint(0, 255)) + "," + str(
                    randint(0, 255)) + ",1)"
            }
            hidden = True
            z = []
            h.append(g)
        cursor = connection.cursor()
        import time
        start_date = str(time.mktime(start_date.timetuple())).split(".")[0]
        current_time = str(time.mktime(current_time.timetuple())).split(".")[0]

        sql = "select st.table_name,st.metrics_table from administer_services as s join service_table_ref as st " \
              "on s.id=st.service_id join administer_service_cluster_reference as ads " \
              "on s.id=ads.service_id where ads.cluster_id_id='" + cluster_id + "'"

        cursor.execute(sql)
        tables = cursor.fetchall()
        service_data = []
        for table in tables:
            sql = "select sm.* from " + table[0] + " as s join " + table[1] + " as sm on s.id=sm.node_id " \
                  + " and s.ip='" + ip + "'" \
                 " and sm.updated_at >='" + str(start_date) +\
                  "' and sm.updated_at <= '" + str(current_time) + "'"
            cursor.execute(sql)
            colnames = [desc[0] for desc in cursor.description]
            colnames.remove("id")
            colnames.remove("node_id")
            a = cursor.fetchall()
            z = []
            w = []
            date_l = []
            date = []
            if a:
                # hidden = False
                for i in range(len(colnames)):
                    if colnames[i] == "updated_at":
                        for j in range(len(a)):
                            pop_column = list(a[j])
                            pop_column.pop(0)
                            category = datetime.utcfromtimestamp(pop_column[i]).strftime(format)
                            date.append(category)

                        date_l.append(date)
                        date = []
                    else:
                        for j in range(len(a)):
                            pop_column = list(a[j])
                            pop_column.pop(0)
                            z.append(pop_column[i])

                        g = {
                            "label": colnames[i],
                            "data": z,
                            # "hidden": hidden,
                            "pointRadius": 0,
                            "borderColor": "rgba(" + str(randint(0, 255)) + "," + str(randint(0, 255)) + "," + str(
                                randint(0, 255)) + ",1)"
                        }
                        z = []
                        w.append(g)
                    # hidden = True
                service_data.append({table[0]: [date_l[0], w]})

        return JsonResponse({"date": dt, "cpu": h, "vm_shared": vm_shared, "vm_used": vm_used, "vm_free": vm_free,
                             "vm_available": vm_available, "vm_total": vm_total, "vm_buffer": vm_buffer,
                             "vm_cache": vm_cache, "sm_total": sm_total, "sm_used": sm_used, "sm_free": sm_free,
                             "dio_write_count": dio_write_count, "dio_read_count": dio_read_count,
                             "dio_read_time": dio_read_time, "dio_write_time": dio_write_time,
                             "du_disk_free": du_disk_free,
                             "du_disk_percentage": du_disk_percentage,
                             "du_disk_used": du_disk_used,
                             "du_disk_total": du_disk_total,
                             "network":r,
                             "process": p, "service_data": service_data
                             }, safe=False)


class Edit_node(View):

    def get(self, request, id):
        context = context_processors.base_variables_all(request)
        nodes = Nodes.objects.filter(approved=0).all()

        context['nodes'] = nodes
        cluster_id = str(request.session[str(request.session['user'])])
        edit_node = Nodes.objects.get(id=id)
        context["edit_node"] = edit_node
        context["edit_cluster"] = Clusters.objects.get(id=cluster_id)

        return render(request, 'nodes/edit_nodes.html', context)

    def post(self, request, id):
        node_ip = request.POST["node_ip"]
        node_hostname = request.POST["hostname"]
        node_name = request.POST["name"]
        node_fqdn = request.POST["fqdn"]
        assoc_ip = Nodes.objects.filter(id=id).values("ip").first()["ip"]
        edited_ip = Nodes.objects.filter(ip=node_ip).exists()
        if assoc_ip != node_ip:
            if edited_ip:
                messages.error(request, "node with this ip already exists")
                return redirect("edit_node", id)

        try:
            edit_node = Nodes.objects.get(id=id)
            edit_node.ip = node_ip
            edit_node.hostname = node_hostname
            edit_node.name = node_name
            edit_node.fqdn = node_fqdn
            edit_node.save()
            messages.success(request, "node succesfully updated")
        except Exception as e:
            messages.error(request, str(e))

        return redirect("list_nodes")


class UnApproved_nodes(View):
    def get(self, request):
        context = context_processors.base_variables_all(request)
        nodes = Nodes.objects.filter(approved=0).all()

        if not nodes:
            messages.info(request, "No nodes to approve right now")
        else:
            context['nodes'] = nodes

        return render(request, 'nodes/unapproved_index.html', context)

    def post(self, request):
        pass


class ToggleApprove_nodes(View):

    def get(self, request):
        pass

    def post(self, request):
        if 'status' in request.POST:
            status = request.POST["status"]
        else:
            data = {'result': 0, "msg": 'node approval status is not set.Please refresh the page and try again'}
            return JsonResponse(data)

        if 'id' in request.POST:
            id = request.POST["id"]
        else:
            data = {'result': 0, "msg": 'Node id is not set.Please refresh the page and try again'}
            return JsonResponse(data)
        if Nodes.objects.filter(id=int(id)).update(approved=int(status)):
            return JsonResponse({'result': 1, 'msg': ''})
        else:
            return JsonResponse({'result': 0, 'msg': 'Sorry !! Due to some error. We are unable to perform the request.'
                                                     'Please refresh the page and try again'})

class CreateConnection:

    @staticmethod
    def connect(request, url, payload=None, post=None):
        data = ""
        try:
            if post:
                data = requests.post(url, headers={"API-KEY": helper.get_api_key()}, data=json.dumps(payload))
            else:
                data = requests.get(url, headers={"API-KEY": helper.get_api_key()}, data=payload)
        except requests.exceptions.HTTPError as e:
            messages.error(request, e)
            return e.args
        except requests.exceptions.ConnectionError as e:
            messages.error(request, e)
            return e.args
        except requests.exceptions.RequestException as e:
            messages.error(request, e)
            return e.args
        except requests.exceptions.ReadTimeout as e:
            messages.error(request, e)
            return e.args

        return data
