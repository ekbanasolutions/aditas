from django.conf.urls import url

from nodes import nodes

urlpatterns = [
    url(r'^list_nodes/$', nodes.Nodes_status.as_view(), name="list_nodes"),
    url(r'^edit_node/(?P<id>\d+)/$', nodes.Edit_node.as_view(), name="edit_node"),
    url(r'^node_details/(?P<id>\d+)/$', nodes.Node_detail.as_view(), name="node_details_one"),
    url(r'^realtime/(?P<id>\d+)/$', nodes.Realtime_graphs.as_view(), name="realtime"),
    url(r'^node_details/$', nodes.Node_detail.as_view(), name="node_details"),
    url(r'^unapproved_nodes/$', nodes.UnApproved_nodes.as_view(), name="unapproved_nodes"),
    url(r'^toggle_approval/$', nodes.ToggleApprove_nodes.as_view(), name="toggle_approval"),
]