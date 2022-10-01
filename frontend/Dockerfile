# build stage
FROM node:lts-alpine as build-stage

WORKDIR frontend

COPY ./frontend/package.json ./package.json
COPY ./frontend/package-lock.json ./package-lock.json

RUN npm install

COPY ./frontend .

EXPOSE 8080

RUN npm run build

CMD ["npm", "run", "dev", "--", "--port", "8080", "--host"]

# production stage
#FROM nginx:stable-alpine as production-stage
#
#COPY --from=build-stage /frontend/dist /usr/share/nginx/html
#
#EXPOSE 80
#
#CMD ["npm", "run", "serve"]
#CMD ["nginx", "-g", "daemon off;"]