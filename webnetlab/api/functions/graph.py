from pathlib import Path

import yaml

from core.settings import settings


def get_icon_path(kind: str) -> str:
    return "/static/images/" + kind + ".png"


def load_nodes_and_links(lab_name: str) -> tuple or dict:
    path_to_clab_yaml = f"{settings.path_to_lab_files}{lab_name}/{lab_name}.clab.yml"

    try:
        configuration = yaml.safe_load(Path(path_to_clab_yaml).read_text())
    except yaml.YAMLError as e:
        return {"error": "Could not parse lab configuration file, {}".format(e)}

    nodes_info = configuration["topology"]["nodes"]
    links_info = configuration["topology"]["links"]

    return nodes_info, links_info


def create_topology(lab_name: str) -> dict:
    topology = {"nodes": [], "links": []}
    nodes_info, links_info = load_nodes_and_links(lab_name)

    for node in nodes_info:
        topology["nodes"].append({
            "name": node,
            "meta": {
                "kind": nodes_info[node]["kind"],
                "image": nodes_info[node]["image"],
                "mgmt_ip": nodes_info[node]["mgmt_ipv4"],
            },
            "icon": get_icon_path(nodes_info[node]["kind"]),
        })

    for link_dict in links_info:
        link = link_dict["endpoints"]
        end_a, end_z = link
        end_a_host, end_a_src = end_a.split(":")
        end_z_host, end_z_src = end_z.split(":")

        topology["links"].append({
            "source": end_a_host,
            "target": end_z_host,
            "meta": {
                "interface": {
                    "source": end_a_src,
                    "target": end_z_src,
                }
            }
        })

    return topology
