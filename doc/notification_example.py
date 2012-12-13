{
  "_context_roles": [
    "admin"
  ],
  "_context_request_id": "req-ce50d8ec-eaf3-40c3-b82b-4fa9674d32e8",
  "_context_quota_class": null,
  "event_type": "scheduler.run_instance.start",
  "_context_service_catalog": null,
  "timestamp": "2012-11-12 02:53:58.438575",
  "_context_auth_token": "bdedeaeddeba430abcea4452a4f4cfeb",
  "_context_instance_lock_checked": false,
  "_context_user_id": "f5f8d00c205741a8afb79da4d7da2ff1",
  "payload": {
    "request_spec": {
      "block_device_mapping": [
      ],
      "image": {
        "status": "active",
        "name": "image_ubuntu",
        "deleted": false,
        "container_format": "ovf",
        "created_at": "2012-10-29T13:54:24.000000",
        "disk_format": "qcow2",
        "updated_at": "2012-10-29T13:57:37.000000",
        "properties": {
          "each_time_info_1351490247": "{u'cache_enable': True, u'user': u'f5f8d00c205741a8afb79da4d7da2ff1', u'time': 1351490247, u'cache_hit': False, 'be_cached': False, u'tenant': u'49d0548301a440f2bb5374b8ceef3a73'}",
          "image_id_sha1": "5e6427e277c75cb4e5fbae4df3a4bd15b524de6d",
          "image_total_info": "{u'store_get': 1, u'used_times': 1}"
        },
        "min_disk": 0,
        "min_ram": 0,
        "checksum": "2a8e5a2e9b320aa5a85e2a1f9332e6f9",
        "owner": "49d0548301a440f2bb5374b8ceef3a73",
        "is_public": true,
        "deleted_at": null,
        "id": "c38e4e61-522c-4b63-8530-b408c328e1bd",
        "size": 437690880
      },
      "instance_type": {
        "memory_mb": 4096,
        "root_gb": 10,
        "deleted_at": null,
        "name": "m1.medium",
        "deleted": false,
        "created_at": null,
        "ephemeral_gb": 40,
        "updated_at": null,
        "disabled": false,
        "vcpus": 2,
        "extra_specs": {
          
        },
        "swap": 0,
        "rxtx_factor": 1.0,
        "is_public": true,
        "flavorid": "3",
        "vcpu_weight": null,
        "id": 1
      },
      "instance_properties": {
        "vm_state": "building",
        "availability_zone": null,
        "ramdisk_id": "",
        "instance_type_id": 1,
        "user_data": null,
        "vm_mode": null,
        "reservation_id": "r-z4s2g8zp",
        "user_id": "f5f8d00c205741a8afb79da4d7da2ff1",
        "display_description": "openstack_heart",
        "key_data": null,
        "power_state": 0,
        "progress": 0,
        "project_id": "49d0548301a440f2bb5374b8ceef3a73",
        "config_drive": "",
        "ephemeral_gb": 40,
        "access_ip_v6": null,
        "access_ip_v4": null,
        "kernel_id": "",
        "key_name": null,
        "display_name": "openstack_heart",
        "config_drive_id": "",
        "architecture": null,
        "root_gb": 10,
        "locked": false,
        "launch_time": "2012-11-12T02:53:58Z",
        "memory_mb": 4096,
        "vcpus": 2,
        "image_ref": "c38e4e61-522c-4b63-8530-b408c328e1bd",
        "root_device_name": null,
        "auto_disk_config": null,
        "os_type": null,
        "metadata": {
          "ori_user": "para",
          "service": "openstack",
          "Para": "for test",
          "resource_id": "DDB"
        }
      },
      "security_group": [
        "default"
      ],
      "instance_uuids": [
        "8d55e4ee-cbaa-49c2-94b2-5cf71b87d348"
      ]
    }
  },
  "_context_project_name": "admin",
  "_context_read_deleted": "no",
  "priority": "INFO",
  "_context_is_admin": true,
  "_context_project_id": "49d0548301a440f2bb5374b8ceef3a73",
  "_context_timestamp": "2012-11-12T02:53:58.170519",
  "_context_user_name": "admin",
  "publisher_id": "scheduler.debian",
  "message_id": "63f2b9ea-16d0-4c8a-9126-e74a9b77c8dd",
  "_context_remote_address": "127.0.0.1"
}