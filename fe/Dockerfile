# build stage
FROM node:22-alpine as vite-builder
## Create 'app' folder inside the container use it to run the subsecuent commands from there
WORKDIR /app
## Copy both 'package.json' and 'package-lock.json' (if available)
COPY ./fe/package*.json ./
# install project dependencies
RUN npm install
## copy project files and folders to the current working directory (i.e. 'app' folder)
COPY ./fe ./
## build app for production with minification
RUN npm run build

# production stage
FROM nginx:stable-alpine as production-stage
## Copy build front-end from the 'build stage'
COPY --from=vite-builder /app/dist /usr/share/nginx/html