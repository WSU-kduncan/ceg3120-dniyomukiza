## Web Server Documentation
INSTALL,CONTROLSERVICES,LOGS,FIREWALL CONFIGURATION
+    Load balancer will direct request to the appropriate server. Haproxy is the software we will be using to distribute work among servers.
+    Some VPN will behave in same way as proxies but will add extra security features like encryption. 
+  nslookup ip/domain name will print a web ip or the other way around
+  Each service will run processes. Example Apache as service will run processes for each individual web request. Nginx is known to handle the concurrency of these requests.
+  Services control and manage processes. The earlier listen on specific ports of servers