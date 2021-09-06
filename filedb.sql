-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: localhost    Database: filedb
-- ------------------------------------------------------
-- Server version	5.7.31-log

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
-- Table structure for table `amount_receive`
--

DROP TABLE IF EXISTS `amount_receive`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `amount_receive` (
  `VNo` int(11) DEFAULT NULL,
  `CNo` int(11) DEFAULT NULL,
  `dDt` datetime DEFAULT NULL,
  `Amt` double DEFAULT NULL,
  `Rem` varchar(250) DEFAULT NULL,
  `IsAdjust` int(11) DEFAULT NULL,
  `EDt` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `amount_receive`
--

LOCK TABLES `amount_receive` WRITE;
/*!40000 ALTER TABLE `amount_receive` DISABLE KEYS */;
/*!40000 ALTER TABLE `amount_receive` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `amount_receive_detail`
--

DROP TABLE IF EXISTS `amount_receive_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `amount_receive_detail` (
  `VNo` int(11) DEFAULT NULL,
  `SNo` int(11) DEFAULT NULL,
  `Bill` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `amount_receive_detail`
--

LOCK TABLES `amount_receive_detail` WRITE;
/*!40000 ALTER TABLE `amount_receive_detail` DISABLE KEYS */;
/*!40000 ALTER TABLE `amount_receive_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bill_detail`
--

DROP TABLE IF EXISTS `bill_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bill_detail` (
  `VNo` int(11) DEFAULT NULL,
  `SrNo` int(11) DEFAULT NULL,
  `PNm` varchar(250) DEFAULT NULL,
  `HSNCode` varchar(250) DEFAULT NULL,
  `GSTPer` double DEFAULT NULL,
  `Qty` double DEFAULT NULL,
  `uUnit` varchar(250) DEFAULT NULL,
  `rRate` double DEFAULT NULL,
  `Total` double DEFAULT NULL,
  `DisPer` double DEFAULT NULL,
  `DisAmt` double DEFAULT NULL,
  `GNm` varchar(250) DEFAULT NULL,
  `sSize` varchar(250) DEFAULT NULL,
  `Finish` varchar(250) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bill_detail`
--

LOCK TABLES `bill_detail` WRITE;
/*!40000 ALTER TABLE `bill_detail` DISABLE KEYS */;
INSERT INTO `bill_detail` VALUES (1,1,'5 Cartons Only Baby Toy Pistol','9505',12,27.5,'Gross',720,19800,0,0,'','S',''),(2,1,'5 Cartons Only Baby Toy Pistol','9505',12,27.5,'Gross',720,19800,0,0,'','S',''),(3,1,'5 Cartons Only Baby Toy Pistol','9505',12,27.5,'Gross',720,19800,0,0,'','S',''),(4,1,'5 Cartons Only Baby Toy Pistol','9505',12,27.5,'Gross',720,19800,0,0,'','S',''),(5,1,'10 Cartons Only Baby Toy Pistols','9505',12,55,'Gross',720,39600,0,0,'','S',''),(6,1,'7 Cartons Baby Toy Pistols Only','9505',12,38.5,'Gross',720,27720,0,0,'','S',''),(7,1,'2 Cartons Only Baby Toy Pistol','9505',12,10,'Gross',720,7200,0,0,'','B',''),(8,1,'10 Cartons Baby toy pistols','9505',12,100,'Gross',192,19200,0,0,'','mini',''),(8,2,'5 Cartons  Baby Toy Pistol','9505',12,45,'Gross',204,9180,0,0,'','small',''),(8,3,'5 Cartons  Baby Toy Pistol','9505',12,35,'Gross',300,10500,0,0,'','medium',''),(8,4,'2 Cartons Baby Toy Pistol','9505',12,6,'Gross',660,3960,0,0,'','big',''),(9,1,'10 Cartons Baby toy pistols','9505',12,100,'Gross',192,19200,0,0,'','small',''),(9,2,'5 Cartons  Baby Toy Pistol','9505',12,45,'Gross',204,9180,0,0,'','small',''),(9,3,'5 Cartons  Baby Toy Pistol','9505',12,35,'Gross',300,10500,0,0,'','medium',''),(9,4,'2 Cartons Baby Toy Pistol','9505',12,6,'Gross',660,3960,0,0,'','big',''),(10,1,'10 Cartons Baby toy pistols','9505',12,100,'Gross',192,19200,0,0,'','mini',''),(10,2,'10 Cartons Baby toy pistols','9505',12,90,'Gross',204,18360,0,0,'','small',''),(10,3,'2 Cartons Baby Toy Pistol','9505',12,6,'Gross',660,3960,0,0,'','big',''),(11,1,'10 Cartons Baby toy pistols','9505',12,90,'Gross',204,18360,0,0,'','small',''),(11,2,'10 Cartons Baby toy pistols','9505',12,70,'Gross',300,21000,0,0,'','medium',''),(12,1,'10 Cartons Baby toy pistols','9505',12,70,'Gross',300,21000,0,0,'','medium',''),(12,2,'10 Cartons Baby toy pistols','9505',12,30,'Gross',660,19800,0,0,'','big',''),(13,1,'10 Cartons Baby toy pistols','9505',12,100,'Gross',192,19200,0,0,'','mini',''),(13,2,'10 Cartons Baby toy pistols','9505',12,70,'Gross',300,21000,0,0,'','medium',''),(14,1,'10 Cartons Baby toy pistols','9505',12,100,'Gross',192,19200,0,0,'','mini',''),(14,2,'10 Cartons Baby toy pistols','9505',12,90,'Gross',204,18360,0,0,'','small',''),(14,3,'2 Cartons Baby Toy Pistol','9505',12,6,'Gross',660,3960,0,0,'','BI',''),(15,1,'10 Cartons Baby toy pistols','9505',12,70,'Gross',300,21000,0,0,'','medium',''),(15,2,'10 Cartons Baby toy pistols','9505',12,30,'Gross',660,19800,0,0,'','big',''),(16,1,'10 Cartons Baby toy pistols','9505',12,90,'Gross',204,18360,0,0,'','small',''),(16,2,'10 Cartons Baby toy pistols','9505',12,30,'Gross',660,19800,0,0,'','big',''),(17,1,'12 Cartons Baby Toy Pistols','9505',12,66,'Gross',576,38016,0,0,'','ST',''),(18,1,'13 Cartons Baby Toy Pistols','9505',12,71.5,'Gross',576,41184,0,0,'','ST',''),(19,1,'13 Cartons Baby Toy Pistols','9505',12,71.5,'Gross',576,41184,0,0,'','ST',''),(20,1,'12 Cartons Baby Toy Pistols','9505',12,66,'Gross',576,38016,0,0,'','ST',''),(21,1,'10 Cartons Baby toy pistols','9505',12,55,'Gross',576,31680,0,0,'','ST',''),(22,1,'10 Cartons Baby toy pistols','9505',12,55,'Gross',576,31680,0,0,'','ST','');
/*!40000 ALTER TABLE `bill_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bill_master`
--

DROP TABLE IF EXISTS `bill_master`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bill_master` (
  `VNo` int(11) DEFAULT NULL,
  `BillNo` int(11) DEFAULT NULL,
  `dDt` date DEFAULT NULL,
  `PNo` int(11) DEFAULT NULL,
  `PNm` varchar(250) DEFAULT NULL,
  `Address` varchar(250) DEFAULT NULL,
  `StateNm` varchar(250) DEFAULT NULL,
  `StateCode` varchar(250) DEFAULT NULL,
  `GSTNo` varchar(250) DEFAULT NULL,
  `Mob` varchar(250) DEFAULT NULL,
  `ONo` varchar(250) DEFAULT NULL,
  `ODt` varchar(250) DEFAULT NULL,
  `BookedBy` varchar(250) DEFAULT NULL,
  `NOP` varchar(250) DEFAULT NULL,
  `LRNo` varchar(250) DEFAULT NULL,
  `LRDt` varchar(250) DEFAULT NULL,
  `Transport` varchar(250) DEFAULT NULL,
  `Freight` varchar(250) DEFAULT NULL,
  `PvtMark` varchar(250) DEFAULT NULL,
  `PlaceOfSupply` varchar(250) DEFAULT NULL,
  `Wt` varchar(250) DEFAULT NULL,
  `Total` double DEFAULT NULL,
  `TotDis` double DEFAULT NULL,
  `TotTVal` double DEFAULT NULL,
  `TotCGST` double DEFAULT NULL,
  `TotSGST` double DEFAULT NULL,
  `TotIGST` double DEFAULT NULL,
  `TotGST` double DEFAULT NULL,
  `TotAmt` double DEFAULT NULL,
  `ExpNm1` varchar(250) DEFAULT NULL,
  `ExpAmt1` double DEFAULT NULL,
  `ExpNm2` varchar(250) DEFAULT NULL,
  `ExpAmt2` double DEFAULT NULL,
  `GTot` double DEFAULT NULL,
  `EDt` datetime DEFAULT NULL,
  `ESugam` varchar(250) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bill_master`
--

LOCK TABLES `bill_master` WRITE;
/*!40000 ALTER TABLE `bill_master` DISABLE KEYS */;
INSERT INTO `bill_master` VALUES (1,1,'2020-06-06',0,'Tip Top Fancy','Peoples Buildings,Rice Bazar\r\nKunnalkulam','Kerala','32','32AVBPB9259L1ZH','','','-  -','','','','-  -','SRB','','TT/5','','',19800,0,19800,0,0,2376,2376,22176,'',0,'Round Off',0,22176,'2020-06-06 11:58:44',''),(2,2,'2020-06-09',0,'Kuttapai & Sons','Disco Bazar, Jews Street,\r\nErnakulam\r\n','Kerala','32','32ADDPI3295B1Z2','','','-  -','','','','-  -','SRB','','KS/5','','',19800,0,19800,0,0,2376,2376,22176,'',0,'Round Off',0,22176,'2020-06-09 11:32:02',''),(3,3,'2020-06-09',0,'Madan Gift Toys & Crockery','Jayanti Building,\r\nG.H. Road,Calicut','Kerala','32','32AQOPM1059K1ZN','','','-  -','','','','-  -','SRB','','MG/5','','',19800,0,19800,0,0,2376,2376,22176,'',0,'Round Off',0,22176,'2020-06-09 11:42:57',''),(4,4,'2020-06-10',0,'Madan Gift Toys & Crockery','Jayanti Building,\r\nG.H. Road,Calicut','Kerala','32','32AQOPM1059K1ZN','','','-  -','','','','-  -','SRB','','MG/5','','',19800,0,19800,0,0,2376,2376,22176,'',0,'Round Off',0,22176,'2020-06-10 12:41:41',''),(5,5,'2020-06-12',0,'Madan Gift Toys & Crockery','Jayanti Building,\r\nG.H. Road,Calicut','Kerala','32','32AQOPM1059K1ZN','','','-  -','','','','-  -','SRB','','MG/10','','',39600,0,39600,0,0,4752,4752,44352,'',0,'Round Off',0,44352,'2020-06-12 16:22:46',''),(6,6,'2020-06-15',0,'Ranjeet Toy Industries','Dhopra Road,Gandhi Marg\r\nRailway Road,\r\nAligarh','Uttar Pradesh','09','09AYNPA2702Q1ZS','','','-  -','','','','-  -','','','RI/7','','',27720,0,27720,1663.2,1663.2,0,3326.4,31046.4,'',0,'Round Off',-0.4,31046,'2020-06-15 10:46:01',''),(7,15,'2020-06-25',0,'L.N.M. Enterprises','\r\n985,Chhaini Market,\r\nSadar Bazar,\r\nDelhi-6\r\n','Delhi','07','07AADFLAA26E1ZA','','','-  -','','','','-  -','D.A.T.','','LM/2','','',7200,0,7200,0,0,864,864,8064,'',0,'Round Off',0,8064,'2020-06-25 17:01:59',''),(8,8,'2020-06-18',0,'Dinesh Toy Industries','Gular Road ,Gali No.7 ,Aligarh\r\n','Uttar Pradesh','09','09AJVPK2804Q1ZE','','','- - --','','','','- - --','','','','','',42840,0,42840,2570.4,2570.4,0,5140.8,47980.8,'',0,'Round Off',0.2,47981,'2020-06-27 10:24:32',''),(9,7,'2020-06-16',0,'King Toy Industries','\r\n12/24 Bania Para ,Aligarh\r\n','Uttar Pradesh','09','09CQZPK8494B1ZZ','','','-  -','','','','-  -','','','','','',42840,0,42840,2570.4,2570.4,0,5140.8,47980.8,'',0,'Round Off',0.2,47981,'2020-06-27 10:32:07',''),(10,9,'2020-06-19',0,'Dinesh Toy Industries','Gular Road ,Gali No.7 ,Aligarh\r\n','Uttar Pradesh','09','09AJVPK2804Q1ZE','','','-  -','','','','-  -','','','','','',41520,0,41520,2491.2,2491.2,0,4982.4,46502.4,'',0,'Round Off',-0.4,46502,'2020-06-27 10:36:00',''),(11,10,'2020-06-21',0,'King Toy Industries','\r\n12/24 Bania Para ,Aligarh\r\n','Uttar Pradesh','09','09CQZPK8494B1ZZ','','','-  -','','','','-  -','','','','','',39360,0,39360,2361.6,2361.6,0,4723.2,44083.2,'',0,'Round Off',-0.2,44083,'2020-06-27 10:40:03',''),(12,11,'2020-06-22',0,'King Toy Industries','\r\n12/24 Bania Para ,Aligarh\r\n','Uttar Pradesh','09','09CQZPK8494B1ZZ','','','-  -','','','','-  -','','','','','',40800,0,40800,2448,2448,0,4896,45696,'',0,'Round Off',0,45696,'2020-06-27 10:44:08',''),(13,12,'2020-06-22',0,'Dinesh Toy Industries','Gular Road ,Gali No.7 ,Aligarh\r\n','Uttar Pradesh','09','09AJVPK2804Q1ZE','','','-  -','','','','-  -','','','','','',40200,0,40200,2412,2412,0,4824,45024,'',0,'Round Off',0,45024,'2020-06-27 10:49:16',''),(14,13,'2020-06-23',0,'King Toy Industries','\r\n12/24 Bania Para ,Aligarh\r\n','Uttar Pradesh','09','09CQZPK8494B1ZZ','','','-  -','','','','-  -','','','','','',41520,0,41520,2491.2,2491.2,0,4982.4,46502.4,'',0,'Round Off',-0.4,46502,'2020-06-27 10:52:08',''),(15,14,'2020-06-24',0,'Dinesh Toy Industries','Gular Road ,Gali No.7 ,Aligarh\r\n','Uttar Pradesh','09','09AJVPK2804Q1ZE','','','-  -','','','','-  -','','','','','',40800,0,40800,2448,2448,0,4896,45696,'',0,'Round Off',0,45696,'2020-06-27 10:53:56',''),(16,16,'2020-06-26',0,'King Toy Industries','\r\n12/24 Bania Para ,Aligarh\r\n','Uttar Pradesh','09','09CQZPK8494B1ZZ','','','-  -','','','','-  -','','','','','',38160,0,38160,2289.6,2289.6,0,4579.2,42739.2,'',0,'Round Off',-0.2,42739,'2020-06-27 11:13:39',''),(17,17,'2020-06-27',0,'Dinesh Toy Industries','Gular Road ,Gali No.7 ,Aligarh\r\n','Uttar Pradesh','09','09AJVPK2804Q1ZE','','','-  -','','','','-  -','','','','','',38016,0,38016,2280.96,2280.96,0,4561.92,42577.92,'',0,'Round Off',0.08,42578,'2020-07-04 13:20:50',''),(18,18,'2020-06-27',0,'King Toy Industries','\r\n12/24 Bania Para ,Aligarh\r\n','Uttar Pradesh','09','09CQZPK8494B1ZZ','','','-  -','','','','-  -','','','','','',41184,0,41184,2471.04,2471.04,0,4942.08,46126.08,'',0,'Round Off',-0.08,46126,'2020-07-04 13:24:58',''),(19,19,'2020-06-28',0,'Dinesh Toy Industries','Gular Road ,Gali No.7 ,Aligarh\r\n','Uttar Pradesh','09','09AJVPK2804Q1ZE','','','-  -','','','','-  -','','','','','',41184,0,41184,2471.04,2471.04,0,4942.08,46126.08,'',0,'Round Off',-0.08,46126,'2020-07-04 13:27:40',''),(20,20,'2020-06-29',0,'King Toy Industries','\r\n12/24 Bania Para ,Aligarh\r\n','Uttar Pradesh','09','09CQZPK8494B1ZZ','','','-  -','','','','-  -','','','','','',38016,0,38016,2280.96,2280.96,0,4561.92,42577.92,'',0,'Round Off',0.08,42578,'2020-07-04 13:31:03',''),(21,21,'2020-06-29',0,'Dinesh Toy Industries','Gular Road ,Gali No.7 ,Aligarh\r\n','Uttar Pradesh','09','09AJVPK2804Q1ZE','','','-  -','','','','-  -','','','','','',31680,0,31680,1900.8,1900.8,0,3801.6,35481.6,'',0,'Round Off',0.4,35482,'2020-07-04 13:34:46',''),(22,22,'2020-06-30',0,'King Toy Industries','\r\n12/24 Bania Para ,Aligarh\r\n','Uttar Pradesh','09','09CQZPK8494B1ZZ','','10','-  -','','','','-  -','','','','','',31680,0,31680,1900.8,1900.8,0,3801.6,35481.6,'',0,'Round Off',0.4,35482,'2020-07-04 13:37:43','');
/*!40000 ALTER TABLE `bill_master` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bill_tax`
--

DROP TABLE IF EXISTS `bill_tax`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bill_tax` (
  `VNo` int(11) DEFAULT NULL,
  `HSNCode` varchar(250) DEFAULT NULL,
  `TVal` double DEFAULT NULL,
  `CGSTPer` double DEFAULT NULL,
  `CGSTAmt` double DEFAULT NULL,
  `SGSTPer` double DEFAULT NULL,
  `SGSTAmt` double DEFAULT NULL,
  `IGSTPer` double DEFAULT NULL,
  `IGSTAmt` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bill_tax`
--

LOCK TABLES `bill_tax` WRITE;
/*!40000 ALTER TABLE `bill_tax` DISABLE KEYS */;
INSERT INTO `bill_tax` VALUES (1,'',19800,0,0,0,0,12,2376),(2,'',19800,0,0,0,0,12,2376),(3,'',19800,0,0,0,0,12,2376),(4,'',19800,0,0,0,0,12,2376),(5,'',39600,0,0,0,0,12,4752),(6,'',27720,6,1663.2,6,1663.2,0,0),(7,'',7200,0,0,0,0,12,864),(8,'',42840,6,2570.4,6,2570.4,0,0),(9,'',42840,6,2570.4,6,2570.4,0,0),(10,'',41520,6,2491.2,6,2491.2,0,0),(11,'',39360,6,2361.6,6,2361.6,0,0),(12,'',40800,6,2448,6,2448,0,0),(13,'',40200,6,2412,6,2412,0,0),(14,'',41520,6,2491.2,6,2491.2,0,0),(15,'',40800,6,2448,6,2448,0,0),(16,'',38160,6,2289.6,6,2289.6,0,0),(17,'',38016,6,2280.96,6,2280.96,0,0),(18,'',41184,6,2471.04,6,2471.04,0,0),(19,'',41184,6,2471.04,6,2471.04,0,0),(20,'',38016,6,2280.96,6,2280.96,0,0),(21,'',31680,6,1900.8,6,1900.8,0,0),(22,'',31680,6,1900.8,6,1900.8,0,0);
/*!40000 ALTER TABLE `bill_tax` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company`
--

DROP TABLE IF EXISTS `company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `company` (
  `CNo` int(11) DEFAULT NULL,
  `Nm` varchar(250) DEFAULT NULL,
  `Address` varchar(250) DEFAULT NULL,
  `StateNm` varchar(250) DEFAULT NULL,
  `StateCode` varchar(250) DEFAULT NULL,
  `GSTNo` varchar(250) DEFAULT NULL,
  `SupOf` varchar(250) DEFAULT NULL,
  `Color1` varchar(250) DEFAULT NULL,
  `Color2` varchar(250) DEFAULT NULL,
  `BillFormat` varchar(250) DEFAULT NULL,
  `BankDet1` varchar(250) DEFAULT NULL,
  `BankDet2` varchar(250) DEFAULT NULL,
  `BankDet3` varchar(250) DEFAULT NULL,
  `ShowSerialNo` int(11) DEFAULT NULL,
  `BankNm` varchar(250) DEFAULT NULL,
  `Mo` varchar(250) DEFAULT NULL,
  `LeftMargin` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company`
--

LOCK TABLES `company` WRITE;
/*!40000 ALTER TABLE `company` DISABLE KEYS */;
INSERT INTO `company` VALUES (1,'GURU JI INDUSTRIES','10/1575 Opposite Guru Gobind Singh Bhawan, Delhi Gate, Aligarh - 202001 (U.P.)','Uttar Pradesh','09','GSTIN:- 096AMIPB4736C1ZC','Mfg. & Supplier of : Baby Pistol, Locks','-3342337','-16744320','','HDFC','HDFC0004818','Railway road Aligarh',0,'50200047537725','Mob. 8077699483',0.5);
/*!40000 ALTER TABLE `company` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mbl`
--

DROP TABLE IF EXISTS `mbl`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mbl` (
  `bname` varchar(30) DEFAULT NULL,
  `bauthor` varchar(30) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `bprice` decimal(10,0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mbl`
--

LOCK TABLES `mbl` WRITE;
/*!40000 ALTER TABLE `mbl` DISABLE KEYS */;
/*!40000 ALTER TABLE `mbl` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `party`
--

DROP TABLE IF EXISTS `party`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `party` (
  `PNo` int(11) NOT NULL AUTO_INCREMENT,
  `Nm` varchar(250) DEFAULT NULL,
  `City` varchar(250) DEFAULT NULL,
  `Address` varchar(250) DEFAULT NULL,
  `PState` varchar(250) DEFAULT NULL,
  `StateCode` varchar(250) DEFAULT NULL,
  `GSTNo` varchar(250) DEFAULT NULL,
  `PostalAddress` varchar(250) DEFAULT NULL,
  `Agent` varchar(250) DEFAULT NULL,
  `ContactPerson` varchar(250) DEFAULT NULL,
  `MoNo` varchar(250) DEFAULT NULL,
  `PhNo` varchar(250) DEFAULT NULL,
  `Email` varchar(250) DEFAULT NULL,
  `Transport` varchar(250) DEFAULT NULL,
  `TD` double DEFAULT NULL,
  PRIMARY KEY (`PNo`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `party`
--

LOCK TABLES `party` WRITE;
/*!40000 ALTER TABLE `party` DISABLE KEYS */;
INSERT INTO `party` VALUES (2,'one','two','three','Uttar Pradesh','09','123456werty','three','four','five','six','seven','eight@gmail.com','seven',NULL);
/*!40000 ALTER TABLE `party` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `PNo` int(11) DEFAULT NULL,
  `Nm` varchar(250) DEFAULT NULL,
  `HSNCode` varchar(250) DEFAULT NULL,
  `UnitNm` varchar(250) DEFAULT NULL,
  `SellRate` double DEFAULT NULL,
  `IGST` double DEFAULT NULL,
  `SGST` double DEFAULT NULL,
  `CGST` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (1,'5 Star','','',0,0,0,0);
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rate_list`
--

DROP TABLE IF EXISTS `rate_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rate_list` (
  `GNo` int(11) DEFAULT NULL,
  `PNo` int(11) DEFAULT NULL,
  `Finish` varchar(250) DEFAULT NULL,
  `PRate` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rate_list`
--

LOCK TABLES `rate_list` WRITE;
/*!40000 ALTER TABLE `rate_list` DISABLE KEYS */;
/*!40000 ALTER TABLE `rate_list` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `statename`
--

DROP TABLE IF EXISTS `statename`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `statename` (
  `SrNo` int(11) DEFAULT NULL,
  `Nm` varchar(250) DEFAULT NULL,
  `StateInitial` varchar(250) DEFAULT NULL,
  `StateCode` varchar(250) DEFAULT NULL,
  `StateType` varchar(250) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `statename`
--

LOCK TABLES `statename` WRITE;
/*!40000 ALTER TABLE `statename` DISABLE KEYS */;
INSERT INTO `statename` VALUES (1,'Andhra Pradesh','AP','28','STATE'),(2,'Andaman and Nicobar Islands','AN','35','UT'),(3,'Arunachal Pradesh','AR','12','STATE'),(4,'Assam','AS','18','STATE'),(5,'Bihar','BR','10','STATE'),(6,'Chandigarh','CH','04','UT'),(7,'Chhattisgarh','CG','22','STATE'),(8,'Dadar and Nagar Haveli','DH','26','UT'),(9,'Daman and Diu','DD','25','UT'),(10,'Delhi','DL','07','UT'),(11,'Goa','GA','30','STATE'),(12,'Gujarat','GJ','24','STATE'),(13,'Haryana','HR','06','STATE'),(14,'Himachal Pradesh','HP','02','STATE'),(15,'Jammu and Kashmir','JK','01','STATE'),(16,'Jharkhand','JH','20','STATE'),(17,'Karnataka','KA','29','STATE'),(18,'Kerala','KL','32','STATE'),(19,'Lakshadweep','LD','31','UT'),(20,'Madhya Pradesh','MP','23','STATE'),(21,'Maharashtra','MH','27','STATE'),(22,'Manipur','MN','14','STATE'),(23,'Meghalaya','ML','17','STATE'),(24,'Mizoram','MZ','15','STATE'),(25,'Nagaland','NL','13','STATE'),(26,'Odisha','OR','21','STATE'),(27,'Pondicherry','PY','34','UT'),(28,'Punjab','PB','03','STATE'),(29,'Rajasthan','RJ','08','STATE'),(30,'Sikkim','SK','11','STATE'),(31,'Tamil Nadu','TN','33','STATE'),(32,'Telangana','TN','36','STATE'),(33,'Tripura','TR','16','STATE'),(34,'Uttar Pradesh','UP','09','STATE'),(35,'Uttarakhand','UK','05','STATE'),(36,'West Bangal','WB','19','STATE');
/*!40000 ALTER TABLE `statename` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `UserName` varchar(250) DEFAULT NULL,
  `Password` varchar(250) DEFAULT NULL,
  `URole` varchar(250) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('admin','5678','Admin'),('user','123','Operator');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `voucher_master`
--

DROP TABLE IF EXISTS `voucher_master`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `voucher_master` (
  `VNm` varchar(250) DEFAULT NULL,
  `VType` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `voucher_master`
--

LOCK TABLES `voucher_master` WRITE;
/*!40000 ALTER TABLE `voucher_master` DISABLE KEYS */;
/*!40000 ALTER TABLE `voucher_master` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-09-01  8:57:09
