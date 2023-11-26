#!/bin/bash
echo "#Cloudflare" > ./Nginx/cfg/cloudflare_ip.conf;
for i in `curl https://www.cloudflare.com/ips-v4`; do
        echo "set_real_ip_from $i;" >> ./Nginx/cfg/cloudflare_ip.conf;
done
for i in `curl https://www.cloudflare.com/ips-v6`; do
        echo "set_real_ip_from $i;" >> ./Nginx/cfg/cloudflare_ip.conf;
done

echo "" >> ./Nginx/cfg/cloudflare_ip.conf;
echo "real_ip_header CF-Connecting-IP;" >> ./Nginx/cfg/cloudflare_ip.conf;

