# iptalbes

```
# Generated by iptables-save v1.4.7 on Fri Jan 11 19:38:15 2019
*nat
:PREROUTING ACCEPT [764:53104]
:POSTROUTING ACCEPT [61:3685]
:OUTPUT ACCEPT [61:3685]
-A PREROUTING -d 221.23.25.10.18/32 -p tcp -j LOG 
-A PREROUTING -d 221.23.25.10.18/32 -p tcp -m tcp --dport 655 -j LOG 
-A PREROUTING -d 221.23.25.10.18/32 -p tcp -m tcp --dport 338 -j DNAT --to-destination 10.10.16.158:3389 
-A PREROUTING -d 221.23.25.10.18/32 -p tcp -m tcp --dport 338 -j DNAT --to-destination 10.10.16.235:3389 
-A PREROUTING -d 221.23.25.10.18/32 -p tcp -m tcp --dport 655 -j DNAT --to-destination 10.10.16.225:3389 
-A PREROUTING -d 221.23.25.10.18/32 -p tcp -m tcp --dport 338 -m comment --comment "dn" -j DNAT --to-destination 10.10.16.232:3389 
-A POSTROUTING -d 10.10.16.225/32 -j SNAT --to-source 10.88.88.52 
-A POSTROUTING -d 10.10.16.158/32 -p tcp -m tcp --dport 3389 -j SNAT --to-source 10.88.88.52 
-A POSTROUTING -d 10.10.16.235/32 -p tcp -m tcp --dport 3389 -j SNAT --to-source 10.88.88.52 
-A POSTROUTING -d 10.10.16.232/32 -p tcp -m tcp --dport 3389 -j SNAT --to-source 10.88.88.52 
COMMIT
# Completed on Fri Jan 11 19:38:15 2019
# Generated by iptables-save v1.4.7 on Fri Jan 11 19:38:15 2019
*filter
:INPUT ACCEPT [0:0]
:FORWARD ACCEPT [0:0]
:OUTPUT ACCEPT [0:0]

-A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT 
-A INPUT -p tcp -m tcp --dport 80 -j ACCEPT 
-A INPUT -p icmp -j ACCEPT 
-A INPUT -i lo -j ACCEPT 
-A INPUT -p tcp -m state --state NEW -m tcp --dport 22 -j ACCEPT 
-A INPUT -j REJECT --reject-with icmp-host-prohibited 
-A FORWARD -d 10.10.16.235/32 -p tcp -m tcp --dport 3388 -j ACCEPT 
-A FORWARD -m state --state RELATED,ESTABLISHED -j ACCEPT 
-A FORWARD -j REJECT --reject-with icmp-host-prohibited 
-A OUTPUT -j ACCEPT 
COMMIT
# Completed on Fri Jan 11 19:38:15 2019
```