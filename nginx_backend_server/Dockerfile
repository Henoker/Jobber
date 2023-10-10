FROM nginx:1.20.1-alpine
RUN rm /etc/nginx/conf.d/default.conf
RUN mkdir -p /home/app/staticfiles
COPY nginx.conf /etc/nginx/conf.d
