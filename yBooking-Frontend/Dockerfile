FROM node:latest as build

WORKDIR /app
COPY package*.json yarn.lock ./
RUN yarn install --frozen-lockfile
COPY . .

RUN yarn run build


FROM nginx:1.19.0-alpine

COPY --from=build /app/dist /usr/share/nginx/html
COPY ./nginx/nginx.conf /etc/nginx/conf.d/default.conf

COPY ./.well-known/pki-validation/5221279AE246D926027FD2533DD94CC4.txt /usr/share/nginx/html/.well-known/pki-validation/

CMD ["nginx", "-g", "daemon off;"]
