/*
Navicat MySQL Data Transfer

Source Server         : 本地
Source Server Version : 50519
Source Host           : localhost:3306
Source Database       : test

Target Server Type    : MYSQL
Target Server Version : 50519
File Encoding         : 65001

Date: 2017-05-24 23:50:38
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for task
-- ----------------------------
DROP TABLE IF EXISTS `task`;
CREATE TABLE `task` (
  `id` varchar(36) NOT NULL,
  `index_` varchar(255) DEFAULT NULL,
  `content` varchar(3000) DEFAULT NULL,
  `work_time` varchar(20) DEFAULT NULL,
  `question_id` varchar(100) DEFAULT NULL,
  `resolution` varchar(255) DEFAULT NULL,
  `complete_rate` varchar(255) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  `user_id` varchar(36) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of task
-- ----------------------------
INSERT INTO `task` VALUES ('1', '2', '2', '2', '2', '2', '2', '2017-05-24 23:10:17', '2');
INSERT INTO `task` VALUES ('3c773a5c-0b08-403b-9e2f-3a3c4b1d6cb7', null, null, '45', null, null, '45', '2017-05-24 23:44:42', null);
INSERT INTO `task` VALUES ('544668ec-ae22-4147-b1b0-81e9f9fa5614', null, null, '4', null, null, '5', '2017-05-24 23:45:43', null);
SET FOREIGN_KEY_CHECKS=1;
