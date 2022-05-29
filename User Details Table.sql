CREATE DATABASE  IF NOT EXISTS `mydata` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `mydata`;
-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: localhost    Database: mydata
-- ------------------------------------------------------
-- Server version	8.0.29

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
-- Table structure for table `userdetails`
--

DROP TABLE IF EXISTS `userdetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `userdetails` (
  `firstname` varchar(200) NOT NULL,
  `lastname` varchar(200) DEFAULT NULL,
  `rollnumber` varchar(200) NOT NULL,
  `password` varchar(200) DEFAULT NULL,
  `securityquestion` varchar(200) DEFAULT NULL,
  `securityanswer` varchar(200) DEFAULT NULL,
  `department` varchar(200) DEFAULT NULL,
  `course` varchar(200) DEFAULT NULL,
  `semester` varchar(200) DEFAULT NULL,
  `year` varchar(200) DEFAULT NULL,
  `professor` varchar(200) DEFAULT NULL,
  `photo` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`rollnumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userdetails`
--

LOCK TABLES `userdetails` WRITE;
/*!40000 ALTER TABLE `userdetails` DISABLE KEYS */;
INSERT INTO `userdetails` VALUES ('stuti','aswani','1','stuti1','What is your middle name?','pradeep','AIDE','ML','2','AY 22-23','abc',NULL),('yash','bhargava','2','yash1','Which city were you born in?','bhopal','AIDE','WebDev','2','AY 22-23','acb',NULL),('satya','nadella','3','satya','What was the name of your first pet?','a','CSE','DSA','2','AY 21-22','abc',NULL),('mark','zuckerberg','4','mark','What was the name of your first pet?','b',NULL,NULL,NULL,NULL,NULL,NULL),('sundar','','5','sundar','What was the name of your first pet?','c',NULL,NULL,NULL,NULL,NULL,NULL),('sakshi','aswani','6','sakshi','Which city were you born in?','ajmer','CSE','DSA','1','AY 21-22','a',NULL);
/*!40000 ALTER TABLE `userdetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'mydata'
--

--
-- Dumping routines for database 'mydata'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-29 15:04:22
