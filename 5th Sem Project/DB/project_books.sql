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
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `books` (
  `ISBN` int NOT NULL,
  `title` varchar(100) NOT NULL,
  `price` int NOT NULL,
  `genre` varchar(20) NOT NULL,
  `publisher_name` varchar(100) NOT NULL,
  PRIMARY KEY (`ISBN`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES (123,'To Kill a Mockingbird',700,'Classic','Hachette Livre'),(124,'1984',750,'Classic','McGraw-Hill Education'),(125,'Romeo and Juliet',500,'Classic','Scholastic'),(126,'Orwell',800,'Classic','Hachette Livre'),(127,'The Lion And The Mouse',700,'Fiction','Hachette Livre'),(128,'The Fox and The Grapes',650,'Fiction','Houghton Mifflin Harcourt'),(129,'Hansel and Gretel',500,'Fiction','Penguin Random House'),(130,'The Shining',600,'Horror','McGraw-Hill Education'),(131,'The Conjuring',800,'Horror','Scholastic'),(132,'The Exorcist',1000,'Horror','Houghton Mifflin Harcourt'),(133,'It',760,'Horror','Hachette Livre'),(134,'V for Vendetta',850,'Comic','Penguin Random House'),(135,'Batman: The Dark Knight Returns',700,'Comic','Houghton Mifflin Harcourt'),(136,'Saga',650,'Comic','Hachette Livre'),(137,'Dragon Ball Super',550,'Comic','Scholastic'),(138,'Hamlet',700,'Drama','Penguin Random House'),(139,'Waiting For Godot',850,'Drama','Houghton Mifflin Harcourt'),(140,'The Crucible',900,'Drama','McGraw-Hill Education'),(141,'Sherlock Holmes',950,'Crime','Houghton Mifflin Harcourt'),(142,'And There Were None',650,'Crime','Houghton Mifflin Harcourt'),(143,'Murder on The Orient Express',750,'Crime','Penguin Random House'),(144,'Scranton Strangler',650,'Crime','Hachette Livre'),(145,'The Titanic',600,'Classic','Penguin Random House'),(146,'Threat Level Midnight',700,'Fiction','Houghton Mifflin Harcourt'),(147,'The Halloween',500,'Horror','Scholastic'),(148,'Superman',450,'Comic','McGraw-Hill Education'),(149,'The Office',400,'Drama','Scholastic'),(150,'The JBL',500,'Crime','Houghton Mifflin Harcourt'),(151,'Game Of Thrones',550,'Classic','Scholastic'),(152,'Ford vs Ferrari',450,'Fiction','Penguin Random House'),(153,'The Circus',650,'Horror','Houghton Mifflin Harcourt'),(154,'The Mighty',700,'Comic','McGraw-Hill Education');
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,STRICT_ALL_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ALLOW_INVALID_DATES,ERROR_FOR_DIVISION_BY_ZERO,TRADITIONAL,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `books_BEFORE_INSERT` BEFORE INSERT ON `books` FOR EACH ROW BEGIN
IF (NEW.ISBN <99 OR NEW.ISBN > 999)
        THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Invalid ISBN';
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-28 11:01:25
