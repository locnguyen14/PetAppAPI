FROM python:3.8-alpine

# Add scripts to path of running containers
ENV PATH="/scripts:${PATH}" 

COPY ./requirements.txt /requirements.txt 
# Required Alpine packages to install uWSGI
RUN \
    apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .tmp gcc libc-dev linux-headers musl-dev postgresql-dev && \
    apk add libffi-dev && \
    python3 -m pip install -r requirements.txt --no-cache-dir && \
    apk --purge del .tmp

RUN mkdir /app
COPY ./app /app
WORKDIR /app
COPY ./scripts /scripts

# all executable permissions
RUN chmod +x /scripts/*

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

# minimize access
RUN adduser -D user
RUN chown -R user:user /vol
RUN chmod -R 755 /vol/web
USER user

CMD ["entrypoint.sh"]

