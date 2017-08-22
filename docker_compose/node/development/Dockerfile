FROM node:latest



COPY ./frontend /exchange/frontend
WORKDIR /exchange/frontend

RUN npm install && npm run build-development

COPY ./docker_compose/node/development/start.sh /start.sh
RUN sed -i 's/\r//' /start.sh
RUN chmod +x /start.sh
