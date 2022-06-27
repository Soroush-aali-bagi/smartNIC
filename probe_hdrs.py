from scapy.all import *

TYPE_PROBE = 0x812

class Probe(Packet):
   fields_desc = [ BitField("tenant", 0, 6),
                   BitField("bos", 0, 2)]

class PProbe(Packet):
   fields_desc = [ BitField("nicid", 0, 8)]
                   
class ProbeData(Packet):
   fields_desc = [ BitField("congestion", 0, 1),
                   BitField("table_miss", 0, 1),
                   BitField("swid", 0, 6),
                   BitField("first_destination", 0, 32),#IntField
                   BitField("ingress_time", 0, 48)] #11B
   
bind_layers(Ether, Probe, type=TYPE_PROBE)
bind_layers(Probe, IP, bos=0)
bind_layers(Probe, ProbeData, bos=1)
bind_layers(Probe, PProbe, bos=2)
bind_layers(ProbeData, IP)
bind_layers(PProbe, IP)

