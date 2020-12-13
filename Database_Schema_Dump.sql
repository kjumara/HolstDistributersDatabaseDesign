CREATE DATABASE  IF NOT EXISTS `databasesystemsprojectfall2020` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `databasesystemsprojectfall2020`;
-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: databasesystemsprojectfall2020
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
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `cnum` int NOT NULL,
  `cname` varchar(45) DEFAULT NULL,
  `cfladdress` varchar(45) DEFAULT NULL,
  `csladdress` varchar(45) DEFAULT NULL,
  `ccity` varchar(45) DEFAULT NULL,
  `cstate` varchar(45) DEFAULT NULL,
  `czip` int DEFAULT NULL,
  `cstfladdress` varchar(45) DEFAULT NULL,
  `cstsladdress` varchar(45) DEFAULT NULL,
  `cstcity` varchar(45) DEFAULT NULL,
  `cststate` varchar(45) DEFAULT NULL,
  `cstzip` varchar(45) DEFAULT NULL,
  `territorynum` int DEFAULT NULL,
  `salesrepno` int DEFAULT NULL,
  PRIMARY KEY (`cnum`),
  KEY `territorynum_idx` (`territorynum`),
  KEY `salesrepno_idx` (`salesrepno`),
  CONSTRAINT `salesrepno` FOREIGN KEY (`salesrepno`) REFERENCES `sales_rep` (`SRNUM`),
  CONSTRAINT `territorynum` FOREIGN KEY (`territorynum`) REFERENCES `territory` (`TNUM`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,'Echo Albert','432-2313 Lorem Ave','578-8514 Fringilla Avenue','Grand Island','NE',46447,'Ap #217-4681 Sed Av.','632-4694 Amet Road','Omaha','NV','63619',19,1),(2,'Rama Sharp','688-5846 Fermentum Ave','P.O. Box 669, 6723 Cras Avenue','Kenosha','Wisconsin',99977,'Ap #109-5291 Vel St.','Ap #610-6765 Tellus Avenue','Racine','OR','31574',19,1),(3,'Stacey Leach','143-5109 Phasellus St.','944-6379 Suspendisse St.','Atlanta','GA',45679,'P.O. Box 732, 3181 Nullam Street','Ap #682-1291 Sagittis. St.','Georgia','WI','26179',7,1),(4,'Ina Keller','P.O. Box 984, 4494 Nec Rd.','P.O. Box 420, 8180 Commodo Av.','Fresno','CA',94405,'276 Amet, Rd.','P.O. Box 193, 3086 Mauris Av.','San Francisco','Missouri','90855',1,2),(5,'Igor Berry','P.O. Box 373, 8681 Vel, Av.','764-8789 Nunc St.','San Diego','CA',92274,'364 Rutrum Av.','Ap #458-7888 Donec Ave','San Diego','Kansas','91496',11,5),(6,'Roth Guthrie','P.O. Box 393, 6048 Nulla Ave','Ap #822-8463 Convallis Avenue','Austin','Texas',79195,'930 Cursus, St.','Ap #845-9943 Nisl. Av.','Fort Worth','Utah','90971',9,1),(7,'Ulric Pena','7645 Duis Street','8629 Rhoncus. St.','Seattle','WA',10912,'3564 Ac Road','260-4292 Iaculis Rd.','Olympia','LA','25755',8,10),(8,'Colette Hardy','Ap #931-7315 Dictum Road','Ap #223-6058 Quisque St.','Metairie','Louisiana',92000,'9676 In, Rd.','Ap #193-3735 Nam Avenue','Lafayette','IN','16438',3,9),(9,'Benjamin Powell','334-9184 Egestas Rd.','Ap #229-1151 Ornare Av.','Evansville','IN',95892,'8013 Tincidunt Rd.','Ap #627-4681 Donec Av.','Gary','VA','24885',4,5),(10,'Chaney Bryant','Ap #990-365 Malesuada Ave','1800 Id, St.','Tacoma','WA',13756,'5271 At, Road','Ap #452-3477 Varius Avenue','Seattle','Alabama','94682',1,9),(11,'Avye Simpson','870-3476 Non Road','696-495 Eget, Rd.','Bellevue','Washington',34200,'802-639 Pede. Rd.','5378 Molestie Road','Bellevue','CO','43213',11,8),(12,'Paula Hinton','316-9133 Accumsan Ave','400-3161 Fermentum St.','West Valley City','Utah',15860,'P.O. Box 710, 1960 Pharetra, St.','P.O. Box 764, 8237 Eu Rd.','Sandy','Louisiana','71502',2,7),(13,'Jasmine Walter','P.O. Box 652, 3206 Tortor Rd.','7917 Libero Av.','Minneapolis','MN',67688,'319-8670 Pede, St.','381-2548 Quisque St.','Bloomington','ID','53335',19,5),(14,'Ulysses Donaldson','121-871 Eget Ave','Ap #727-983 Molestie Ave','Gulfport','MS',26286,'719 Mauris. Road','329-6389 Elit St.','Southaven','DE','92592',9,18),(15,'Kylan Leon','Ap #163-989 Egestas St.','5158 Duis Avenue','Chattanooga','Tennessee',25698,'289-3689 Aliquam Av.','P.O. Box 552, 2023 Malesuada Road','Nashville','AR','42603',11,14),(16,'Lawrence Clemons','3763 Orci Rd.','602-8698 Nunc Rd.','Salem','Oregon',15346,'9703 Aenean St.','P.O. Box 409, 322 Parturient St.','Hillsboro','MA','86839',10,15),(17,'Tyrone Petty','109-3413 Ac Rd.','P.O. Box 199, 4806 Sed, St.','Olathe','KS',79945,'5806 Pellentesque Rd.','9236 Sapien. Rd.','Topeka','Illinois','68136',8,13),(18,'Amelia Mendoza','5814 Fames Ave','Ap #117-9794 Orci. Ave','St. Petersburg','Florida',33212,'Ap #677-2472 Orci, Avenue','Ap #845-7951 Nisi St.','Miami','TN','21586',14,11),(19,'Cairo Pruitt','355-6410 Nec, Rd.','P.O. Box 643, 5320 Cubilia Rd.','Aurora','CO',51796,'Ap #830-6340 Lectus. Road','941-4052 Urna. Ave','Aurora','Mississippi','14300',12,10),(20,'Wendy Lancaster','2527 Feugiat St.','P.O. Box 692, 2443 Sit Rd.','Columbus','GA',49251,'Ap #260-8381 Risus. Avenue','Ap #324-4239 Nam St.','Georgia','Iowa','57530',14,9);
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer_sales`
--

DROP TABLE IF EXISTS `customer_sales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer_sales` (
  `CNUM` int NOT NULL,
  `PREVBALANCE` decimal(10,2) DEFAULT NULL,
  `BALANCE` decimal(10,2) DEFAULT NULL,
  `CREDITLIMIT` decimal(10,2) DEFAULT NULL,
  `MTDSALES` decimal(10,2) DEFAULT NULL,
  `YTDSALES` decimal(10,2) DEFAULT NULL,
  `INVOICETOTAL` decimal(10,2) DEFAULT NULL,
  `CURPAYMENT` decimal(10,2) DEFAULT NULL,
  `SALESREPNUM` int DEFAULT NULL,
  PRIMARY KEY (`CNUM`),
  KEY `SRNUM_idx` (`SALESREPNUM`),
  CONSTRAINT `SALESREPNUM` FOREIGN KEY (`SALESREPNUM`) REFERENCES `sales_rep_sales` (`SRNUM`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer_sales`
--

LOCK TABLES `customer_sales` WRITE;
/*!40000 ALTER TABLE `customer_sales` DISABLE KEYS */;
INSERT INTO `customer_sales` VALUES (1,12.45,436.74,8196.25,592.76,4400.28,NULL,NULL,3),(2,412.45,166.99,9582.68,842.12,5435.99,NULL,NULL,18),(3,345.12,524.71,3324.67,432.33,3979.09,NULL,NULL,19),(4,4576.21,122.62,7875.29,635.30,3587.51,NULL,NULL,3),(5,456.87,38.93,9402.44,879.48,6000.28,NULL,NULL,17),(6,120.12,826.82,3386.34,491.51,9238.87,NULL,NULL,16),(7,78345.50,17.32,8724.38,819.12,8193.49,NULL,NULL,8),(8,784.17,606.13,3462.88,621.06,3250.87,NULL,NULL,13),(9,12786.41,978.68,1141.25,647.93,1673.87,NULL,NULL,19),(10,1234.46,485.02,5317.63,714.48,8954.72,NULL,NULL,16),(11,754.57,439.08,3164.41,938.63,8061.99,NULL,NULL,3),(12,12.75,1440.31,9869.14,NULL,NULL,NULL,NULL,6),(13,456.78,534.30,9852.48,2.58,8113.04,NULL,NULL,20),(14,135.65,760.59,9654.96,321.81,7185.78,NULL,NULL,4),(15,943.14,233599.92,8717.36,233915.20,234903.67,NULL,NULL,18),(16,79.53,718.41,4621.95,41.11,6391.58,NULL,NULL,17),(17,12.79,991.94,6957.64,401.61,7188.54,NULL,NULL,12),(18,7856.27,804.49,922.38,884.74,6767.97,NULL,NULL,9),(19,122.78,46.62,3738.95,218.85,2274.22,NULL,NULL,8),(20,45.27,3492.10,4098.21,343.32,2482.12,NULL,NULL,1);
/*!40000 ALTER TABLE `customer_sales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `invoice`
--

DROP TABLE IF EXISTS `invoice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `invoice` (
  `inum` int NOT NULL,
  `ishipdate` date DEFAULT NULL,
  `ishipcharge` decimal(10,2) DEFAULT NULL,
  `itax` decimal(10,2) DEFAULT NULL,
  `ifullpartially` tinytext,
  `orderno` int DEFAULT NULL,
  `total` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`inum`),
  KEY `ordernum_idx` (`orderno`),
  CONSTRAINT `ordernum` FOREIGN KEY (`orderno`) REFERENCES `orders` (`onum`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `invoice`
--

LOCK TABLES `invoice` WRITE;
/*!40000 ALTER TABLE `invoice` DISABLE KEYS */;
INSERT INTO `invoice` VALUES (1,'2020-10-13',48.18,0.00,'0',4,243.03),(3,'2020-11-04',16.47,5.20,'0',4,216.52),(4,'2020-11-10',43.54,5.30,'1',19,1197.69),(5,'2020-11-14',1.95,1.00,'1',12,801.58),(6,'2020-11-04',66.01,12.00,'0',15,720.28),(7,'2020-11-19',56.06,2.00,'0',2,230767.06),(8,'2020-11-03',67.97,3.00,'0',17,470.97),(9,'2020-11-09',1.50,1.00,'0',1,28.50),(11,'2020-11-15',59.20,5.43,'1',1,246.63),(12,'2020-11-08',52.67,5.00,'0',18,219.37),(13,'2020-11-06',83.51,3.21,'0',14,799.72),(14,'2020-11-16',52.60,4.21,'0',8,2045.81),(15,'2020-11-16',66.18,4.41,'1',3,32270.59),(16,'2020-11-18',66.48,5.31,'1',17,471.79),(17,'2020-11-01',32.00,5.12,'0',17,437.12),(18,'2020-11-13',72.31,5.12,'0',4,272.28),(19,'2020-11-06',48.16,5.12,'1',19,1202.13),(21,'2020-11-18',10.00,0.05,'0',8,10.05),(22,'2020-11-11',30.00,5.00,'0',11,29015.00),(23,'2020-11-11',10.00,2.00,'f',5,12865.57),(25,'2020-11-11',30.00,5.00,'f',1,49.00),(26,'2020-10-10',30.00,5.00,'f',1,49.00),(27,'2020-11-11',30.00,5.00,'f',1,49.00),(29,'2020-11-11',1.00,1.00,'f',1,16.00),(30,'2020-11-11',50.00,1.00,'f',1,65.00),(31,'2020-01-01',3.00,1.00,'f',1,18.00),(32,'2020-11-11',30.00,1.00,'f',1,45.00),(34,'2020-11-11',200.00,9.00,'f',2,230918.00),(35,'2020-11-11',40.00,2.00,'f',1,68.00),(36,'2020-11-11',50.00,4.00,'f',1,80.00),(37,'2020-11-11',12.00,1.00,'f',1,39.00),(38,'2020-11-11',24.00,1.00,'f',1,51.00),(39,'2020-11-11',12.00,1.00,'f',1,39.00),(40,'2020-11-11',40.00,1.00,'f',12,839.63),(41,'2020-11-11',50.00,4.00,'f',1,80.00),(42,'2020-10-10',23.00,1.00,'f',1,50.00),(43,'2020-12-12',20.00,1.00,'f',12,819.63),(44,'2020-11-11',23.00,1.00,'f',12,822.63);
/*!40000 ALTER TABLE `invoice` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `getTotal` BEFORE INSERT ON `invoice` FOR EACH ROW SET NEW.total=
	   (
		SELECT SUM(numordered*quotedprice)+NEW.ishipcharge+NEW.itax
        FROM orderhaspart
        WHERE onum = NEW.orderno
        ) */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `updateTotal` BEFORE UPDATE ON `invoice` FOR EACH ROW SET NEW.total=
	   (
		SELECT SUM(numordered*quotedprice)+NEW.ishipcharge+NEW.itax
        FROM orderhaspart
        WHERE onum = NEW.orderno
        ) */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `invoice_records`
--

DROP TABLE IF EXISTS `invoice_records`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `invoice_records` (
  `inum` int DEFAULT NULL,
  `date` date DEFAULT NULL,
  `cnum` int DEFAULT NULL,
  `srnum` int DEFAULT NULL,
  `invoice_total` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `invoice_records`
--

LOCK TABLES `invoice_records` WRITE;
/*!40000 ALTER TABLE `invoice_records` DISABLE KEYS */;
INSERT INTO `invoice_records` VALUES (46,'2020-11-11',10,9,147.00);
/*!40000 ALTER TABLE `invoice_records` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orderhaspart`
--

DROP TABLE IF EXISTS `orderhaspart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orderhaspart` (
  `onum` int NOT NULL,
  `prtnum` int NOT NULL,
  `numordered` int DEFAULT NULL,
  `quotedprice` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`onum`,`prtnum`),
  KEY `prtnum_idx` (`prtnum`),
  CONSTRAINT `onum` FOREIGN KEY (`onum`) REFERENCES `orders` (`onum`),
  CONSTRAINT `partno` FOREIGN KEY (`prtnum`) REFERENCES `part` (`PRTNUM`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orderhaspart`
--

LOCK TABLES `orderhaspart` WRITE;
/*!40000 ALTER TABLE `orderhaspart` DISABLE KEYS */;
INSERT INTO `orderhaspart` VALUES (1,18,1,12.00),(1,19,1,14.00),(2,2,1451,159.00),(3,1,161,200.00),(4,15,15,12.99),(5,16,643,19.99),(6,14,15,600.05),(7,12,153,56.89),(8,10,153,13.00),(9,9,34,190.45),(10,8,54,69.96),(11,5,69,420.00),(12,10,21,38.03),(13,5,213,20.00),(14,3,31,23.00),(15,1,3,214.09),(16,2,2,98.99),(17,5,4,100.00),(18,9,5,32.34),(19,10,115,9.99);
/*!40000 ALTER TABLE `orderhaspart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `onum` int NOT NULL,
  `odate` date DEFAULT NULL,
  `odesc` varchar(45) DEFAULT NULL,
  `ocustponum` int DEFAULT NULL,
  `ototal` decimal(10,0) DEFAULT NULL,
  `oreleased` tinytext,
  `customernum` int DEFAULT NULL,
  PRIMARY KEY (`onum`),
  KEY `customernumber1_idx` (`customernum`),
  CONSTRAINT `customernumber1` FOREIGN KEY (`customernum`) REFERENCES `customer_sales` (`CNUM`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (1,'2020-11-19','tincidunt',40,505,'1',12),(2,'2020-11-13','consectetuer',17,233,'0',15),(3,'2020-11-02','diam.',72,907,'0',10),(4,'2020-11-10','Phasellus',5,887,'1',8),(5,'2020-11-04','pellentesque,',21,601,'0',2),(6,'2020-11-12','porttitor',71,598,'0',9),(7,'2020-11-03','feugiat',48,513,'1',12),(8,'2020-11-14','eu',90,554,'1',20),(9,'2020-11-03','ultricies',55,907,'0',14),(10,'2020-11-02','Donec',73,154,'1',12),(11,'2020-11-05','in',11,369,'0',10),(12,'2020-11-03','mollis',10,696,'0',15),(13,'2020-11-15','malesuada.',49,641,'0',9),(14,'2020-11-12','Integer',37,873,'0',1),(15,'2020-11-11','quam',50,729,'1',7),(16,'2020-11-06','accumsan',50,871,'1',2),(17,'2020-11-10','faucibus',83,74,'0',15),(18,'2020-11-15','tellus',92,432,'1',11),(19,'2020-11-07','Morbi',96,449,'1',17);
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `part`
--

DROP TABLE IF EXISTS `part`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `part` (
  `PRTNUM` int NOT NULL,
  `PRTDESC` varchar(45) DEFAULT NULL,
  `PRTPRICE` decimal(10,2) DEFAULT NULL,
  `PRTMTDSALES` decimal(10,2) DEFAULT NULL,
  `PRTYTDSALES` decimal(10,2) DEFAULT NULL,
  `PRTUNITSONHAND` int DEFAULT NULL,
  `PRTUNITSALLOCATED` int DEFAULT NULL,
  `PRTREORDERPOINT` int DEFAULT NULL,
  PRIMARY KEY (`PRTNUM`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `part`
--

LOCK TABLES `part` WRITE;
/*!40000 ALTER TABLE `part` DISABLE KEYS */;
INSERT INTO `part` VALUES (1,'Printer',74.99,5867.47,83103.53,9,3,124),(2,'Whiteboard',12.99,387.71,8929.37,481,2,10),(3,'Band T-Shirt',13.99,202.92,2971.92,157,98,83),(4,'Pens',5.99,497.06,1197.68,342,86,21),(5,'Kitten Calendar',23.99,1712.82,27887.06,238,37,34),(6,'Printer Ink',64.99,522.45,46297.65,164,28,64),(7,'Bulk Printer Paper',34.99,909.85,9607.23,105,27,22),(8,'Snackbars',9.99,58.94,2354.75,35,50,34),(9,'Laptop Fan',45.99,2367.91,20918.04,861,71,56),(10,'Dog Toys',3.99,158.56,1065.59,138,-61,12),(11,'Cat Tree',35.99,1592.02,38538.30,419,1,9),(12,'New CD',23.99,46.93,1267.51,492,96,34),(13,'Record',4.99,384.61,2753.27,202,76,65),(14,'Flash Drive',24.99,1987.08,2506.17,344,-99,32),(15,'Pencils',4.99,331.06,4721.33,74,35,45),(16,'Toolbox',32.99,3074.06,37276.61,760,98,56),(17,'Sticker Book',6.99,467.43,2874.32,578,87,62),(18,'Erasers',3.99,218.70,3456.20,607,36,65),(19,'Temporary Tattoos',2.99,219.60,2683.41,310,27,44),(20,'Oreos',6.99,19.53,4114.75,734,33,33);
/*!40000 ALTER TABLE `part` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payment`
--

DROP TABLE IF EXISTS `payment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payment` (
  `pynum` int NOT NULL,
  `pydate` date DEFAULT NULL,
  `pyamt` decimal(10,2) DEFAULT NULL,
  `customer` int DEFAULT NULL,
  PRIMARY KEY (`pynum`),
  KEY `thecustomer_idx` (`customer`),
  CONSTRAINT `thecustomer` FOREIGN KEY (`customer`) REFERENCES `customer_sales` (`CNUM`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payment`
--

LOCK TABLES `payment` WRITE;
/*!40000 ALTER TABLE `payment` DISABLE KEYS */;
INSERT INTO `payment` VALUES (1,'2020-11-11',36.96,2),(2,'2020-11-11',13.43,14),(3,'2020-11-11',54.29,7),(4,'2020-11-12',32.14,9),(5,'2020-11-12',95.83,7),(6,'2020-11-12',84.72,4),(7,'2020-11-12',36.10,18),(8,'2020-11-13',24.37,1),(9,'2020-11-13',12.54,8),(10,'2020-11-13',87.60,15),(11,'2020-11-16',3.36,11),(12,'2020-11-18',50.01,11),(13,'2020-11-18',40.96,1),(14,'2020-11-18',53.80,10),(15,'2020-11-20',46.09,6),(16,'2020-11-20',68.04,17),(17,'2020-11-20',2.94,10),(18,'2020-11-20',7.60,19),(19,'2020-11-20',28.18,5),(20,'2020-11-26',18.11,5);
/*!40000 ALTER TABLE `payment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sales_rep`
--

DROP TABLE IF EXISTS `sales_rep`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sales_rep` (
  `SRNUM` int NOT NULL,
  `SRNAME` varchar(45) DEFAULT NULL,
  `SRADDRESS` varchar(45) DEFAULT NULL,
  `SRCITY` varchar(45) DEFAULT NULL,
  `SRSTATE` varchar(45) DEFAULT NULL,
  `SRZIP` varchar(45) DEFAULT NULL,
  `TNO` int DEFAULT NULL,
  PRIMARY KEY (`SRNUM`),
  KEY `TNO_idx` (`TNO`),
  CONSTRAINT `SRNUM` FOREIGN KEY (`SRNUM`) REFERENCES `sales_rep_sales` (`SRNUM`),
  CONSTRAINT `TNO` FOREIGN KEY (`TNO`) REFERENCES `territory` (`TNUM`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sales_rep`
--

LOCK TABLES `sales_rep` WRITE;
/*!40000 ALTER TABLE `sales_rep` DISABLE KEYS */;
INSERT INTO `sales_rep` VALUES (1,'Annette Eisner','123 Almond','Blank','California','83912',1),(2,'Naomi Vickie','23 Green','Gray','Texas','12934',2),(3,'Mamie Case','343 Purple','Fire','Maine','29482',4),(4,'Ferdinand Edmund','49 Queens','L. Fire','Vermont','39394',12),(5,'Ebony Herman','91 Joker','Franklin','Ohio','12394',15),(6,'Candice Katrina ','791 Bird','Cranberry','California','29921',19),(7,'Saundra Hurley','93 Owl','Harvey','Florida','39481',2),(8,'Ashe Ubert','283 Baroney','Summerfield','Maine','30498',7),(9,'John Smith','22 Squirrel','Taylor','Vermont','92847',9),(10,'Estelle Albert','28 Sheperdsville','Flushing','Florida','86457',11),(11,'Marina Freeman','11 Ritz','Strawberry','Colorado','57291',9),(12,'Dimitri Blaiddyd','101 King','Defiance','New York','29384',1),(13,'Cathleen Audrey','842 Ice','Springfield','New Jersey','21837',3),(14,'Steve Rogers','31 Church','Mobile','Ohio','23841',5),(15,'Thomas Farmer','233 Almond','Stow','New Jersey','39481',12),(16,'Alyssa Coleman','111 Coffee','Irwin','Florida','39948',14),(17,'Howard Long ','348 Joker','Somerset','Texas','28341',13),(18,'Irving Emmett','234 River','Plainview','Colorado','39482',10),(19,'Jon Vasquez','383 Henry','Salem','New York','09183',20),(20,'Marcos Johns','937 Lizard','Orange','Maryland','28384',18);
/*!40000 ALTER TABLE `sales_rep` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sales_rep_sales`
--

DROP TABLE IF EXISTS `sales_rep_sales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sales_rep_sales` (
  `SRNUM` int NOT NULL,
  `SRMTDSALES` decimal(10,2) DEFAULT NULL,
  `SRMTDCOMMISSION` decimal(10,2) DEFAULT NULL,
  `SRYTDSALES` decimal(10,2) DEFAULT NULL,
  `SRYTDCOMMISSION` decimal(10,2) DEFAULT NULL,
  `SRCOMISSIONRATE` decimal(10,2) DEFAULT NULL,
  `TNUM` int DEFAULT NULL,
  PRIMARY KEY (`SRNUM`),
  KEY `TNUM_idx` (`TNUM`),
  CONSTRAINT `TNUM` FOREIGN KEY (`TNUM`) REFERENCES `territory` (`TNUM`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sales_rep_sales`
--

LOCK TABLES `sales_rep_sales` WRITE;
/*!40000 ALTER TABLE `sales_rep_sales` DISABLE KEYS */;
INSERT INTO `sales_rep_sales` VALUES (1,3482.35,104.47,93935.46,2818.06,0.03,11),(2,1384.23,41.53,91344.04,2740.32,0.03,15),(3,3823.32,344.10,81291.91,7316.27,0.09,6),(4,1293.94,77.64,23842.12,1430.53,0.06,9),(5,2984.34,149.22,35821.24,1791.06,0.05,8),(6,4983.32,299.00,32749.93,1965.00,0.06,11),(7,4173.34,208.67,30560.13,1528.01,0.05,17),(8,1934.13,116.05,93747.34,5624.84,0.06,6),(9,5866.21,469.30,73483.38,5878.67,0.08,9),(10,9024.13,541.45,82390.12,4943.41,0.06,19),(11,1204.12,60.21,32984.29,1649.21,0.05,17),(12,9421.34,659.49,83261.39,5828.30,0.07,1),(13,1390.95,97.37,93712.34,6559.86,0.07,3),(14,243187.33,7295.62,324597.10,9737.92,0.03,8),(15,3109.43,217.66,38472.12,2693.05,0.07,19),(16,3712.12,185.61,47832.34,2391.62,0.05,17),(17,3294.12,197.65,98736.23,5924.17,0.06,15),(18,4932.23,345.26,49872.38,3491.07,0.07,3),(19,1293.12,38.79,98487.32,2954.62,0.03,1),(20,4439.48,310.76,39864.23,2790.50,0.07,7);
/*!40000 ALTER TABLE `sales_rep_sales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `supplies`
--

DROP TABLE IF EXISTS `supplies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `supplies` (
  `VNUM` int NOT NULL,
  `PRTNUM` int NOT NULL,
  `VPRICE` decimal(10,2) DEFAULT NULL,
  `MINQUANTITY` int DEFAULT NULL,
  `EXPECTEDTIME` int DEFAULT NULL,
  PRIMARY KEY (`VNUM`,`PRTNUM`),
  KEY `PRTNUM_idx` (`PRTNUM`),
  CONSTRAINT `PRTNUM` FOREIGN KEY (`PRTNUM`) REFERENCES `part` (`PRTNUM`),
  CONSTRAINT `VNUM` FOREIGN KEY (`VNUM`) REFERENCES `vendor` (`VNUM`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `supplies`
--

LOCK TABLES `supplies` WRITE;
/*!40000 ALTER TABLE `supplies` DISABLE KEYS */;
INSERT INTO `supplies` VALUES (1,7,9.79,31,3),(2,4,28.95,96,43),(3,5,15.37,86,8),(4,2,90.02,41,8),(5,1,4.00,47,20),(6,6,49.91,13,23),(7,6,37.56,23,7),(8,7,38.06,76,14),(9,7,77.63,12,2),(10,8,73.99,30,16),(11,3,37.03,14,23),(12,5,63.19,81,16),(13,1,4.84,64,13),(14,6,34.65,76,15),(15,5,58.71,86,35),(16,9,89.61,5,33),(17,7,71.90,65,7),(18,11,90.70,12,38),(19,15,37.78,66,17),(20,5,16.81,39,9);
/*!40000 ALTER TABLE `supplies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `territory`
--

DROP TABLE IF EXISTS `territory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `territory` (
  `TNUM` int NOT NULL,
  `TNAME` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`TNUM`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `territory`
--

LOCK TABLES `territory` WRITE;
/*!40000 ALTER TABLE `territory` DISABLE KEYS */;
INSERT INTO `territory` VALUES (1,'Michigan'),(2,'Alabama'),(3,'Colorado'),(4,'Alaska'),(5,'Louisiana'),(6,'Maine'),(7,'Maryland'),(8,'Ohio'),(9,'Vermont'),(10,'Wyoming'),(11,'California'),(12,'Nevada'),(13,'Kentucky'),(14,'Georgia'),(15,'Texas'),(16,'Kansas'),(17,'Florida'),(18,'Arkansas'),(19,'New Jersey'),(20,'Rhode Island');
/*!40000 ALTER TABLE `territory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vendor`
--

DROP TABLE IF EXISTS `vendor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vendor` (
  `VNUM` int NOT NULL,
  `VNAME` varchar(45) DEFAULT NULL,
  `VADDRESS` varchar(45) DEFAULT NULL,
  `VCITY` varchar(45) DEFAULT NULL,
  `VSTATE` varchar(45) DEFAULT NULL,
  `VZIP` int DEFAULT NULL,
  PRIMARY KEY (`VNUM`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vendor`
--

LOCK TABLES `vendor` WRITE;
/*!40000 ALTER TABLE `vendor` DISABLE KEYS */;
INSERT INTO `vendor` VALUES (1,'Sullivan Douglas','12 Clover','Neptune','Kentucky',13894),(2,'Ava Dixon','64 Hill','Rochester','New Jersey',34523),(3,'Lila Ahmad','224 Sherwood','Florence','California',35263),(4,'Ronny Ward','1 Henry','Flint','Georgia',34812),(5,'Atlanta Strong','212 Spade','Rochester','New Jersey',39831),(6,'Miguel Patrick','234 Sunset','Florence','California',23485),(7,'Elouise Clark','98 Addison','Savannah','New York',48571),(8,'Evie-Grace Bourne','214 Mad','Woodside','Florida',94521),(9,'Maria Little','2842 Marshfield','Florence','Kansas',90372),(10,'Orion Redfern','83 Heart','Flint','California',13471),(11,'Vera Mckenna','98 Pilgrin','Neptune','Georgia',89345),(12,'Eve Steele','64 Fifth','Woodside','Florida',43572),(13,'Opal Southern','3 Lakeshore','Florence','California',23573),(14,'Reece Munro','21 Diamond','Flint','Georgia',30841),(15,'Gladys Holland','55 Hillside','Lexington','Florida',32456),(16,'Beck Mcphee','245 French','Rochester','New Jersey',84352),(17,'Kevin Blue','93 Seventh','Lexington','Kansas',12464),(18,'Brook Dalton','12 Forrest','Savannah','New York',12453),(19,'Sebastien Gay','832 Amethyst','Neptune','New Jersey',18034),(20,'Denzel Taylor','82 First','Savannah','New York',12455);
/*!40000 ALTER TABLE `vendor` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-08 15:14:44
