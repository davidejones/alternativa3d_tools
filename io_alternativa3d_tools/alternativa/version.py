from struct import pack, unpack, calcsize
from dataclasses import dataclass


@dataclass
class A3DVersion:
    major: int = 0
    minor: int = 0

    def read(self, file):
        self.major = int(unpack('>H', file.read(calcsize('>H')))[0])
        self.minor = int(unpack('>H', file.read(calcsize('>H')))[0])

    def write(self, file):
        file.write(pack('>H', self.major))
        file.write(pack('>H', self.minor))

    @staticmethod
    def from_file_path(file_path):
        # minor = 0
        # with open(file_path, 'rb') as f:
        #     major = unpack('>H', f.read(calcsize('>H')))[0] & 0x0FFF
        #     if major > 1:
        #         minor = int(unpack('>H', f.read(calcsize('>H')))[0])
        minor = 0
        with open(file_path, 'rb') as f:
            major = unpack('>H', f.read(calcsize('>H')))[0]
        if major != 1:
            # we need to parse v2
            pass
        return A3DVersion(major, minor)

