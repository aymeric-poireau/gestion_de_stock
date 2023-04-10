-- MySQL dump 10.13 Distrib 8.0.32, pour Win64 (x86_64)
--
-- Hôte : localhost Base de données : Boutique
-- ------------------------------------------------------
-- Version du serveur 8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 NOMS DE JEU UTF8MB4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Structure du tableau 'catégories'
--

TABLE DÉROULANTE  SI EXISTE 'catégories';
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE 'categories` (
  'id' int NOT NULL AUTO_INCREMENT,
  'nom' varchar(255) NON NULL,
  CLÉ PRIMAIRE ('id')
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Données relatives au dumping pour les « catégories » du tableau
--

VERROUILLER LES TABLES 'CATÉGORIES' ÉCRIRE;
/*!40000 ALTER TABLE 'catégories' DÉSACTIVER LES CLÉS */;
INSÉRER DANS les « catégories » VALEURS (1,«Alimentation »),(14,«Vetements »),(16,«Bureautique »);
/*!40000 ALTER TABLE 'catégories' ACTIVER LES CLÉS */;
DÉVERROUILLER LES TABLES;

--
-- Structure des tableaux pour le tableau 'produits'
--

DROP TABLE IF EXISTS 'produits';
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE 'produits` (
  'id' int NOT NULL AUTO_INCREMENT,
  'nom' varchar(255) NON NULL,
  le texte « description »,
  'prix' int NOT NULL,
  'quantite' int NOT NULL,
  'id_categorie' int NOT NULL,
  CLÉ PRIMAIRE ('id')
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Données relatives au dumping pour le tableau « produits »
--

LOCK TABLES 'produits' WRITE;
/*!40000 ALTER TABLE 'produits' DÉSACTIVER KEYS */;
INSÉRER DANS 'produits' VALUES (1,'Chemise en lin','Chemise aerer qui porte chaud l hiver',2,50,1),(11,'Chemise en jean','Une chemise en jean est generalement faite de denim plus ou moins epais Ainsi il existe différents modeles adaptes pour chaque saison',40,25,14),(23,'Chemise en polyester' ,'le polyester est une alternative de plus en plus vogue dans l industrie textile',800,25,16),(25,'Chemise en chambray','Ce tissu est plus leger et respirant que le denim et possede un tissage lisse et serre',820,25,16);
/*!40000 ALTER TABLE 'produits' ACTIVER KEYS */;
DÉVERROUILLER LES TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump terminé le 2023-03-20 8:40:14
