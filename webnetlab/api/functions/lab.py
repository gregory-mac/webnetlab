import subprocess
from pathlib import Path
import yaml

from core.settings import settings


def scan_for_lab_folders(path: str) -> list[str]:
    lab_list = []
    for lab_dir in Path(path).iterdir():
        if Path.is_dir(lab_dir):
            lab_list.append(str(lab_dir.name))
    return lab_list


def parse_lab_specification(lab_spec_filename: str) -> dict:
    try:
        return yaml.safe_load(Path(lab_spec_filename).read_text())
    except yaml.YAMLError as e:
        return {"error": "Could not parse lab specification file, {}".format(e)}
    except FileNotFoundError as e:
        return {"error": "Could not find lab specification file, {}".format(e)}


def get_node_information(lab_name: str) -> dict:
    path_to_clab_yaml = f"{settings.path_to_lab_files}{lab_name}/{lab_name}.clab.yml"

    try:
        configuration = yaml.safe_load(Path(path_to_clab_yaml).read_text())
    except yaml.YAMLError as e:
        return {"error": "Could not parse lab configuration file, {}".format(e)}

    node_info = {}

    try:
        for node in configuration["topology"]["nodes"]:
            node_info[node] = {}
            node_info[node]["ssh_port"] = f'{settings.server_ip}:{configuration["topology"]["nodes"][node]["ports"][0].split(":")[0]}'
            node_info[node]["kind"] = configuration["topology"]["nodes"][node]["kind"]
            node_info[node]["image"] = configuration["topology"]["nodes"][node]["image"]
        return node_info
    except KeyError:
        pass


def deploy_lab(clab_yml: str):
    cmd = f"sudo containerlab deploy --reconfigure -t {clab_yml}"
    subprocess.run(cmd.split())


def destroy_lab(clab_yml: str):
    cmd = f"sudo containerlab destroy --cleanup -t {clab_yml}"
    subprocess.run(cmd.split())


def check_status():
    cmd = "sudo containerlab inspect --all"
    output = subprocess.run(cmd.split(), capture_output=True)
    if "no containers found" in output.stderr.decode("utf-8"):
        return False
    return True

