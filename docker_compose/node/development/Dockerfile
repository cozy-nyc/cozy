FROM node:latest


WORKDIR /exchange/frontend
COPY ./frontend /exchange/frontend

RUN npm install && npm run build-development

COPY ./docker_compose/node/development/start.sh /start.sh
RUN sed -i 's/\r//' /start.sh
RUN chmod +x /start.sh
