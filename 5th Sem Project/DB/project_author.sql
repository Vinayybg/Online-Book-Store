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
-- Table structure for table `author`
--

DROP TABLE IF EXISTS `author`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `author` (
  `ID` int NOT NULL,
  `name` varchar(100) NOT NULL,
  `book_isbn` int DEFAULT NULL,
  KEY `fk_author_books1_idx` (`book_isbn`),
  CONSTRAINT `fk_author_books1` FOREIGN KEY (`book_isbn`) REFERENCES `books` (`ISBN`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `author`
--

LOCK TABLES `author` WRITE;
/*!40000 ALTER TABLE `author` DISABLE KEYS */;
INSERT INTO `author` VALUES (1456,'Georges Simenon',123),(1456,'Georges Simenon',124),(1456,'Georges Simenon',148),(4365,'Harold Robbins',125),(4365,'Harold Robbins',126),(4365,'Harold Robbins',151),(4561,'Barbara Cartland',127),(4561,'Barbara Cartland',128),(4561,'Barbara Cartland',150),(5432,'Sidney Sheldon',129),(5432,'Sidney Sheldon',130),(5442,'Enid Blyton',131),(5442,'Enid Blyton',132),(5476,'Agatha Christie',133),(5476,'Agatha Christie',134),(5476,'Agatha Christie',135),(5476,'Agatha Christie',149),(6554,'Danielle Steel',136),(6554,'Danielle Steel',137),(6554,'Danielle Steel',138),(6554,'Danielle Steel',147),(6753,'J. K. Rowling',139),(6753,'J. K. Rowling',140),(6753,'J. K. Rowling',141),(6753,'J. K. Rowling',146),(6753,'J. K. Rowling',153),(9857,'William Shakespeare',142),(9857,'William Shakespeare',143),(9857,'William Shakespeare',144),(9857,'William Shakespeare',145),(9857,'William Shakespeare',152),(9857,'William Shakespeare',154);
/*!40000 ALTER TABLE `author` ENABLE KEYS */;
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
