import os
import subprocess
from pathlib import Path
from dotenv import load_dotenv
import re
from typing import List, Optional, Union

load_dotenv()
# TODO: colocar o get e set de device_index no __init__


class Audio_Device():
    def __init__(self, device_name: Optional[str] = None) -> None:
        self.device_name = device_name
        if self.device_name is None:
            self.get_bluetooth_card_name()
        if self.device_name is not None:
            self.set_bluetooth_card_name()

    def get_bluetooth_card_name(self):
        self.device_name = os.environ["device_name"]

    def set_bluetooth_card_name(self):
        """
        Configura um arquivo de ambiente com o nome do dispositivo.
        
        ARGS:
            device_name: Nome do Dispositivo
        
        Returns:
            True
        """
        BASE_PATH = Path(__file__).parents[0]
        with open(f"{BASE_PATH}/.env", "w") as file:
            file.write(f"device_name = {self.device_name}")
        
        return True

    def get_device_id(self):
        try:
            device_name = os.environ["device_name"]
        except KeyError:
            load_dotenv()
            device_name = os.environ["device_name"]
        grep_cmd = f'grep__-B 1__name: <{device_name}>'
        device_index = self.send_command_and_grep(grep_cmd)
        device_index = re.findall(r"\s\d*\n", device_index)[0].strip()
        self.device_index = device_index
    
    def set_device_id(self):
        self.get_device_id()
        BASE_PATH = Path(__file__).parents[0]
        with open(f"{BASE_PATH}/.env", "a") as file:
            file.write(f"\ndevice_index = {self.device_index}")
        return True

    def send_command_and_grep(self, grep_cmd: Union[str, List]):
        cmd = ['pacmd', 'list-cards']
        
        p1 = subprocess.Popen(cmd, stdout=subprocess.PIPE)

        if isinstance(grep_cmd, List):
            for idx, cmds in enumerate(grep_cmd):
                _stdin = p1.stdout
                if idx > 0:
                    _stdin = _p.stdout
                cmds = cmds.split("__")
                _p = subprocess.Popen(cmds, stdin=_stdin, stdout=subprocess.PIPE)
        
            output, _ = _p.communicate()
        
        elif isinstance(grep_cmd, str):
            grep_cmd = grep_cmd.split("__")
            _p = subprocess.Popen(grep_cmd, stdin=p1.stdout, stdout=subprocess.PIPE)
            output, _ = _p.communicate()

        return output.decode()

    def find_device_profile(self):
        """Usa o device_name para buscar as informações do dispositivo."""
        device_name = os.environ["device_name"]

        grep_cmd = ['grep', '-B', '1', '-A', '45', f'name: <{device_name}>']
        print(self.send_command_and_grep(grep_cmd))

    def get_active_profile(self):
        """Usa o device_name para buscar o perfil ativo."""   
        grep_cmd_1 = f'grep__-A 40__index: {self.device_index}'
        grep_cmd_2 = 'grep__active profile'
        active_profile = self.send_command_and_grep([grep_cmd_1, grep_cmd_2])
        return active_profile.strip()

    def set_profile(self):
        profiles = ["a2dp_sink", "handsfree_head_unit"]
        profile = self.get_active_profile()
        old_profile = re.findall(r"<(\w*)>", profile)[0]
        print(profiles)
        profiles.remove(old_profile)
        print(profiles)
        cmd = ['pacmd', 'set-card-profile', self.device_index, profiles[0]]
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        p.communicate()
        print(self.get_active_profile())

    def get_devide_description(self):
        pass

if __name__ == "__main__":
    headset = Audio_Device()
    headset.set_device_id()
    headset.set_profile()
