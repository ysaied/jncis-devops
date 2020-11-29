#!/usr/bin/python2

"""
JET firewall filter example application
"""

from compiled.authentication_service_pb2 import LoginStub, LoginRequest
from compiled.jnx_addr_pb2 import IpAddress
from compiled.firewall_service_pb2 import *
import grpc

DEVICE = "172.25.11.1"
APP_USER = "lab"
APP_PASSWORD = "lab123"
PORT = "32767"
CLIENT_ID = "SampleApp"
IFD_NAME = "ge-0/0/0"
APP_TIMEOUT = 10


def pause():
    raw_input("Press Enter to continue...")


if __name__ == "__main__":
    print "Executing Python app"

    # Create gRPC communication channel
    channel = grpc.insecure_channel(DEVICE + ":" + PORT)

    # Create stub for authentication services
    auth_stub = LoginStub(channel)
    # Authenticate
    login_request = LoginRequest(
        user_name=APP_USER, password=APP_PASSWORD, client_id=CLIENT_ID)

    try:
        login_response = auth_stub.LoginCheck(login_request, APP_TIMEOUT)
    except:
        print "ERROR: gRPC server connection failed!"
        sys.exit()

    if login_response.result is True:
        print "Connected to gRPC Server."
    else:
        print "ERROR: gRPC connection authentication error!"
        sys.exit()

    # Create stub for firewall service
    fw_stub = AclServiceStub(channel)

    # Configure the firewall filter. In this app:
    #  term1: source=IP1, destination=IP2, action=discard
    #  term2: action=accept
    IP1 = IpAddress(addr_string="10.0.0.2")
    IP2 = IpAddress(addr_string="10.0.0.1")
    matchIP1 = AclMatchIpAddress(
        addr=IP1, prefix_len=32, match_op=ACL_MATCH_OP_EQUAL)
    matchIP2 = AclMatchIpAddress(
        addr=IP2, prefix_len=32, match_op=ACL_MATCH_OP_EQUAL)

    term1match1 = AclEntryMatchInet(
        match_src_addrs=[matchIP1], match_dst_addrs=[matchIP2])
    t1 = AclEntryInetTerminatingAction(action_discard=1)
    nt1 = AclEntryInetNonTerminatingAction(
        action_count=AclActionCounter(counter_name="Match1"),
        action_syslog=1, action_log=1, action_sample=1)
    term1Action1 = AclEntryInetAction(action_t=t1, actions_nt=nt1)
    adj = AclAdjacency(type=ACL_ADJACENCY_AFTER)
    term1 = AclInetEntry(
        ace_name="t1", ace_op=ACL_ENTRY_OPERATION_ADD,
        adjacency=adj, matches=term1match1, actions=term1Action1)
    tlist1 = AclEntry(inet_entry=term1)

    term2match1 = AclEntryMatchInet()
    t2 = AclEntryInetTerminatingAction(action_accept=1)
    term2Action1 = AclEntryInetAction(action_t=t2)
    term2 = AclInetEntry(
        ace_name="t2", ace_op=ACL_ENTRY_OPERATION_ADD, adjacency=adj,
        matches=term2match1, actions=term2Action1)
    tlist2 = AclEntry(inet_entry=term2)

    filter = AccessList(
        acl_name="jet-created-filter", acl_type=ACL_TYPE_CLASSIC,
        acl_family=ACL_FAMILY_INET, acl_flag=ACL_FLAGS_NONE,
        ace_list=[tlist1, tlist2])
    print filter

    # Call the API to create the firewall filter
    result = fw_stub.AccessListAdd(filter, APP_TIMEOUT)
    print "\nInvoking fw_stub.AccessListAdd", result
    if result.status is ACL_STATUS_EOK:
        print "AccessListAdd RPC Passed"
    else:
        print "AccessListAdd RPC Failed"

    # Configure filter to attach on 0th IFL in INPUT direction
    bind_obj_point = AccessListBindObjPoint(intf=IFD_NAME + '.0')
    bind = AccessListObjBind(
        acl=filter, obj_type=ACL_BIND_OBJ_TYPE_INTERFACE,
        bind_object=bind_obj_point, bind_direction=ACL_BIND_DIRECTION_INPUT,
        bind_family=ACL_FAMILY_INET)
    # print bind

    # Call the API to bind the interface to a filter
    bindaddresult = fw_stub.AccessListBindAdd(bind, APP_TIMEOUT)
    print "\nInvoking fw_stub.AccessListBindAdd", bindaddresult
    if bindaddresult.status is ACL_STATUS_EOK:
        print "AccessListBindAdd RPC Passed"
    else:
        print "AccessListBindAdd RPC Failed"

    # Wait for the user
    pause()

    # Call the API to unbind the filter from the interface
    binddelresult = fw_stub.AccessListBindDelete(bind, APP_TIMEOUT)
    print "\nInvoking fw_stub.AccessListBindDelete", binddelresult
    if binddelresult.status is ACL_STATUS_EOK:
        print "AccessListBindDelete RPC Passed"
    else:
        print "AccessListBindDelete RPC Failed"

    # Call the API to delete the firewall filter
    filter = AccessList(acl_name="jet-created-filter", acl_family=ACL_FAMILY_INET)
    # print filter
    acldelresult = fw_stub.AccessListDelete(filter, APP_TIMEOUT)
    print "\nInvoking fw_stub.AccessListDelete", acldelresult
    if acldelresult.status is ACL_STATUS_EOK:
        print "AccessListDelete RPC Passed"
    else:
        print "AccessListDelete RPC Failed"
