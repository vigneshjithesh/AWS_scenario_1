#!/bin/bash
# Update and install Apache web server
sudo yum update -y
sudo yum install httpd -y

# Start and enable httpd service
sudo systemctl start httpd
sudo systemctl enable httpd

# Deploy sample website
echo "Deploying E-Commerce website..."
sudo mv index.html /var/www/html/

# Restart service
sudo systemctl restart httpd
echo "Website deployed successfully!"
