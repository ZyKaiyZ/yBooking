# yBooking

yBooking is a small project designed to provide a booking platform with basic functionality. Users can browse available listings, make bookings, and manage their own listings. This repository serves as a starting point for building a booking platform.

## Features

* User registration and login
* Browsing and searching for available accommodations
* Viewing detailed information about accommodations
* Booking accommodations
* Publishing and managing accommodation listings
* Managing favorite accommodations
* Managing and canceling bookings
* Password recovery via email

## Execution

To run yBooking on your localhost, follow these steps:

1. Create a file named `.env` in the `./yBooking-Backend/` directory and set your environment variables as shown below:

   ```plaintext
   # DB config
   DB_HOST=db
   DB_PORT=3306
   DB_USER=<YOUR-DB-USER>
   DB_PASSWORD=<YOUR-DB-PASSWORD>
   DB_NAME=<YOUR-DB-NAME>

   # MAIL config
   MAIL_SERVER=<YOUR-SMTP-SERVER>
   MAIL_PORT=<YOUR-SMTP-PORT>
   MAIL_USE_TLS=True
   MAIL_USERNAME=<YOUR-SMTP-USERNAME>
   MAIL_PASSWORD=<YOUR-SMTP-PASSWORD>
   MAIL_DEFAULT_SENDER=noreply@ybooking.com
   ```

   Replace `<YOUR-DB-USER>`, `<YOUR-DB-PASSWORD>`, `<YOUR-DB-NAME>`, `<YOUR-SMTP-SERVER>`, `<YOUR-SMTP-PORT>`, `<YOUR-SMTP-USERNAME>`, and `<YOUR-SMTP-PASSWORD>` with your actual values.
2. If needed, modify the `baseUrl` in `./yBooking-Frontend/main.js` to match your API endpoint. Locate the following line in the file:

   ```javascript
   export const baseUrl = "http://localhost/api";
   ```

   Replace `"http://localhost/api"` with the appropriate base URL for your setup.
3. In the terminal, navigate to the `/yBooking/` directory and execute the `docker_script.sh` file:

   ```plaintext
   sh docker_script.sh
   ```
4. Open your browser and visit `http://localhost` to access the home page. Since there is no data initially, you need to insert data and create a data table in MySQL.
5. To access the phpMyAdmin page, visit `http://localhost:7414`. You can perform database operations here. Login with the username `root` and leave the password field blank, as it is the default account. The server field is unnecessary.
6. Execute the following instructions in the phpMyAdmin SQL query window to create the required data tables in MySQL:

   ```sql
   -- user table
   CREATE TABLE `user` (
     `email` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
     `password` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
     UNIQUE KEY `email` (`email`)
   );

   -- like_list table
   CREATE TABLE `like_list` (
     `product_id` int(100) NOT NULL,
     `user` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL
   );

   -- product_order table
   CREATE TABLE `product_order` (
     `product_id` int(100) NOT NULL,
     `user` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL
   );

   -- products table
   CREATE TABLE `products` (
     `product_id` int(100) NOT NULL,
     `country` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
     `city` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
     `start_date` date NOT NULL,
     `end_date` date NOT NULL,
     `price` int(11) NOT NULL,
     `img` varchar(500) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
     `owner` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
     `del_flag` int(1) NOT NULL DEFAULT '0'
   ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

   ```

7. Finally, visit `http://localhost` in your browser to explore the yBooking website.

By following these instructions, you can set up and run yBooking on your local machine.
