# compatible php base image for most compose dependencies
FROM php:8.1-apache

# working dir
WORKDIR /var/www/html

# installing php extensions and dependencies
RUN apt-get update && apt-get install -y \
    git \
    unzip \
    libzip-dev \
    && docker-php-ext-install zip pdo_mysql

#This enables apache modules
RUN a2enmod rewrite

# This will Update Apache configuration to serve from /var/www/html/public directory with defined virtual host
COPY apache-config.conf /etc/apache2/sites-available/000-default.conf

# Install Composer dependency manager
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Copy all files to working dir
COPY . /var/www/html

# Install PHP dependencies from compose.json file
RUN composer install

# Setting file permissions
RUN chown -R www-data:www-data /var/www/html
RUN chmod -R 775 /var/www/html/storage

# Expose port 80 for the host
EXPOSE 80

# Start Apache
CMD ["apache2-foreground"]