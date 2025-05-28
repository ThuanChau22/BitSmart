FROM node:lts-alpine AS development
WORKDIR /app
COPY package*.json .
RUN npm ci
COPY . .
CMD ["npx", "ng", "serve", "--host", "0.0.0.0"]

FROM development AS build
RUN npm run build

FROM nginx:stable-alpine
COPY --from=build /app/nginx /etc/nginx/templates
WORKDIR /usr/share/nginx/html
RUN rm -rf ./*
COPY --from=build /app/dist/bitsmart/browser .
CMD ["nginx", "-g", "daemon off;"]
