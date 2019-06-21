FROM docker.elastic.co/elasticsearch/elasticsearch-oss:6.6.1
COPY config/elasticsearch.yml /usr/share/elasticsearch/config/
ENV DISCOVERY_SERVICE elasticsearch-discovery
ENV HTTP_CORS_ENABLE true
ENV HTTP_CORS_ALLOW_ORIGIN *
ENV MAX_LOCAL_STORAGE_NODES 3
COPY config/custom-entrypoint.sh /custom-entrypoint.sh
RUN chmod -v +x /custom-entrypoint.sh

ENTRYPOINT ["/custom-entrypoint.sh"]
CMD ["eswrapper"]