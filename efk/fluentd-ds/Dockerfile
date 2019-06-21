FROM fluent/fluentd:v0.12
USER root
RUN apk add --update --virtual .build-deps \
        sudo build-base ruby-dev \
 # cutomize following instruction as you wish
 && sudo -u root  gem install fluent-plugin-kubernetes_metadata_filter
EXPOSE 24224