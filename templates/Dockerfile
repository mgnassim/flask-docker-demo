# Use the official Nginx image from Docker Hub
FROM nginx:alpine

# Set the working directory inside the container
WORKDIR /usr/share/nginx/html

# Copy only the necessary files: static files and nginx config
COPY static /usr/share/nginx/html/static
COPY templates/nginx.conf /etc/nginx/nginx.conf

# Expose port 80 to the outside world
EXPOSE 80
