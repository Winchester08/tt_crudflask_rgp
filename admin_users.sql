-- Adminer 4.8.1 MySQL 10.9.2-MariaDB-log dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

DROP TABLE IF EXISTS `admin_users`;
CREATE TABLE `admin_users` (
  `id` int(5) NOT NULL AUTO_INCREMENT,
  `name` varchar(40) NOT NULL,
  `lastname` varchar(40) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `user_type` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=Aria DEFAULT CHARSET=utf8mb4 PAGE_CHECKSUM=1;

INSERT INTO `admin_users` (`id`, `name`, `lastname`, `username`, `password`, `user_type`) VALUES
(5,	'Jonh Rick',	'Jameson',	'ricky',	'us-ADC000',	'sale'),
(8,	'Ernesto',	'Camacho',	'ernest_x',	'us-ADC000',	'sale'),
(3,	'Yazmin',	'Garcia',	'yazmin',	'us-ADC000',	'sales'),
(4,	'Celia',	'Gabbiani',	'celiag',	'us-ADC000',	'administrator'),
(6,	'Rigo',	'Winchester',	'ro',	'us-ADC000',	'Admin'),
(9,	'Armin',	'James',	'armin',	'us-ADC000',	'sale');

-- 2024-05-10 23:18:44
