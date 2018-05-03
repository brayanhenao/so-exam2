#!/usr/bin/env python

"""
Autor: Brayan Henao
"""

import cli.app
import psutil as psu
from slackclient import SlackClient


@cli.app.CommandLineApp
def automatic_message():
    token = 'xoxp-358505374103-356911436881-357460471010-5b1cd8ac0d38e205656a76269314c67a'
    client = SlackClient(token)
    cpu_usage = psu.cpu_times()
    cpu_percent = psu.cpu_percent(interval=1, percpu=True)
    disk_usage = psu.disk_usage('/')
    memory_virtual = psu.virtual_memory()
    memory_swap = psu.swap_memory()

    cpu = 'CPU INFO: \n' + cpu_usage + '\n' + cpu_percent + '\n\n'
    disk = 'DISK INFO: \n' + disk_usage + '\n\n'
    memory = 'MEMORY INFO: \n' + memory_virtual + '\n' + memory_swap + '\n\n'

    client.api_call(
      "chat.postMessage",
      channel="CAH6V4LR2",
      text=cpu+disk+memory
    )


if __name__ == '__main__':
    automatic_message.run()
