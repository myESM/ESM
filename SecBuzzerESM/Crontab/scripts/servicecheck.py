import docker
import psutil
import os
from pathlib import Path
from pprint import pprint

# from colorama import Fore, init
# from terminaltables import AsciiTable
client = docker.DockerClient(base_url='unix://var/run/docker.sock')
# docker_table_data = [[], []]
# for _ in client.containers.list(all=True):
#     docker_table_data[0].append(_.name)
#     docker_table_data[1].append(f"{Fore.GREEN if 'run' in _.status else Fore.RED}{_.status}{Fore.RESET}")
# docker_table=AsciiTable(docker_table_data)
# print(docker_table.table)
def bytes2human(n):
    # http://code.activestate.com/recipes/578019
    # >>> bytes2human(10000)
    # '9.8K'
    # >>> bytes2human(100001221)
    # '95.4M'
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value, s)
    return "%sB" % n

data = {}

mem_info = psutil.virtual_memory()
mem = {
    'total': bytes2human(mem_info.total),
    'available': bytes2human(mem_info.available),
    'percent': mem_info.percent}

es_directory = Path('/es_volume/')
es_dir_size = bytes2human(sum(f.stat().st_size for f in es_directory.glob('**/*') if f.is_file()))
fluentd_directory = Path('/fluentd_log/')
fluentd_dir_size = bytes2human(sum(f.stat().st_size for f in fluentd_directory.glob('**/*') if f.is_file()))

data['mem'] = mem
data['containers'] = {container.name: container.status for container in client.containers.list(all=True)}
data['log_size'] = {
    'es_dir_size': es_dir_size,
    'fluentd_dir_size': fluentd_dir_size 
}
pprint(data)

