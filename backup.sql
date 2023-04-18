-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: aswangreen
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (5,'adminLvl1'),(1,'dataEntryAdmin'),(4,'fullAdmin'),(3,'ServiceManagerAdmin'),(2,'tahsealAdmin');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=209 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
INSERT INTO `auth_group_permissions` VALUES (1,1,25),(2,1,26),(4,1,28),(5,1,29),(6,1,30),(8,1,32),(9,1,33),(10,1,34),(11,1,35),(12,1,36),(21,1,45),(22,1,46),(24,1,48),(25,1,49),(26,1,50),(28,1,52),(29,1,53),(30,1,54),(32,1,56),(33,1,57),(34,1,58),(36,1,60),(37,1,65),(38,1,66),(39,1,67),(40,1,68),(41,1,69),(42,1,70),(43,1,71),(44,1,72),(45,1,73),(46,1,74),(47,1,75),(48,1,76),(49,1,77),(50,1,78),(51,1,79),(52,1,80),(57,2,81),(58,2,82),(59,2,83),(60,2,84),(62,3,61),(63,3,62),(64,3,63),(61,3,64),(65,4,1),(66,4,2),(67,4,3),(68,4,4),(69,4,5),(70,4,6),(71,4,7),(72,4,8),(73,4,9),(74,4,10),(75,4,11),(76,4,12),(77,4,13),(78,4,14),(79,4,15),(80,4,16),(81,4,17),(82,4,18),(83,4,19),(84,4,20),(85,4,21),(86,4,22),(87,4,23),(88,4,24),(89,4,25),(90,4,26),(91,4,27),(92,4,28),(93,4,29),(94,4,30),(95,4,31),(96,4,32),(97,4,33),(98,4,34),(99,4,35),(100,4,36),(101,4,37),(102,4,38),(103,4,39),(104,4,40),(105,4,41),(106,4,42),(107,4,43),(108,4,44),(109,4,45),(110,4,46),(111,4,47),(112,4,48),(113,4,49),(114,4,50),(115,4,51),(116,4,52),(117,4,53),(118,4,54),(119,4,55),(120,4,56),(121,4,57),(122,4,58),(123,4,59),(124,4,60),(125,4,61),(126,4,62),(127,4,63),(128,4,64),(129,4,65),(130,4,66),(131,4,67),(132,4,68),(133,4,69),(134,4,70),(135,4,71),(136,4,72),(137,4,73),(138,4,74),(139,4,75),(140,4,76),(141,4,77),(142,4,78),(143,4,79),(144,4,80),(145,4,81),(146,4,82),(147,4,83),(148,4,84),(149,5,25),(150,5,26),(151,5,27),(152,5,28),(153,5,29),(154,5,30),(155,5,31),(156,5,32),(157,5,33),(158,5,34),(159,5,35),(160,5,36),(161,5,37),(162,5,38),(163,5,39),(164,5,40),(165,5,41),(166,5,42),(167,5,43),(168,5,44),(169,5,45),(170,5,46),(171,5,47),(172,5,48),(173,5,49),(174,5,50),(175,5,51),(176,5,52),(177,5,53),(178,5,54),(179,5,55),(180,5,56),(181,5,57),(182,5,58),(183,5,59),(184,5,60),(185,5,61),(186,5,62),(187,5,63),(188,5,64),(189,5,65),(190,5,66),(191,5,67),(192,5,68),(193,5,69),(194,5,70),(195,5,71),(196,5,72),(197,5,73),(198,5,74),(199,5,75),(200,5,76),(201,5,77),(202,5,78),(203,5,79),(204,5,80),(205,5,81),(206,5,82),(207,5,83),(208,5,84);
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=85 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add area',7,'add_area'),(26,'Can change area',7,'change_area'),(27,'Can delete area',7,'delete_area'),(28,'Can view area',7,'view_area'),(29,'Can add client',8,'add_client'),(30,'Can change client',8,'change_client'),(31,'Can delete client',8,'delete_client'),(32,'Can view client',8,'view_client'),(33,'Can add contact request types',9,'add_contactrequesttypes'),(34,'Can change contact request types',9,'change_contactrequesttypes'),(35,'Can delete contact request types',9,'delete_contactrequesttypes'),(36,'Can view contact request types',9,'view_contactrequesttypes'),(37,'Can add departement',10,'add_departement'),(38,'Can change departement',10,'change_departement'),(39,'Can delete departement',10,'delete_departement'),(40,'Can view departement',10,'view_departement'),(41,'Can add employee',11,'add_employee'),(42,'Can change employee',11,'change_employee'),(43,'Can delete employee',11,'delete_employee'),(44,'Can view employee',11,'view_employee'),(45,'Can add offers',12,'add_offers'),(46,'Can change offers',12,'change_offers'),(47,'Can delete offers',12,'delete_offers'),(48,'Can view offers',12,'view_offers'),(49,'Can add service',13,'add_service'),(50,'Can change service',13,'change_service'),(51,'Can delete service',13,'delete_service'),(52,'Can view service',13,'view_service'),(53,'Can add simple service',14,'add_simpleservice'),(54,'Can change simple service',14,'change_simpleservice'),(55,'Can delete simple service',14,'delete_simpleservice'),(56,'Can view simple service',14,'view_simpleservice'),(57,'Can add typee',15,'add_typee'),(58,'Can change typee',15,'change_typee'),(59,'Can delete typee',15,'delete_typee'),(60,'Can view typee',15,'view_typee'),(61,'Can add sub service',16,'add_subservice'),(62,'Can change sub service',16,'change_subservice'),(63,'Can delete sub service',16,'delete_subservice'),(64,'Can view sub service',16,'view_subservice'),(65,'Can add request simple service',17,'add_requestsimpleservice'),(66,'Can change request simple service',17,'change_requestsimpleservice'),(67,'Can delete request simple service',17,'delete_requestsimpleservice'),(68,'Can view request simple service',17,'view_requestsimpleservice'),(69,'Can add follow contract services',18,'add_followcontractservices'),(70,'Can change follow contract services',18,'change_followcontractservices'),(71,'Can delete follow contract services',18,'delete_followcontractservices'),(72,'Can view follow contract services',18,'view_followcontractservices'),(73,'Can add contract',19,'add_contract'),(74,'Can change contract',19,'change_contract'),(75,'Can delete contract',19,'delete_contract'),(76,'Can view contract',19,'view_contract'),(77,'Can add contact request',20,'add_contactrequest'),(78,'Can change contact request',20,'change_contactrequest'),(79,'Can delete contact request',20,'delete_contactrequest'),(80,'Can view contact request',20,'view_contactrequest'),(81,'Can add collect order',21,'add_collectorder'),(82,'Can change collect order',21,'change_collectorder'),(83,'Can delete collect order',21,'delete_collectorder'),(84,'Can view collect order',21,'view_collectorder');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$320000$Gga5npZdnRB3Ekq8OeAIJ3$1fLdpBKrJC/pClV8widg67TWOKMCACqShBChyQLCV/k=','2023-03-19 21:27:06.957000',1,'a','','','ahmedsayed124680@gmail.com',1,1,'2023-03-12 22:27:50.459000'),(2,'pbkdf2_sha256$320000$XLw5UoEyB7Ah9kmbrr9002$XuMnLdWtFnPiv6sGY7WK/ybjcs04aSvrf0OEALraFaA=','2023-04-18 01:27:16.807183',0,'dataEntry1','╪┤┘è┘à╪º╪í','┘à╪¡┘à╪»','',1,1,'2023-03-12 22:29:30.000000'),(3,'pbkdf2_sha256$320000$daXZIQueWKLBrWWwPJqWzb$kMZJPRiOUzO/iDLAGE8OtllGYDnrabeSDDVdToq8hSc=','2023-03-17 13:39:30.000000',0,'customerService1','╪│╪º╪▒╪⌐','╪╣╪º╪»┘ä','',1,1,'2023-03-12 22:40:10.000000'),(4,'pbkdf2_sha256$320000$KvxIF01lUurJQZvNiyUVJk$VCDI2P2PoEb2KiO9tHB5YhGi4MfaVdq2u7oPlKxBB7c=',NULL,0,'manager1','┘à╪¡┘à╪»','╪╣┘ä╪º╪í','',1,1,'2023-03-17 13:52:57.000000'),(5,'pbkdf2_sha256$320000$rqAFLZNvR6m1mUBs1ht5dw$EiYX658eg05uJII5AMPeOyiiwlrhPRlJwjAgvh518/4=',NULL,0,'manager2','┘à╪╣╪¬╪▓','╪º╪▒╪¿╪º╪¿','',1,1,'2023-03-17 13:53:16.000000'),(6,'pbkdf2_sha256$320000$0DzdcVFQ6PeWiy2beKIVCT$7E6Yepe5Pu5zoSoX9wu2nTgh9fmS5pGm35uIwE/jM/w=','2023-04-07 21:26:55.964987',1,'aa','','','ahmedsayed143d1@gmail.com',1,1,'2023-04-03 20:45:39.440000'),(7,'pbkdf2_sha256$320000$n6raE6ksJISPxbI7V0ONVB$ZtO6LGUDBW/YxkFI8bvoGVCePCuQrpNk80b1RdN+lAY=','2023-04-18 02:22:06.000000',0,'tahseal1','┘ü┘è╪▒╪º','-','',0,1,'2023-04-06 03:46:23.000000'),(8,'pbkdf2_sha256$320000$Ee5Kl91r0f4qhszCEJYjbX$qDr7BRQzAEhLcW6g18ReYKW2b+P48At+Q1Lq7fuzzBM=',NULL,1,'1','','','asd@asd.com',1,1,'2023-04-09 14:06:44.836159'),(9,'pbkdf2_sha256$320000$4IQxbo0aPgGKn8XSA2acJ1$VwG+gLUrpWWe4kT8A2EqI838bPGquF2gD1YYNh3nk0M=',NULL,1,'aaa','','','asd@asd.com',1,1,'2023-04-09 14:08:01.348667'),(10,'pbkdf2_sha256$320000$IpoHVvEVdaS7uFt1wQl4UQ$fu4JQcAPijFmLJAeA3qSLLlg0EmGvX3IZEql6KaK2uI=',NULL,1,'q','','','ashasmm@asd.com',1,1,'2023-04-09 14:08:50.612061');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
INSERT INTO `auth_user_groups` VALUES (4,2,1),(1,3,1),(3,4,5),(2,5,4),(5,7,2);
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
INSERT INTO `auth_user_user_permissions` VALUES (1,7,81),(2,7,82),(3,7,83),(4,7,84);
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dataentry_area`
--

DROP TABLE IF EXISTS `dataentry_area`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dataentry_area` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `is_deleted` tinyint(1) NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `created_at_date` date DEFAULT NULL,
  `updated_at` datetime(6) DEFAULT NULL,
  `updated_at_date` date DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `counter` int DEFAULT NULL,
  `is_test` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dataentry_area`
--

LOCK TABLES `dataentry_area` WRITE;
/*!40000 ALTER TABLE `dataentry_area` DISABLE KEYS */;
INSERT INTO `dataentry_area` VALUES (1,0,'2022-10-13 16:52:03.000000','2022-10-13','2023-04-07 19:55:45.588165','2023-04-07','┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒',0,1),(2,0,'2023-04-04 00:32:17.000000','2023-04-04','2023-04-07 19:55:45.585237','2023-04-07','╪º┘ä┘à┘à┘è╪▓ 1 ┘ê 2',0,1),(3,0,'2023-04-04 00:32:17.000000','2023-04-04','2023-04-07 19:55:45.580354','2023-04-07','╪º┘ä╪╣┘é╪º╪»',0,1),(4,0,'2023-04-04 00:32:17.000000','2023-04-04','2023-04-07 19:55:45.572014','2023-04-07','╪╣╪¿╪º╪» ╪º┘ä╪▒╪¡┘à┘å ┘ê╪┤╪º╪▒╪╣ ╪º┘ä╪│╪º╪»╪º╪¬',0,1),(5,0,'2023-04-04 00:32:17.000000','2023-04-04','2023-04-07 19:55:45.562246','2023-04-07','╪º┘ä┘à┘é╪º┘ê┘ä┘ê┘å',0,1),(6,0,'2023-04-04 00:32:17.000000','2023-04-04','2023-04-07 19:55:45.547609','2023-04-07','╪«╪º┘ä╪» ╪¿┘å ╪º┘ä┘ê┘ä┘è╪»',0,1),(7,0,'2023-04-04 00:32:17.000000','2023-04-04','2023-04-07 19:55:45.422130','2023-04-07','┘à┘ê┘ä ╪º┘ä╪¡┘â┘è┘à',0,1),(8,0,'2023-04-04 00:32:17.000000','2023-04-04','2023-04-07 19:55:45.418225','2023-04-07','╪¼╪¿┘ä ╪¬┘é┘ê┘é',0,1),(9,0,'2023-04-04 00:32:17.000000','2023-04-04','2023-04-07 19:55:45.416273','2023-04-07','╪º┘ä╪▒╪╢┘ê╪º┘å',0,1),(10,0,'2023-04-04 00:32:17.000000','2023-04-04','2023-04-07 19:55:45.413345','2023-04-07','┘å╪¼╪╣ ╪º┘ä┘à╪¡╪╖╪⌐',0,1),(11,0,'2023-04-04 00:32:17.000000','2023-04-04','2023-04-07 19:55:45.410418','2023-04-07','┘â╪▒┘ê╪▒',0,1),(12,0,'2023-04-04 00:32:17.000000','2023-04-04','2023-04-07 19:55:45.407490','2023-04-07','╪º┘ä╪Ñ╪│┘â╪º┘å ╪º┘ä┘à┘à┘è╪▓',0,1),(13,0,'2023-04-04 00:32:17.000000','2023-04-04','2023-04-07 19:55:45.404561','2023-04-07','╪º┘ä┘à╪¡┘à┘ê╪»┘è╪⌐',0,1);
/*!40000 ALTER TABLE `dataentry_area` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dataentry_client`
--

DROP TABLE IF EXISTS `dataentry_client`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dataentry_client` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `is_deleted` tinyint(1) NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `created_at_date` date DEFAULT NULL,
  `updated_at` datetime(6) DEFAULT NULL,
  `updated_at_date` date DEFAULT NULL,
  `serialNum` int DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `phone` varchar(11) DEFAULT NULL,
  `password` varchar(150) DEFAULT NULL,
  `nationalId` varchar(14) DEFAULT NULL,
  `streetName` varchar(150) DEFAULT NULL,
  `addressBuilding` varchar(150) DEFAULT NULL,
  `addressApartment` varchar(150) DEFAULT NULL,
  `addressDetails` longtext,
  `created_prev_date` date DEFAULT NULL,
  `activation_request` tinyint(1) NOT NULL,
  `outsource` tinyint(1) NOT NULL,
  `is_employee` tinyint(1) NOT NULL,
  `missing_info` tinyint(1) NOT NULL,
  `activation_request_accepted` tinyint(1) NOT NULL,
  `is_test` tinyint(1) NOT NULL,
  `contactMe` varchar(50) DEFAULT NULL,
  `image` varchar(100) NOT NULL,
  `notes` longtext,
  `deserved` int NOT NULL,
  `area_id` bigint DEFAULT NULL,
  `belongs_to_id` bigint DEFAULT NULL,
  `created_by_id` bigint DEFAULT NULL,
  `modified_by_id` bigint DEFAULT NULL,
  `contractDate` date DEFAULT NULL,
  `customFilter` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `serialNum` (`serialNum`),
  KEY `DataEntry_client_belongs_to_id_6940f772_fk_DataEntry_employee_id` (`belongs_to_id`),
  KEY `DataEntry_client_created_by_id_7e64d3d4_fk_DataEntry_employee_id` (`created_by_id`),
  KEY `DataEntry_client_modified_by_id_12bb92c5_fk_DataEntry` (`modified_by_id`),
  KEY `DataEntry_client_area_id_10b253a0_fk_DataEntry_area_id` (`area_id`),
  KEY `DataEntry_client_name_342e1f57` (`name`),
  KEY `DataEntry_client_phone_b914f2f5` (`phone`),
  KEY `DataEntry_client_password_d1c465d4` (`password`),
  KEY `DataEntry_client_nationalId_760ee648` (`nationalId`),
  CONSTRAINT `DataEntry_client_area_id_10b253a0_fk_DataEntry_area_id` FOREIGN KEY (`area_id`) REFERENCES `dataentry_area` (`id`),
  CONSTRAINT `DataEntry_client_belongs_to_id_6940f772_fk_DataEntry_employee_id` FOREIGN KEY (`belongs_to_id`) REFERENCES `dataentry_employee` (`id`),
  CONSTRAINT `DataEntry_client_created_by_id_7e64d3d4_fk_DataEntry_employee_id` FOREIGN KEY (`created_by_id`) REFERENCES `dataentry_employee` (`id`),
  CONSTRAINT `DataEntry_client_modified_by_id_12bb92c5_fk_DataEntry` FOREIGN KEY (`modified_by_id`) REFERENCES `dataentry_employee` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=86 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dataentry_client`
--

LOCK TABLES `dataentry_client` WRITE;
/*!40000 ALTER TABLE `dataentry_client` DISABLE KEYS */;
INSERT INTO `dataentry_client` VALUES (3,0,'2023-04-04 00:32:43.000000','2023-04-04','2023-04-17 15:58:23.343876','2023-04-17',NULL,'╪¡╪│╪º┘à ╪º┘ä╪»┘è┘å ╪╖┘ç ┘à╪¡┘à┘ê╪» ','1227207578',NULL,NULL,NULL,' ╪╣┘à╪º╪▒┘ç 1','╪┤┘é┘ç 7','╪╣┘à╪º┘è╪▒ ┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒ ','2023-01-01',0,0,0,0,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(4,0,'2023-04-04 00:32:43.000000','2023-04-04','2023-04-17 15:58:23.350858','2023-04-17',775,'╪«╪»┘è╪¼┘ç ┘à╪¡┘à╪» ╪¡╪│┘å','1152218744',NULL,NULL,'╪╣┘à╪º┘è╪▒ ┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒','╪╣┘à╪º╪▒┘ç 10','╪╣┘à╪º╪▒┘ç 10','╪╣┘à╪º┘è╪▒ ┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒   - ╪╣┘à╪º╪▒┘ç 10 - ╪╣┘à╪º╪▒┘ç 10','2023-04-09',0,0,0,0,0,1,'0','user_profile_image_placeholer.png','┘à┘ä╪º╪¡╪╕╪⌐ 1 - ┘à┘ä╪º╪¡╪╕╪⌐ 2',260,1,NULL,2,NULL,'2023-04-01',NULL),(5,1,'2023-04-04 00:32:43.000000','2023-04-04','2023-04-07 19:56:44.736863','2023-04-07',743,'┘à╪¡┘à╪» ╪¡╪│┘è┘å ╪╣┘ä┘è ╪¡╪│┘å ','1223520148',NULL,NULL,NULL,'╪╣┘à╪º╪▒┘ç 33','╪┤┘é┘ç 6','┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(6,0,'2023-04-04 00:32:43.000000','2023-04-04','2023-04-17 15:58:23.359836','2023-04-17',744,'┘à╪¡┘à╪» ╪¡╪│┘è┘å ╪╣┘ä┘è ╪¡╪│┘å ','1223520148',NULL,NULL,'┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒','╪╣┘à╪º╪▒┘ç 28','╪┤┘é┘ç 28',' ┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒ - ╪╣┘à╪º╪▒┘ç 28 - ╪┤┘é┘ç 28','2023-04-04',0,0,0,0,0,1,'0','user_profile_image_placeholer.png',NULL,20,1,NULL,2,NULL,NULL,NULL),(7,0,'2023-04-04 00:32:43.000000','2023-04-04','2023-04-17 15:58:23.368810','2023-04-17',695,'╪╡╪º╪¿╪▒ ┘à╪¡┘à╪» ╪╣┘ä┘è ┘à╪¡┘à╪»','1158500999',NULL,NULL,'╪«┘ä┘ü ╪º┘ä╪¿┘å╪▓┘è┘å╪⌐','╪╣┘à╪º╪▒┘ç 39','╪┤┘é┘ç 19',' ╪«┘ä┘ü ╪º┘ä╪¿┘å╪▓┘è┘å╪⌐ - ╪╣┘à╪º╪▒┘ç 39 - ╪┤┘é┘ç 19','2023-04-06',0,0,0,0,0,1,'0','user_profile_image_placeholer.png',NULL,20,1,NULL,2,NULL,NULL,NULL),(8,0,'2023-04-04 00:32:43.000000','2023-04-04','2023-04-17 15:58:23.373796','2023-04-17',145,'╪¡╪│┘å ╪º╪¡┘à╪» ╪▓┘è┘å ╪º┘ä╪╣╪º╪¿╪»┘è┘å ','1226848230',NULL,NULL,'┘à╪»┘è┘å╪⌐ ┘å╪º╪╡╪▒- ╪¿╪│╪º╪▒ ┘à╪º╪▒┘â╪¬ ┘ü╪º┘à┘è┘ä┘ë  ','╪╣┘à╪º╪▒┘ç 5','╪┤┘é┘ç 7',' ┘à╪»┘è┘å╪⌐ ┘å╪º╪╡╪▒- ╪¿╪│╪º╪▒ ┘à╪º╪▒┘â╪¬ ┘ü╪º┘à┘è┘ä┘ë   - ╪╣┘à╪º╪▒┘ç 5 - ╪┤┘é┘ç 7','2023-04-06',0,0,0,0,0,1,'0','user_profile_image_placeholer.png',NULL,20,1,NULL,2,NULL,NULL,NULL),(9,0,'2023-04-04 00:32:43.000000','2023-04-04','2023-04-17 15:58:23.379782','2023-04-17',146,'╪╣┘ä╪º╪í ╪º┘ä╪»┘è┘å ╪º╪¡┘à╪» ╪╣╪¿╪» ╪º┘ä┘à╪╣╪╖┘ë ','1121552425',NULL,NULL,'┘à╪»┘è┘å╪⌐ ┘å╪º╪╡╪▒ ┘è╪│╪º╪▒ ┘à╪º╪▒┘â╪¬ ┘ü╪º┘à┘è┘ä┘ë ','╪╣┘à╪º╪▒┘ç 15','╪┤┘é┘ç 9',' ┘à╪»┘è┘å╪⌐ ┘å╪º╪╡╪▒ ┘è╪│╪º╪▒ ┘à╪º╪▒┘â╪¬ ┘ü╪º┘à┘è┘ä┘ë  - ╪╣┘à╪º╪▒┘ç 15 - ╪┤┘é┘ç 9','2023-04-06',0,0,0,0,0,1,'0','user_profile_image_placeholer.png',NULL,20,1,NULL,2,NULL,NULL,NULL),(10,0,'2023-04-04 00:32:43.000000','2023-04-04','2023-04-17 15:58:23.383769','2023-04-17',492,'╪▓┘è╪º╪» ╪│╪╣╪» ╪▓╪╣┘ä┘ê┘ä ','1116112775',NULL,NULL,'┘à╪»┘è┘å╪⌐ ┘å╪º╪╡╪▒ ','╪╣┘à╪º╪▒┘ç 5','╪┤┘é┘ç 6',' ┘à╪»┘è┘å╪⌐ ┘å╪º╪╡╪▒  - ╪╣┘à╪º╪▒┘ç 5 - ╪┤┘é┘ç 6','2023-04-06',0,0,0,0,0,1,'0','user_profile_image_placeholer.png',NULL,20,1,NULL,2,NULL,NULL,NULL),(11,0,'2023-04-04 00:32:43.000000','2023-04-04','2023-04-17 15:58:23.387759','2023-04-17',493,'┘ç╪¿╪⌐ ╪╣╪┤╪▒┘ë ╪▒╪º╪╢┘ë ╪º┘ä┘à┘ç╪»┘ë','1153598639',NULL,NULL,'╪«┘ä┘ü ╪º┘ä╪¼╪▒╪º╪¼','╪╣┘à╪º╪▒╪⌐ 3','╪┤┘é┘ç 4',' ╪«┘ä┘ü ╪º┘ä╪¼╪▒╪º╪¼ - ╪╣┘à╪º╪▒╪⌐ 3 - ╪┤┘é┘ç 4','2023-04-06',0,0,0,0,0,1,'0','user_profile_image_placeholer.png',NULL,20,1,NULL,2,NULL,NULL,NULL),(12,0,'2023-04-04 00:32:43.000000','2023-04-04','2023-04-17 15:58:23.392745','2023-04-17',494,'┘à╪¡┘à╪» ╪╣╪¿╪» ╪º┘ä╪╣╪▓┘è╪▓ ╪º╪¡┘à╪» ','1149657546',NULL,NULL,'╪º┘ä╪»┘ê╪▒ ╪º┘ä╪½╪º┘ä╪½ ╪«┘ä┘ü ╪º┘ä╪¿┘å╪▓┘è┘å╪⌐','╪╣┘à╪º╪▒┘ç 5','╪┤┘é┘ç 6',' ╪º┘ä╪»┘ê╪▒ ╪º┘ä╪½╪º┘ä╪½ ╪«┘ä┘ü ╪º┘ä╪¿┘å╪▓┘è┘å╪⌐ - ╪╣┘à╪º╪▒┘ç 5 - ╪┤┘é┘ç 6','2023-04-06',0,0,0,0,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,2,NULL,NULL,NULL),(13,0,'2023-04-04 00:32:43.000000','2023-04-04','2023-04-17 15:58:23.396735','2023-04-17',495,'╪│┘ä╪╖╪º┘å ╪╣╪¿╪» ╪º┘ä╪¡┘à┘è╪» ┘ç╪º╪▒┘ê┘å ','1141433235',NULL,NULL,NULL,'32','4- ╪º┘ä╪»┘ê╪▒ ╪º┘ä╪¬╪º┘å┘ë','┘à╪»┘è┘å╪⌐ ┘å╪º╪╡╪▒ ','2023-01-01',0,0,0,0,0,1,'0','user_profile_image_placeholer.png','',0,1,NULL,NULL,NULL,NULL,NULL),(14,0,'2023-04-04 00:32:43.000000','2023-04-04','2023-04-17 15:58:23.400724','2023-04-17',NULL,'┘à╪╡╪╖┘ü┘ë ╪¼┘à╪╣╪⌐ ┘à┘ç╪»┘ë','1155958380',NULL,NULL,NULL,NULL,NULL,'┘à╪»┘è┘å╪⌐ ┘å╪º╪╡╪▒ - ╪¿╪╣╪» ┘â╪º┘ü┘è╪⌐ ╪│╪º┘å╪│┘è╪¬','2023-01-01',0,0,0,0,0,1,'0','user_profile_image_placeholer.png','',0,1,NULL,NULL,NULL,NULL,NULL),(15,0,'2023-04-04 00:32:43.000000','2023-04-04','2023-04-18 02:09:31.684627','2023-04-18',1183,'╪┤╪º╪░┘ä┘ë ╪╣╪╖╪º┘ä┘ä╪⌐ ┘à╪¡┘à╪»','01145944291',NULL,NULL,'- ┘à╪▒┘â╪▓ ╪¡╪▒┘è╪⌐ ┘ä╪╣┘ä╪º╪¼ ╪º╪»┘à╪º┘å','-','┘ü┘è┘ä╪º ╪¼╪º╪¿╪▒ ╪╣┘ê╪╢','- ┘à╪▒┘â╪▓ ╪¡╪▒┘è╪⌐ ┘ä╪╣┘ä╪º╪¼ ╪º╪»┘à╪º┘å  - - - ┘ü┘è┘ä╪º ╪¼╪º╪¿╪▒ ╪╣┘ê╪╢','2023-04-18',0,0,0,0,0,1,'0','user_profile_image_placeholer.png','-',20,1,NULL,2,NULL,'2023-02-18',NULL),(16,0,'2023-04-04 00:32:43.000000','2023-04-04','2023-04-17 15:58:23.408702','2023-04-17',1192,'╪╣╪¿╪» ╪º┘ä┘å╪º╪╡╪▒ ╪╡╪º╪¿╪▒ ╪º╪¡┘à╪» ','1222127883',NULL,NULL,NULL,NULL,'┘ü┘è┘ä╪º ╪╣╪¿╪» ╪º┘ä┘å╪º╪╡╪▒ ','┘à╪»┘è┘å╪⌐ ┘å╪º╪╡╪▒- ╪¡╪▒ ┘à╪»┘è┘å╪⌐ ╪º┘ä┘é╪╢╪º╪⌐- ╪¿╪¼┘ê╪º╪▒ ┘à╪¿╪º┘å┘ë ╪╣┘ä┘ë ╪º┘ä┘å┘è┘ä ','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(17,0,'2023-04-04 00:32:43.000000','2023-04-04','2023-04-17 15:58:23.412692','2023-04-17',1193,'╪º╪¡┘à╪» ╪╣╪¿╪» ╪º┘ä╪┤╪º┘ü┘ë ╪╣╪¿╪» ╪º┘ä╪¡┘à┘è╪» ','12880645559',NULL,NULL,NULL,'10','7- ╪º┘ä╪»┘ê╪▒ ╪º┘ä╪▒╪º╪¿╪╣ ','┘à╪»┘è┘å╪⌐ ┘å╪º╪╡╪▒- ╪╣┘à╪º┘è╪▒ ┘à╪»┘è┘å╪⌐ ┘å╪º╪╡╪▒ ','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(18,0,'2023-04-04 00:32:43.000000','2023-04-04','2023-04-17 15:58:23.416682','2023-04-17',999,'┘ü╪¬╪¡┘è ╪│╪╣╪» ╪º┘ä╪»┘è┘å ╪╣╪¿╪» ╪º┘ä╪▒╪¡┘à┘å','1221547073',NULL,NULL,NULL,'20','╪º┘ä╪»┘ê╪▒ ╪º┘ä╪▒╪º╪¿╪╣ - 8','┘à╪»┘è┘å╪⌐ ┘å╪º╪╡╪▒ - ╪º┘à╪º┘à ┘à╪│╪¼╪» ╪º┘ä╪┤┘è╪« ╪┤╪╣┘è╪¿ ','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(19,0,'2023-04-04 00:32:43.000000','2023-04-04','2023-04-17 15:58:23.419673','2023-04-17',1554,'╪º╪¡┘à╪» ╪¡╪│┘è┘å ╪╣┘ä┘è ╪¡╪│┘å','1228001781',NULL,NULL,NULL,'╪╣┘à╪º╪▒┘ç 14','╪»┘ê╪▒ ╪º┘ä╪º┘ê┘ä ╪╣┘ä┘ê┘è ╪┤┘é┘ç 3','┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒ ╪¿╪¼┘ê╪º╪▒ ╪º┘ä╪¼┘à╪╣┘è┘ç','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(20,0,'2023-04-04 00:32:43.000000','2023-04-04','2023-04-17 15:58:23.427656','2023-04-17',1555,'┘ç╪┤╪º┘à ╪│╪╣╪» ╪º┘ä╪»┘è┘å ╪º╪¡┘à╪»','1143037537',NULL,NULL,NULL,NULL,'╪»┘ê╪▒ ╪½╪º┘å┘è ╪╣┘ä┘ê┘è','╪¿╪¼┘ê╪º╪▒ ╪╡┘å ╪│┘è╪¬ ┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(21,0,'2023-04-04 00:32:43.000000','2023-04-04','2023-04-17 15:58:23.434637','2023-04-17',1556,'╪º╪¡┘à╪» ╪╣╪¿╪» ╪▒╪º╪▓┘é ╪º╪¡┘à╪»','1208226646',NULL,NULL,NULL,NULL,'╪»┘ê╪▒ ╪½╪º┘ä╪¬ ╪╣┘ä┘ê┘è','╪¿╪¼┘ê╪º╪▒ ╪╡┘å ╪│┘è╪¬ ┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(22,0,'2023-04-04 00:32:43.000000','2023-04-04','2023-04-17 15:58:23.439621','2023-04-17',1557,'╪º╪┤╪▒┘ü ╪º┘ä╪º┘à┘è╪▒ ╪º╪¿╪▒╪º┘ç┘è┘à','1003596068',NULL,NULL,NULL,NULL,'╪»┘ê╪▒ ╪½╪º┘å┘è ╪╣┘ä┘ê┘è','╪¿╪¼┘ê╪º╪▒ ╪╡┘å ╪│┘è╪¬ ┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(23,0,'2023-04-04 00:32:43.000000','2023-04-04','2023-04-17 15:58:23.443610','2023-04-17',1558,'╪º╪¡┘à╪» ╪╣╪¿╪»╪º┘ä╪┤╪º┘ü┘è ╪º┘å┘ê╪▒','1007650964',NULL,NULL,NULL,NULL,'╪»┘ê╪▒ ╪½╪º┘ä╪½ ╪╣┘ä┘ê┘è','╪¿╪¼┘ê╪º╪▒ ╪╡┘å ╪│┘è╪¬ ┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(24,0,'2023-04-04 00:32:43.000000','2023-04-04','2023-04-17 15:58:23.450592','2023-04-17',1559,'┘à╪│╪¬╪┤╪º╪▒ ╪«╪º┘ä╪» ┘à╪¡┘à╪» ╪▒┘è╪º┘å','1007650964',NULL,NULL,NULL,NULL,NULL,'╪¿╪¼┘ê╪º╪▒ ╪╡┘å ╪│┘è╪¬ ┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(25,0,'2023-04-04 00:32:43.000000','2023-04-04','2023-04-17 15:58:23.453582','2023-04-17',1560,'╪º┘ä┘à╪│╪¬╪┤╪º╪▒ ╪╣┘à╪▒┘ê ┘è╪¡┘è┘è ╪º╪¿┘ê ╪▓┘è╪»','1202443351',NULL,NULL,NULL,NULL,NULL,'╪¿╪¼┘ê╪º╪▒ ╪╡┘å ╪│┘è╪¬ ┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(26,0,'2023-04-04 00:32:43.000000','2023-04-04','2023-04-17 15:58:23.456574','2023-04-17',1561,'╪│┘à┘è╪▒┘ç ╪│┘è╪» ╪╣┘ä┘è ╪º┘ä╪╖┘è╪¿','1060745466',NULL,NULL,NULL,NULL,'╪»┘ê╪▒ ╪º┘ä╪¬╪º┘ä╪¬ ','╪¿╪¼┘ê╪º╪▒ ╪╡┘å ╪│┘è╪¬ ┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒-╪╣┘à╪º╪▒┘ç ┘à┘ç┘å╪»╪│ ╪╡┘ä╪º╪¡ ╪º┘ä╪»┘è┘å ┘à┘â┘è','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(27,0,'2023-04-04 00:32:43.000000','2023-04-04','2023-04-17 15:58:23.460564','2023-04-17',1562,'╪│┘ê╪▓╪º┘å ╪╡┘ä╪º╪¡ ╪º┘ä╪»┘è┘å ╪╣╪¿╪»╪º┘ä╪╣╪╕┘è┘à ╪º╪¡┘à╪»','1003661367',NULL,NULL,NULL,'╪╣┘à╪º╪▒┘ç 9','╪»┘ê╪▒ ╪º┘ä╪▒╪º╪¿╪╣','╪¿╪¼┘ê╪º╪▒ ┘ü┘å╪»┘é ╪│╪º╪▒┘ç ┘è╪│╪º╪▒ ┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒ ┘à╪»┘è┘å┘ç ╪º┘ä┘é╪╢╪º┘ç','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(28,0,'2023-04-04 00:32:43.000000','2023-04-04','2023-04-17 15:58:23.465551','2023-04-17',1563,'╪╣╪╡╪º┘à ╪╣╪¿╪»╪º┘ä┘ä┘ç ┘à╪¡┘à╪»','1011355371',NULL,NULL,NULL,'╪╣┘à╪º╪▒┘ç 9','╪»┘ê╪▒ ╪º┘ä╪│╪º╪»╪│','╪¿╪¼┘ê╪º╪▒ ┘ü┘å╪»┘é ╪│╪º╪▒┘ç ┘è╪│╪º╪▒ ┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒ ┘à╪»┘è┘å┘ç ╪º┘ä┘é╪╢╪º┘ç','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(29,0,'2023-04-04 00:32:43.000000','2023-04-04','2023-04-17 15:58:23.469540','2023-04-17',1564,'╪▒┘à╪╢╪º┘å ╪╣┘ê╪╢ ╪º┘ä┘ä┘ç ╪╡╪º╪¿╪▒ ╪╣┘ä┘è','1000095956',NULL,NULL,NULL,'╪╣┘à╪º╪▒┘ç 11','╪»┘ê╪▒ ╪½╪º┘ä╪½ ','╪¿╪¼┘ê╪º╪▒ ┘ü┘å╪»┘é ╪│╪º╪▒┘ç ┘è╪│╪º╪▒ ┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒ ┘à╪»┘è┘å┘ç ╪º┘ä┘é╪╢╪º┘ç','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(30,0,'2023-04-04 00:32:43.000000','2023-04-04','2023-04-17 15:58:23.472532','2023-04-17',1448,'┘à╪╡╪╖┘ü┘ë ╪º┘ä╪│┘è╪» ┘à╪¡┘à╪» ╪º┘ä╪│┘è╪»','1289488890',NULL,NULL,NULL,'╪º┘à╪º┘à ╪┤╪º╪▒╪╣ ╪º┘ä┘ü╪▒┘å','╪º┘ä╪»┘ê╪▒1 ┘ü┘è┘ä╪º 13','╪«┘ä┘ü ╪º┘ä╪º╪│╪¬╪º╪»-┘à╪╖┘ä╪╣ ┘à╪»┘è┘å╪⌐ ┘å╪º╪╡╪▒ ','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(31,0,'2023-04-04 00:32:43.000000','2023-04-04','2023-04-17 15:58:23.475524','2023-04-17',1449,'╪º┘ä╪│┘è╪» ┘à╪¡┘à╪» ╪º┘ä╪│┘è╪»','1140979666',NULL,NULL,NULL,'╪º┘à╪º┘à ╪┤╪º╪▒╪╣ ╪º┘ä┘ü╪▒┘å','╪º┘ä╪»┘ê╪▒ 1 ┘ü┘è┘ä╪º 13','╪«┘ä┘ü ╪º┘ä╪º╪│╪¬╪º╪»-┘à╪╖┘ä╪╣ ┘à╪»┘è┘å╪⌐ ┘å╪º╪╡╪▒ ','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(32,0,'2023-04-04 00:32:43.000000','2023-04-04','2023-04-17 15:58:23.480511','2023-04-17',1450,'╪│╪º┘à┘è╪⌐ ╪╣╪¿╪» ╪º┘ä┘à┘å╪╣┘à ╪¡┘å┘ü┘ë','1283832495',NULL,NULL,NULL,'╪╣┘à╪º╪▒╪⌐10','╪º┘ä╪»┘ê╪▒1 ╪┤┘é╪⌐2','┘à╪»┘è┘å╪⌐ ┘å╪º╪╡╪▒','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(33,0,'2023-04-04 00:32:43.000000','2023-04-04','2023-04-17 15:58:23.484500','2023-04-17',1610,'╪╣╪¿╪»╪º┘ä┘å╪º╪╡╪▒ ┘à╪¡┘à╪» ╪º┘ä╪│┘è╪»','1002566014',NULL,NULL,NULL,NULL,'╪»┘ê╪▒ 2','┘à╪╖┘ä╪╣ ┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒ ╪¿╪¼┘ê╪º╪▒ ┘à╪│╪¼╪» ╪º┘ä┘å┘ê╪▒','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(34,0,'2023-04-04 00:32:43.000000','2023-04-04','2023-04-17 15:58:23.487492','2023-04-17',1611,'┘à╪¡┘à╪» ╪╣╪¿╪»╪º┘ä┘å╪º╪╡╪▒ ┘à╪¡┘à╪» ╪º┘ä╪│┘è╪»','1223884418',NULL,NULL,NULL,NULL,'╪»┘ê╪▒ 3','┘à╪╖┘ä╪╣ ┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒ ╪¿╪¼┘ê╪º╪▒ ┘à╪│╪¼╪» ╪º┘ä┘å┘ê╪▒','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(35,0,'2023-04-04 00:32:43.000000','2023-04-04','2023-04-17 15:58:23.491482','2023-04-17',1612,'┘à╪¡┘à╪» ╪¿┘ç╪¼╪¬ ┘ü┘ç┘à┘è ╪¿╪▒╪║┘ê╪¬','1110288778',NULL,NULL,NULL,NULL,'╪»┘ê╪▒ 6','┘à╪╖┘ä╪╣ ┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒ ╪¿╪¼┘ê╪º╪▒ ┘à╪│╪¼╪» ╪º┘ä┘å┘ê╪▒','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(36,0,'2023-04-04 00:32:43.000000','2023-04-04','2023-04-17 15:58:23.497466','2023-04-17',1690,'╪▓┘è┘å╪¿ ╪╣╪╖╪º ╪¼╪º╪» ┘à╪¡┘à╪¡┘à┘ê╪»','1008867518',NULL,NULL,NULL,NULL,'╪»┘ê╪▒ ╪¬╪º┘ä╪¬ ╪┤┘é┘ç 7','╪╣┘à╪º╪▒╪º╪¬ ╪º┘ä┘à┘ç┘å╪»╪│ ╪╡┘ä╪º╪¡ ╪º┘ä╪»┘è┘å ┘à┘â┘è','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(37,0,'2023-04-04 00:32:43.000000','2023-04-04','2023-04-17 15:58:23.501456','2023-04-17',1691,'╪º╪¡┘à╪» ╪╣╪º╪¿╪»┘è┘å ╪º╪¡┘à╪»','1158781599',NULL,NULL,NULL,'╪╣┘à╪º╪▒┘ç ┘à╪│╪¬╪┤╪º╪▒ ╪º╪│┘à╪º╪╣┘è┘ä',NULL,'╪¿╪¼┘ê╪º╪▒ ┘à╪»╪▒╪│┘ç ╪º┘ä╪│╪º╪»╪º╪¬ ╪¿╪¼┘ê╪º╪▒ ┘é┘ç┘ê┘ç ╪º┘ê┘ä┘è','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(38,0,'2023-04-04 00:32:43.000000','2023-04-04','2023-04-17 15:58:23.504446','2023-04-17',1700,'╪º┘ä╪¡╪│┘è┘å ┘à┘å╪╡┘ê╪▒ ╪╣╪¿╪»╪º┘ä┘ê╪º╪¡╪»','1210019899',NULL,NULL,NULL,NULL,NULL,'╪¿╪¼┘ê╪º╪▒ ╪¡╪╢╪º┘å┘ç ╪º╪¼┘è╪º┘ä┘å╪º(┘å┘è┘ä ╪º┘ä┘à┘é╪º┘ê┘ä┘è┘å ╪╣┘ä┘è ┘å┘è┘ä)','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(39,0,'2023-04-04 00:32:43.000000','2023-04-04','2023-04-17 15:58:23.510431','2023-04-17',1851,'┘à╪¡┘à╪» ╪▓┘â┘è ╪º┘ä┘à┘ê╪¼┘è','1068027607',NULL,NULL,NULL,NULL,'╪┤╪º╪▒╪╣ ╪º┘ä┘à╪│╪¼╪» ╪º┘ä┘å┘ê╪▒','╪╣┘à╪º╪▒┘ç ┘ê╪▒╪½┘ç ┘à╪▒╪¡┘ê┘à ┘à┘ç┘å╪º','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(40,0,'2023-04-04 00:32:43.000000','2023-04-04','2023-04-17 15:58:23.514421','2023-04-17',1857,'╪╣┘à╪▒ ┘ü┘ê╪▓┘è ╪º╪¡┘à╪»','1221088817',NULL,NULL,NULL,'╪¬╪¬┘é╪│┘è┘à ┘é╪╢╪º┘ç','┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒','┘ü┘è┘ä╪º ┘à╪│╪¬╪┤╪º╪▒ ┘ü┘ê╪▓┘è ┘ü╪╢┘ä','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(41,0,'2023-04-04 00:32:44.000000','2023-04-04','2023-04-17 15:58:23.518410','2023-04-17',1960,'╪º┘à ╪º╪┤╪▒┘ü ┘è┘ê╪│┘ü ╪¼╪▒╪│ ',NULL,NULL,NULL,NULL,'╪╣┘à╪º╪▒┘ç 1','╪»┘ê╪▒ ╪▒╪º╪¿╪╣ ╪┤┘é┘ç 8','┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(42,0,'2023-04-04 00:32:44.000000','2023-04-04','2023-04-17 15:58:23.521401','2023-04-17',1961,' ╪º╪»┘è╪¿┘ç ╪╣╪¿╪»╪º┘ä╪¿╪º┘é┘è ╪º┘ä╪┤┘è╪«','1154727109',NULL,NULL,NULL,'╪╣┘à╪º╪▒┘ç 31','╪»┘ê╪▒ ╪½╪º┘ä╪½ ╪┤┘é┘ç 6','┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒ ','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(43,0,'2023-04-04 00:32:44.000000','2023-04-04','2023-04-17 15:58:23.527386','2023-04-17',1962,'╪º╪¡┘à╪» ╪¡╪│┘å ╪│╪▒╪º╪¼','1128607959',NULL,NULL,NULL,'╪╣┘à╪º╪▒┘ç 32','╪»┘ê╪▒ 3 ╪┤┘é┘ç 6','┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(44,0,'2023-04-04 00:32:44.000000','2023-04-04','2023-04-17 15:58:23.531376','2023-04-17',1963,'╪╣╪¿╪»╪º┘ä┘à╪º┘ä┘â ┘à╪¡┘à╪» ╪º╪¡┘à╪» ┘à╪¡┘à╪»','1111852551',NULL,NULL,NULL,'╪╣┘à╪º╪▒┘ç 32','╪»┘ê╪▒ ╪▒╪º╪¿╪╣ ╪┤┘é┘ç 8','┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(45,0,'2023-04-04 00:32:44.000000','2023-04-04','2023-04-17 15:58:23.535363','2023-04-17',1964,'╪╣╪¿╪»╪º┘ä╪┤┘â┘ê╪▒ ┘à╪¼╪º╪▓┘è ┘à╪¡┘à╪»','1141563967',NULL,NULL,NULL,'╪╣┘à╪º╪▒┘ç 9','╪»┘ê╪▒ ╪½╪º┘ä╪¬ ╪┤┘é┘ç 6','┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(46,0,'2023-04-04 00:32:44.000000','2023-04-04','2023-04-17 15:58:23.539353','2023-04-17',1965,'┘ê╪º╪ª┘ä ╪▒┘ü╪╣╪¬ ┘à╪¡┘à╪»','1099107622',NULL,NULL,NULL,'╪╣┘à╪º╪▒┘ç 10','╪»┘ê╪▒ ╪º┘ä╪º┘ê┘ä ╪┤┘é┘ç 1','┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒ ','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(47,0,'2023-04-04 00:32:44.000000','2023-04-04','2023-04-17 15:58:23.543343','2023-04-17',1966,'╪╡╪¿╪▒┘è ╪▒┘â╪º╪¿┘è ╪º╪¿╪▒╪º┘ç┘è┘à',NULL,NULL,NULL,NULL,'┘ü┘è┘ä╪º 42 ','╪»┘ê╪▒ ╪º┘ä╪º┘ê┘ä ╪▒┘é┘à ╪┤┘é┘ç 1','┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(48,0,'2023-04-04 00:32:44.000000','2023-04-04','2023-04-17 15:58:23.550324','2023-04-17',1983,'╪╣╪¿╪»╪º┘ä┘ä┘ç ┘à╪¡┘à╪» ╪╣╪¿╪»╪º┘ä┘ä┘ç','1062855001',NULL,NULL,NULL,'╪»┘ê╪▒ ╪º┘ä╪º╪▒╪╢┘è ╪┤┘é┘ç 1','╪╣┘à╪º╪▒┘ç 9','╪¿╪¼┘ê╪º╪▒ ┘ü┘å╪»┘é ╪│╪º╪▒┘ç ┘à╪»┘è┘å┘ç ╪º┘ä┘é╪╢╪º┘ç ','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(49,0,'2023-04-04 00:32:44.000000','2023-04-04','2023-04-17 15:58:23.553316','2023-04-17',2019,'╪º╪│┘ä╪º┘à ╪╣╪¿╪»╪º┘ä┘à┘å╪╣┘à ┘à╪¡┘à╪»','1154117216',NULL,NULL,NULL,'╪╣┘à╪º╪▒┘ç 33','╪»┘ê╪▒ ╪º┘ä╪▒╪º┘è╪╣ ╪┤┘é┘ç 7','┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(50,0,'2023-04-04 00:32:44.000000','2023-04-04','2023-04-17 15:58:23.556308','2023-04-17',2020,'╪º┘è┘à┘å ┘â┘à╪º┘ä ╪¬┘ê┘ü┘è┘é','1001506508',NULL,NULL,NULL,'╪╣┘à╪º╪▒┘ç 38','╪»┘ê╪▒ ╪▒╪º╪¿╪╣ ╪┤┘é┘ç 8','┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(51,0,'2023-04-04 00:32:44.000000','2023-04-04','2023-04-17 15:58:23.559300','2023-04-17',2021,'╪º╪¡┘à╪» ╪╣╪¿╪»╪º┘ä╪¡┘à┘è╪» ┘à╪¡┘à╪» ','1141721257',NULL,NULL,NULL,'╪╣┘à╪º╪▒┘ç 23','╪»┘ê╪▒ ╪¬╪º┘ä╪¬ ╪┤┘é┘ç 5','┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(52,0,'2023-04-04 00:32:44.000000','2023-04-04','2023-04-17 15:58:23.567280','2023-04-17',2027,'╪│╪º┘à┘è┘ç ╪╣┘ê╪╢ ╪╣╪¿╪»╪º┘ä╪╣╪▓┘è╪▓ ','1150268287',NULL,NULL,NULL,'╪╣┘à╪º╪▒┘ç 4','╪»┘ê╪▒ ╪º┘ä╪º╪▒╪╢┘è ','┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(53,0,'2023-04-04 00:32:44.000000','2023-04-04','2023-04-17 15:58:23.573264','2023-04-17',2070,'┘à╪¡┘à┘ê╪» ┘à╪¡┘à╪» ┘ü╪ñ╪º╪»','1154858225',NULL,NULL,NULL,NULL,NULL,'┘à╪¡┘ä ╪¡┘ê╪▒╪│','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(54,0,'2023-04-04 00:32:44.000000','2023-04-04','2023-04-17 15:58:23.578251','2023-04-17',2071,'╪│┘ç╪º┘à ╪º╪¿╪▒╪º┘ç┘è┘à ┘à╪¡┘à╪»','1120477826',NULL,NULL,NULL,NULL,'╪╡╪º┘ä┘ê┘å ╪│┘ç╪º ╪│╪º┘ç┘ê','╪╡╪º┘ä┘ê┘å ╪│┘ç╪º ╪│╪º┘ç┘ê','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(55,0,'2023-04-04 00:32:44.000000','2023-04-04','2023-04-17 15:58:23.583236','2023-04-17',2072,'╪º╪¡┘à╪» ╪▒┘à╪╢╪º┘å ╪╣╪¿╪»╪º┘ä┘à┘é╪╡┘ê╪»','1126964496',NULL,NULL,NULL,NULL,NULL,'┘à╪¡┘ä ╪╣┘ä┘è ╪º┘ä╪▒┘ü','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(56,0,'2023-04-04 00:32:44.000000','2023-04-04','2023-04-17 15:58:23.589220','2023-04-17',2081,'╪º╪¡┘à╪» ╪╣╪¿╪»╪º┘ä┘ä┘ç ╪¡╪│╪¿ ╪º┘ä┘ä┘ç',NULL,NULL,NULL,NULL,'╪╣┘à╪º╪▒┘ç 24','╪»┘ê╪▒ ╪º┘ä╪º┘ê┘ä ╪┤┘é┘ç 1','┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(57,0,'2023-04-04 00:32:44.000000','2023-04-04','2023-04-17 15:58:23.592212','2023-04-17',2082,'╪º╪¡┘à╪» ╪│┘è╪» ┘à╪¡┘à╪» ┘ç╪┤╪º┘à ','1111773973',NULL,NULL,NULL,'╪╣┘à╪º╪▒┘ç 9','╪»┘ê╪▒ ╪º┘ä╪▒╪º┘è╪╣ ╪┤┘é┘ç 7','┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(58,0,'2023-04-04 00:32:44.000000','2023-04-04','2023-04-17 15:58:23.596202','2023-04-17',2039,'╪╡┘ä╪º╪¡ ╪º┘ä╪»┘è┘å ','1112310107',NULL,NULL,NULL,'╪╣┘à╪º╪▒┘ç 1 ┘à╪»╪«┘ä ╪ú','╪»┘ê╪▒ ╪º┘ä╪º┘ê┘ä ╪┤┘é┘ç2','╪º┘à╪º┘à ┘à╪│╪º┘â┘å ╪º┘ä╪╖╪º┘ä╪¿╪º╪¬ ╪«┘ä┘ü ┘ü╪▒┘å ','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(59,0,'2023-04-04 00:32:44.000000','2023-04-04','2023-04-17 15:58:23.599193','2023-04-17',2040,'┘à╪¡┘à┘ê╪» ┘à╪¡┘à╪»','1005009934',NULL,NULL,NULL,'╪╣┘à╪º╪▒┘ç 1 ┘à╪»╪«┘ä ╪ú','╪»┘ê╪▒ ╪º┘ä╪¬╪º┘ä╪¬ ╪┤┘é┘ç 6','╪º┘à╪º┘à ┘à╪│╪º┘â┘å ╪º┘ä╪╖╪º┘ä╪¿╪º╪¬ ╪«┘ä┘ü ┘ü╪▒┘å ','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(60,0,'2023-04-04 00:32:44.000000','2023-04-04','2023-04-17 15:58:23.602185','2023-04-17',2041,'╪º╪¡┘à╪» ┘à┘å┘è╪▒ ┘à╪¡┘à╪» ┘ü╪¬╪¡ ╪º┘ä┘ä┘ç','1228072010',NULL,NULL,NULL,'╪╣┘à╪º╪▒┘ç ┘à┘ç┘å╪»╪│ ┘à┘å┘è╪▒ ┘à╪¡┘à╪» ┘ü╪¬╪¡ ╪º┘ä┘ä┘ç','╪»┘ê╪▒ ╪º┘ä╪º┘ê┘ä ╪┤┘é┘ç 2','┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(61,0,'2023-04-04 00:32:44.000000','2023-04-04','2023-04-17 15:58:23.607172','2023-04-17',2042,'┘à╪¡┘à╪» ┘à┘å┘è╪▒ ┘à╪¡┘à╪» ┘ü╪¬╪¡ ╪º┘ä┘ä┘ç','1002526186',NULL,NULL,NULL,'╪╣┘à╪º╪▒┘ç ┘à┘ç┘å╪»╪│ ┘à┘å┘è╪▒ ┘à╪¡┘à╪» ┘ü╪¬╪¡ ╪º┘ä┘ä┘ç','╪»┘ê╪▒ ╪º┘ä╪¬╪º┘å┘è ╪┤┘é┘ç 3','┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(62,0,'2023-04-04 00:32:44.000000','2023-04-04','2023-04-17 15:58:23.609166','2023-04-17',2043,' ┘à┘å┘è╪▒ ┘à╪¡┘à╪» ┘ü╪¬╪¡ ╪º┘ä┘ä┘ç','1228072010',NULL,NULL,NULL,'╪╣┘à╪º╪▒┘ç ┘à┘ç┘å╪»╪│ ┘à┘å┘è╪▒ ┘à╪¡┘à╪» ┘ü╪¬╪¡ ╪º┘ä┘ä┘ç','╪»┘ê╪▒ ╪º┘ä╪º╪▒╪╢┘è ╪º┘ä╪┤┘é┘ç 1','┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(63,0,'2023-04-04 00:32:44.000000','2023-04-04','2023-04-17 15:58:23.613157','2023-04-17',2044,'┘à╪¡┘à┘ê╪» ╪º╪¡┘à╪» ┘à╪¡┘à┘ê╪»','1154709014',NULL,NULL,NULL,'╪╣┘à╪º╪▒┘ç ╪¡╪¼ ┘à╪¡┘à┘ê╪»',NULL,'╪¼┘à╪¿ ╪╣┘à╪º╪▒┘ç ┘à┘ç┘å╪»╪│ ┘à┘å┘è╪▒','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(64,0,'2023-04-04 00:32:44.000000','2023-04-04','2023-04-17 15:58:23.617145','2023-04-17',2045,'┘à╪╡╪╖┘ü┘è ╪º┘ä╪¡╪│┘å ╪╖┘ç','1001016690',NULL,NULL,NULL,'╪╣┘à╪º╪▒┘ç ╪¡╪¼ ┘à╪¡┘à┘ê╪»','╪»┘ê╪▒ ╪º┘ä╪¬╪º┘å┘è ╪┤┘é┘ç 1','╪¼┘à╪¿ ╪╣┘à╪º╪▒┘ç ┘à┘ç┘å╪»╪│ ┘à┘å┘è╪▒','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(65,0,'2023-04-04 00:32:44.000000','2023-04-04','2023-04-17 15:58:23.621134','2023-04-17',2046,'┘å╪º╪░╪¼ ╪╡┘ä╪º╪¡ ╪º╪¡┘à╪»','1159483383',NULL,NULL,NULL,NULL,'╪»┘ê╪▒ ╪º┘ä╪º┘ê┘ä ╪┤┘é┘ç 2','┘à╪╖┘ä╪╣ ╪º┘ä╪º╪│╪¬╪º╪»','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(66,0,'2023-04-04 00:32:44.000000','2023-04-04','2023-04-17 15:58:23.624126','2023-04-17',2047,'╪º╪¿╪▒╪º┘ç┘è┘à ┘ü╪º┘ê┘è ╪╣╪¿╪»╪º┘ä┘ä┘ç','1121070019',NULL,NULL,NULL,'╪¼┘à╪¿ ╪º┘ä┘ü╪▒┘å','╪»┘ê╪▒ ╪º┘ä╪¬╪º┘ä╪¬ ╪┤┘é┘ç 6','┘à╪╖┘ä╪╣ ╪º┘ä╪º╪│╪¬╪º╪»','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(67,0,'2023-04-04 00:32:44.000000','2023-04-04','2023-04-17 15:58:23.627119','2023-04-17',2048,'╪¿╪┤┘è╪▒ ╪¼┘à╪╣┘ç ╪╣┘ä┘è','112804594',NULL,NULL,NULL,'╪¼┘à╪¿ ╪º┘ä┘ü╪▒┘å','╪»┘ê╪▒ ╪º┘ä╪¬╪º┘å┘è ╪┤┘é┘ç 3','┘à╪╖┘ä╪╣ ╪º┘ä╪º╪│╪¬╪º╪»','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(68,0,'2023-04-04 00:32:44.000000','2023-04-04','2023-04-17 15:58:23.631109','2023-04-17',2049,'╪╣┘è╪» ┘à╪¡┘à╪» ╪╣╪¿╪»┘ç','1110673211',NULL,NULL,NULL,'╪╣┘à╪º╪▒┘ç 1 ┘à╪»╪«┘ä ╪¿','╪»┘ê╪▒ ╪▒╪º╪¿╪╣ ╪┤┘é┘ç 9','┘à╪╖┘ä╪╣ ╪º┘ä╪º╪│╪¬╪º╪»','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(69,0,'2023-04-04 00:32:44.000000','2023-04-04','2023-04-17 15:58:23.636095','2023-04-17',2050,'┘è┘ê╪│┘ü ┘à╪¡┘à┘ê╪» ╪¿╪»╪▒┘è','1156090427',NULL,NULL,NULL,'╪╣┘à╪º╪▒┘ç 1 ┘à╪»╪«┘ä ╪¿','╪»┘ê╪▒ ╪│╪º╪»╪│ ╪┤┘é┘ç 11','┘à╪╖┘ä╪╣ ╪º┘ä╪º╪│╪¬╪º╪»','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(70,0,'2023-04-04 00:32:44.000000','2023-04-04','2023-04-17 15:58:23.639086','2023-04-17',2122,'╪º╪¿╪¬╪│╪º┘à ╪▓┘è╪»╪º┘å ╪╣╪¿┘è╪» ╪╣┘ä┘è',NULL,NULL,NULL,NULL,'╪╣┘à╪º╪▒┘ç ╪º╪¡┘à╪» ╪¡╪º┘à╪»','╪»╪▒ ╪¬╪º┘å┘è ╪┤┘é┘ç 2','╪┤╪º╪▒╪╣ ╪º┘à╪º┘à ┘à╪│╪¼╪» ╪º┘ä┘å┘ê╪▒','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(71,0,'2023-04-04 00:32:44.000000','2023-04-04','2023-04-17 15:58:23.642078','2023-04-17',2123,'╪│╪╣╪º╪» ┘à╪╡╪╖┘ü┘è ╪º╪¡┘à╪»','1143035777',NULL,NULL,NULL,'┘ü┘è┘ä╪º ╪▒┘é┘à 14 ┘è┘ê╪│┘ü ╪º╪¿╪▒╪º┘ç┘è┘à',NULL,'╪╣┘å╪» ┘ü┘å╪»┘é ╪╡┘å ╪│┘è╪¬','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(72,0,'2023-04-04 00:32:44.000000','2023-04-04','2023-04-17 15:58:23.646070','2023-04-17',2022,'╪º┘à┘è╪▒┘ç ┘ê╪¡┘è╪» ╪╣┘ä┘è','1114313818',NULL,NULL,NULL,'╪╣┘à╪º╪▒┘ç ╪º┘ä╪¡╪¼ ┘å╪¿┘è┘ä ','╪»┘ê╪▒ ╪¬╪º┘å┘è ╪┤┘é┘ç 3','╪¿╪¼┘ê╪º╪▒ ╪¬╪▒┘ê┘à┘è╪¬ ╪º┘ä╪▒┘è ╪º┘ä╪╣┘à╪º╪▒┘ç ╪º┘ä┘è ╪¼┘à╪¿ ╪º┘ä╪º╪í ┘ê╪▒╪»╪º┘å┘è ','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(73,0,'2023-04-04 00:32:44.000000','2023-04-04','2023-04-17 15:58:23.651054','2023-04-17',2023,'┘â╪▒┘è┘à ╪╣╪¿╪»╪º┘ä┘à╪╣╪╖┘è ┘à╪¡┘à╪»','1013528135',NULL,NULL,NULL,'╪╣┘à╪º╪▒┘ç ╪º┘ä╪¡╪¼ ┘å╪¿┘è┘ä ','╪»┘ê╪▒ ╪▒╪º╪¿╪╣ ╪┤┘é┘ç 6','╪º┘ä╪╣┘à╪º╪▒┘ç ╪¼┘à╪¿ ┘â┘ê╪º┘ü┘è╪▒ ╪º┘ä╪º╪í ╪º┘ä┘ê╪▒╪»╪º┘å┘è ','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(74,0,'2023-04-04 00:32:44.000000','2023-04-04','2023-04-17 15:58:23.654046','2023-04-17',2024,'╪╣┘ä┘è╪º╪í ┘ç╪┤╪º┘à ╪╡╪º┘ä╪¡ ╪│┘ä┘è┘à╪º┘å','1005832448',NULL,NULL,NULL,'╪¡╪¼ ╪╡┘ä╪º╪¡','╪»┘ê╪▒ ╪¬╪º┘å┘è ╪┤┘é┘ç 3','╪º┘ä╪╣┘à╪º╪▒┘ç ╪¼┘à╪¿ ┘â┘ê╪º┘ü┘è╪▒ ╪º┘ä╪º╪í ╪º┘ä┘ê╪▒╪»╪º┘å┘è ','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(75,0,'2023-04-04 00:32:44.000000','2023-04-04','2023-04-17 15:58:23.657038','2023-04-17',2128,'╪│┘è╪» ╪╣┘ä┘è ╪¡╪│┘å','10087410104',NULL,NULL,NULL,'╪╣┘à╪º┘è╪▒ ╪│┘ê┘ç╪º╪¼','╪»┘ê╪▒ ╪º┘ä╪¬╪º┘å┘è ╪┤┘é┘ç 4','┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(76,0,'2023-04-04 00:32:44.000000','2023-04-04','2023-04-17 15:58:23.660030','2023-04-17',2129,'╪¿╪¡╪▒ ╪º╪¡┘à╪» ╪│┘è╪»','1100515886',NULL,NULL,NULL,'╪«┘ä┘ü ╪╣┘à╪º┘è╪▒ ╪│┘ê┘ç╪º╪¼','╪»┘ê╪▒ ╪¬╪º┘ä╪¬ ╪┤┘é┘ç 5','┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(77,0,'2023-04-04 00:32:44.000000','2023-04-04','2023-04-17 15:58:23.666015','2023-04-17',140,'╪│┘è╪» ┘à╪¡┘à╪» ╪¡╪│┘è┘å ╪¡┘à╪»╪º┘å ','1000016655',NULL,NULL,NULL,'2','╪╣┘à╪º╪▒┘ç20','╪╖╪▒┘è┘é ╪º┘ä╪│╪º╪»╪º╪¬ -╪¡┘ë ┘à╪»┘è┘å╪⌐ ┘å╪º╪╡╪▒ ╪¿╪¼┘ê╪º╪▒ ┘à╪│╪¼╪» ┘à╪»┘è┘å╪⌐ ┘å╪º╪╡╪▒ ','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(78,0,'2023-04-04 00:32:44.000000','2023-04-04','2023-04-17 15:58:23.669007','2023-04-17',NULL,'┘ê┘ä┘è╪» ╪╣╪¿╪»╪º┘ä╪¿╪º┘é┘è ╪º┘à┘è┘å ╪║╪▒┘è╪¿','1029961615',NULL,NULL,NULL,'┘ü┘è┘ä╪º ╪º┘à┘è╪▒┘ç ┘à╪│╪¬╪┤╪º╪▒ ╪╣╪¿╪»╪º┘ä╪¿╪º┘é┘è',NULL,'┘å╪»┘è┘å┘ç ╪º┘ä┘é╪╢╪º┘ç','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(79,0,'2023-04-04 00:32:44.000000','2023-04-04','2023-04-17 15:58:23.671998','2023-04-17',2188,'┘à╪¡┘à╪» ╪º╪¡┘à╪» ╪╣╪¿╪»╪º┘ä╪╣╪╕┘è┘à ','1009997059',NULL,NULL,NULL,NULL,'┘à╪¿┘å┘è ╪╣┘à╪º╪▒┘ç ╪¿┘è╪╢╪º╪í','╪¿╪¼┘ê╪º╪▒ ╪╡┘å ╪│┘è╪¬ ╪¿╪¼┘ê╪º╪▒ ┘ü┘è┘ä╪º ┘à┘å┘è╪▒ ┘â┘è┘å╪¼','2023-01-01',0,0,0,1,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,NULL,NULL,NULL,NULL),(80,0,'2023-04-04 01:01:59.000000','2023-04-04','2023-04-17 15:58:23.674991','2023-04-17',13,'┘à╪¡┘à╪» ╪╣┘ê╪╢ ╪╣╪¿╪»┘ç ','1120001614',NULL,NULL,'╪¡┘è ┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒ ┘à╪»╪▒╪│┘ç ╪º┘ä┘ä╪║╪º╪¬ ╪º┘ä┘ü╪▒┘å╪│┘è  1','╪º┘à╪º┘à ┘å┘ç╪º┘è╪⌐ ╪│┘ê╪▒ ┘à╪»╪▒╪│╪⌐ ╪º┘ä┘ä╪║╪º╪¬ ┘ü╪▒┘å╪│┘ë - ╪º┘ä╪»┘ê╪▒ ╪º┘ä╪º╪▒╪╢┘ë ','╪º┘à╪º┘à ┘å┘ç╪º┘è╪⌐ ╪│┘ê╪▒ ┘à╪»╪▒╪│╪⌐ ╪º┘ä┘ä╪║╪º╪¬ ┘ü╪▒┘å╪│┘ë - ╪º┘ä╪»┘ê╪▒ ╪º┘ä╪º╪▒╪╢┘ë ',' ╪¡┘è ┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒ ┘à╪»╪▒╪│┘ç ╪º┘ä┘ä╪║╪º╪¬ ╪º┘ä┘ü╪▒┘å╪│┘è  1 - ╪º┘à╪º┘à ┘å┘ç╪º┘è╪⌐ ╪│┘ê╪▒ ┘à╪»╪▒╪│╪⌐ ╪º┘ä┘ä╪║╪º╪¬ ┘ü╪▒┘å╪│┘ë - ╪º┘ä╪»┘ê╪▒ ╪º┘ä╪º╪▒╪╢┘ë  - ╪º┘à╪º┘à ┘å┘ç╪º┘è╪⌐ ╪│┘ê╪▒ ┘à╪»╪▒╪│╪⌐ ╪º┘ä┘ä╪║╪º╪¬ ┘ü╪▒┘å╪│┘ë - ╪º┘ä╪»┘ê╪▒ ╪º┘ä╪º╪▒╪╢┘ë ','2023-04-04',0,0,0,0,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,2,NULL,NULL,NULL),(82,0,'2023-04-04 02:25:43.000000','2023-04-04','2023-04-17 15:58:23.679977','2023-04-17',98,'╪¡╪│╪º┘à ╪º┘ä╪»┘è┘å ╪╖┘ç ┘à╪¡┘à┘ê╪» ','1227207578',NULL,NULL,'╪╣┘à╪º┘è╪▒ ┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒ ',' ╪╣┘à╪º╪▒┘ç 1',' ╪╣┘à╪º╪▒┘ç 1',' ╪╣┘à╪º┘è╪▒ ┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒  -  ╪╣┘à╪º╪▒┘ç 1 -  ╪╣┘à╪º╪▒┘ç 1','2023-04-04',0,0,0,0,0,1,'0','user_profile_image_placeholer.png','',0,1,NULL,2,NULL,NULL,NULL),(84,0,'2023-04-04 02:29:54.000000','2023-04-04','2023-04-17 15:58:23.683967','2023-04-17',2,'┘à╪¡┘à╪» ╪¡╪│┘å ╪╣╪º╪¿╪»','1120001614',NULL,NULL,'    ╪º┘à╪º┘à ┘å┘ç╪º┘è╪⌐ ╪│┘ê╪▒ ┘à╪»╪▒╪│╪⌐ ╪º┘ä┘ä╪║╪º╪¬ ┘ü╪▒┘å╪│┘ë - ╪º┘ä╪»┘ê╪▒ ╪º┘ä╪º╪▒╪╢┘ë  - ╪╣┘à╪º╪▒╪⌐ 1A - ╪┤┘é┘ç 2','╪╣┘à╪º╪▒╪⌐ 1A','╪┤┘é┘ç 2','     ╪º┘à╪º┘à ┘å┘ç╪º┘è╪⌐ ╪│┘ê╪▒ ┘à╪»╪▒╪│╪⌐ ╪º┘ä┘ä╪║╪º╪¬ ┘ü╪▒┘å╪│┘ë - ╪º┘ä╪»┘ê╪▒ ╪º┘ä╪º╪▒╪╢┘ë  - ╪╣┘à╪º╪▒╪⌐ 1A - ╪┤┘é┘ç 2 - ╪╣┘à╪º╪▒╪⌐ 1A - ╪┤┘é┘ç 2','2023-04-04',0,0,0,0,0,1,'0','user_profile_image_placeholer.png',NULL,0,1,NULL,2,NULL,NULL,NULL),(85,0,'2023-04-16 21:17:07.340616','2023-04-16','2023-04-17 15:58:23.686959','2023-04-17',56,'┘à╪╡╪╖┘ü┘ë ╪¼┘à╪╣╪⌐ ┘à┘ç╪»┘ë','1155958380',NULL,NULL,'┘à╪»┘è┘å╪⌐ ┘å╪º╪╡╪▒ - ╪¿╪╣╪» ┘â╪º┘ü┘è╪⌐ ╪│╪º┘å╪│┘è╪¬','-','-','┘à╪»┘è┘å╪⌐ ┘å╪º╪╡╪▒ - ╪¿╪╣╪» ┘â╪º┘ü┘è╪⌐ ╪│╪º┘å╪│┘è╪¬ - - - -','2023-04-16',0,0,0,0,0,1,'0','user_profile_image_placeholer.png','-',30,3,NULL,2,NULL,'2023-04-17',NULL);
/*!40000 ALTER TABLE `dataentry_client` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dataentry_collectorder`
--

DROP TABLE IF EXISTS `dataentry_collectorder`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dataentry_collectorder` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `is_deleted` tinyint(1) NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `created_at_date` date DEFAULT NULL,
  `updated_at` datetime(6) DEFAULT NULL,
  `updated_at_date` date DEFAULT NULL,
  `month` int DEFAULT NULL,
  `confirmed` tinyint(1) NOT NULL,
  `reason` varchar(100) DEFAULT NULL,
  `required` int NOT NULL,
  `created_prev_date` date DEFAULT NULL,
  `is_test` tinyint(1) NOT NULL,
  `collector_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `DataEntry_collectord_collector_id_7f6227b6_fk_DataEntry` (`collector_id`),
  CONSTRAINT `DataEntry_collectord_collector_id_7f6227b6_fk_DataEntry` FOREIGN KEY (`collector_id`) REFERENCES `dataentry_employee` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dataentry_collectorder`
--

LOCK TABLES `dataentry_collectorder` WRITE;
/*!40000 ALTER TABLE `dataentry_collectorder` DISABLE KEYS */;
INSERT INTO `dataentry_collectorder` VALUES (1,0,'2023-04-16 18:19:11.485589','2023-04-16','2023-04-16 18:19:11.486611','2023-04-16',NULL,0,NULL,380,'2023-04-16',1,4),(2,0,'2023-04-16 19:10:39.022554','2023-04-16','2023-04-16 19:10:39.022554','2023-04-16',NULL,0,NULL,380,'2023-04-16',1,4),(3,0,'2023-04-16 20:49:52.255516','2023-04-16','2023-04-16 20:49:52.256517','2023-04-16',NULL,0,NULL,380,'2023-04-17',1,5),(4,0,'2023-04-16 21:03:37.220523','2023-04-16','2023-04-16 21:03:37.220523','2023-04-16',NULL,0,NULL,20,'2023-04-16',1,4),(5,0,'2023-04-16 21:30:15.763574','2023-04-16','2023-04-16 21:30:15.763574','2023-04-16',NULL,0,NULL,0,'2023-04-16',1,4),(6,0,'2023-04-16 21:43:20.628606','2023-04-16','2023-04-16 21:43:20.628606','2023-04-16',NULL,0,NULL,60,'2023-04-16',1,4),(7,0,'2023-04-17 20:30:25.359560','2023-04-17','2023-04-17 20:30:25.359560','2023-04-17',NULL,0,NULL,280,'2023-04-17',1,4),(8,0,'2023-04-17 20:33:35.016886','2023-04-17','2023-04-17 20:33:35.016886','2023-04-17',NULL,0,NULL,280,'2023-04-17',1,4),(9,0,'2023-04-17 20:35:36.496579','2023-04-17','2023-04-17 20:35:36.496579','2023-04-17',NULL,0,NULL,280,'2023-04-17',1,4),(10,0,'2023-04-17 20:42:45.234382','2023-04-17','2023-04-17 20:42:45.234382','2023-04-17',NULL,0,NULL,280,'2023-04-17',1,4),(11,0,'2023-04-17 20:52:13.953343','2023-04-17','2023-04-17 20:52:13.953343','2023-04-17',NULL,0,NULL,280,'2023-04-17',1,4),(12,0,'2023-04-17 20:52:48.216813','2023-04-17','2023-04-17 20:52:48.216813','2023-04-17',NULL,0,NULL,280,'2023-04-17',1,4),(13,0,'2023-04-17 20:58:19.881380','2023-04-17','2023-04-17 20:58:19.881380','2023-04-17',NULL,0,NULL,280,'2023-04-17',1,4),(14,0,'2023-04-17 20:58:58.833704','2023-04-17','2023-04-17 20:58:58.833704','2023-04-17',NULL,0,NULL,300,'2023-04-17',1,4),(15,0,'2023-04-17 22:01:45.083633','2023-04-18','2023-04-17 22:01:45.083633','2023-04-18',NULL,0,NULL,260,'2023-04-18',1,4),(16,0,'2023-04-17 22:02:00.825375','2023-04-18','2023-04-17 22:02:00.825375','2023-04-18',NULL,0,NULL,150,'2023-04-18',1,4),(17,0,'2023-04-18 02:15:09.771101','2023-04-18','2023-04-18 02:15:09.771101','2023-04-18',NULL,0,NULL,20,'2023-04-18',1,5),(18,0,'2023-04-18 02:16:57.465710','2023-04-18','2023-04-18 02:16:57.465710','2023-04-18',NULL,0,NULL,0,'2023-04-18',1,5),(19,0,'2023-04-18 02:17:28.544008','2023-04-18','2023-04-18 02:17:28.544008','2023-04-18',NULL,0,NULL,20,'2023-04-18',1,5),(20,0,'2023-04-18 02:20:06.911255','2023-04-18','2023-04-18 02:20:06.911255','2023-04-18',NULL,0,NULL,20,'2023-04-18',1,4);
/*!40000 ALTER TABLE `dataentry_collectorder` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dataentry_collectorder_areas`
--

DROP TABLE IF EXISTS `dataentry_collectorder_areas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dataentry_collectorder_areas` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `collectorder_id` bigint NOT NULL,
  `area_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `DataEntry_collectorder_a_collectorder_id_area_id_b59e3f68_uniq` (`collectorder_id`,`area_id`),
  KEY `DataEntry_collectord_area_id_1e7f4edd_fk_DataEntry` (`area_id`),
  CONSTRAINT `DataEntry_collectord_area_id_1e7f4edd_fk_DataEntry` FOREIGN KEY (`area_id`) REFERENCES `dataentry_area` (`id`),
  CONSTRAINT `DataEntry_collectord_collectorder_id_be9b6d26_fk_DataEntry` FOREIGN KEY (`collectorder_id`) REFERENCES `dataentry_collectorder` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dataentry_collectorder_areas`
--

LOCK TABLES `dataentry_collectorder_areas` WRITE;
/*!40000 ALTER TABLE `dataentry_collectorder_areas` DISABLE KEYS */;
INSERT INTO `dataentry_collectorder_areas` VALUES (1,1,1),(2,2,1),(3,3,1),(4,4,1),(5,6,1),(6,7,1),(7,8,1),(8,9,1),(9,10,1),(10,11,1),(11,12,1),(12,13,1),(13,14,1),(14,15,1),(15,16,1),(16,17,1),(17,19,1),(18,20,1);
/*!40000 ALTER TABLE `dataentry_collectorder_areas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dataentry_collectorder_clients`
--

DROP TABLE IF EXISTS `dataentry_collectorder_clients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dataentry_collectorder_clients` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `collectorder_id` bigint NOT NULL,
  `client_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `DataEntry_collectorder_c_collectorder_id_client_i_641fb557_uniq` (`collectorder_id`,`client_id`),
  KEY `DataEntry_collectord_client_id_d9b339a5_fk_DataEntry` (`client_id`),
  CONSTRAINT `DataEntry_collectord_client_id_d9b339a5_fk_DataEntry` FOREIGN KEY (`client_id`) REFERENCES `dataentry_client` (`id`),
  CONSTRAINT `DataEntry_collectord_collectorder_id_ca713a78_fk_DataEntry` FOREIGN KEY (`collectorder_id`) REFERENCES `dataentry_collectorder` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=54 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dataentry_collectorder_clients`
--

LOCK TABLES `dataentry_collectorder_clients` WRITE;
/*!40000 ALTER TABLE `dataentry_collectorder_clients` DISABLE KEYS */;
INSERT INTO `dataentry_collectorder_clients` VALUES (1,1,9),(2,1,10),(3,1,11),(4,1,12),(5,1,13),(6,1,14),(7,1,15),(8,2,9),(9,2,10),(10,2,11),(11,2,12),(12,2,13),(13,2,14),(14,2,15),(15,3,9),(16,3,10),(17,3,11),(18,3,12),(19,3,13),(20,3,14),(21,3,15),(22,4,10),(23,6,10),(24,6,11),(25,6,12),(26,7,9),(27,7,10),(28,8,9),(29,8,10),(30,9,9),(31,9,10),(32,10,9),(33,10,10),(34,11,9),(35,11,10),(36,12,9),(37,12,10),(38,13,9),(39,13,10),(40,14,9),(41,14,10),(42,14,15),(43,15,9),(44,16,10),(45,16,11),(46,16,12),(47,16,13),(48,16,14),(49,16,15),(50,16,17),(51,17,18),(52,19,18),(53,20,15);
/*!40000 ALTER TABLE `dataentry_collectorder_clients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dataentry_contactrequest`
--

DROP TABLE IF EXISTS `dataentry_contactrequest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dataentry_contactrequest` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `is_deleted` tinyint(1) NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `created_at_date` date DEFAULT NULL,
  `updated_at` datetime(6) DEFAULT NULL,
  `updated_at_date` date DEFAULT NULL,
  `is_test` tinyint(1) NOT NULL,
  `client_id` bigint DEFAULT NULL,
  `contactRequest_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `DataEntry_contactreq_client_id_d8e27ac4_fk_DataEntry` (`client_id`),
  KEY `DataEntry_contactreq_contactRequest_id_46d6024a_fk_DataEntry` (`contactRequest_id`),
  CONSTRAINT `DataEntry_contactreq_client_id_d8e27ac4_fk_DataEntry` FOREIGN KEY (`client_id`) REFERENCES `dataentry_client` (`id`),
  CONSTRAINT `DataEntry_contactreq_contactRequest_id_46d6024a_fk_DataEntry` FOREIGN KEY (`contactRequest_id`) REFERENCES `dataentry_contactrequest` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dataentry_contactrequest`
--

LOCK TABLES `dataentry_contactrequest` WRITE;
/*!40000 ALTER TABLE `dataentry_contactrequest` DISABLE KEYS */;
/*!40000 ALTER TABLE `dataentry_contactrequest` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dataentry_contactrequesttypes`
--

DROP TABLE IF EXISTS `dataentry_contactrequesttypes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dataentry_contactrequesttypes` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `eNum` int DEFAULT NULL,
  `is_test` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dataentry_contactrequesttypes`
--

LOCK TABLES `dataentry_contactrequesttypes` WRITE;
/*!40000 ALTER TABLE `dataentry_contactrequesttypes` DISABLE KEYS */;
/*!40000 ALTER TABLE `dataentry_contactrequesttypes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dataentry_contract`
--

DROP TABLE IF EXISTS `dataentry_contract`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dataentry_contract` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `is_deleted` tinyint(1) NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `created_at_date` date DEFAULT NULL,
  `updated_at` datetime(6) DEFAULT NULL,
  `updated_at_date` date DEFAULT NULL,
  `serialNum` int DEFAULT NULL,
  `created_prev_date` date DEFAULT NULL,
  `notes` longtext,
  `is_test` tinyint(1) NOT NULL,
  `belong_to_id` bigint DEFAULT NULL,
  `client_id` bigint DEFAULT NULL,
  `created_by_id` bigint DEFAULT NULL,
  `modified_by_id` bigint DEFAULT NULL,
  `lastPay` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `serialNum` (`serialNum`),
  UNIQUE KEY `client_id` (`client_id`),
  KEY `DataEntry_contract_belong_to_id_874b1068_fk_DataEntry` (`belong_to_id`),
  KEY `DataEntry_contract_created_by_id_4051be4f_fk_DataEntry` (`created_by_id`),
  KEY `DataEntry_contract_modified_by_id_9f38184a_fk_DataEntry` (`modified_by_id`),
  CONSTRAINT `DataEntry_contract_belong_to_id_874b1068_fk_DataEntry` FOREIGN KEY (`belong_to_id`) REFERENCES `dataentry_employee` (`id`),
  CONSTRAINT `DataEntry_contract_client_id_a0a61c0b_fk_DataEntry_client_id` FOREIGN KEY (`client_id`) REFERENCES `dataentry_client` (`id`),
  CONSTRAINT `DataEntry_contract_created_by_id_4051be4f_fk_DataEntry` FOREIGN KEY (`created_by_id`) REFERENCES `dataentry_employee` (`id`),
  CONSTRAINT `DataEntry_contract_modified_by_id_9f38184a_fk_DataEntry` FOREIGN KEY (`modified_by_id`) REFERENCES `dataentry_employee` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dataentry_contract`
--

LOCK TABLES `dataentry_contract` WRITE;
/*!40000 ALTER TABLE `dataentry_contract` DISABLE KEYS */;
INSERT INTO `dataentry_contract` VALUES (6,0,'2023-04-04 02:25:43.000000','2023-04-04','2023-04-07 19:56:57.929335','2023-04-07',98,'2023-04-04',NULL,0,3,82,2,NULL,NULL),(8,0,'2023-04-04 02:51:04.000000','2023-04-04','2023-04-07 19:56:57.919575','2023-04-07',2,'2023-04-04',NULL,0,3,84,2,NULL,NULL),(9,0,'2023-04-04 04:23:10.000000','2023-04-04','2023-04-09 14:29:27.485364','2023-04-09',775,'2023-04-09',NULL,0,3,4,2,NULL,NULL),(10,0,'2023-04-04 04:23:38.000000','2023-04-04','2023-04-07 19:56:57.897127','2023-04-07',744,'2023-04-04',NULL,0,3,6,2,NULL,NULL),(11,0,'2023-04-06 01:54:23.000000','2023-04-06','2023-04-07 19:56:57.888343','2023-04-07',695,'2023-04-06',NULL,0,2,7,2,NULL,NULL),(12,0,'2023-04-06 02:16:00.000000','2023-04-06','2023-04-07 19:56:57.877607','2023-04-07',145,'2023-04-06',NULL,0,3,8,2,NULL,NULL),(13,0,'2023-04-06 02:17:59.000000','2023-04-06','2023-04-07 19:56:57.866871','2023-04-07',146,'2023-04-06',NULL,0,3,9,2,NULL,NULL),(14,0,'2023-04-06 03:07:01.000000','2023-04-06','2023-04-07 19:56:57.857111','2023-04-07',492,'2023-04-06',NULL,0,3,10,2,NULL,NULL),(15,0,'2023-04-06 03:07:54.000000','2023-04-06','2023-04-07 19:56:57.846818','2023-04-07',493,'2023-04-06',NULL,0,3,11,2,NULL,NULL),(16,0,'2023-04-06 20:19:57.547000','2023-04-06','2023-04-06 20:19:57.567000','2023-04-06',494,'2023-04-06',NULL,0,3,12,2,NULL,NULL),(17,0,'2023-04-16 21:17:07.362497','2023-04-16','2023-04-16 21:17:07.379414','2023-04-16',56,'2023-04-16',NULL,0,3,85,2,NULL,NULL),(18,0,'2023-04-18 01:46:23.159834','2023-04-18','2023-04-18 01:48:23.031583','2023-04-18',1183,'2023-04-04','',0,3,15,2,NULL,'2023-03-18');
/*!40000 ALTER TABLE `dataentry_contract` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dataentry_contract_services`
--

DROP TABLE IF EXISTS `dataentry_contract_services`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dataentry_contract_services` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `contract_id` bigint NOT NULL,
  `service_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `DataEntry_contract_services_contract_id_service_id_27c5a325_uniq` (`contract_id`,`service_id`),
  KEY `DataEntry_contract_s_service_id_502d2dde_fk_DataEntry` (`service_id`),
  CONSTRAINT `DataEntry_contract_s_contract_id_b938a3d9_fk_DataEntry` FOREIGN KEY (`contract_id`) REFERENCES `dataentry_contract` (`id`),
  CONSTRAINT `DataEntry_contract_s_service_id_502d2dde_fk_DataEntry` FOREIGN KEY (`service_id`) REFERENCES `dataentry_service` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dataentry_contract_services`
--

LOCK TABLES `dataentry_contract_services` WRITE;
/*!40000 ALTER TABLE `dataentry_contract_services` DISABLE KEYS */;
INSERT INTO `dataentry_contract_services` VALUES (6,6,18),(8,8,21),(19,9,28),(22,9,29),(11,10,24),(12,11,24),(13,12,24),(14,13,24),(15,14,24),(16,15,24),(17,16,24),(18,16,25),(23,17,31),(24,18,32);
/*!40000 ALTER TABLE `dataentry_contract_services` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dataentry_departement`
--

DROP TABLE IF EXISTS `dataentry_departement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dataentry_departement` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `is_deleted` tinyint(1) NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `created_at_date` date DEFAULT NULL,
  `updated_at` datetime(6) DEFAULT NULL,
  `updated_at_date` date DEFAULT NULL,
  `name` varchar(50) NOT NULL,
  `notes` longtext,
  `is_test` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dataentry_departement`
--

LOCK TABLES `dataentry_departement` WRITE;
/*!40000 ALTER TABLE `dataentry_departement` DISABLE KEYS */;
INSERT INTO `dataentry_departement` VALUES (1,0,'2023-03-12 22:31:56.000000','2023-03-13','2023-04-07 19:56:08.385820','2023-04-07','╪º╪»╪«╪º┘ä ╪º┘ä╪¿┘è╪º┘å╪º╪¬ ┘ê╪º┘ä╪¬╪¡╪╡┘è┘ä','╪º╪»╪«╪º┘ä ╪º┘ä╪¿┘è╪º┘å╪º╪¬ ┘ê╪º┘ä╪¬╪¡╪╡┘è┘ä',1),(2,0,'2023-03-12 22:41:22.000000','2023-03-13','2023-04-07 19:56:08.382893','2023-04-07','╪«╪»┘à╪⌐ ╪º┘ä╪╣┘à┘ä╪º╪í',NULL,1);
/*!40000 ALTER TABLE `dataentry_departement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dataentry_employee`
--

DROP TABLE IF EXISTS `dataentry_employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dataentry_employee` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `is_deleted` tinyint(1) NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `created_at_date` date DEFAULT NULL,
  `updated_at` datetime(6) DEFAULT NULL,
  `updated_at_date` date DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `role` varchar(50) DEFAULT NULL,
  `job2` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL,
  `phone` varchar(11) DEFAULT NULL,
  `jobTitle` varchar(50) DEFAULT NULL,
  `dateOfEmployment` date DEFAULT NULL,
  `created_prev_date` date DEFAULT NULL,
  `dateOfBirth` date DEFAULT NULL,
  `naId` varchar(14) DEFAULT NULL,
  `typee` varchar(50) DEFAULT NULL,
  `salaryType` varchar(50) DEFAULT NULL,
  `salary` int DEFAULT NULL,
  `eNum` int DEFAULT NULL,
  `notes` longtext,
  `is_test` tinyint(1) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `departement_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `eNum` (`eNum`),
  KEY `DataEntry_employee_departement_id_2f5e3ce8_fk_DataEntry` (`departement_id`),
  CONSTRAINT `DataEntry_employee_departement_id_2f5e3ce8_fk_DataEntry` FOREIGN KEY (`departement_id`) REFERENCES `dataentry_departement` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dataentry_employee`
--

LOCK TABLES `dataentry_employee` WRITE;
/*!40000 ALTER TABLE `dataentry_employee` DISABLE KEYS */;
INSERT INTO `dataentry_employee` VALUES (1,0,'2023-03-12 22:33:10.000000','2023-03-13','2023-04-07 19:56:20.266010','2023-04-07','╪┤┘è┘à╪º╪í ╪º╪¡┘à╪»','┘à╪│╪ñ┘ê┘ä ╪º╪»╪«╪º┘ä ╪¿┘è╪º┘å╪º╪¬','dataEntry',NULL,'sh123456','╪º╪│┘ê╪º┘å - ╪º┘ä╪│┘è┘ä','01078955641','┘à╪│╪ñ┘ê┘ä ╪º╪»╪«╪º┘ä ╪¿┘è╪º┘å╪º╪¬','2023-03-12','2023-03-12','2001-03-12','30103122800904','┘à┘ê╪╕┘ü','╪┤┘ç╪▒┘ë',2500,3,NULL,1,'2023-03-12 22:33:08.000000',1),(2,0,'2023-03-12 22:42:14.000000','2023-03-13','2023-04-07 19:56:20.260154','2023-04-07','╪│╪º╪▒╪⌐ ╪╣╪º╪»┘ä','┘à╪│╪ñ┘ê┘ä ╪«╪»┘à╪⌐ ╪╣┘à┘ä╪º╪í','customer service',NULL,'sar1234567',NULL,'0127485647','┘à╪│╪ñ┘ê┘ä ╪«╪»┘à╪⌐ ╪╣┘à┘ä╪º╪í','2023-03-12','2023-03-12','2002-03-12','30203122800056','┘à┘ê╪╕┘ü','╪┤┘ç╪▒┘ë',2500,6,NULL,1,'2023-03-12 22:42:13.000000',2),(3,0,'2023-04-03 23:56:53.000000','2023-04-04','2023-04-07 19:56:20.255274','2023-04-07','╪¿╪»┘ê┘å','placeholder','non',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,1,NULL,1),(4,0,'2023-04-13 07:19:57.423655','2023-04-13','2023-04-13 07:19:57.423655','2023-04-13','╪º┘è┘à┘å ┘à╪¡┘à╪» ╪º┘ä╪│┘è╪»','┘à╪│╪ª┘ê┘ä ╪¬╪¡╪╡┘è┘ä','collector',NULL,NULL,'╪º╪│┘ê╪º┘å - ╪º┘ä╪│┘è┘ä ╪º┘ä╪▒┘è┘ü┘ë','01145988513','┘à╪│╪ª┘ê┘ä ╪¬╪¡╪╡┘è┘ä','2023-04-01','2023-04-13','2023-04-13','29854688956146','┘à┘ê╪╕┘ü','╪┤┘ç╪▒┘ë',3100,11,'',1,NULL,1),(5,0,'2023-04-13 07:21:24.422913','2023-04-13','2023-04-13 07:21:24.422913','2023-04-13','┘à╪¡┘à╪» ╪╣┘ä┘ë ╪¡╪│┘è┘å','┘à╪│╪ª┘ê┘ä ╪¬╪¡╪╡┘è┘ä','collector',NULL,NULL,'╪º╪│┘ê╪º┘å - ╪º┘ä╪╡╪»╪º┘é╪⌐ ╪º┘ä╪¼╪»┘è╪»╪⌐','01044568895','┘à╪│╪ª┘ê┘ä ╪¬╪¡╪╡┘è┘ä','2023-03-13','2023-04-13','2023-04-13','29955664784546','┘à┘ê╪╕┘ü','╪┤┘ç╪▒┘ë',3100,16,'',1,NULL,1);
/*!40000 ALTER TABLE `dataentry_employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dataentry_followcontractservices`
--

DROP TABLE IF EXISTS `dataentry_followcontractservices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dataentry_followcontractservices` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `is_deleted` tinyint(1) NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `created_at_date` date DEFAULT NULL,
  `updated_at` datetime(6) DEFAULT NULL,
  `updated_at_date` date DEFAULT NULL,
  `area` varchar(50) DEFAULT NULL,
  `startingDate` date DEFAULT NULL,
  `serviceDueDate` date DEFAULT NULL,
  `serviceCollectDayStart` int DEFAULT NULL,
  `serviceCollectDayEnd` int DEFAULT NULL,
  `serviceDueStatus` varchar(50) DEFAULT NULL,
  `collcetStatusNums` varchar(50) DEFAULT NULL,
  `total_amount` int DEFAULT NULL,
  `collected_amount` int DEFAULT NULL,
  `collected_month` int DEFAULT NULL,
  `collected_date` date DEFAULT NULL,
  `remain_amount` int DEFAULT NULL,
  `created_prev_date` date DEFAULT NULL,
  `is_test` tinyint(1) NOT NULL,
  `client_id` bigint DEFAULT NULL,
  `created_by_id` bigint DEFAULT NULL,
  `modified_by_id` bigint DEFAULT NULL,
  `service_id` bigint DEFAULT NULL,
  `notes` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `DataEntry_followcont_client_id_91371deb_fk_DataEntry` (`client_id`),
  KEY `DataEntry_followcont_created_by_id_a076735f_fk_DataEntry` (`created_by_id`),
  KEY `DataEntry_followcont_modified_by_id_c4257b71_fk_DataEntry` (`modified_by_id`),
  KEY `DataEntry_followcont_service_id_6cb82b99_fk_DataEntry` (`service_id`),
  KEY `DataEntry_followcontractservices_collcetStatusNums_9b310456` (`collcetStatusNums`),
  CONSTRAINT `DataEntry_followcont_client_id_91371deb_fk_DataEntry` FOREIGN KEY (`client_id`) REFERENCES `dataentry_client` (`id`),
  CONSTRAINT `DataEntry_followcont_created_by_id_a076735f_fk_DataEntry` FOREIGN KEY (`created_by_id`) REFERENCES `dataentry_employee` (`id`),
  CONSTRAINT `DataEntry_followcont_modified_by_id_c4257b71_fk_DataEntry` FOREIGN KEY (`modified_by_id`) REFERENCES `dataentry_employee` (`id`),
  CONSTRAINT `DataEntry_followcont_service_id_6cb82b99_fk_DataEntry` FOREIGN KEY (`service_id`) REFERENCES `dataentry_service` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dataentry_followcontractservices`
--

LOCK TABLES `dataentry_followcontractservices` WRITE;
/*!40000 ALTER TABLE `dataentry_followcontractservices` DISABLE KEYS */;
INSERT INTO `dataentry_followcontractservices` VALUES (6,0,'2023-04-04 02:25:43.000000','2023-04-04','2023-04-07 19:57:45.419574','2023-04-07','┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒',NULL,NULL,25,5,'┘ä┘à ┘è╪¬┘à ╪º╪»╪º╪í ╪º┘ä╪«╪»┘à╪⌐','┘ü┘ë ╪º┘å╪¬╪╕╪º╪▒ ┘à┘è╪╣╪º╪» ╪º┘ä╪¬╪¡╪╡┘è┘ä',60,0,5,NULL,60,NULL,0,82,2,NULL,18,NULL),(7,0,'2023-04-04 02:31:46.000000','2023-04-04','2023-04-07 19:57:45.407861','2023-04-07','┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒',NULL,NULL,25,5,'┘ä┘à ┘è╪¬┘à ╪º╪»╪º╪í ╪º┘ä╪«╪»┘à╪⌐','┘ü┘ë ╪º┘å╪¬╪╕╪º╪▒ ┘à┘è╪╣╪º╪» ╪º┘ä╪¬╪¡╪╡┘è┘ä',123,0,5,NULL,123,NULL,0,84,2,NULL,20,NULL),(8,0,'2023-04-04 02:51:04.000000','2023-04-04','2023-04-07 19:57:45.393657','2023-04-07','┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒',NULL,NULL,25,5,'┘ä┘à ┘è╪¬┘à ╪º╪»╪º╪í ╪º┘ä╪«╪»┘à╪⌐','┘ü┘ë ╪º┘å╪¬╪╕╪º╪▒ ┘à┘è╪╣╪º╪» ╪º┘ä╪¬╪¡╪╡┘è┘ä',20,0,5,NULL,20,NULL,0,84,2,NULL,21,NULL),(9,0,'2023-04-04 04:23:10.000000','2023-04-04','2023-04-08 02:25:12.786169','2023-04-08','┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒',NULL,NULL,25,5,'┘ä┘à ┘è╪¬┘à ╪º╪»╪º╪í ╪º┘ä╪«╪»┘à╪⌐','┘à╪╖┘ä┘ê╪¿ ╪º┘ä╪»┘ü╪╣',40,0,4,NULL,40,NULL,0,4,2,NULL,27,NULL),(10,0,'2023-04-04 04:23:10.000000','2023-04-04','2023-04-08 02:05:54.374022','2023-04-08','┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒',NULL,NULL,25,5,'┘ä┘à ┘è╪¬┘à ╪º╪»╪º╪í ╪º┘ä╪«╪»┘à╪⌐','┘à╪╖┘ä┘ê╪¿ ╪º┘ä╪»┘ü╪╣',60,0,4,NULL,60,NULL,0,4,2,NULL,26,NULL),(11,0,'2023-04-04 04:23:38.000000','2023-04-04','2023-04-07 19:57:45.363396','2023-04-07','┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒',NULL,NULL,25,5,'┘ä┘à ┘è╪¬┘à ╪º╪»╪º╪í ╪º┘ä╪«╪»┘à╪⌐','┘à╪╖┘ä┘ê╪¿ ╪º┘ä╪»┘ü╪╣',20,0,4,NULL,20,NULL,0,6,2,NULL,24,NULL),(12,0,'2023-04-06 01:54:23.000000','2023-04-06','2023-04-07 19:57:45.354613','2023-04-07','┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒',NULL,NULL,25,5,'┘ä┘à ┘è╪¬┘à ╪º╪»╪º╪í ╪º┘ä╪«╪»┘à╪⌐','┘à╪╖┘ä┘ê╪¿ ╪º┘ä╪»┘ü╪╣',20,0,4,NULL,20,NULL,0,7,2,NULL,24,NULL),(13,0,'2023-04-06 02:16:00.000000','2023-04-06','2023-04-07 19:57:45.346804','2023-04-07','┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒',NULL,NULL,25,5,'┘ä┘à ┘è╪¬┘à ╪º╪»╪º╪í ╪º┘ä╪«╪»┘à╪⌐','┘à╪╖┘ä┘ê╪¿ ╪º┘ä╪»┘ü╪╣',20,0,4,NULL,20,NULL,0,8,2,NULL,24,NULL),(14,0,'2023-04-06 02:17:59.000000','2023-04-06','2023-04-07 19:57:45.337045','2023-04-07','┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒',NULL,NULL,25,5,'┘ä┘à ┘è╪¬┘à ╪º╪»╪º╪í ╪º┘ä╪«╪»┘à╪⌐','┘à╪╖┘ä┘ê╪¿ ╪º┘ä╪»┘ü╪╣',20,0,4,NULL,20,NULL,0,9,2,NULL,24,NULL),(15,0,'2023-04-06 03:07:01.000000','2023-04-06','2023-04-07 19:57:45.328260','2023-04-07','┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒',NULL,NULL,25,5,'┘ä┘à ┘è╪¬┘à ╪º╪»╪º╪í ╪º┘ä╪«╪»┘à╪⌐','┘à╪╖┘ä┘ê╪¿ ╪º┘ä╪»┘ü╪╣',20,0,4,NULL,20,NULL,0,10,2,NULL,24,NULL),(16,0,'2023-04-06 03:07:54.000000','2023-04-06','2023-04-07 19:57:45.320452','2023-04-07','┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒',NULL,NULL,25,5,'┘ä┘à ┘è╪¬┘à ╪º╪»╪º╪í ╪º┘ä╪«╪»┘à╪⌐','┘à╪╖┘ä┘ê╪¿ ╪º┘ä╪»┘ü╪╣',20,0,4,NULL,20,NULL,0,11,2,NULL,24,NULL),(17,0,'2023-04-06 20:19:57.591000','2023-04-06','2023-04-06 20:19:57.591000','2023-04-06','-',NULL,NULL,25,5,'Γöÿ├ñΓöÿ├á Γöÿ├¿Γò¬┬¼Γöÿ├á Γò¬┬║Γò¬┬╗Γò¬┬║Γò¬├¡ Γò¬┬║Γöÿ├ñΓò¬┬½Γò¬┬╗Γöÿ├áΓò¬ΓîÉ','Γöÿ├áΓò¬ΓòûΓöÿ├ñΓöÿ├¬Γò¬┬┐ Γò¬┬║Γöÿ├ñΓò¬┬╗Γöÿ├╝Γò¬Γòú',20,0,4,NULL,20,NULL,0,12,2,NULL,24,NULL),(18,0,'2023-04-06 20:19:57.606000','2023-04-06','2023-04-06 20:19:57.606000','2023-04-06','-',NULL,NULL,25,5,'Γöÿ├ñΓöÿ├á Γöÿ├¿Γò¬┬¼Γöÿ├á Γò¬┬║Γò¬┬╗Γò¬┬║Γò¬├¡ Γò¬┬║Γöÿ├ñΓò¬┬½Γò¬┬╗Γöÿ├áΓò¬ΓîÉ','Γöÿ├áΓò¬ΓòûΓöÿ├ñΓöÿ├¬Γò¬┬┐ Γò¬┬║Γöÿ├ñΓò¬┬╗Γöÿ├╝Γò¬Γòú',200,0,4,NULL,200,NULL,0,12,2,NULL,25,NULL),(19,0,'2023-04-08 10:36:23.863319','2023-04-08','2023-04-09 14:29:27.494218','2023-04-09','-',NULL,NULL,25,5,'┘ä┘à ┘è╪¬┘à ╪º╪»╪º╪í ╪º┘ä╪«╪»┘à╪⌐','┘à╪╖┘ä┘ê╪¿ ╪º┘ä╪»┘ü╪╣',40,0,4,NULL,40,NULL,0,4,2,NULL,28,NULL),(20,0,'2023-04-08 10:36:23.870709','2023-04-08','2023-04-09 14:29:27.501455','2023-04-09','-',NULL,NULL,25,5,'┘ä┘à ┘è╪¬┘à ╪º╪»╪º╪í ╪º┘ä╪«╪»┘à╪⌐','┘à╪╖┘ä┘ê╪¿ ╪º┘ä╪»┘ü╪╣',60,0,4,NULL,60,NULL,0,4,2,NULL,29,NULL),(21,0,'2023-04-08 15:03:44.965421','2023-04-08','2023-04-08 15:03:44.965421','2023-04-08','-',NULL,NULL,25,5,'┘ä┘à ┘è╪¬┘à ╪º╪»╪º╪í ╪º┘ä╪«╪»┘à╪⌐','┘à╪╖┘ä┘ê╪¿ ╪º┘ä╪»┘ü╪╣',60,0,4,NULL,60,NULL,0,4,2,NULL,30,NULL),(22,0,'2023-04-16 21:17:07.398682','2023-04-16','2023-04-16 21:17:07.398682','2023-04-16','-',NULL,NULL,25,5,'┘ä┘à ┘è╪¬┘à ╪º╪»╪º╪í ╪º┘ä╪«╪»┘à╪⌐','┘à╪╖┘ä┘ê╪¿ ╪º┘ä╪»┘ü╪╣',30,0,4,NULL,30,NULL,0,85,2,NULL,31,NULL),(23,0,'2023-04-18 01:46:23.181775','2023-04-18','2023-04-18 02:07:59.056159','2023-04-18','-',NULL,NULL,25,5,'╪¬┘à ╪º╪»╪º╪í ╪º┘ä╪«╪»┘à╪⌐','╪¼╪º╪▒┘ë ╪º┘ä╪¬╪¡╪╡┘è┘ä',20,0,4,NULL,20,NULL,0,15,2,NULL,32,NULL);
/*!40000 ALTER TABLE `dataentry_followcontractservices` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dataentry_offers`
--

DROP TABLE IF EXISTS `dataentry_offers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dataentry_offers` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `is_deleted` tinyint(1) NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `created_at_date` date DEFAULT NULL,
  `updated_at` datetime(6) DEFAULT NULL,
  `updated_at_date` date DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `image` varchar(100) NOT NULL,
  `is_test` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dataentry_offers`
--

LOCK TABLES `dataentry_offers` WRITE;
/*!40000 ALTER TABLE `dataentry_offers` DISABLE KEYS */;
/*!40000 ALTER TABLE `dataentry_offers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dataentry_requestsimpleservice`
--

DROP TABLE IF EXISTS `dataentry_requestsimpleservice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dataentry_requestsimpleservice` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `is_deleted` tinyint(1) NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `created_at_date` date DEFAULT NULL,
  `updated_at` datetime(6) DEFAULT NULL,
  `updated_at_date` date DEFAULT NULL,
  `is_test` tinyint(1) NOT NULL,
  `client_id` bigint DEFAULT NULL,
  `service_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `DataEntry_requestsim_client_id_3cd9d317_fk_DataEntry` (`client_id`),
  KEY `DataEntry_requestsim_service_id_9d0eb9d4_fk_DataEntry` (`service_id`),
  CONSTRAINT `DataEntry_requestsim_client_id_3cd9d317_fk_DataEntry` FOREIGN KEY (`client_id`) REFERENCES `dataentry_client` (`id`),
  CONSTRAINT `DataEntry_requestsim_service_id_9d0eb9d4_fk_DataEntry` FOREIGN KEY (`service_id`) REFERENCES `dataentry_simpleservice` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dataentry_requestsimpleservice`
--

LOCK TABLES `dataentry_requestsimpleservice` WRITE;
/*!40000 ALTER TABLE `dataentry_requestsimpleservice` DISABLE KEYS */;
/*!40000 ALTER TABLE `dataentry_requestsimpleservice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dataentry_service`
--

DROP TABLE IF EXISTS `dataentry_service`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dataentry_service` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `is_deleted` tinyint(1) NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `created_at_date` date DEFAULT NULL,
  `updated_at` datetime(6) DEFAULT NULL,
  `updated_at_date` date DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `is_main` tinyint(1) NOT NULL,
  `price` int NOT NULL,
  `billSerial` int DEFAULT NULL,
  `billed_at` date DEFAULT NULL,
  `fixedDeliveryDate` int DEFAULT NULL,
  `fixedPriceCollectDate` int DEFAULT NULL,
  `fixedPriceCollectDate_more` date DEFAULT NULL,
  `notes` longtext,
  `is_test` tinyint(1) NOT NULL,
  `priceType` longtext,
  `supervisor_id` bigint DEFAULT NULL,
  `typee` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `billSerial` (`billSerial`),
  KEY `DataEntry_service_supervisor_id_c3abb2eb_fk_DataEntry` (`supervisor_id`),
  CONSTRAINT `DataEntry_service_supervisor_id_c3abb2eb_fk_DataEntry` FOREIGN KEY (`supervisor_id`) REFERENCES `dataentry_employee` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dataentry_service`
--

LOCK TABLES `dataentry_service` WRITE;
/*!40000 ALTER TABLE `dataentry_service` DISABLE KEYS */;
INSERT INTO `dataentry_service` VALUES (10,0,'2023-04-04 00:07:06.000000','2023-04-04','2023-04-07 19:57:11.950950','2023-04-07','╪¬┘å╪╕┘è┘ü ┘à┘å╪▓┘ä┘ë ╪¿╪│┘è╪╖',0,20,NULL,NULL,1,25,NULL,NULL,1,NULL,NULL,'continuous'),(11,0,'2023-04-04 00:07:06.000000','2023-04-04','2023-04-07 19:57:11.948022','2023-04-07','╪¬┘å╪╕┘è┘ü ┘à┘å╪▓┘ä┘ë - ╪╣┘à┘è┘é ',0,60,NULL,NULL,1,25,NULL,NULL,1,NULL,NULL,'month'),(12,0,'2023-04-04 00:07:06.000000','2023-04-04','2023-04-07 19:57:11.944118','2023-04-07','╪¬┘å╪╕┘è┘ü ╪│┘ä╪º┘ä┘à ╪╣┘à╪º╪▒╪⌐',0,50,NULL,NULL,1,25,NULL,NULL,1,NULL,NULL,'once'),(13,0,'2023-04-04 00:36:46.000000','2023-04-04','2023-04-07 19:57:11.941190','2023-04-07','╪¼┘à╪╣ ┘à┘å╪▓┘ä┘ë',0,20,NULL,NULL,1,25,NULL,NULL,1,NULL,NULL,'continuous'),(14,0,'2023-04-04 01:01:59.000000','2023-04-04','2023-04-07 19:57:11.937286','2023-04-07','╪▒╪┤ ┘ê╪¬╪╣┘é┘è┘à',0,60,NULL,NULL,1,25,NULL,NULL,1,NULL,NULL,'month'),(15,0,'2023-04-04 01:01:59.000000','2023-04-04','2023-04-07 19:57:11.934358','2023-04-07','╪¼┘à╪╣ ┘à┘å╪▓┘ä┘ë',0,30,NULL,NULL,1,25,NULL,NULL,1,NULL,NULL,'once'),(16,0,'2023-04-04 01:04:33.000000','2023-04-04','2023-04-07 19:57:11.930454','2023-04-07',' ╪▒╪┤ ┘ê╪¬╪╣┘é┘è┘à ',0,60,NULL,NULL,1,25,NULL,NULL,1,NULL,NULL,'month'),(17,0,'2023-04-04 01:04:33.000000','2023-04-04','2023-04-07 19:57:11.927526','2023-04-07','╪¼┘à╪╣ ┘à┘å╪▓┘ä┘ë',0,40,NULL,NULL,1,25,NULL,NULL,1,NULL,NULL,'once'),(18,0,'2023-04-04 02:25:43.000000','2023-04-04','2023-04-07 19:57:11.924598','2023-04-07','╪¼┘à╪╣ ┘à┘å╪▓┘ä┘ë',0,60,NULL,NULL,1,25,NULL,NULL,1,NULL,NULL,'once'),(19,0,'2023-04-04 02:28:01.000000','2023-04-04','2023-04-07 19:57:11.921670','2023-04-07',' ╪¼┘à╪╣ ┘à┘å╪▓┘ä┘ë',0,40,NULL,NULL,1,25,NULL,NULL,1,NULL,NULL,'month'),(20,0,'2023-04-04 02:31:46.000000','2023-04-04','2023-04-07 19:57:11.918743','2023-04-07','┘ä╪¬╪º┘ä╪¬',0,123,NULL,NULL,1,25,NULL,NULL,1,NULL,NULL,'continuous'),(21,0,'2023-04-04 02:51:04.000000','2023-04-04','2023-04-07 19:57:11.915814','2023-04-07','╪¼┘à╪╣ ┘à┘å╪▓┘ä┘ë',0,20,NULL,NULL,1,25,NULL,NULL,1,'weekly',NULL,'continuous'),(22,0,'2023-04-04 04:23:10.000000','2023-04-04','2023-04-07 19:57:11.912886','2023-04-07','╪¬┘å╪╕┘è┘ü ┘à┘å╪▓┘ä┘ë ╪¿╪│┘è╪╖',0,20,NULL,NULL,1,25,NULL,NULL,1,'weekly',NULL,'continuous'),(23,0,'2023-04-04 04:23:10.000000','2023-04-04','2023-04-07 19:57:11.909958','2023-04-07','╪¬┘å╪╕┘è┘ü ┘à┘å╪▓┘ä┘ë - ╪╣┘à┘è┘é',0,90,NULL,NULL,1,25,NULL,NULL,1,'once',NULL,'once'),(24,0,'2023-04-04 04:23:38.000000','2023-04-04','2023-04-07 19:57:11.907030','2023-04-07','╪¼┘à╪╣ ┘à┘å╪▓┘ä┘ë',0,20,NULL,NULL,1,25,NULL,NULL,1,'month',NULL,'continuous'),(25,0,'2023-04-06 20:19:57.493000','2023-04-06','2023-04-07 19:57:26.079146','2023-04-07','╪¼┘à╪╣ ┘à┘å╪▓┘ä┘ë',0,200,NULL,NULL,1,25,NULL,'',1,'once',NULL,'once'),(26,0,'2023-04-08 01:33:05.976348','2023-04-08','2023-04-08 02:04:45.685414','2023-04-08','╪¬┘å╪╕┘è┘ü  ┘à┘å╪▓┘ä┘ë - ╪╣┘à┘è┘é',0,60,NULL,NULL,1,25,NULL,'',1,'month',NULL,'╪«╪»┘è╪¼┘ç ┘à╪¡┘à╪» ╪¡╪│┘å'),(27,0,'2023-04-08 02:03:25.802889','2023-04-08','2023-04-08 02:05:17.838731','2023-04-08','╪¬┘å╪╕┘è┘ü ┘à┘å╪▓┘ä┘ë  - ╪¿╪│┘è╪╖',0,40,NULL,NULL,1,25,NULL,'',1,'month',NULL,'continuous'),(28,0,'2023-04-08 10:28:20.908262','2023-04-08','2023-04-08 10:28:20.908262','2023-04-08','╪¬┘å╪╕┘è┘ü ┘à┘å╪▓┘ä┘ë ╪¿╪│┘è╪╖',0,40,NULL,NULL,1,25,NULL,NULL,1,'month',NULL,'continuous'),(29,0,'2023-04-08 10:28:21.009348','2023-04-08','2023-04-08 10:28:21.009348','2023-04-08','╪¬┘å╪╕┘è┘ü ┘à┘å╪▓┘ä┘ë ╪╣┘à┘è┘é',0,60,NULL,NULL,1,25,NULL,NULL,1,'month',NULL,'continuous'),(30,0,'2023-04-08 15:03:44.922475','2023-04-08','2023-04-08 15:03:44.922475','2023-04-08',' ╪¬┘å╪╕┘è┘ü ┘à┘å╪▓┘ä┘ë ╪╣┘à┘è┘é',0,60,NULL,NULL,1,25,NULL,NULL,1,'month',NULL,'continuous'),(31,0,'2023-04-16 21:17:07.323560','2023-04-16','2023-04-16 21:17:07.323560','2023-04-16','fghg',0,30,NULL,NULL,1,25,NULL,NULL,1,'month',NULL,'continuous'),(32,0,'2023-04-18 01:46:23.126920','2023-04-18','2023-04-18 01:47:05.326257','2023-04-18','╪¼┘à╪╣ ┘à┘å╪▓┘ä┘ë',0,45,NULL,NULL,1,25,NULL,'',1,'month',NULL,'continuous');
/*!40000 ALTER TABLE `dataentry_service` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dataentry_simpleservice`
--

DROP TABLE IF EXISTS `dataentry_simpleservice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dataentry_simpleservice` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `is_deleted` tinyint(1) NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `created_at_date` date DEFAULT NULL,
  `updated_at` datetime(6) DEFAULT NULL,
  `updated_at_date` date DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `eNum` int DEFAULT NULL,
  `is_test` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dataentry_simpleservice`
--

LOCK TABLES `dataentry_simpleservice` WRITE;
/*!40000 ALTER TABLE `dataentry_simpleservice` DISABLE KEYS */;
/*!40000 ALTER TABLE `dataentry_simpleservice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dataentry_subservice`
--

DROP TABLE IF EXISTS `dataentry_subservice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dataentry_subservice` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `is_deleted` tinyint(1) NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `created_at_date` date DEFAULT NULL,
  `updated_at` datetime(6) DEFAULT NULL,
  `updated_at_date` date DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `price` int DEFAULT NULL,
  `baseService_id` bigint DEFAULT NULL,
  `typee_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `DataEntry_subservice_baseService_id_2d39e50a_fk_DataEntry` (`baseService_id`),
  KEY `DataEntry_subservice_typee_id_7cc15568_fk_DataEntry_typee_id` (`typee_id`),
  CONSTRAINT `DataEntry_subservice_baseService_id_2d39e50a_fk_DataEntry` FOREIGN KEY (`baseService_id`) REFERENCES `dataentry_service` (`id`),
  CONSTRAINT `DataEntry_subservice_typee_id_7cc15568_fk_DataEntry_typee_id` FOREIGN KEY (`typee_id`) REFERENCES `dataentry_typee` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dataentry_subservice`
--

LOCK TABLES `dataentry_subservice` WRITE;
/*!40000 ALTER TABLE `dataentry_subservice` DISABLE KEYS */;
/*!40000 ALTER TABLE `dataentry_subservice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dataentry_typee`
--

DROP TABLE IF EXISTS `dataentry_typee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dataentry_typee` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dataentry_typee`
--

LOCK TABLES `dataentry_typee` WRITE;
/*!40000 ALTER TABLE `dataentry_typee` DISABLE KEYS */;
/*!40000 ALTER TABLE `dataentry_typee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=308 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2023-03-12 22:29:31.027000','2','dataEntry1',1,'[{\"added\": {}}]',4,1),(2,'2023-03-12 22:30:07.141000','2','dataEntry1',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Staff status\"]}}]',4,1),(3,'2023-03-12 22:31:56.222000','1','Γò¬┬║Γò¬┬╗Γò¬┬½Γò¬┬║Γöÿ├ñ Γò¬┬║Γöÿ├ñΓò¬┬┐Γöÿ├¿Γò¬┬║Γöÿ├ÑΓò¬┬║Γò¬┬¼ Γöÿ├¬Γò¬┬║Γöÿ├ñΓò¬┬¼Γò¬┬íΓò¬ΓòíΓöÿ├¿Γöÿ├ñ',1,'[{\"added\": {}}]',10,1),(4,'2023-03-12 22:33:10.795000','1','Γò¬ΓöñΓöÿ├¿Γöÿ├áΓò¬┬║Γò¬├¡ Γò¬┬║Γò¬┬íΓöÿ├áΓò¬┬╗',1,'[{\"added\": {}}]',11,1),(5,'2023-03-12 22:38:01.204000','1','Γò¬ΓöñΓöÿ├¿Γöÿ├áΓò¬┬║Γò¬├¡ Γò¬┬║Γò¬┬íΓöÿ├áΓò¬┬╗',2,'[{\"changed\": {\"fields\": [\"\\u0643\\u0644\\u0645\\u0629 \\u0627\\u0644\\u0633\\u0631\"]}}]',11,1),(6,'2023-03-12 22:40:10.573000','3','customerService1',1,'[{\"added\": {}}]',4,1),(7,'2023-03-12 22:40:52.392000','3','customerService1',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Staff status\", \"Last login\"]}}]',4,1),(8,'2023-03-12 22:41:22.446000','2','Γò¬┬½Γò¬┬╗Γöÿ├áΓò¬ΓîÉ Γò¬┬║Γöÿ├ñΓò¬ΓòúΓöÿ├áΓöÿ├ñΓò¬┬║Γò¬├¡',1,'[{\"added\": {}}]',10,1),(9,'2023-03-12 22:42:14.212000','2','Γò¬ΓöéΓò¬┬║Γò¬ΓûÆΓò¬ΓîÉ Γò¬ΓòúΓò¬┬║Γò¬┬╗Γöÿ├ñ',1,'[{\"added\": {}}]',11,1),(10,'2023-03-12 22:43:47.766000','1','dataEntryAdmin',1,'[{\"added\": {}}]',3,1),(11,'2023-03-12 22:45:48.320000','1','dataEntryAdmin',2,'[{\"changed\": {\"fields\": [\"Permissions\"]}}]',3,1),(12,'2023-03-12 22:46:10.267000','2','tahsealAdmin',1,'[{\"added\": {}}]',3,1),(13,'2023-03-12 22:46:31.243000','3','ServiceManagerAdmin',1,'[{\"added\": {}}]',3,1),(14,'2023-03-17 13:38:56.156000','3','customerService1',2,'[{\"changed\": {\"fields\": [\"password\"]}}]',4,1),(15,'2023-03-17 13:39:13.127000','3','customerService1',2,'[{\"changed\": {\"fields\": [\"Groups\", \"Last login\"]}}]',4,1),(16,'2023-03-17 13:52:57.650000','4','manager1',1,'[{\"added\": {}}]',4,1),(17,'2023-03-17 13:53:16.185000','5','manager2',1,'[{\"added\": {}}]',4,1),(18,'2023-03-17 13:54:13.001000','4','fullAdmin',1,'[{\"added\": {}}]',3,1),(19,'2023-03-17 13:54:45.009000','5','adminLvl1',1,'[{\"added\": {}}]',3,1),(20,'2023-03-17 13:55:06.869000','5','manager2',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Staff status\", \"Groups\"]}}]',4,1),(21,'2023-03-17 13:55:25.745000','4','manager1',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Staff status\", \"Groups\"]}}]',4,1),(22,'2023-03-17 20:30:38.788000','1','Γöÿ├áΓò¬┬╗Γöÿ├¿Γöÿ├ÑΓò¬ΓîÉ Γöÿ├ÑΓò¬┬║Γò¬ΓòíΓò¬ΓûÆ',1,'[{\"added\": {}}]',7,1),(23,'2023-03-19 21:26:19.706000','2','dataEntry1',2,'[{\"changed\": {\"fields\": [\"password\"]}}]',4,1),(24,'2023-03-19 21:27:21.446000','2','dataEntry1',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1),(25,'2023-04-03 23:56:53.523000','3','Γò¬┬┐Γò¬┬╗Γöÿ├¬Γöÿ├Ñ',1,'[{\"added\": {}}]',11,6),(26,'2023-04-03 23:58:31.320000','3','Γò¬┬¼Γöÿ├ÑΓò¬ΓòòΓöÿ├¿Γöÿ├⌐ Γò¬ΓöéΓöÿ├ñΓò¬┬║Γöÿ├ñΓöÿ├á',3,'',13,6),(27,'2023-04-03 23:58:31.324000','2','Γò¬┬¼Γöÿ├ÑΓò¬ΓòòΓöÿ├¿Γöÿ├╝ Γò¬ΓöéΓöÿ├ñΓò¬┬║Γöÿ├ñΓöÿ├á',3,'',13,6),(28,'2023-04-03 23:58:31.327000','1','Γò¬┬¼Γöÿ├ÑΓò¬ΓòòΓöÿ├¿Γöÿ├╝ Γöÿ├áΓöÿ├ÑΓò¬ΓûôΓöÿ├ñΓöÿ├½ Γò¬ΓòúΓöÿ├áΓöÿ├¿Γöÿ├⌐',3,'',13,6),(29,'2023-04-03 23:58:42.316000','1','as',3,'',8,6),(30,'2023-04-04 00:04:56.278000','6','Γò¬┬¼Γöÿ├ÑΓò¬ΓòòΓöÿ├¿Γöÿ├╝ Γò¬ΓöéΓöÿ├ñΓò¬┬║Γöÿ├ñΓöÿ├á Γò¬ΓòúΓöÿ├áΓò¬┬║Γò¬ΓûÆΓò¬ΓîÉ',3,'',13,6),(31,'2023-04-04 00:04:56.281000','5','Γò¬┬¼Γöÿ├ÑΓò¬ΓòòΓöÿ├¿Γöÿ├╝ Γöÿ├áΓöÿ├ÑΓò¬ΓûôΓöÿ├ñΓöÿ├½ - Γò¬ΓòúΓöÿ├áΓöÿ├¿Γöÿ├⌐ ',3,'',13,6),(32,'2023-04-04 00:04:56.282000','4','Γò¬┬¼Γöÿ├ÑΓò¬ΓòòΓöÿ├¿Γöÿ├╝ Γöÿ├áΓöÿ├ÑΓò¬ΓûôΓöÿ├ñΓöÿ├½ Γò¬┬┐Γò¬ΓöéΓöÿ├¿Γò¬Γòû',3,'',13,6),(33,'2023-04-04 00:07:03.954000','9','Γò¬┬¼Γöÿ├ÑΓò¬ΓòòΓöÿ├¿Γöÿ├╝ Γò¬ΓöéΓöÿ├ñΓò¬┬║Γöÿ├ñΓöÿ├á Γò¬ΓòúΓöÿ├áΓò¬┬║Γò¬ΓûÆΓò¬ΓîÉ',3,'',13,6),(34,'2023-04-04 00:07:03.957000','8','Γò¬┬¼Γöÿ├ÑΓò¬ΓòòΓöÿ├¿Γöÿ├╝ Γöÿ├áΓöÿ├ÑΓò¬ΓûôΓöÿ├ñΓöÿ├½ - Γò¬ΓòúΓöÿ├áΓöÿ├¿Γöÿ├⌐ ',3,'',13,6),(35,'2023-04-04 00:07:03.958000','7','Γò¬┬¼Γöÿ├ÑΓò¬ΓòòΓöÿ├¿Γöÿ├╝ Γöÿ├áΓöÿ├ÑΓò¬ΓûôΓöÿ├ñΓöÿ├½ Γò¬┬┐Γò¬ΓöéΓöÿ├¿Γò¬Γòû',3,'',13,6),(36,'2023-04-04 00:32:18.002000','13','Γò¬┬║Γöÿ├ñΓöÿ├áΓò¬┬íΓöÿ├áΓöÿ├¬Γò¬┬╗Γöÿ├¿Γò¬ΓîÉ',1,'new through import_export',7,6),(37,'2023-04-04 00:32:18.004000','12','Γò¬┬║Γöÿ├ñΓò¬├æΓò¬ΓöéΓöÿ├óΓò¬┬║Γöÿ├Ñ Γò¬┬║Γöÿ├ñΓöÿ├áΓöÿ├áΓöÿ├¿Γò¬Γûô',1,'new through import_export',7,6),(38,'2023-04-04 00:32:18.005000','11','Γöÿ├óΓò¬ΓûÆΓöÿ├¬Γò¬ΓûÆ',1,'new through import_export',7,6),(39,'2023-04-04 00:32:18.007000','10','Γöÿ├ÑΓò¬┬╝Γò¬Γòú Γò¬┬║Γöÿ├ñΓöÿ├áΓò¬┬íΓò¬ΓòûΓò¬ΓîÉ',1,'new through import_export',7,6),(40,'2023-04-04 00:32:18.009000','9','Γò¬┬║Γöÿ├ñΓò¬ΓûÆΓò¬ΓòóΓöÿ├¬Γò¬┬║Γöÿ├Ñ',1,'new through import_export',7,6),(41,'2023-04-04 00:32:18.011000','8','Γò¬┬╝Γò¬┬┐Γöÿ├ñ Γò¬┬¼Γöÿ├⌐Γöÿ├¬Γöÿ├⌐',1,'new through import_export',7,6),(42,'2023-04-04 00:32:18.012000','7','Γöÿ├áΓöÿ├¬Γöÿ├ñ Γò¬┬║Γöÿ├ñΓò¬┬íΓöÿ├óΓöÿ├¿Γöÿ├á',1,'new through import_export',7,6),(43,'2023-04-04 00:32:18.014000','6','Γò¬┬½Γò¬┬║Γöÿ├ñΓò¬┬╗ Γò¬┬┐Γöÿ├Ñ Γò¬┬║Γöÿ├ñΓöÿ├¬Γöÿ├ñΓöÿ├¿Γò¬┬╗',1,'new through import_export',7,6),(44,'2023-04-04 00:32:18.016000','5','Γò¬┬║Γöÿ├ñΓöÿ├áΓöÿ├⌐Γò¬┬║Γöÿ├¬Γöÿ├ñΓöÿ├¬Γöÿ├Ñ',1,'new through import_export',7,6),(45,'2023-04-04 00:32:18.018000','4','Γò¬ΓòúΓò¬┬┐Γò¬┬║Γò¬┬╗ Γò¬┬║Γöÿ├ñΓò¬ΓûÆΓò¬┬íΓöÿ├áΓöÿ├Ñ Γöÿ├¬Γò¬ΓöñΓò¬┬║Γò¬ΓûÆΓò¬Γòú Γò¬┬║Γöÿ├ñΓò¬ΓöéΓò¬┬║Γò¬┬╗Γò¬┬║Γò¬┬¼',1,'new through import_export',7,6),(46,'2023-04-04 00:32:18.019000','3','Γò¬┬║Γöÿ├ñΓò¬ΓòúΓöÿ├⌐Γò¬┬║Γò¬┬╗',1,'new through import_export',7,6),(47,'2023-04-04 00:32:18.020000','2','Γò¬┬║Γöÿ├ñΓöÿ├áΓöÿ├áΓöÿ├¿Γò¬Γûô 1 Γöÿ├¬ 2',1,'new through import_export',7,6),(48,'2023-04-04 00:32:18.022000','1','Γöÿ├áΓò¬┬╗Γöÿ├¿Γöÿ├ÑΓöÿ├º Γöÿ├ÑΓò¬┬║Γò¬ΓòíΓò¬ΓûÆ',2,'update through import_export',7,6),(49,'2023-04-04 00:32:44.133000','1','Γò¬ΓöñΓò¬ΓòúΓöÿ├¿Γò¬┬┐ Γò¬ΓòúΓöÿ├ñΓöÿ├½ Γò¬ΓöéΓöÿ├¿Γò¬┬╗ Γò¬┬║Γò¬┬íΓöÿ├áΓò¬┬╗ ',1,'new through import_export',8,6),(50,'2023-04-04 00:32:44.135000','2','Γöÿ├áΓò¬┬íΓöÿ├áΓò¬┬╗ Γò¬ΓòúΓöÿ├¬Γò¬Γòó Γò¬ΓòúΓò¬┬┐Γò¬┬╗Γöÿ├º ',2,'update through import_export',8,6),(51,'2023-04-04 00:32:44.136000','3','Γò¬┬íΓò¬ΓöéΓò¬┬║Γöÿ├á Γò¬┬║Γöÿ├ñΓò¬┬╗Γöÿ├¿Γöÿ├Ñ Γò¬ΓòûΓöÿ├º Γöÿ├áΓò¬┬íΓöÿ├áΓöÿ├¬Γò¬┬╗ ',1,'new through import_export',8,6),(52,'2023-04-04 00:32:44.138000','4','Γò¬┬½Γò¬┬╗Γöÿ├¿Γò¬┬╝Γöÿ├º Γöÿ├áΓò¬┬íΓöÿ├áΓò¬┬╗ Γò¬┬íΓò¬ΓöéΓöÿ├Ñ',1,'new through import_export',8,6),(53,'2023-04-04 00:32:44.139000','5','Γöÿ├áΓò¬┬íΓöÿ├áΓò¬┬╗ Γò¬┬íΓò¬ΓöéΓöÿ├¿Γöÿ├Ñ Γò¬ΓòúΓöÿ├ñΓöÿ├¿ Γò¬┬íΓò¬ΓöéΓöÿ├Ñ ',1,'new through import_export',8,6),(54,'2023-04-04 00:32:44.140000','6','Γöÿ├áΓò¬┬íΓöÿ├áΓò¬┬╗ Γò¬┬íΓò¬ΓöéΓöÿ├¿Γöÿ├Ñ Γò¬ΓòúΓöÿ├ñΓöÿ├¿ Γò¬┬íΓò¬ΓöéΓöÿ├Ñ ',1,'new through import_export',8,6),(55,'2023-04-04 00:32:44.142000','7','Γò¬ΓòíΓò¬┬║Γò¬┬┐Γò¬ΓûÆ Γöÿ├áΓò¬┬íΓöÿ├áΓò¬┬╗ Γò¬ΓòúΓöÿ├ñΓöÿ├¿ Γöÿ├áΓò¬┬íΓöÿ├áΓò¬┬╗',1,'new through import_export',8,6),(56,'2023-04-04 00:32:44.143000','8','Γò¬┬íΓò¬ΓöéΓöÿ├Ñ Γò¬┬║Γò¬┬íΓöÿ├áΓò¬┬╗ Γò¬ΓûôΓöÿ├¿Γöÿ├Ñ Γò¬┬║Γöÿ├ñΓò¬ΓòúΓò¬┬║Γò¬┬┐Γò¬┬╗Γöÿ├¿Γöÿ├Ñ ',1,'new through import_export',8,6),(57,'2023-04-04 00:32:44.145000','9','Γò¬ΓòúΓöÿ├ñΓò¬┬║Γò¬├¡ Γò¬┬║Γöÿ├ñΓò¬┬╗Γöÿ├¿Γöÿ├Ñ Γò¬┬║Γò¬┬íΓöÿ├áΓò¬┬╗ Γò¬ΓòúΓò¬┬┐Γò¬┬╗ Γò¬┬║Γöÿ├ñΓöÿ├áΓò¬ΓòúΓò¬ΓòûΓöÿ├½ ',1,'new through import_export',8,6),(58,'2023-04-04 00:32:44.147000','10','Γò¬ΓûôΓöÿ├¿Γò¬┬║Γò¬┬╗ Γò¬ΓöéΓò¬ΓòúΓò¬┬╗ Γò¬ΓûôΓò¬ΓòúΓöÿ├ñΓöÿ├¬Γöÿ├ñ ',1,'new through import_export',8,6),(59,'2023-04-04 00:32:44.149000','11','Γöÿ├ºΓò¬┬┐Γò¬ΓîÉ Γò¬ΓòúΓò¬ΓöñΓò¬ΓûÆΓöÿ├½ Γò¬ΓûÆΓò¬┬║Γò¬ΓòóΓöÿ├½ Γò¬┬║Γöÿ├ñΓöÿ├áΓöÿ├ºΓò¬┬╗Γöÿ├½',1,'new through import_export',8,6),(60,'2023-04-04 00:32:44.152000','12','Γöÿ├áΓò¬┬íΓöÿ├áΓò¬┬╗ Γò¬ΓòúΓò¬┬┐Γò¬┬╗ Γò¬┬║Γöÿ├ñΓò¬ΓòúΓò¬ΓûôΓöÿ├¿Γò¬Γûô Γò¬┬║Γò¬┬íΓöÿ├áΓò¬┬╗ ',1,'new through import_export',8,6),(61,'2023-04-04 00:32:44.155000','13','Γò¬ΓöéΓöÿ├ñΓò¬ΓòûΓò¬┬║Γöÿ├Ñ Γò¬ΓòúΓò¬┬┐Γò¬┬╗ Γò¬┬║Γöÿ├ñΓò¬┬íΓöÿ├áΓöÿ├¿Γò¬┬╗ Γöÿ├ºΓò¬┬║Γò¬ΓûÆΓöÿ├¬Γöÿ├Ñ ',1,'new through import_export',8,6),(62,'2023-04-04 00:32:44.157000','14','Γöÿ├áΓò¬ΓòíΓò¬ΓòûΓöÿ├╝Γöÿ├½ Γò¬┬╝Γöÿ├áΓò¬ΓòúΓò¬ΓîÉ Γöÿ├áΓöÿ├ºΓò¬┬╗Γöÿ├½',1,'new through import_export',8,6),(63,'2023-04-04 00:32:44.159000','15','Γò¬ΓöñΓò¬┬║Γò¬ΓûæΓöÿ├ñΓöÿ├½ Γò¬ΓòúΓò¬ΓòûΓò¬┬║Γöÿ├ñΓöÿ├ñΓò¬ΓîÉ Γöÿ├áΓò¬┬íΓöÿ├áΓò¬┬╗ ',1,'new through import_export',8,6),(64,'2023-04-04 00:32:44.162000','16','Γò¬ΓòúΓò¬┬┐Γò¬┬╗ Γò¬┬║Γöÿ├ñΓöÿ├ÑΓò¬┬║Γò¬ΓòíΓò¬ΓûÆ Γò¬ΓòíΓò¬┬║Γò¬┬┐Γò¬ΓûÆ Γò¬┬║Γò¬┬íΓöÿ├áΓò¬┬╗ ',1,'new through import_export',8,6),(65,'2023-04-04 00:32:44.164000','17','Γò¬┬║Γò¬┬íΓöÿ├áΓò¬┬╗ Γò¬ΓòúΓò¬┬┐Γò¬┬╗ Γò¬┬║Γöÿ├ñΓò¬ΓöñΓò¬┬║Γöÿ├╝Γöÿ├½ Γò¬ΓòúΓò¬┬┐Γò¬┬╗ Γò¬┬║Γöÿ├ñΓò¬┬íΓöÿ├áΓöÿ├¿Γò¬┬╗ ',1,'new through import_export',8,6),(66,'2023-04-04 00:32:44.166000','18','Γöÿ├╝Γò¬┬¼Γò¬┬íΓöÿ├¿ Γò¬ΓöéΓò¬ΓòúΓò¬┬╗ Γò¬┬║Γöÿ├ñΓò¬┬╗Γöÿ├¿Γöÿ├Ñ Γò¬ΓòúΓò¬┬┐Γò¬┬╗ Γò¬┬║Γöÿ├ñΓò¬ΓûÆΓò¬┬íΓöÿ├áΓöÿ├Ñ',1,'new through import_export',8,6),(67,'2023-04-04 00:32:44.168000','19','Γò¬┬║Γò¬┬íΓöÿ├áΓò¬┬╗ Γò¬┬íΓò¬ΓöéΓöÿ├¿Γöÿ├Ñ Γò¬ΓòúΓöÿ├ñΓöÿ├¿ Γò¬┬íΓò¬ΓöéΓöÿ├Ñ',1,'new through import_export',8,6),(68,'2023-04-04 00:32:44.170000','20','Γöÿ├ºΓò¬ΓöñΓò¬┬║Γöÿ├á Γò¬ΓöéΓò¬ΓòúΓò¬┬╗ Γò¬┬║Γöÿ├ñΓò¬┬╗Γöÿ├¿Γöÿ├Ñ Γò¬┬║Γò¬┬íΓöÿ├áΓò¬┬╗',1,'new through import_export',8,6),(69,'2023-04-04 00:32:44.173000','21','Γò¬┬║Γò¬┬íΓöÿ├áΓò¬┬╗ Γò¬ΓòúΓò¬┬┐Γò¬┬╗ Γò¬ΓûÆΓò¬┬║Γò¬ΓûôΓöÿ├⌐ Γò¬┬║Γò¬┬íΓöÿ├áΓò¬┬╗',1,'new through import_export',8,6),(70,'2023-04-04 00:32:44.175000','22','Γò¬┬║Γò¬ΓöñΓò¬ΓûÆΓöÿ├╝ Γò¬┬║Γöÿ├ñΓò¬┬║Γöÿ├áΓöÿ├¿Γò¬ΓûÆ Γò¬┬║Γò¬┬┐Γò¬ΓûÆΓò¬┬║Γöÿ├ºΓöÿ├¿Γöÿ├á',1,'new through import_export',8,6),(71,'2023-04-04 00:32:44.177000','23','Γò¬┬║Γò¬┬íΓöÿ├áΓò¬┬╗ Γò¬ΓòúΓò¬┬┐Γò¬┬╗Γò¬┬║Γöÿ├ñΓò¬ΓöñΓò¬┬║Γöÿ├╝Γöÿ├¿ Γò¬┬║Γöÿ├ÑΓöÿ├¬Γò¬ΓûÆ',1,'new through import_export',8,6),(72,'2023-04-04 00:32:44.179000','24','Γöÿ├áΓò¬ΓöéΓò¬┬¼Γò¬ΓöñΓò¬┬║Γò¬ΓûÆ Γò¬┬½Γò¬┬║Γöÿ├ñΓò¬┬╗ Γöÿ├áΓò¬┬íΓöÿ├áΓò¬┬╗ Γò¬ΓûÆΓöÿ├¿Γò¬┬║Γöÿ├Ñ',1,'new through import_export',8,6),(73,'2023-04-04 00:32:44.180000','25','Γò¬┬║Γöÿ├ñΓöÿ├áΓò¬ΓöéΓò¬┬¼Γò¬ΓöñΓò¬┬║Γò¬ΓûÆ Γò¬ΓòúΓöÿ├áΓò¬ΓûÆΓöÿ├¬ Γöÿ├¿Γò¬┬íΓöÿ├¿Γöÿ├¿ Γò¬┬║Γò¬┬┐Γöÿ├¬ Γò¬ΓûôΓöÿ├¿Γò¬┬╗',1,'new through import_export',8,6),(74,'2023-04-04 00:32:44.183000','26','Γò¬ΓöéΓöÿ├áΓöÿ├¿Γò¬ΓûÆΓöÿ├º Γò¬ΓöéΓöÿ├¿Γò¬┬╗ Γò¬ΓòúΓöÿ├ñΓöÿ├¿ Γò¬┬║Γöÿ├ñΓò¬ΓòûΓöÿ├¿Γò¬┬┐',1,'new through import_export',8,6),(75,'2023-04-04 00:32:44.185000','27','Γò¬ΓöéΓöÿ├¬Γò¬ΓûôΓò¬┬║Γöÿ├Ñ Γò¬ΓòíΓöÿ├ñΓò¬┬║Γò¬┬í Γò¬┬║Γöÿ├ñΓò¬┬╗Γöÿ├¿Γöÿ├Ñ Γò¬ΓòúΓò¬┬┐Γò¬┬╗Γò¬┬║Γöÿ├ñΓò¬ΓòúΓò¬ΓòòΓöÿ├¿Γöÿ├á Γò¬┬║Γò¬┬íΓöÿ├áΓò¬┬╗',1,'new through import_export',8,6),(76,'2023-04-04 00:32:44.187000','28','Γò¬ΓòúΓò¬ΓòíΓò¬┬║Γöÿ├á Γò¬ΓòúΓò¬┬┐Γò¬┬╗Γò¬┬║Γöÿ├ñΓöÿ├ñΓöÿ├º Γöÿ├áΓò¬┬íΓöÿ├áΓò¬┬╗',1,'new through import_export',8,6),(77,'2023-04-04 00:32:44.189000','29','Γò¬ΓûÆΓöÿ├áΓò¬ΓòóΓò¬┬║Γöÿ├Ñ Γò¬ΓòúΓöÿ├¬Γò¬Γòó Γò¬┬║Γöÿ├ñΓöÿ├ñΓöÿ├º Γò¬ΓòíΓò¬┬║Γò¬┬┐Γò¬ΓûÆ Γò¬ΓòúΓöÿ├ñΓöÿ├¿',1,'new through import_export',8,6),(78,'2023-04-04 00:32:44.190000','30','Γöÿ├áΓò¬ΓòíΓò¬ΓòûΓöÿ├╝Γöÿ├½ Γò¬┬║Γöÿ├ñΓò¬ΓöéΓöÿ├¿Γò¬┬╗ Γöÿ├áΓò¬┬íΓöÿ├áΓò¬┬╗ Γò¬┬║Γöÿ├ñΓò¬ΓöéΓöÿ├¿Γò¬┬╗',1,'new through import_export',8,6),(79,'2023-04-04 00:32:44.192000','31','Γò¬┬║Γöÿ├ñΓò¬ΓöéΓöÿ├¿Γò¬┬╗ Γöÿ├áΓò¬┬íΓöÿ├áΓò¬┬╗ Γò¬┬║Γöÿ├ñΓò¬ΓöéΓöÿ├¿Γò¬┬╗',1,'new through import_export',8,6),(80,'2023-04-04 00:32:44.194000','32','Γò¬ΓöéΓò¬┬║Γöÿ├áΓöÿ├¿Γò¬ΓîÉ Γò¬ΓòúΓò¬┬┐Γò¬┬╗ Γò¬┬║Γöÿ├ñΓöÿ├áΓöÿ├ÑΓò¬ΓòúΓöÿ├á Γò¬┬íΓöÿ├ÑΓöÿ├╝Γöÿ├½',1,'new through import_export',8,6),(81,'2023-04-04 00:32:44.196000','33','Γò¬ΓòúΓò¬┬┐Γò¬┬╗Γò¬┬║Γöÿ├ñΓöÿ├ÑΓò¬┬║Γò¬ΓòíΓò¬ΓûÆ Γöÿ├áΓò¬┬íΓöÿ├áΓò¬┬╗ Γò¬┬║Γöÿ├ñΓò¬ΓöéΓöÿ├¿Γò¬┬╗',1,'new through import_export',8,6),(82,'2023-04-04 00:32:44.198000','34','Γöÿ├áΓò¬┬íΓöÿ├áΓò¬┬╗ Γò¬ΓòúΓò¬┬┐Γò¬┬╗Γò¬┬║Γöÿ├ñΓöÿ├ÑΓò¬┬║Γò¬ΓòíΓò¬ΓûÆ Γöÿ├áΓò¬┬íΓöÿ├áΓò¬┬╗ Γò¬┬║Γöÿ├ñΓò¬ΓöéΓöÿ├¿Γò¬┬╗',1,'new through import_export',8,6),(83,'2023-04-04 00:32:44.201000','35','Γöÿ├áΓò¬┬íΓöÿ├áΓò¬┬╗ Γò¬┬┐Γöÿ├ºΓò¬┬╝Γò¬┬¼ Γöÿ├╝Γöÿ├ºΓöÿ├áΓöÿ├¿ Γò¬┬┐Γò¬ΓûÆΓò¬ΓòæΓöÿ├¬Γò¬┬¼',1,'new through import_export',8,6),(84,'2023-04-04 00:32:44.203000','36','Γò¬ΓûôΓöÿ├¿Γöÿ├ÑΓò¬┬┐ Γò¬ΓòúΓò¬ΓòûΓò¬┬║ Γò¬┬╝Γò¬┬║Γò¬┬╗ Γöÿ├áΓò¬┬íΓöÿ├áΓò¬┬íΓöÿ├áΓöÿ├¬Γò¬┬╗',1,'new through import_export',8,6),(85,'2023-04-04 00:32:44.205000','37','Γò¬┬║Γò¬┬íΓöÿ├áΓò¬┬╗ Γò¬ΓòúΓò¬┬║Γò¬┬┐Γò¬┬╗Γöÿ├¿Γöÿ├Ñ Γò¬┬║Γò¬┬íΓöÿ├áΓò¬┬╗',1,'new through import_export',8,6),(86,'2023-04-04 00:32:44.206000','38','Γò¬┬║Γöÿ├ñΓò¬┬íΓò¬ΓöéΓöÿ├¿Γöÿ├Ñ Γöÿ├áΓöÿ├ÑΓò¬ΓòíΓöÿ├¬Γò¬ΓûÆ Γò¬ΓòúΓò¬┬┐Γò¬┬╗Γò¬┬║Γöÿ├ñΓöÿ├¬Γò¬┬║Γò¬┬íΓò¬┬╗',1,'new through import_export',8,6),(87,'2023-04-04 00:32:44.208000','39','Γöÿ├áΓò¬┬íΓöÿ├áΓò¬┬╗ Γò¬ΓûôΓöÿ├óΓöÿ├¿ Γò¬┬║Γöÿ├ñΓöÿ├áΓöÿ├¬Γò¬┬╝Γöÿ├¿',1,'new through import_export',8,6),(88,'2023-04-04 00:32:44.210000','40','Γò¬ΓòúΓöÿ├áΓò¬ΓûÆ Γöÿ├╝Γöÿ├¬Γò¬ΓûôΓöÿ├¿ Γò¬┬║Γò¬┬íΓöÿ├áΓò¬┬╗',1,'new through import_export',8,6),(89,'2023-04-04 00:32:44.211000','41','Γò¬┬║Γöÿ├á Γò¬┬║Γò¬ΓöñΓò¬ΓûÆΓöÿ├╝ Γöÿ├¿Γöÿ├¬Γò¬ΓöéΓöÿ├╝ Γò¬┬╝Γò¬ΓûÆΓò¬Γöé ',1,'new through import_export',8,6),(90,'2023-04-04 00:32:44.214000','42',' Γò¬┬║Γò¬┬╗Γöÿ├¿Γò¬┬┐Γöÿ├º Γò¬ΓòúΓò¬┬┐Γò¬┬╗Γò¬┬║Γöÿ├ñΓò¬┬┐Γò¬┬║Γöÿ├⌐Γöÿ├¿ Γò¬┬║Γöÿ├ñΓò¬ΓöñΓöÿ├¿Γò¬┬½',1,'new through import_export',8,6),(91,'2023-04-04 00:32:44.217000','43','Γò¬┬║Γò¬┬íΓöÿ├áΓò¬┬╗ Γò¬┬íΓò¬ΓöéΓöÿ├Ñ Γò¬ΓöéΓò¬ΓûÆΓò¬┬║Γò¬┬╝',1,'new through import_export',8,6),(92,'2023-04-04 00:32:44.221000','44','Γò¬ΓòúΓò¬┬┐Γò¬┬╗Γò¬┬║Γöÿ├ñΓöÿ├áΓò¬┬║Γöÿ├ñΓöÿ├ó Γöÿ├áΓò¬┬íΓöÿ├áΓò¬┬╗ Γò¬┬║Γò¬┬íΓöÿ├áΓò¬┬╗ Γöÿ├áΓò¬┬íΓöÿ├áΓò¬┬╗',1,'new through import_export',8,6),(93,'2023-04-04 00:32:44.225000','45','Γò¬ΓòúΓò¬┬┐Γò¬┬╗Γò¬┬║Γöÿ├ñΓò¬ΓöñΓöÿ├óΓöÿ├¬Γò¬ΓûÆ Γöÿ├áΓò¬┬╝Γò¬┬║Γò¬ΓûôΓöÿ├¿ Γöÿ├áΓò¬┬íΓöÿ├áΓò¬┬╗',1,'new through import_export',8,6),(94,'2023-04-04 00:32:44.229000','46','Γöÿ├¬Γò¬┬║Γò¬┬¬Γöÿ├ñ Γò¬ΓûÆΓöÿ├╝Γò¬ΓòúΓò¬┬¼ Γöÿ├áΓò¬┬íΓöÿ├áΓò¬┬╗',1,'new through import_export',8,6),(95,'2023-04-04 00:32:44.234000','47','Γò¬ΓòíΓò¬┬┐Γò¬ΓûÆΓöÿ├¿ Γò¬ΓûÆΓöÿ├óΓò¬┬║Γò¬┬┐Γöÿ├¿ Γò¬┬║Γò¬┬┐Γò¬ΓûÆΓò¬┬║Γöÿ├ºΓöÿ├¿Γöÿ├á',1,'new through import_export',8,6),(96,'2023-04-04 00:32:44.237000','48','Γò¬ΓòúΓò¬┬┐Γò¬┬╗Γò¬┬║Γöÿ├ñΓöÿ├ñΓöÿ├º Γöÿ├áΓò¬┬íΓöÿ├áΓò¬┬╗ Γò¬ΓòúΓò¬┬┐Γò¬┬╗Γò¬┬║Γöÿ├ñΓöÿ├ñΓöÿ├º',1,'new through import_export',8,6),(97,'2023-04-04 00:32:44.240000','49','Γò¬┬║Γò¬ΓöéΓöÿ├ñΓò¬┬║Γöÿ├á Γò¬ΓòúΓò¬┬┐Γò¬┬╗Γò¬┬║Γöÿ├ñΓöÿ├áΓöÿ├ÑΓò¬ΓòúΓöÿ├á Γöÿ├áΓò¬┬íΓöÿ├áΓò¬┬╗',1,'new through import_export',8,6),(98,'2023-04-04 00:32:44.242000','50','Γò¬┬║Γöÿ├¿Γöÿ├áΓöÿ├Ñ Γöÿ├óΓöÿ├áΓò¬┬║Γöÿ├ñ Γò¬┬¼Γöÿ├¬Γöÿ├╝Γöÿ├¿Γöÿ├⌐',1,'new through import_export',8,6),(99,'2023-04-04 00:32:44.245000','51','Γò¬┬║Γò¬┬íΓöÿ├áΓò¬┬╗ Γò¬ΓòúΓò¬┬┐Γò¬┬╗Γò¬┬║Γöÿ├ñΓò¬┬íΓöÿ├áΓöÿ├¿Γò¬┬╗ Γöÿ├áΓò¬┬íΓöÿ├áΓò¬┬╗ ',1,'new through import_export',8,6),(100,'2023-04-04 00:32:44.247000','52','Γò¬ΓöéΓò¬┬║Γöÿ├áΓöÿ├¿Γöÿ├º Γò¬ΓòúΓöÿ├¬Γò¬Γòó Γò¬ΓòúΓò¬┬┐Γò¬┬╗Γò¬┬║Γöÿ├ñΓò¬ΓòúΓò¬ΓûôΓöÿ├¿Γò¬Γûô ',1,'new through import_export',8,6),(101,'2023-04-04 00:32:44.249000','53','Γöÿ├áΓò¬┬íΓöÿ├áΓöÿ├¬Γò¬┬╗ Γöÿ├áΓò¬┬íΓöÿ├áΓò¬┬╗ Γöÿ├╝Γò¬├▒Γò¬┬║Γò¬┬╗',1,'new through import_export',8,6),(102,'2023-04-04 00:32:44.252000','54','Γò¬ΓöéΓöÿ├ºΓò¬┬║Γöÿ├á Γò¬┬║Γò¬┬┐Γò¬ΓûÆΓò¬┬║Γöÿ├ºΓöÿ├¿Γöÿ├á Γöÿ├áΓò¬┬íΓöÿ├áΓò¬┬╗',1,'new through import_export',8,6),(103,'2023-04-04 00:32:44.255000','55','Γò¬┬║Γò¬┬íΓöÿ├áΓò¬┬╗ Γò¬ΓûÆΓöÿ├áΓò¬ΓòóΓò¬┬║Γöÿ├Ñ Γò¬ΓòúΓò¬┬┐Γò¬┬╗Γò¬┬║Γöÿ├ñΓöÿ├áΓöÿ├⌐Γò¬ΓòíΓöÿ├¬Γò¬┬╗',1,'new through import_export',8,6),(104,'2023-04-04 00:32:44.257000','56','Γò¬┬║Γò¬┬íΓöÿ├áΓò¬┬╗ Γò¬ΓòúΓò¬┬┐Γò¬┬╗Γò¬┬║Γöÿ├ñΓöÿ├ñΓöÿ├º Γò¬┬íΓò¬ΓöéΓò¬┬┐ Γò¬┬║Γöÿ├ñΓöÿ├ñΓöÿ├º',1,'new through import_export',8,6),(105,'2023-04-04 00:32:44.259000','57','Γò¬┬║Γò¬┬íΓöÿ├áΓò¬┬╗ Γò¬ΓöéΓöÿ├¿Γò¬┬╗ Γöÿ├áΓò¬┬íΓöÿ├áΓò¬┬╗ Γöÿ├ºΓò¬ΓöñΓò¬┬║Γöÿ├á ',1,'new through import_export',8,6),(106,'2023-04-04 00:32:44.261000','58','Γò¬ΓòíΓöÿ├ñΓò¬┬║Γò¬┬í Γò¬┬║Γöÿ├ñΓò¬┬╗Γöÿ├¿Γöÿ├Ñ ',1,'new through import_export',8,6),(107,'2023-04-04 00:32:44.263000','59','Γöÿ├áΓò¬┬íΓöÿ├áΓöÿ├¬Γò¬┬╗ Γöÿ├áΓò¬┬íΓöÿ├áΓò¬┬╗',1,'new through import_export',8,6),(108,'2023-04-04 00:32:44.265000','60','Γò¬┬║Γò¬┬íΓöÿ├áΓò¬┬╗ Γöÿ├áΓöÿ├ÑΓöÿ├¿Γò¬ΓûÆ Γöÿ├áΓò¬┬íΓöÿ├áΓò¬┬╗ Γöÿ├╝Γò¬┬¼Γò¬┬í Γò¬┬║Γöÿ├ñΓöÿ├ñΓöÿ├º',1,'new through import_export',8,6),(109,'2023-04-04 00:32:44.267000','61','Γöÿ├áΓò¬┬íΓöÿ├áΓò¬┬╗ Γöÿ├áΓöÿ├ÑΓöÿ├¿Γò¬ΓûÆ Γöÿ├áΓò¬┬íΓöÿ├áΓò¬┬╗ Γöÿ├╝Γò¬┬¼Γò¬┬í Γò¬┬║Γöÿ├ñΓöÿ├ñΓöÿ├º',1,'new through import_export',8,6),(110,'2023-04-04 00:32:44.269000','62',' Γöÿ├áΓöÿ├ÑΓöÿ├¿Γò¬ΓûÆ Γöÿ├áΓò¬┬íΓöÿ├áΓò¬┬╗ Γöÿ├╝Γò¬┬¼Γò¬┬í Γò¬┬║Γöÿ├ñΓöÿ├ñΓöÿ├º',1,'new through import_export',8,6),(111,'2023-04-04 00:32:44.271000','63','Γöÿ├áΓò¬┬íΓöÿ├áΓöÿ├¬Γò¬┬╗ Γò¬┬║Γò¬┬íΓöÿ├áΓò¬┬╗ Γöÿ├áΓò¬┬íΓöÿ├áΓöÿ├¬Γò¬┬╗',1,'new through import_export',8,6),(112,'2023-04-04 00:32:44.273000','64','Γöÿ├áΓò¬ΓòíΓò¬ΓòûΓöÿ├╝Γöÿ├¿ Γò¬┬║Γöÿ├ñΓò¬┬íΓò¬ΓöéΓöÿ├Ñ Γò¬ΓòûΓöÿ├º',1,'new through import_export',8,6),(113,'2023-04-04 00:32:44.275000','65','Γöÿ├ÑΓò¬┬║Γò¬ΓûæΓò¬┬╝ Γò¬ΓòíΓöÿ├ñΓò¬┬║Γò¬┬í Γò¬┬║Γò¬┬íΓöÿ├áΓò¬┬╗',1,'new through import_export',8,6),(114,'2023-04-04 00:32:44.278000','66','Γò¬┬║Γò¬┬┐Γò¬ΓûÆΓò¬┬║Γöÿ├ºΓöÿ├¿Γöÿ├á Γöÿ├╝Γò¬┬║Γöÿ├¬Γöÿ├¿ Γò¬ΓòúΓò¬┬┐Γò¬┬╗Γò¬┬║Γöÿ├ñΓöÿ├ñΓöÿ├º',1,'new through import_export',8,6),(115,'2023-04-04 00:32:44.281000','67','Γò¬┬┐Γò¬ΓöñΓöÿ├¿Γò¬ΓûÆ Γò¬┬╝Γöÿ├áΓò¬ΓòúΓöÿ├º Γò¬ΓòúΓöÿ├ñΓöÿ├¿',1,'new through import_export',8,6),(116,'2023-04-04 00:32:44.285000','68','Γò¬ΓòúΓöÿ├¿Γò¬┬╗ Γöÿ├áΓò¬┬íΓöÿ├áΓò¬┬╗ Γò¬ΓòúΓò¬┬┐Γò¬┬╗Γöÿ├º',1,'new through import_export',8,6),(117,'2023-04-04 00:32:44.288000','69','Γöÿ├¿Γöÿ├¬Γò¬ΓöéΓöÿ├╝ Γöÿ├áΓò¬┬íΓöÿ├áΓöÿ├¬Γò¬┬╗ Γò¬┬┐Γò¬┬╗Γò¬ΓûÆΓöÿ├¿',1,'new through import_export',8,6),(118,'2023-04-04 00:32:44.292000','70','Γò¬┬║Γò¬┬┐Γò¬┬¼Γò¬ΓöéΓò¬┬║Γöÿ├á Γò¬ΓûôΓöÿ├¿Γò¬┬╗Γò¬┬║Γöÿ├Ñ Γò¬ΓòúΓò¬┬┐Γöÿ├¿Γò¬┬╗ Γò¬ΓòúΓöÿ├ñΓöÿ├¿',1,'new through import_export',8,6),(119,'2023-04-04 00:32:44.295000','71','Γò¬ΓöéΓò¬ΓòúΓò¬┬║Γò¬┬╗ Γöÿ├áΓò¬ΓòíΓò¬ΓòûΓöÿ├╝Γöÿ├¿ Γò¬┬║Γò¬┬íΓöÿ├áΓò¬┬╗',1,'new through import_export',8,6),(120,'2023-04-04 00:32:44.298000','72','Γò¬┬║Γöÿ├áΓöÿ├¿Γò¬ΓûÆΓöÿ├º Γöÿ├¬Γò¬┬íΓöÿ├¿Γò¬┬╗ Γò¬ΓòúΓöÿ├ñΓöÿ├¿',1,'new through import_export',8,6),(121,'2023-04-04 00:32:44.301000','73','Γöÿ├óΓò¬ΓûÆΓöÿ├¿Γöÿ├á Γò¬ΓòúΓò¬┬┐Γò¬┬╗Γò¬┬║Γöÿ├ñΓöÿ├áΓò¬ΓòúΓò¬ΓòûΓöÿ├¿ Γöÿ├áΓò¬┬íΓöÿ├áΓò¬┬╗',1,'new through import_export',8,6),(122,'2023-04-04 00:32:44.304000','74','Γò¬ΓòúΓöÿ├ñΓöÿ├¿Γò¬┬║Γò¬├¡ Γöÿ├ºΓò¬ΓöñΓò¬┬║Γöÿ├á Γò¬ΓòíΓò¬┬║Γöÿ├ñΓò¬┬í Γò¬ΓöéΓöÿ├ñΓöÿ├¿Γöÿ├áΓò¬┬║Γöÿ├Ñ',1,'new through import_export',8,6),(123,'2023-04-04 00:32:44.306000','75','Γò¬ΓöéΓöÿ├¿Γò¬┬╗ Γò¬ΓòúΓöÿ├ñΓöÿ├¿ Γò¬┬íΓò¬ΓöéΓöÿ├Ñ',1,'new through import_export',8,6),(124,'2023-04-04 00:32:44.308000','76','Γò¬┬┐Γò¬┬íΓò¬ΓûÆ Γò¬┬║Γò¬┬íΓöÿ├áΓò¬┬╗ Γò¬ΓöéΓöÿ├¿Γò¬┬╗',1,'new through import_export',8,6),(125,'2023-04-04 00:32:44.310000','77','Γò¬ΓöéΓöÿ├¿Γò¬┬╗ Γöÿ├áΓò¬┬íΓöÿ├áΓò¬┬╗ Γò¬┬íΓò¬ΓöéΓöÿ├¿Γöÿ├Ñ Γò¬┬íΓöÿ├áΓò¬┬╗Γò¬┬║Γöÿ├Ñ ',1,'new through import_export',8,6),(126,'2023-04-04 00:32:44.312000','78','Γöÿ├¬Γöÿ├ñΓöÿ├¿Γò¬┬╗ Γò¬ΓòúΓò¬┬┐Γò¬┬╗Γò¬┬║Γöÿ├ñΓò¬┬┐Γò¬┬║Γöÿ├⌐Γöÿ├¿ Γò¬┬║Γöÿ├áΓöÿ├¿Γöÿ├Ñ Γò¬ΓòæΓò¬ΓûÆΓöÿ├¿Γò¬┬┐',1,'new through import_export',8,6),(127,'2023-04-04 00:32:44.314000','79','Γöÿ├áΓò¬┬íΓöÿ├áΓò¬┬╗ Γò¬┬║Γò¬┬íΓöÿ├áΓò¬┬╗ Γò¬ΓòúΓò¬┬┐Γò¬┬╗Γò¬┬║Γöÿ├ñΓò¬ΓòúΓò¬ΓòòΓöÿ├¿Γöÿ├á ',1,'new through import_export',8,6),(128,'2023-04-04 01:30:24.619000','1','Γò¬ΓöñΓò¬ΓòúΓöÿ├¿Γò¬┬┐ Γò¬ΓòúΓöÿ├ñΓöÿ├½ Γò¬ΓöéΓöÿ├¿Γò¬┬╗ Γò¬┬║Γò¬┬íΓöÿ├áΓò¬┬╗ ',3,'',8,6),(129,'2023-04-04 02:29:43.284000','81','Γöÿ├áΓò¬┬íΓöÿ├áΓò¬┬╗ Γò¬ΓòúΓöÿ├¬Γò¬Γòó Γò¬ΓòúΓò¬┬┐Γò¬┬╗Γöÿ├º ',3,'',8,6),(130,'2023-04-04 02:29:43.288000','2','Γöÿ├áΓò¬┬íΓöÿ├áΓò¬┬╗ Γò¬ΓòúΓöÿ├¬Γò¬Γòó Γò¬ΓòúΓò¬┬┐Γò¬┬╗Γöÿ├º ',3,'',8,6),(131,'2023-04-04 02:50:57.906000','7','7',3,'',19,6),(132,'2023-04-04 04:48:33.421000','11','Γöÿ├áΓò¬┬íΓöÿ├áΓò¬┬╗ Γò¬┬íΓò¬ΓöéΓöÿ├¿Γöÿ├Ñ Γò¬ΓòúΓöÿ├ñΓöÿ├¿ Γò¬┬íΓò¬ΓöéΓöÿ├Ñ ',2,'[]',18,6),(133,'2023-04-04 04:48:43.253000','11','Γöÿ├áΓò¬┬íΓöÿ├áΓò¬┬╗ Γò¬┬íΓò¬ΓöéΓöÿ├¿Γöÿ├Ñ Γò¬ΓòúΓöÿ├ñΓöÿ├¿ Γò¬┬íΓò¬ΓöéΓöÿ├Ñ ',2,'[{\"changed\": {\"fields\": [\"\\u062d\\u0627\\u0644\\u0629 \\u0627\\u062f\\u0627\\u0621 \\u0627\\u0644\\u062e\\u062f\\u0645\\u0629\", \"CollcetStatusNums\"]}}]',18,6),(134,'2023-04-04 04:48:51.067000','10','Γò¬┬½Γò¬┬╗Γöÿ├¿Γò¬┬╝Γöÿ├º Γöÿ├áΓò¬┬íΓöÿ├áΓò¬┬╗ Γò¬┬íΓò¬ΓöéΓöÿ├Ñ',2,'[{\"changed\": {\"fields\": [\"\\u062d\\u0627\\u0644\\u0629 \\u0627\\u062f\\u0627\\u0621 \\u0627\\u0644\\u062e\\u062f\\u0645\\u0629\", \"CollcetStatusNums\"]}}]',18,6),(135,'2023-04-04 04:49:05.742000','9','Γò¬┬½Γò¬┬╗Γöÿ├¿Γò¬┬╝Γöÿ├º Γöÿ├áΓò¬┬íΓöÿ├áΓò¬┬╗ Γò¬┬íΓò¬ΓöéΓöÿ├Ñ',2,'[{\"changed\": {\"fields\": [\"\\u062d\\u0627\\u0644\\u0629 \\u0627\\u062f\\u0627\\u0621 \\u0627\\u0644\\u062e\\u062f\\u0645\\u0629\", \"CollcetStatusNums\"]}}]',18,6),(136,'2023-04-04 04:49:34.583000','11','Γöÿ├áΓò¬┬íΓöÿ├áΓò¬┬╗ Γò¬┬íΓò¬ΓöéΓöÿ├¿Γöÿ├Ñ Γò¬ΓòúΓöÿ├ñΓöÿ├¿ Γò¬┬íΓò¬ΓöéΓöÿ├Ñ ',2,'[{\"changed\": {\"fields\": [\"CollcetStatusNums\"]}}]',18,6),(137,'2023-04-06 03:46:24.207000','7','tahseal1',1,'[{\"added\": {}}]',4,6),(138,'2023-04-06 03:48:09.035000','7','tahseal1',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Groups\", \"User permissions\"]}}]',4,6),(139,'2023-04-06 04:16:42.269000','11','Γöÿ├áΓò¬┬íΓöÿ├áΓò¬┬╗ Γò¬┬íΓò¬ΓöéΓöÿ├¿Γöÿ├Ñ Γò¬ΓòúΓöÿ├ñΓöÿ├¿ Γò¬┬íΓò¬ΓöéΓöÿ├Ñ ',2,'[{\"changed\": {\"fields\": [\"\\u062d\\u0627\\u0644\\u0629 \\u0627\\u062f\\u0627\\u0621 \\u0627\\u0644\\u062e\\u062f\\u0645\\u0629\", \"CollcetStatusNums\"]}}]',18,6),(140,'2023-04-06 04:17:12.328000','10','Γò¬┬½Γò¬┬╗Γöÿ├¿Γò¬┬╝Γöÿ├º Γöÿ├áΓò¬┬íΓöÿ├áΓò¬┬╗ Γò¬┬íΓò¬ΓöéΓöÿ├Ñ',2,'[{\"changed\": {\"fields\": [\"\\u062d\\u0627\\u0644\\u0629 \\u0627\\u062f\\u0627\\u0621 \\u0627\\u0644\\u062e\\u062f\\u0645\\u0629\", \"CollcetStatusNums\"]}}]',18,6),(141,'2023-04-06 04:17:26.738000','9','Γò¬┬½Γò¬┬╗Γöÿ├¿Γò¬┬╝Γöÿ├º Γöÿ├áΓò¬┬íΓöÿ├áΓò¬┬╗ Γò¬┬íΓò¬ΓöéΓöÿ├Ñ',2,'[{\"changed\": {\"fields\": [\"\\u062d\\u0627\\u0644\\u0629 \\u0627\\u062f\\u0627\\u0621 \\u0627\\u0644\\u062e\\u062f\\u0645\\u0629\", \"CollcetStatusNums\"]}}]',18,6),(142,'2023-04-06 04:18:12.165000','16','Γöÿ├ºΓò¬┬┐Γò¬ΓîÉ Γò¬ΓòúΓò¬ΓöñΓò¬ΓûÆΓöÿ├½ Γò¬ΓûÆΓò¬┬║Γò¬ΓòóΓöÿ├½ Γò¬┬║Γöÿ├ñΓöÿ├áΓöÿ├ºΓò¬┬╗Γöÿ├½',2,'[]',18,6),(143,'2023-04-06 05:02:28.668000','6','Γò¬┬íΓò¬ΓöéΓò¬┬║Γöÿ├á Γò¬┬║Γöÿ├ñΓò¬┬╗Γöÿ├¿Γöÿ├Ñ Γò¬ΓòûΓöÿ├º Γöÿ├áΓò¬┬íΓöÿ├áΓöÿ├¬Γò¬┬╗ ',2,'[{\"changed\": {\"fields\": [\"\\u0631\\u0642\\u0645 \\u0627\\u0644\\u0634\\u0647\\u0631\"]}}]',18,6),(144,'2023-04-06 05:02:46.546000','7','Γöÿ├áΓò¬┬íΓöÿ├áΓò¬┬╗ Γò¬┬íΓò¬ΓöéΓöÿ├Ñ Γò¬ΓòúΓò¬┬║Γò¬┬┐Γò¬┬╗',2,'[{\"changed\": {\"fields\": [\"\\u0631\\u0642\\u0645 \\u0627\\u0644\\u0634\\u0647\\u0631\"]}}]',18,6),(145,'2023-04-06 05:02:54.923000','8','Γöÿ├áΓò¬┬íΓöÿ├áΓò¬┬╗ Γò¬┬íΓò¬ΓöéΓöÿ├Ñ Γò¬ΓòúΓò¬┬║Γò¬┬┐Γò¬┬╗',2,'[{\"changed\": {\"fields\": [\"\\u0631\\u0642\\u0645 \\u0627\\u0644\\u0634\\u0647\\u0631\"]}}]',18,6),(146,'2023-04-07 19:55:45.594020','13','╪º┘ä┘à╪¡┘à┘ê╪»┘è╪⌐',2,'update through import_export',7,6),(147,'2023-04-07 19:55:45.596951','12','╪º┘ä╪Ñ╪│┘â╪º┘å ╪º┘ä┘à┘à┘è╪▓',2,'update through import_export',7,6),(148,'2023-04-07 19:55:45.597931','11','┘â╪▒┘ê╪▒',2,'update through import_export',7,6),(149,'2023-04-07 19:55:45.609639','10','┘å╪¼╪╣ ╪º┘ä┘à╪¡╪╖╪⌐',2,'update through import_export',7,6),(150,'2023-04-07 19:55:45.611591','9','╪º┘ä╪▒╪╢┘ê╪º┘å',2,'update through import_export',7,6),(151,'2023-04-07 19:55:45.612564','8','╪¼╪¿┘ä ╪¬┘é┘ê┘é',2,'update through import_export',7,6),(152,'2023-04-07 19:55:45.614519','7','┘à┘ê┘ä ╪º┘ä╪¡┘â┘è┘à',2,'update through import_export',7,6),(153,'2023-04-07 19:55:45.616471','6','╪«╪º┘ä╪» ╪¿┘å ╪º┘ä┘ê┘ä┘è╪»',2,'update through import_export',7,6),(154,'2023-04-07 19:55:45.617447','5','╪º┘ä┘à┘é╪º┘ê┘ä┘ê┘å',2,'update through import_export',7,6),(155,'2023-04-07 19:55:45.619399','4','╪╣╪¿╪º╪» ╪º┘ä╪▒╪¡┘à┘å ┘ê╪┤╪º╪▒╪╣ ╪º┘ä╪│╪º╪»╪º╪¬',2,'update through import_export',7,6),(156,'2023-04-07 19:55:45.621348','3','╪º┘ä╪╣┘é╪º╪»',2,'update through import_export',7,6),(157,'2023-04-07 19:55:45.622327','2','╪º┘ä┘à┘à┘è╪▓ 1 ┘ê 2',2,'update through import_export',7,6),(158,'2023-04-07 19:55:45.624277','1','┘à╪»┘è┘å┘ç ┘å╪º╪╡╪▒',2,'update through import_export',7,6),(159,'2023-04-07 19:56:08.393631','2','╪«╪»┘à╪⌐ ╪º┘ä╪╣┘à┘ä╪º╪í',2,'update through import_export',10,6),(160,'2023-04-07 19:56:08.395582','1','╪º╪»╪«╪º┘ä ╪º┘ä╪¿┘è╪º┘å╪º╪¬ ┘ê╪º┘ä╪¬╪¡╪╡┘è┘ä',2,'update through import_export',10,6),(161,'2023-04-07 19:56:20.305061','3','╪¿╪»┘ê┘å',2,'update through import_export',11,6),(162,'2023-04-07 19:56:20.309942','2','╪│╪º╪▒╪⌐ ╪╣╪º╪»┘ä',2,'update through import_export',11,6),(163,'2023-04-07 19:56:20.313846','1','╪┤┘è┘à╪º╪í ╪º╪¡┘à╪»',2,'update through import_export',11,6),(164,'2023-04-07 19:56:44.759848','84','┘à╪¡┘à╪» ╪¡╪│┘å ╪╣╪º╪¿╪»',2,'update through import_export',8,6),(165,'2023-04-07 19:56:44.761802','82','╪¡╪│╪º┘à ╪º┘ä╪»┘è┘å ╪╖┘ç ┘à╪¡┘à┘ê╪» ',2,'update through import_export',8,6),(166,'2023-04-07 19:56:44.762774','80','┘à╪¡┘à╪» ╪╣┘ê╪╢ ╪╣╪¿╪»┘ç ',2,'update through import_export',8,6),(167,'2023-04-07 19:56:44.764729','79','┘à╪¡┘à╪» ╪º╪¡┘à╪» ╪╣╪¿╪»╪º┘ä╪╣╪╕┘è┘à ',2,'update through import_export',8,6),(168,'2023-04-07 19:56:44.766678','78','┘ê┘ä┘è╪» ╪╣╪¿╪»╪º┘ä╪¿╪º┘é┘è ╪º┘à┘è┘å ╪║╪▒┘è╪¿',2,'update through import_export',8,6),(169,'2023-04-07 19:56:44.767654','77','╪│┘è╪» ┘à╪¡┘à╪» ╪¡╪│┘è┘å ╪¡┘à╪»╪º┘å ',2,'update through import_export',8,6),(170,'2023-04-07 19:56:44.769609','76','╪¿╪¡╪▒ ╪º╪¡┘à╪» ╪│┘è╪»',2,'update through import_export',8,6),(171,'2023-04-07 19:56:44.771561','75','╪│┘è╪» ╪╣┘ä┘è ╪¡╪│┘å',2,'update through import_export',8,6),(172,'2023-04-07 19:56:44.773524','74','╪╣┘ä┘è╪º╪í ┘ç╪┤╪º┘à ╪╡╪º┘ä╪¡ ╪│┘ä┘è┘à╪º┘å',2,'update through import_export',8,6),(173,'2023-04-07 19:56:44.774489','73','┘â╪▒┘è┘à ╪╣╪¿╪»╪º┘ä┘à╪╣╪╖┘è ┘à╪¡┘à╪»',2,'update through import_export',8,6),(174,'2023-04-07 19:56:44.776438','72','╪º┘à┘è╪▒┘ç ┘ê╪¡┘è╪» ╪╣┘ä┘è',2,'update through import_export',8,6),(175,'2023-04-07 19:56:44.778391','71','╪│╪╣╪º╪» ┘à╪╡╪╖┘ü┘è ╪º╪¡┘à╪»',2,'update through import_export',8,6),(176,'2023-04-07 19:56:44.779368','70','╪º╪¿╪¬╪│╪º┘à ╪▓┘è╪»╪º┘å ╪╣╪¿┘è╪» ╪╣┘ä┘è',2,'update through import_export',8,6),(177,'2023-04-07 19:56:44.781321','69','┘è┘ê╪│┘ü ┘à╪¡┘à┘ê╪» ╪¿╪»╪▒┘è',2,'update through import_export',8,6),(178,'2023-04-07 19:56:44.783270','68','╪╣┘è╪» ┘à╪¡┘à╪» ╪╣╪¿╪»┘ç',2,'update through import_export',8,6),(179,'2023-04-07 19:56:44.784247','67','╪¿╪┤┘è╪▒ ╪¼┘à╪╣┘ç ╪╣┘ä┘è',2,'update through import_export',8,6),(180,'2023-04-07 19:56:44.786201','66','╪º╪¿╪▒╪º┘ç┘è┘à ┘ü╪º┘ê┘è ╪╣╪¿╪»╪º┘ä┘ä┘ç',2,'update through import_export',8,6),(181,'2023-04-07 19:56:44.788150','65','┘å╪º╪░╪¼ ╪╡┘ä╪º╪¡ ╪º╪¡┘à╪»',2,'update through import_export',8,6),(182,'2023-04-07 19:56:44.790102','64','┘à╪╡╪╖┘ü┘è ╪º┘ä╪¡╪│┘å ╪╖┘ç',2,'update through import_export',8,6),(183,'2023-04-07 19:56:44.792058','63','┘à╪¡┘à┘ê╪» ╪º╪¡┘à╪» ┘à╪¡┘à┘ê╪»',2,'update through import_export',8,6),(184,'2023-04-07 19:56:44.806698','62',' ┘à┘å┘è╪▒ ┘à╪¡┘à╪» ┘ü╪¬╪¡ ╪º┘ä┘ä┘ç',2,'update through import_export',8,6),(185,'2023-04-07 19:56:44.814505','61','┘à╪¡┘à╪» ┘à┘å┘è╪▒ ┘à╪¡┘à╪» ┘ü╪¬╪¡ ╪º┘ä┘ä┘ç',2,'update through import_export',8,6),(186,'2023-04-07 19:56:44.818409','60','╪º╪¡┘à╪» ┘à┘å┘è╪▒ ┘à╪¡┘à╪» ┘ü╪¬╪¡ ╪º┘ä┘ä┘ç',2,'update through import_export',8,6),(187,'2023-04-07 19:56:44.821337','59','┘à╪¡┘à┘ê╪» ┘à╪¡┘à╪»',2,'update through import_export',8,6),(188,'2023-04-07 19:56:44.825241','58','╪╡┘ä╪º╪¡ ╪º┘ä╪»┘è┘å ',2,'update through import_export',8,6),(189,'2023-04-07 19:56:44.829173','57','╪º╪¡┘à╪» ╪│┘è╪» ┘à╪¡┘à╪» ┘ç╪┤╪º┘à ',2,'update through import_export',8,6),(190,'2023-04-07 19:56:44.832081','56','╪º╪¡┘à╪» ╪╣╪¿╪»╪º┘ä┘ä┘ç ╪¡╪│╪¿ ╪º┘ä┘ä┘ç',2,'update through import_export',8,6),(191,'2023-04-07 19:56:44.835010','55','╪º╪¡┘à╪» ╪▒┘à╪╢╪º┘å ╪╣╪¿╪»╪º┘ä┘à┘é╪╡┘ê╪»',2,'update through import_export',8,6),(192,'2023-04-07 19:56:44.837937','54','╪│┘ç╪º┘à ╪º╪¿╪▒╪º┘ç┘è┘à ┘à╪¡┘à╪»',2,'update through import_export',8,6),(193,'2023-04-07 19:56:44.839888','53','┘à╪¡┘à┘ê╪» ┘à╪¡┘à╪» ┘ü╪ñ╪º╪»',2,'update through import_export',8,6),(194,'2023-04-07 19:56:44.842375','52','╪│╪º┘à┘è┘ç ╪╣┘ê╪╢ ╪╣╪¿╪»╪º┘ä╪╣╪▓┘è╪▓ ',2,'update through import_export',8,6),(195,'2023-04-07 19:56:44.845303','51','╪º╪¡┘à╪» ╪╣╪¿╪»╪º┘ä╪¡┘à┘è╪» ┘à╪¡┘à╪» ',2,'update through import_export',8,6),(196,'2023-04-07 19:56:44.847256','50','╪º┘è┘à┘å ┘â┘à╪º┘ä ╪¬┘ê┘ü┘è┘é',2,'update through import_export',8,6),(197,'2023-04-07 19:56:44.849207','49','╪º╪│┘ä╪º┘à ╪╣╪¿╪»╪º┘ä┘à┘å╪╣┘à ┘à╪¡┘à╪»',2,'update through import_export',8,6),(198,'2023-04-07 19:56:44.851161','48','╪╣╪¿╪»╪º┘ä┘ä┘ç ┘à╪¡┘à╪» ╪╣╪¿╪»╪º┘ä┘ä┘ç',2,'update through import_export',8,6),(199,'2023-04-07 19:56:44.853111','47','╪╡╪¿╪▒┘è ╪▒┘â╪º╪¿┘è ╪º╪¿╪▒╪º┘ç┘è┘à',2,'update through import_export',8,6),(200,'2023-04-07 19:56:44.854087','46','┘ê╪º╪ª┘ä ╪▒┘ü╪╣╪¬ ┘à╪¡┘à╪»',2,'update through import_export',8,6),(201,'2023-04-07 19:56:44.856042','45','╪╣╪¿╪»╪º┘ä╪┤┘â┘ê╪▒ ┘à╪¼╪º╪▓┘è ┘à╪¡┘à╪»',2,'update through import_export',8,6),(202,'2023-04-07 19:56:44.857991','44','╪╣╪¿╪»╪º┘ä┘à╪º┘ä┘â ┘à╪¡┘à╪» ╪º╪¡┘à╪» ┘à╪¡┘à╪»',2,'update through import_export',8,6),(203,'2023-04-07 19:56:44.859945','43','╪º╪¡┘à╪» ╪¡╪│┘å ╪│╪▒╪º╪¼',2,'update through import_export',8,6),(204,'2023-04-07 19:56:44.861898','42',' ╪º╪»┘è╪¿┘ç ╪╣╪¿╪»╪º┘ä╪¿╪º┘é┘è ╪º┘ä╪┤┘è╪«',2,'update through import_export',8,6),(205,'2023-04-07 19:56:44.863849','41','╪º┘à ╪º╪┤╪▒┘ü ┘è┘ê╪│┘ü ╪¼╪▒╪│ ',2,'update through import_export',8,6),(206,'2023-04-07 19:56:44.865802','40','╪╣┘à╪▒ ┘ü┘ê╪▓┘è ╪º╪¡┘à╪»',2,'update through import_export',8,6),(207,'2023-04-07 19:56:44.866775','39','┘à╪¡┘à╪» ╪▓┘â┘è ╪º┘ä┘à┘ê╪¼┘è',2,'update through import_export',8,6),(208,'2023-04-07 19:56:44.868729','38','╪º┘ä╪¡╪│┘è┘å ┘à┘å╪╡┘ê╪▒ ╪╣╪¿╪»╪º┘ä┘ê╪º╪¡╪»',2,'update through import_export',8,6),(209,'2023-04-07 19:56:44.872632','37','╪º╪¡┘à╪» ╪╣╪º╪¿╪»┘è┘å ╪º╪¡┘à╪»',2,'update through import_export',8,6),(210,'2023-04-07 19:56:44.876538','36','╪▓┘è┘å╪¿ ╪╣╪╖╪º ╪¼╪º╪» ┘à╪¡┘à╪¡┘à┘ê╪»',2,'update through import_export',8,6),(211,'2023-04-07 19:56:44.880442','35','┘à╪¡┘à╪» ╪¿┘ç╪¼╪¬ ┘ü┘ç┘à┘è ╪¿╪▒╪║┘ê╪¬',2,'update through import_export',8,6),(212,'2023-04-07 19:56:44.884346','34','┘à╪¡┘à╪» ╪╣╪¿╪»╪º┘ä┘å╪º╪╡╪▒ ┘à╪¡┘à╪» ╪º┘ä╪│┘è╪»',2,'update through import_export',8,6),(213,'2023-04-07 19:56:44.887273','33','╪╣╪¿╪»╪º┘ä┘å╪º╪╡╪▒ ┘à╪¡┘à╪» ╪º┘ä╪│┘è╪»',2,'update through import_export',8,6),(214,'2023-04-07 19:56:44.891176','32','╪│╪º┘à┘è╪⌐ ╪╣╪¿╪» ╪º┘ä┘à┘å╪╣┘à ╪¡┘å┘ü┘ë',2,'update through import_export',8,6),(215,'2023-04-07 19:56:44.895080','31','╪º┘ä╪│┘è╪» ┘à╪¡┘à╪» ╪º┘ä╪│┘è╪»',2,'update through import_export',8,6),(216,'2023-04-07 19:56:44.898008','30','┘à╪╡╪╖┘ü┘ë ╪º┘ä╪│┘è╪» ┘à╪¡┘à╪» ╪º┘ä╪│┘è╪»',2,'update through import_export',8,6),(217,'2023-04-07 19:56:44.899959','29','╪▒┘à╪╢╪º┘å ╪╣┘ê╪╢ ╪º┘ä┘ä┘ç ╪╡╪º╪¿╪▒ ╪╣┘ä┘è',2,'update through import_export',8,6),(218,'2023-04-07 19:56:44.901913','28','╪╣╪╡╪º┘à ╪╣╪¿╪»╪º┘ä┘ä┘ç ┘à╪¡┘à╪»',2,'update through import_export',8,6),(219,'2023-04-07 19:56:44.903863','27','╪│┘ê╪▓╪º┘å ╪╡┘ä╪º╪¡ ╪º┘ä╪»┘è┘å ╪╣╪¿╪»╪º┘ä╪╣╪╕┘è┘à ╪º╪¡┘à╪»',2,'update through import_export',8,6),(220,'2023-04-07 19:56:44.905818','26','╪│┘à┘è╪▒┘ç ╪│┘è╪» ╪╣┘ä┘è ╪º┘ä╪╖┘è╪¿',2,'update through import_export',8,6),(221,'2023-04-07 19:56:44.907769','25','╪º┘ä┘à╪│╪¬╪┤╪º╪▒ ╪╣┘à╪▒┘ê ┘è╪¡┘è┘è ╪º╪¿┘ê ╪▓┘è╪»',2,'update through import_export',8,6),(222,'2023-04-07 19:56:44.909719','24','┘à╪│╪¬╪┤╪º╪▒ ╪«╪º┘ä╪» ┘à╪¡┘à╪» ╪▒┘è╪º┘å',2,'update through import_export',8,6),(223,'2023-04-07 19:56:44.911671','23','╪º╪¡┘à╪» ╪╣╪¿╪»╪º┘ä╪┤╪º┘ü┘è ╪º┘å┘ê╪▒',2,'update through import_export',8,6),(224,'2023-04-07 19:56:44.914599','22','╪º╪┤╪▒┘ü ╪º┘ä╪º┘à┘è╪▒ ╪º╪¿╪▒╪º┘ç┘è┘à',2,'update through import_export',8,6),(225,'2023-04-07 19:56:44.916554','21','╪º╪¡┘à╪» ╪╣╪¿╪» ╪▒╪º╪▓┘é ╪º╪¡┘à╪»',2,'update through import_export',8,6),(226,'2023-04-07 19:56:44.918502','20','┘ç╪┤╪º┘à ╪│╪╣╪» ╪º┘ä╪»┘è┘å ╪º╪¡┘à╪»',2,'update through import_export',8,6),(227,'2023-04-07 19:56:44.919478','19','╪º╪¡┘à╪» ╪¡╪│┘è┘å ╪╣┘ä┘è ╪¡╪│┘å',2,'update through import_export',8,6),(228,'2023-04-07 19:56:44.922407','18','┘ü╪¬╪¡┘è ╪│╪╣╪» ╪º┘ä╪»┘è┘å ╪╣╪¿╪» ╪º┘ä╪▒╪¡┘à┘å',2,'update through import_export',8,6),(229,'2023-04-07 19:56:44.924363','17','╪º╪¡┘à╪» ╪╣╪¿╪» ╪º┘ä╪┤╪º┘ü┘ë ╪╣╪¿╪» ╪º┘ä╪¡┘à┘è╪» ',2,'update through import_export',8,6),(230,'2023-04-07 19:56:44.927296','16','╪╣╪¿╪» ╪º┘ä┘å╪º╪╡╪▒ ╪╡╪º╪¿╪▒ ╪º╪¡┘à╪» ',2,'update through import_export',8,6),(231,'2023-04-07 19:56:44.931200','15','╪┤╪º╪░┘ä┘ë ╪╣╪╖╪º┘ä┘ä╪⌐ ┘à╪¡┘à╪» ',2,'update through import_export',8,6),(232,'2023-04-07 19:56:44.935118','14','┘à╪╡╪╖┘ü┘ë ╪¼┘à╪╣╪⌐ ┘à┘ç╪»┘ë',2,'update through import_export',8,6),(233,'2023-04-07 19:56:44.939008','13','╪│┘ä╪╖╪º┘å ╪╣╪¿╪» ╪º┘ä╪¡┘à┘è╪» ┘ç╪º╪▒┘ê┘å ',2,'update through import_export',8,6),(234,'2023-04-07 19:56:44.942476','12','┘à╪¡┘à╪» ╪╣╪¿╪» ╪º┘ä╪╣╪▓┘è╪▓ ╪º╪¡┘à╪» ',2,'update through import_export',8,6),(235,'2023-04-07 19:56:44.945403','11','┘ç╪¿╪⌐ ╪╣╪┤╪▒┘ë ╪▒╪º╪╢┘ë ╪º┘ä┘à┘ç╪»┘ë',2,'update through import_export',8,6),(236,'2023-04-07 19:56:44.948331','10','╪▓┘è╪º╪» ╪│╪╣╪» ╪▓╪╣┘ä┘ê┘ä ',2,'update through import_export',8,6),(237,'2023-04-07 19:56:44.950282','9','╪╣┘ä╪º╪í ╪º┘ä╪»┘è┘å ╪º╪¡┘à╪» ╪╣╪¿╪» ╪º┘ä┘à╪╣╪╖┘ë ',2,'update through import_export',8,6),(238,'2023-04-07 19:56:44.952234','8','╪¡╪│┘å ╪º╪¡┘à╪» ╪▓┘è┘å ╪º┘ä╪╣╪º╪¿╪»┘è┘å ',2,'update through import_export',8,6),(239,'2023-04-07 19:56:44.954186','7','╪╡╪º╪¿╪▒ ┘à╪¡┘à╪» ╪╣┘ä┘è ┘à╪¡┘à╪»',2,'update through import_export',8,6),(240,'2023-04-07 19:56:44.957114','6','┘à╪¡┘à╪» ╪¡╪│┘è┘å ╪╣┘ä┘è ╪¡╪│┘å ',2,'update through import_export',8,6),(241,'2023-04-07 19:56:44.959066','5','┘à╪¡┘à╪» ╪¡╪│┘è┘å ╪╣┘ä┘è ╪¡╪│┘å ',2,'update through import_export',8,6),(242,'2023-04-07 19:56:44.961018','4','╪«╪»┘è╪¼┘ç ┘à╪¡┘à╪» ╪¡╪│┘å',2,'update through import_export',8,6),(243,'2023-04-07 19:56:44.961994','3','╪¡╪│╪º┘à ╪º┘ä╪»┘è┘å ╪╖┘ç ┘à╪¡┘à┘ê╪» ',2,'update through import_export',8,6),(244,'2023-04-07 19:56:57.937143','15','15',2,'update through import_export',19,6),(245,'2023-04-07 19:56:57.939095','14','14',2,'update through import_export',19,6),(246,'2023-04-07 19:56:58.043095','13','13',2,'update through import_export',19,6),(247,'2023-04-07 19:56:58.046998','12','12',2,'update through import_export',19,6),(248,'2023-04-07 19:56:58.050904','11','11',2,'update through import_export',19,6),(249,'2023-04-07 19:56:58.104155','10','10',2,'update through import_export',19,6),(250,'2023-04-07 19:56:58.108057','9','9',2,'update through import_export',19,6),(251,'2023-04-07 19:56:58.111962','8','8',2,'update through import_export',19,6),(252,'2023-04-07 19:56:58.115867','6','6',2,'update through import_export',19,6),(253,'2023-04-07 19:57:11.956815','24','╪¼┘à╪╣ ┘à┘å╪▓┘ä┘ë',2,'update through import_export',13,6),(254,'2023-04-07 19:57:11.958769','23','╪¬┘å╪╕┘è┘ü ┘à┘å╪▓┘ä┘ë - ╪╣┘à┘è┘é',2,'update through import_export',13,6),(255,'2023-04-07 19:57:11.960721','22','╪¬┘å╪╕┘è┘ü ┘à┘å╪▓┘ä┘ë ╪¿╪│┘è╪╖',2,'update through import_export',13,6),(256,'2023-04-07 19:57:11.961697','21','╪¼┘à╪╣ ┘à┘å╪▓┘ä┘ë',2,'update through import_export',13,6),(257,'2023-04-07 19:57:11.963649','20','┘ä╪¬╪º┘ä╪¬',2,'update through import_export',13,6),(258,'2023-04-07 19:57:11.964622','19',' ╪¼┘à╪╣ ┘à┘å╪▓┘ä┘ë',2,'update through import_export',13,6),(259,'2023-04-07 19:57:11.966577','18','╪¼┘à╪╣ ┘à┘å╪▓┘ä┘ë',2,'update through import_export',13,6),(260,'2023-04-07 19:57:11.968526','17','╪¼┘à╪╣ ┘à┘å╪▓┘ä┘ë',2,'update through import_export',13,6),(261,'2023-04-07 19:57:11.970037','16',' ╪▒╪┤ ┘ê╪¬╪╣┘é┘è┘à ',2,'update through import_export',13,6),(262,'2023-04-07 19:57:11.971015','15','╪¼┘à╪╣ ┘à┘å╪▓┘ä┘ë',2,'update through import_export',13,6),(263,'2023-04-07 19:57:11.972970','14','╪▒╪┤ ┘ê╪¬╪╣┘é┘è┘à',2,'update through import_export',13,6),(264,'2023-04-07 19:57:11.974922','13','╪¼┘à╪╣ ┘à┘å╪▓┘ä┘ë',2,'update through import_export',13,6),(265,'2023-04-07 19:57:11.975898','12','╪¬┘å╪╕┘è┘ü ╪│┘ä╪º┘ä┘à ╪╣┘à╪º╪▒╪⌐',2,'update through import_export',13,6),(266,'2023-04-07 19:57:11.977850','11','╪¬┘å╪╕┘è┘ü ┘à┘å╪▓┘ä┘ë - ╪╣┘à┘è┘é ',2,'update through import_export',13,6),(267,'2023-04-07 19:57:11.978826','10','╪¬┘å╪╕┘è┘ü ┘à┘å╪▓┘ä┘ë ╪¿╪│┘è╪╖',2,'update through import_export',13,6),(268,'2023-04-07 19:57:26.080122','25','╪¼┘à╪╣ ┘à┘å╪▓┘ä┘ë',2,'[{\"changed\": {\"fields\": [\"Name\"]}}]',13,6),(269,'2023-04-07 19:57:45.427381','16','┘ç╪¿╪⌐ ╪╣╪┤╪▒┘ë ╪▒╪º╪╢┘ë ╪º┘ä┘à┘ç╪»┘ë',2,'update through import_export',18,6),(270,'2023-04-07 19:57:45.429334','15','╪▓┘è╪º╪» ╪│╪╣╪» ╪▓╪╣┘ä┘ê┘ä ',2,'update through import_export',18,6),(271,'2023-04-07 19:57:45.432263','14','╪╣┘ä╪º╪í ╪º┘ä╪»┘è┘å ╪º╪¡┘à╪» ╪╣╪¿╪» ╪º┘ä┘à╪╣╪╖┘ë ',2,'update through import_export',18,6),(272,'2023-04-07 19:57:45.435191','13','╪¡╪│┘å ╪º╪¡┘à╪» ╪▓┘è┘å ╪º┘ä╪╣╪º╪¿╪»┘è┘å ',2,'update through import_export',18,6),(273,'2023-04-07 19:57:45.438118','12','╪╡╪º╪¿╪▒ ┘à╪¡┘à╪» ╪╣┘ä┘è ┘à╪¡┘à╪»',2,'update through import_export',18,6),(274,'2023-04-07 19:57:45.441046','11','┘à╪¡┘à╪» ╪¡╪│┘è┘å ╪╣┘ä┘è ╪¡╪│┘å ',2,'update through import_export',18,6),(275,'2023-04-07 19:57:45.442998','10','╪«╪»┘è╪¼┘ç ┘à╪¡┘à╪» ╪¡╪│┘å',2,'update through import_export',18,6),(276,'2023-04-07 19:57:45.444951','9','╪«╪»┘è╪¼┘ç ┘à╪¡┘à╪» ╪¡╪│┘å',2,'update through import_export',18,6),(277,'2023-04-07 19:57:45.446903','8','┘à╪¡┘à╪» ╪¡╪│┘å ╪╣╪º╪¿╪»',2,'update through import_export',18,6),(278,'2023-04-07 19:57:45.448854','7','┘à╪¡┘à╪» ╪¡╪│┘å ╪╣╪º╪¿╪»',2,'update through import_export',18,6),(279,'2023-04-07 19:57:45.450805','6','╪¡╪│╪º┘à ╪º┘ä╪»┘è┘å ╪╖┘ç ┘à╪¡┘à┘ê╪» ',2,'update through import_export',18,6),(280,'2023-04-08 01:33:06.386310','26','╪¬┘å╪╕┘è┘ü  ┘à┘å╪▓┘ä┘ë - ╪╣┘à┘è┘é',1,'[{\"added\": {}}]',13,6),(281,'2023-04-08 01:33:12.893031','10','╪«╪»┘è╪¼┘ç ┘à╪¡┘à╪» ╪¡╪│┘å',2,'[{\"changed\": {\"fields\": [\"Service\"]}}]',18,6),(282,'2023-04-08 02:03:25.834448','27','╪¬┘å╪╕┘è┘ü ┘à┘å╪▓┘ä┘ë ╪¿╪│┘è╪╖',1,'[{\"added\": {}}]',13,6),(283,'2023-04-08 02:03:57.886982','9','╪«╪»┘è╪¼┘ç ┘à╪¡┘à╪» ╪¡╪│┘å',2,'[{\"changed\": {\"fields\": [\"Service\"]}}]',18,6),(284,'2023-04-08 02:04:45.742737','26','╪¬┘å╪╕┘è┘ü  ┘à┘å╪▓┘ä┘ë - ╪╣┘à┘è┘é',2,'[{\"changed\": {\"fields\": [\"PriceType\"]}}]',13,6),(285,'2023-04-08 02:04:59.157864','10','╪«╪»┘è╪¼┘ç ┘à╪¡┘à╪» ╪¡╪│┘å',2,'[{\"changed\": {\"fields\": [\"\\u0627\\u0644\\u0645\\u0628\\u0644\\u063a \\u0627\\u0644\\u0645\\u0637\\u0644\\u0648\\u0628 \\u062a\\u062d\\u0635\\u064a\\u0644\\u0647\"]}}]',18,6),(286,'2023-04-08 02:05:10.314333','9','╪«╪»┘è╪¼┘ç ┘à╪¡┘à╪» ╪¡╪│┘å',2,'[{\"changed\": {\"fields\": [\"\\u0627\\u0644\\u0645\\u0628\\u0644\\u063a \\u0627\\u0644\\u0645\\u062a\\u0628\\u0642\\u0649\"]}}]',18,6),(287,'2023-04-08 02:05:17.931523','27','╪¬┘å╪╕┘è┘ü ┘à┘å╪▓┘ä┘ë  - ╪¿╪│┘è╪╖',2,'[{\"changed\": {\"fields\": [\"Name\"]}}]',13,6),(288,'2023-04-08 02:05:37.346548','10','╪«╪»┘è╪¼┘ç ┘à╪¡┘à╪» ╪¡╪│┘å',2,'[{\"changed\": {\"fields\": [\"\\u0627\\u0644\\u0645\\u0628\\u0644\\u063a \\u0627\\u0644\\u0645\\u0637\\u0644\\u0648\\u0628 \\u062a\\u062d\\u0635\\u064a\\u0644\\u0647\"]}}]',18,6),(289,'2023-04-08 02:05:54.403069','10','╪«╪»┘è╪¼┘ç ┘à╪¡┘à╪» ╪¡╪│┘å',2,'[{\"changed\": {\"fields\": [\"\\u0627\\u0644\\u0645\\u0628\\u0644\\u063a \\u0627\\u0644\\u0645\\u0637\\u0644\\u0648\\u0628 \\u062a\\u062d\\u0635\\u064a\\u0644\\u0647\", \"\\u0627\\u0644\\u0645\\u0628\\u0644\\u063a \\u0627\\u0644\\u0645\\u062a\\u0628\\u0642\\u0649\"]}}]',18,6),(290,'2023-04-08 02:25:12.809159','9','╪«╪»┘è╪¼┘ç ┘à╪¡┘à╪» ╪¡╪│┘å',2,'[{\"changed\": {\"fields\": [\"\\u0627\\u0644\\u0645\\u0628\\u0644\\u063a \\u0627\\u0644\\u0645\\u0637\\u0644\\u0648\\u0628 \\u062a\\u062d\\u0635\\u064a\\u0644\\u0647\"]}}]',18,6),(291,'2023-04-08 14:57:06.017911','4','╪«╪»┘è╪¼┘ç ┘à╪¡┘à╪» ╪¡╪│┘å',2,'[{\"changed\": {\"fields\": [\"StreetName\", \"AddressDetails\", \"Notes\"]}}]',8,6),(292,'2023-04-08 15:04:25.974297','4','╪«╪»┘è╪¼┘ç ┘à╪¡┘à╪» ╪¡╪│┘å',2,'[{\"changed\": {\"fields\": [\"StreetName\", \"AddressDetails\", \"Notes\"]}}]',8,6),(293,'2023-04-09 14:10:22.199977','3','customerService1',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\"]}}]',4,6),(294,'2023-04-09 14:10:38.387585','2','dataEntry1',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\"]}}]',4,6),(295,'2023-04-09 14:11:04.668774','4','manager1',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\"]}}]',4,6),(296,'2023-04-09 14:11:14.490515','5','manager2',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\"]}}]',4,6),(297,'2023-04-09 14:11:24.237479','7','tahseal1',2,'[{\"changed\": {\"fields\": [\"First name\"]}}]',4,6),(298,'2023-04-09 14:29:34.867626','4','╪«╪»┘è╪¼┘ç ┘à╪¡┘à╪» ╪¡╪│┘å',2,'[{\"changed\": {\"fields\": [\"StreetName\"]}}]',8,6),(299,'2023-04-13 07:19:57.486641','4','╪º┘è┘à┘å ┘à╪¡┘à╪» ╪º┘ä╪│┘è╪»',1,'[{\"added\": {}}]',11,6),(300,'2023-04-13 07:21:24.423888','5','┘à╪¡┘à╪» ╪╣┘ä┘ë ╪¡╪│┘è┘å',1,'[{\"added\": {}}]',11,6),(301,'2023-04-17 15:50:28.654541','85','┘à╪╡╪╖┘ü┘ë ╪¼┘à╪╣╪⌐ ┘à┘ç╪»┘ë',2,'[{\"changed\": {\"fields\": [\"Area\"]}}]',8,6),(302,'2023-04-18 01:47:05.328252','32','╪¼┘à╪╣ ┘à┘å╪▓┘ä┘ë',2,'[{\"changed\": {\"fields\": [\"Name\", \"Price\"]}}]',13,6),(303,'2023-04-18 01:48:23.033578','18','18',2,'[{\"changed\": {\"fields\": [\"Created prev date\"]}}]',19,6),(304,'2023-04-18 01:48:36.720477','23','╪┤╪º╪░┘ä┘ë ╪╣╪╖╪º┘ä┘ä╪⌐ ┘à╪¡┘à╪» ',2,'[{\"changed\": {\"fields\": [\"\\u062d\\u0627\\u0644\\u0629 \\u0627\\u062f\\u0627\\u0621 \\u0627\\u0644\\u062e\\u062f\\u0645\\u0629\", \"CollcetStatusNums\"]}}]',18,6),(305,'2023-04-18 02:07:59.057157','23','╪┤╪º╪░┘ä┘ë ╪╣╪╖╪º┘ä┘ä╪⌐ ┘à╪¡┘à╪» ',2,'[]',18,6),(306,'2023-04-18 02:09:31.685625','15','╪┤╪º╪░┘ä┘ë ╪╣╪╖╪º┘ä┘ä╪⌐ ┘à╪¡┘à╪»',2,'[{\"changed\": {\"fields\": [\"Name\", \"StreetName\", \"AddressDetails\", \"Deserved\"]}}]',8,6),(307,'2023-04-18 02:22:23.275109','7','tahseal1',2,'[]',4,6);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(7,'DataEntry','area'),(8,'DataEntry','client'),(21,'DataEntry','collectorder'),(20,'DataEntry','contactrequest'),(9,'DataEntry','contactrequesttypes'),(19,'DataEntry','contract'),(10,'DataEntry','departement'),(11,'DataEntry','employee'),(18,'DataEntry','followcontractservices'),(12,'DataEntry','offers'),(17,'DataEntry','requestsimpleservice'),(13,'DataEntry','service'),(14,'DataEntry','simpleservice'),(16,'DataEntry','subservice'),(15,'DataEntry','typee'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'DataEntry','0001_initial','2023-03-12 18:07:41.564313'),(2,'contenttypes','0001_initial','2023-03-12 18:07:41.609837'),(3,'auth','0001_initial','2023-03-12 18:07:42.163404'),(4,'admin','0001_initial','2023-03-12 18:07:42.295167'),(5,'admin','0002_logentry_remove_auto_add','2023-03-12 18:07:42.315623'),(6,'admin','0003_logentry_add_action_flag_choices','2023-03-12 18:07:42.332083'),(7,'contenttypes','0002_remove_content_type_name','2023-03-12 18:07:42.434775'),(8,'auth','0002_alter_permission_name_max_length','2023-03-12 18:07:42.514351'),(9,'auth','0003_alter_user_email_max_length','2023-03-12 18:07:42.574832'),(10,'auth','0004_alter_user_username_opts','2023-03-12 18:07:42.589361'),(11,'auth','0005_alter_user_last_login_null','2023-03-12 18:07:42.655865'),(12,'auth','0006_require_contenttypes_0002','2023-03-12 18:07:42.662252'),(13,'auth','0007_alter_validators_add_error_messages','2023-03-12 18:07:42.674448'),(14,'auth','0008_alter_user_username_max_length','2023-03-12 18:07:42.732209'),(15,'auth','0009_alter_user_last_name_max_length','2023-03-12 18:07:42.801006'),(16,'auth','0010_alter_group_name_max_length','2023-03-12 18:07:42.858772'),(17,'auth','0011_update_proxy_permissions','2023-03-12 18:07:42.884657'),(18,'auth','0012_alter_user_first_name_max_length','2023-03-12 18:07:42.939192'),(19,'sessions','0001_initial','2023-03-12 18:07:42.986531'),(20,'DataEntry','0002_alter_service_typee','2023-04-03 20:48:13.789207'),(21,'DataEntry','0002_alter_service_notes','2023-04-03 23:06:09.202249'),(22,'DataEntry','0003_followcontractservices_notes','2023-04-03 23:06:09.207957'),(23,'DataEntry','0004_alter_service_pricetype','2023-04-04 01:39:30.875623'),(24,'DataEntry','0005_remove_contract_subservices','2023-04-04 04:45:30.098622'),(25,'DataEntry','0006_remove_followcontractservices_subservice','2023-04-04 04:48:20.683262'),(26,'DataEntry','0002_initial','2023-04-07 19:48:40.039274'),(27,'DataEntry','0003_alter_client_name','2023-04-07 19:51:36.281303'),(28,'DataEntry','0004_alter_client_addressbuilding','2023-04-07 19:52:03.512154'),(29,'DataEntry','0005_alter_client_addressapartment','2023-04-07 19:52:18.057409'),(30,'DataEntry','0006_client_contractdate','2023-04-07 21:29:08.135225'),(31,'DataEntry','0007_client_customfilter','2023-04-11 03:44:46.238983'),(32,'DataEntry','0008_contract_lastpay','2023-04-17 23:58:23.189887');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('1c72m5gdinwdui7cgy2j0xce0c8384po','.eJxVjM0OwiAQhN-FsyHCWn48eu8zkGUXpGpoUtqT8d0tSQ-azGm-b-YtAm5rCVtLS5hYXIURp98uIj1T7YAfWO-zpLmuyxRlV-RBmxxnTq_b4f4dFGxlX2c0Cil7BmvonGEAiOBRR9KQiAe2YHWP0hq9Auu8s-h30bMjvojPF-lCN4I:1pktbj:imTJer1zPR7S0L94UgabycuiJziyPTl8283xWWQmDFA','2023-04-21 21:26:55.966939'),('32fsyspbqfj7w5upkxhtgt5tyolxqees','.eJxVjDsOwyAQRO9CHSEwn4WU6XMGi4X1J7FMBHYV5e7BkoukmWLmzXuzPuzb1O-VSj8ndmUdu_x2GOKT1mNIj7COmce8bmVGfiD8XCu_50TL7WT_BFOoU3s7RVE4IKFlCgp1BKcGDy2VsRKt1eC97oAATFLaOCTfmQhgBzRCYpOOJe-vpqKlEvt8ARG2O24:1pcvVX:eCxikeFCsw_I5ofZOc3OZuMxavRQBc-HY-QaWGOE8gI','2023-03-30 21:51:35.880281'),('98puzexhz0o7cq6b68ko5n9h16lu5gi0','.eJxVjjkOwjAURO_iGlm2ZWehA4mSM0R_8SdhsVGWAiHuTiylgHbmzdO8VQfL3HfLFMduYLVXTu1-MwS6xVQKvkK6ZE05zeOAuiB6ayd9zhzvx439E_Qw9evaNiRSeWMgoK04MiDUZGvXSmUcimfyLZCLdRvJGvTSBBsEG8NiMRTpZczLsxyBGU7rideBH0NSny_80EGU:1pe0ZQ:y4oeW86gLn-AvTKKTnxdbEURbSVnMMf53zP0cLmyLTY','2023-04-02 21:28:04.983029'),('m6f6sd7jp189udl2j9sfo1p85lrpvqvq','.eJxVjssOwiAURP-FtSFQoIA7TVz6DeSWe_tQC6aPhTH-uyXpQrczZ07mzQKsSx_WmaYwIDsyxQ6_WQPxTqkUeIPUZR5zWqah4QXhezvza0Z6nHf2T9DD3G_r6KNQ2kmKTSU0gZUGwUSNqoLWGY9KWfRO-loY7YR14LWx5AlNW9USNmk35fVZjsACl-3E64TjkNjnC6p1QAQ:1pdAIs:QUoJR5f2kmBYgaLfMEYSl0B3_iywCkTnnxFFz5el5Zk','2023-03-31 13:39:30.174378'),('qc3vez7zzw99sa5sp1q0z6zvodk08mv9','.eJxVjMEOwiAQRP-FsyHCWigevfsNzbILbbUpBtqT8d-FpAdN5jTz5r3FgPs2DXsJeZhZXIURp9_OIz3D2gZ-4DomSWnd8uxlQ-SxFnlPHJbbwf4JJixTfUc0Cik6BmvoHKED8OBQe9IQiDu2YHWL0hqdAtu73qKroOOe-FKlY077q6rCUoL4fAFNNzxG:1pkEhV:MKJlc9-ati5kMYx_oR5-L8O4l0NoPAJPJafA2t44m6g','2023-04-20 01:46:09.355572'),('s9neb71oasaxd5gpv36kph6y573vwubv','.eJxVjM0OwiAQhN-FsyFFaKHe9O4zNLvsUuoPmNKejO8uTXrQ0yQz33xvMcC6xGEtPA8TiZOw4vDbIfg7p22gG6QxS5_TMk8oN0Tua5HXTPy47OyfIEKJ9W2Q-w4JgnEdse2CV9q26BwEUI6gNTVAG6-AHWPDGr1tAvVN8KD0sUrHOa-vqlogFobHmZ5TEp8vj3lBBA:1poays:dfy535Wglehi6V_7M7G0_1vDkoA3twG_OyiYEywuzL4','2023-05-02 02:22:06.541398');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-18  4:24:31
