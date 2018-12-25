import hashlib
import json
from administer.models import Nodes, Services
from security.models import Api_key
import requests


class helper:
    def __init__(self, request=None, model=None):
        self.model = model
        self.cluster_id = str(request.session[str(request.session['user'])])
        self.NO_CLIENT = 1
        self.INACTIVE_MASTER = 2

    def clientIsInstalledOnMaster(self):
        master = self.get_active_master()
        s_master = self.get_service_master()
        if master:
            return Nodes.objects.filter(ip=master["ip"]).exists()
        elif s_master:
            print("smaster")
            print(Nodes.objects.filter(ip=s_master["ip"]).exists())
            return Nodes.objects.filter(ip=s_master["ip"]).exists()
        else:
            return False

    def atleast_one_client_is_installed(self):
        return Nodes.objects.filter().exists()

    def get_active_master(self):
        master = self.model.objects.filter(cluster=self.cluster_id, state=1, type=1,status="RUNNING").values("ip", "web_port",
                                                                                               "rpyc_port",
                                                                                               "status","id").first()
        return master

    def get_service_master(self):
        master = self.model.objects.filter(cluster=self.cluster_id,type=1).values("ip", "web_port", "rpyc_port",
                                                                              "status","id").first()
        return master

    def get_standby_master(self):
        standby = self.model.objects.filter(cluster=self.cluster_id, state=0, type=1,status="RUNNING").values("ip", "web_port",
                                                                                                "status","id").first()
        return standby

    def get_all_nodes(self):
        node_data = Nodes.objects.filter(approved=1).all()
        nodes = []
        [nodes.append(node.ip) for node in node_data]
        return nodes


    def get_node_data(self,ip):
        return Nodes.objects.filter(ip=ip).values("name","hostname","port","fqdn").first()

    @staticmethod
    def get_api_key():
        key = Api_key.objects.values()[0]['key']
        api_key = hashlib.md5(key.encode()).hexdigest()
        return api_key

    def stop_service(self,url):
        try:
            r_stop = requests.post(url, headers={"API-KEY": helper.get_api_key()},data=json.dumps({"cluster_id":int(self.cluster_id)}))
            if r_stop.status_code != 200:
                return {'success': 0, 'msg': 'Server returned response %s ' % r_stop.status_code}

        except Exception as e:
            data = {'success': 0,
                    'msg': e.args}
            return data

        return r_stop.json()

    def restart_service(self,url):
        try:
            r = requests.post(url,headers={"API-KEY": helper.get_api_key()},data=json.dumps({"cluster_id":int(self.cluster_id)}))
            if r.status_code != 200:
                return {'success': 0, 'msg': 'Server returned response %s ' % r.status_code}
        except ConnectionError as e:
            data = {'success': 0, 'msg': e.args}
            return data

        if r.json()['success'] == 1:
            return r.json()
        else:
            return r.json()

    def restart_all(self, endpoint, master_ip=None):
        if master_ip is None:
            master = self.get_active_master()
            node = self.get_node_data(master["ip"])
            if master:
                url_restart = 'http://%s:%s/%s' % (master["ip"],node["port"], endpoint)
            else:
                data = {'success': 0, 'msg': 'Sorry there is some problem in your configuration files </b>'}
                return data
        else:
            node = self.get_node_data(master_ip)
            url_restart = 'http://%s:%s/%s' % (master_ip,node["port"], endpoint)
            print(url_restart)
        try:
            r_stop = requests.get(url_restart, headers={"API-KEY": self.get_api_key()})
            # print(r_stop)

            print(r_stop.status_code)
            print(r_stop.content)
            print(r_stop.json())

            response_json = None
            try:
                response_json = json.loads(r_stop.content)
            except TypeError:
                response_json = r_stop.json()
            except Exception as e:
                print(e)

            if r_stop.status_code != 200:
                return {'success': 0, 'msg': 'Server returned response %s ' % r_stop.status_code}
        except ConnectionError as e:
            data = {'success': 0, 'msg': e.args}
            return data
        # return r_stop.json()
        return response_json

    def stop_all(self, endpoint):
        master = self.get_active_master()
        node = self.get_node_data(master["ip"])
        if master:
            url_stop_all = 'http://%s:%s/%s' % (master["ip"], node["port"], endpoint)
        else:
            data = {'success': 0, 'msg': 'Sorry there is some problem in your configuration files </b>'}
            return data

        try:
            print(url_stop_all)
            r_stop = requests.get(url_stop_all, headers={"API-KEY": self.get_api_key()})
            print(r_stop)
            if r_stop.status_code != 200:
                return {'success': 0, 'msg': 'Server returned response %s ' % r_stop.status_code}
        except ConnectionError as e:
            data = {'success': 0, 'msg': e.args}
            return data
        print(r_stop.json())
        return r_stop.json()

    def restart_special_service(self, url):
        master = self.get_active_master()

        if master:
            port = master["rpyc_port"]
            data = {"ip": master["ip"], "port": port,"cluster_id":int(self.cluster_id)}
        else:
            data = {'success': 0, 'msg': 'Sorry there is some problem in your configuration files </b>'}
            return data
        try:
            r = requests.post(url, headers={"API-KEY": helper.get_api_key()},data=json.dumps(data))
            if r.status_code != 200:
                return {'success': 0, 'msg': 'Server returned response %s ' % r.status_code}
        except ConnectionError as e:
            data = {'success': 0, 'msg': e.args}
            return data

        return r.json()

    def stop_special_service(self, url):
        master = self.get_active_master()
        if master:
            # port = master["rpyc_port"]
            data = {"cluster_id":int(self.cluster_id)}
        else:
            data = {'success': 0, 'msg': 'Sorry there is some problem in your configuration files </b>'}
            return data

        try:
            r_stop = requests.get(url, headers={"API-KEY": helper.get_api_key()}, data=json.dumps(data))
            print(r_stop)
            if r_stop.status_code != 200:
                return {'success': 0, 'msg': 'Server returned response %s ' % r_stop.status_code}
        except ConnectionError as e:
            data = {'success': 0, 'msg': e.args}
            return data

        print("stop_special_service ")
        print(r_stop.json())
        return r_stop.json()

    @classmethod
    def get_service_id(cls,service_name):
        return Services.objects.filter(name=service_name).first().id

    @staticmethod
    def stop_remote_service(ip,table_name):
        try:
            node = helper().get_node_data(ip)
            url_restart = 'http://%s:%s/kill/service/' % (ip, node["port"])
            op_status = requests.post(url_restart, headers={"API-KEY": helper.get_api_key()},
                                   data=json.dumps({"table_name": table_name}))
            if op_status.status_code != 200:
                return {'success': 0, 'msg': 'Server returned response %s ' % op_status.status_code}
        except ConnectionError as e:
            data = {'success': 0, 'msg': e.args}
            return data

        return op_status.json()

