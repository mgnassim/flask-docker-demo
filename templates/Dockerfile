# Use the official Nginx image from Docker Hub
FROM nginx:alpine

# Set the working directory inside the container
WORKDIR /usr/share/nginx/html

# Copy static files into the Nginx directory
COPY . ./

# Set environment variable for Nginx configuration
ENV NGINX_CONF_PATH /etc/nginx/nginx.conf

# Expose port 80 to the outside world
EXPOSE 80
