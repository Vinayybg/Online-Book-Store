CREATE DATABASE  IF NOT EXISTS `project` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `project`;
-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: project
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `date` date NOT NULL,
  `customer_email` varchar(200) NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  KEY `fk_ORDERS_customer1_idx` (`customer_email`),
  CONSTRAINT `fk_ORDERS_customer1` FOREIGN KEY (`customer_email`) REFERENCES `customer` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=9356 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES ('2020-11-21','adarshrai@gmail.com',1234),('2020-12-15','karthiktiwari@gmail.com',1292),('2020-12-15','karthiktiwari@gmail.com',1516),('2020-12-15','karthiktiwari@gmail.com',1699),('2020-12-14','adarshrai@gmail.com',1928),('2020-12-15','karthiktiwari@gmail.com',2110),('2020-12-21','karthiktiwari@gmail.com',2357),('2020-12-21','adarshrai@gmail.com',2728),('2020-12-15','karthiktiwari@gmail.com',2754),('2020-12-21','adarshrai@gmail.com',3673),('2020-12-15','karthiktiwari@gmail.com',4515),('2020-12-21','adarshrai@gmail.com',4650),('2020-12-15','karthiktiwari@gmail.com',5608),('2020-12-15','karthiktiwari@gmail.com',6065),('2020-12-21','karthiktiwari@gmail.com',6258),('2020-12-15','karthiktiwari@gmail.com',6668),('2020-12-21','adarshrai@gmail.com',7352),('2020-12-21','karthiktiwari@gmail.com',8161),('2020-12-21','adarshrai@gmail.com',8260),('2020-12-15','karthiktiwari@gmail.com',8343),('2020-12-21','karthiktiwari@gmail.com',9031),('2020-12-21','karthiktiwari@gmail.com',9355);
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-28 11:01:26
