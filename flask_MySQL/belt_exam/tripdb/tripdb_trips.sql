-- MySQL dump 10.13  Distrib 8.0.12, for macos10.13 (x86_64)
--
-- Host: 127.0.0.1    Database: tripdb
-- ------------------------------------------------------
-- Server version	8.0.12

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `trips`
--

DROP TABLE IF EXISTS `trips`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `trips` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `start_date` varchar(100) DEFAULT NULL,
  `end_date` varchar(100) DEFAULT NULL,
  `plan` text,
  `user_id` int(11) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `destination_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trips`
--

LOCK TABLES `trips` WRITE;
/*!40000 ALTER TABLE `trips` DISABLE KEYS */;
INSERT INTO `trips` VALUES (6,'Jan 1 2019','Jan 31 2019','Go eat lots of kimchi and kkq bbq, visit temples. ',2,'2018-10-19 11:43:59','2018-10-19 11:43:59','Seoul, Korea'),(7,'Feb 1 2019','Feb 28 2019','Visit the pyramids and ride a camel',2,'2018-10-19 11:44:52','2018-10-19 11:44:52','Caro, Egypt'),(8,'March 1, 2019','March 31, 2019','Visit Eifell tower and eat yummy pastries',2,'2018-10-19 11:45:25','2018-10-19 11:45:25','Paris, France'),(9,'Jan 1 2019','Jan 31 2019','Visit awesome museums, ride a scooter. ',3,'2018-10-19 11:46:29','2018-10-19 11:46:29','Rome, Rome'),(10,'Feb 1 2019','Feb 28 2019','play fetch, swim in a beach, enjoy warm weather.',3,'2018-10-19 11:47:22','2018-10-19 11:47:22','Los Angeles, California'),(11,'March 1, 2019','March 31, 2019','eat street food, halong bay, and caves.',3,'2018-10-19 11:47:58','2018-10-19 11:47:58','Hanoi, Vietnam'),(12,'Jan 1 2019','Jan 31 2019','go swimming, eat coconuts nlon',1,'2018-10-19 13:23:46','2018-10-21 16:17:12','Honolulu, Hawaii'),(13,'Feb 1 2019','Feb 28 2019','get tan, see mayan ruins',1,'2018-10-19 13:25:02','2018-10-19 13:25:02','Cancun, Mexico');
/*!40000 ALTER TABLE `trips` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-10-21 16:23:24
