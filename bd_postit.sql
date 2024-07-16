CREATE DATABASE postit;

use postit;
DROP TABLE IF EXISTS `marca`;
CREATE TABLE `marca` (
  `idmarca` int NOT NULL AUTO_INCREMENT,
  `nombre` char(20) NOT NULL,
  PRIMARY KEY (`idmarca`),
  UNIQUE KEY `nombre_UNIQUE` (`nombre`)
);


LOCK TABLES `marca` WRITE;
INSERT INTO `marca` VALUES (1,'Completado'),(4,'En curso'),(2,'Importante'),(3,'Pendiente');
UNLOCK TABLES;


DROP TABLE IF EXISTS `post_it`;
CREATE TABLE `post_it` (
  `idpost_it` int NOT NULL AUTO_INCREMENT,
  `titulo` varchar(45) NOT NULL,
  `descripcion` varchar(1000) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `prioridad` int unsigned NOT NULL DEFAULT '10',
  `idmarca` int DEFAULT NULL,
  PRIMARY KEY (`idpost_it`),
  KEY `idmarca_idx` (`idmarca`),
  CONSTRAINT `idmarca` FOREIGN KEY (`idmarca`) REFERENCES `marca` (`idmarca`) ON DELETE RESTRICT
);

LOCK TABLES `post_it` WRITE;
INSERT INTO `post_it` VALUES (1,'postit1','descripcion1','2021-10-15',10,2),(2,'postit2','descripcion2','2021-11-10',6,3),(3,'postit3','descripcion3','2022-01-08',1,4),(4,'postit4','descripcion4','2021-10-18',3,1),(5,'postit5','descripcion5','2021-10-19',8,2);
UNLOCK TABLES;
