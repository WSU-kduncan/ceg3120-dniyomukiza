## Web Server Documentation

INSTALL,CONTROLSERVICES,LOGS,FIREWALL CONFIGURATION
+    Load balancer will direct request to the appropriate server. Haproxy is the software we will be using to distribute work among servers.
+    Some VPN will behave in same way as proxies but will add extra security features like encryption. 
+  nslookup ip/domain name will print a web ip or the other way around
+  Each service will run processes. Example Apache as service will run processes for each individual web request. Nginx is known to handle the concurrency of these requests.
+  Services control and manage processes. The earlier listen on specific ports of servers
+  __pstree__ : view process tree associated with a service
+  __systemctl__: view services running on a system
+  Most of services are meant to start on boot
+  __systemctl apache2__: Checks status (running, PID, logs)of service.
+  __journalctl -u service name__: lists logs and time stamps
+  __sudo netstat -tunlp__: checks for listening ports and services
+   __sudo netstat -tunlp | grep :22__: If you wanna narrow down to a specific service(ssh in this example)
+    __curl ipinfo.io__: will display your public ip with location,zipcode and timezone