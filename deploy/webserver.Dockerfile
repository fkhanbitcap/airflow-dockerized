FROM puckel/docker-airflow:1.10.9

ARG AIRFLOW_USER_HOME=/usr/local/airflow
ARG PYTHON_DEPS=""

USER root

RUN if [ -n "${PYTHON_DEPS}" ]; then pip install ${PYTHON_DEPS}; fi

RUN curl -sSL https://get.docker.com/ | sh

ADD ./deploy/wrapdocker /usr/local/bin/wrapdocker
RUN chmod +x /usr/local/bin/wrapdocker

WORKDIR ${AIRFLOW_USER_HOME}
ENTRYPOINT ["/entrypoint.sh"]
CMD ["webserver"]