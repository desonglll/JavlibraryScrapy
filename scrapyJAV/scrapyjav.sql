/*
 Navicat Premium Data Transfer

 Source Server         : mysql
 Source Server Type    : MySQL
 Source Server Version : 80200 (8.2.0)
 Source Host           : localhost:3306
 Source Schema         : scrapyjav

 Target Server Type    : MySQL
 Target Server Version : 80200 (8.2.0)
 File Encoding         : 65001

 Date: 10/02/2024 19:43:58
*/

CREATE DATABASE IF NOT EXISTS `scrapyjav`;
USE `scrapyjav`;

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for works_table
-- ----------------------------
DROP TABLE IF EXISTS `works_table`;
CREATE TABLE `works_table` (
  `id` int NOT NULL AUTO_INCREMENT,
  `link` varchar(255) COLLATE utf8mb3_bin DEFAULT NULL,
  `preview` varchar(255) COLLATE utf8mb3_bin DEFAULT NULL,
  `title` varchar(255) COLLATE utf8mb3_bin DEFAULT NULL,
  `serial_number` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin NOT NULL,
  `release_date` varchar(255) COLLATE utf8mb3_bin DEFAULT NULL,
  `length` varchar(255) COLLATE utf8mb3_bin DEFAULT NULL,
  `director` varchar(255) COLLATE utf8mb3_bin DEFAULT NULL,
  `maker` varchar(255) COLLATE utf8mb3_bin DEFAULT NULL,
  `label` varchar(255) COLLATE utf8mb3_bin DEFAULT NULL,
  `user_rating` varchar(255) COLLATE utf8mb3_bin DEFAULT NULL,
  `genres` varchar(255) COLLATE utf8mb3_bin DEFAULT NULL,
  `cast` varchar(255) COLLATE utf8mb3_bin DEFAULT NULL,
  `subscribed` varchar(255) COLLATE utf8mb3_bin DEFAULT NULL,
  `watched` varchar(255) COLLATE utf8mb3_bin DEFAULT NULL,
  `owned` varchar(255) COLLATE utf8mb3_bin DEFAULT NULL,
  `preview_thumbs` longtext COLLATE utf8mb3_bin DEFAULT NULL,
  PRIMARY KEY (`id`,`serial_number`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=10613 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

SET FOREIGN_KEY_CHECKS = 1;
