# Use the official Nginx image from Docker Hub
FROM nginx:alpine

# Set the working directory inside the container
WORKDIR /usr/share/nginx/html

# Copy the static website files into the container's Nginx directory
COPY ./frontend/ ./

# Expose port 80 to the outside world
EXPOSE 80

# Nginx will serve the files by default, so no need to specify CMD
# The default CMD in the Nginx base image is already set to start Nginx
