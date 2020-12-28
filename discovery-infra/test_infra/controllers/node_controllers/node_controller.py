from typing import Dict, List, Any
from test_infra.controllers.node_controllers import node


class NodeController:
    def list_nodes(self) -> Dict[str, node.Node]:
        raise NotImplementedError

    def list_networks(self) -> List[Any]:
        return NotImplementedError

    def list_leases(self, network_name: str) -> List[Any]:
        return NotImplementedError

    def shutdown_node(self, node_name: str) -> None:
        raise NotImplementedError

    def shutdown_all_nodes(self) -> None:
        raise NotImplementedError

    def start_node(self, node_name: str) -> None:
        raise NotImplementedError

    def start_all_nodes(self) -> List[node.Node]:
        raise NotImplementedError

    def restart_node(self, node_name: str) -> None:
        raise NotImplementedError
    
    def format_node_disk(self, node_name: str) -> None:
        raise NotImplementedError

    def format_all_node_disks(self) -> None:
        raise NotImplementedError

    def attach_disk(self, node_name, disk_size):
        """
        Attaches a disk
        :param node_name: Node to attach disk to
        :param disk_size: Size of disk to attach
        :return: Path to the temp disk file and a randomly generated disk alias, to be used later detaching the disk
        """
        raise NotImplementedError

    def detach_disk(self, node_name, disk_alias):
        """
        Detach a disk from a given node
        :param node_name: Node to detach disk from
        :param disk_alias: The alias used to identify the disk to detach (e.g. as
                           returned by attach_disk)
        """
        raise NotImplementedError

    def get_ingress_and_api_vips(self) -> dict:
        raise NotImplementedError

    def destroy_all_nodes(self) -> None:
        raise NotImplementedError

    def prepare_nodes(self):
        pass

    def is_active(self, node_name) -> bool:
        raise NotImplementedError

    def set_boot_order(self, node_name, cd_first=False) -> None:
        raise NotImplementedError

    def set_correct_boot_order_to_all_nodes(self) -> None:
        raise NotImplementedError

    def get_host_id(self, node_name: str) -> str:
        raise NotImplementedError

    def get_cpu_cores(self, node_name: str) -> int:
        raise NotImplementedError

    def set_cpu_cores(self, node_name: str, core_count: int) -> None:
        raise NotImplementedError

    def get_ram_kib(self, node_name: str) -> int:
        raise NotImplementedError

    def set_ram_kib(self, node_name: str, ram_kib: int) -> None:
        raise NotImplementedError