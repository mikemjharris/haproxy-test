FROM haproxy:1.7

RUN mkdir -p /usr/local/etc/haproxy/

ADD haproxy.cfg /usr/local/etc/haproxy/

CMD ["haproxy", "-f", "/usr/local/etc/haproxy/haproxy.cfg"]
