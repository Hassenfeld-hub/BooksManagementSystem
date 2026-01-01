/*
 Navicat MySQL Dump SQL

 Source Server         : Books Management System
 Source Server Type    : MySQL
 Source Server Version : 80044 (8.0.44)
 Source Host           : localhost:3306
 Source Schema         : booksmanagementsystem

 Target Server Type    : MySQL
 Target Server Version : 80044 (8.0.44)
 File Encoding         : 65001

 Date: 23/12/2025 19:27:39
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for admin
-- ----------------------------
DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin`  (
  `admin_id` bigint NOT NULL COMMENT '数据库管理员账号',
  `password` varchar(15) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin NOT NULL COMMENT '数据库管理员密码',
  `username` varchar(15) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin NOT NULL COMMENT '数据库管理员用户名',
  PRIMARY KEY (`admin_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of admin
-- ----------------------------
INSERT INTO `admin` VALUES (1, 'password123', 'admin01');
INSERT INTO `admin` VALUES (2, 'password123', 'admin02');
INSERT INTO `admin` VALUES (3, 'password123', 'admin03');
INSERT INTO `admin` VALUES (4, 'password123', 'admin04');
INSERT INTO `admin` VALUES (5, 'password123', 'admin05');

-- ----------------------------
-- Table structure for book_info
-- ----------------------------
DROP TABLE IF EXISTS `book_info`;
CREATE TABLE `book_info`  (
  `book_id` bigint NOT NULL COMMENT '图书号',
  `name` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin NOT NULL COMMENT '书名',
  `author` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin NOT NULL COMMENT '作者',
  `publish` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin NOT NULL COMMENT '出版社',
  `ISBN` varchar(15) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin NOT NULL COMMENT '标准书号',
  `language` varchar(15) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin NOT NULL COMMENT '语言',
  `price` decimal(10, 2) NOT NULL COMMENT '价格',
  `pub_date` datetime NOT NULL COMMENT '出版时间',
  `class_id` int NOT NULL COMMENT '分类号',
  `number` int NOT NULL COMMENT '剩余数量',
  PRIMARY KEY (`book_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of book_info
-- ----------------------------
INSERT INTO `book_info` VALUES (1, '深入理解计算机系统', 'Randal E. Bryant', '清华大学出版社', '9787302399256', '中文', 78.00, '2023-05-01 00:00:00', 1, 10);
INSERT INTO `book_info` VALUES (2, '现代操作系统', 'Andrew S. Tanenbaum', '人民邮电出版社', '9787115437177', '中文', 88.00, '2021-09-15 00:00:00', 1, 15);
INSERT INTO `book_info` VALUES (3, '活着', '余华', '作家出版社', '9787506347034', '中文', 42.00, '1993-05-01 00:00:00', 2, 5);
INSERT INTO `book_info` VALUES (4, '百年孤独', '加西亚·马尔克斯', '人民文学出版社', '9787020102485', '中文', 65.00, '1990-04-12 00:00:00', 2, 7);
INSERT INTO `book_info` VALUES (5, '史记', '司马迁', '中华书局', '9787101003537', '中文', 58.00, '2020-03-10 00:00:00', 3, 20);
INSERT INTO `book_info` VALUES (6, '平凡的世界', '路遥', '作家出版社', '9787506344040', '中文', 55.00, '2019-11-30 00:00:00', 2, 8);
INSERT INTO `book_info` VALUES (7, '社会学的邀请', '皮埃尔·布尔迪厄', '三联书店', '9787108036075', '中文', 95.00, '2017-08-09 00:00:00', 3, 12);
INSERT INTO `book_info` VALUES (8, '时间简史', '斯蒂芬·霍金', '浙江人民出版社', '9787213026884', '中文', 128.00, '2003-06-20 00:00:00', 4, 25);
INSERT INTO `book_info` VALUES (9, '追风筝的人', '卡勒德·胡赛尼', '南海出版公司', '9787544247333', '中文', 59.00, '2014-12-25 00:00:00', 2, 18);
INSERT INTO `book_info` VALUES (10, '自私的基因', '理查德·道金斯', '湖南科学技术出版社', '9787535764924', '中文', 78.00, '2006-05-15 00:00:00', 4, 30);
INSERT INTO `book_info` VALUES (11, '人类简史', '尤瓦尔·赫拉利', '中信出版社', '9787508688106', '中文', 98.00, '2015-02-15 00:00:00', 3, 20);
INSERT INTO `book_info` VALUES (12, '追忆似水年华', '马塞尔·普鲁斯特', '人民文学出版社', '9787020003798', '中文', 128.00, '1999-08-05 00:00:00', 2, 5);
INSERT INTO `book_info` VALUES (13, '未来简史', '尤瓦尔·赫拉利', '中信出版社', '9787508688113', '中文', 108.00, '2017-11-15 00:00:00', 3, 17);
INSERT INTO `book_info` VALUES (14, '刀锋', '威廉·萨默塞特·毛姆', '上海译文出版社', '9787532762015', '中文', 75.00, '2009-01-10 00:00:00', 2, 8);
INSERT INTO `book_info` VALUES (15, '月亮与六便士', '威廉·萨默塞特·毛姆', '上海译文出版社', '9787532762008', '中文', 60.00, '2007-07-19 00:00:00', 2, 12);
INSERT INTO `book_info` VALUES (16, '看不见的人', '赫尔曼·黑塞', '北京十月文艺出版社', '9787530204907', '中文', 82.00, '2006-09-15 00:00:00', 2, 10);
INSERT INTO `book_info` VALUES (17, '哈利·波特与魔法石', 'J.K.罗琳', '人民文学出版社', '9787532705423', '中文', 55.00, '2000-06-01 00:00:00', 1, 50);
INSERT INTO `book_info` VALUES (18, '天才在左，疯子在右', '高铭', '中信出版社', '9787508639825', '中文', 45.00, '2009-09-01 00:00:00', 3, 15);
INSERT INTO `book_info` VALUES (19, '诺贝尔奖传记', '莫里斯·赖尔', '上海译文出版社', '9787532762633', '中文', 65.00, '2011-05-20 00:00:00', 4, 18);
INSERT INTO `book_info` VALUES (20, '暗时间', '王小峰', '中信出版社', '9787508641590', '中文', 78.00, '2015-06-10 00:00:00', 1, 25);

-- ----------------------------
-- Table structure for class_info
-- ----------------------------
DROP TABLE IF EXISTS `class_info`;
CREATE TABLE `class_info`  (
  `class_id` int NOT NULL COMMENT '类别号',
  `class_name` varchar(15) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin NOT NULL COMMENT '类别名',
  PRIMARY KEY (`class_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of class_info
-- ----------------------------
INSERT INTO `class_info` VALUES (1, '计算机科学');
INSERT INTO `class_info` VALUES (2, '文学');
INSERT INTO `class_info` VALUES (3, '历史');
INSERT INTO `class_info` VALUES (4, '科学');
INSERT INTO `class_info` VALUES (5, '艺术');

-- ----------------------------
-- Table structure for lend_list
-- ----------------------------
DROP TABLE IF EXISTS `lend_list`;
CREATE TABLE `lend_list`  (
  `ser_num` bigint NOT NULL COMMENT '流水号',
  `book_id` bigint NOT NULL COMMENT '图书号',
  `reader_id` bigint NOT NULL COMMENT '读者证号',
  `lend_date` datetime NOT NULL COMMENT '借出日期',
  `back_date` datetime NOT NULL COMMENT '归还日期',
  PRIMARY KEY (`ser_num`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of lend_list
-- ----------------------------
INSERT INTO `lend_list` VALUES (1, 1, 1, '2023-06-01 00:00:00', '2023-06-15 00:00:00');
INSERT INTO `lend_list` VALUES (2, 2, 2, '2023-06-05 00:00:00', '2023-06-19 00:00:00');
INSERT INTO `lend_list` VALUES (3, 3, 3, '2023-06-10 00:00:00', '2023-06-24 00:00:00');
INSERT INTO `lend_list` VALUES (4, 4, 4, '2023-06-12 00:00:00', '2023-06-26 00:00:00');
INSERT INTO `lend_list` VALUES (5, 5, 5, '2023-06-15 00:00:00', '2023-06-29 00:00:00');
INSERT INTO `lend_list` VALUES (6, 6, 6, '2023-06-20 00:00:00', '2023-07-04 00:00:00');
INSERT INTO `lend_list` VALUES (7, 7, 7, '2023-06-22 00:00:00', '2023-07-06 00:00:00');
INSERT INTO `lend_list` VALUES (8, 8, 8, '2023-06-25 00:00:00', '2023-07-09 00:00:00');
INSERT INTO `lend_list` VALUES (9, 9, 9, '2023-06-28 00:00:00', '2023-07-12 00:00:00');
INSERT INTO `lend_list` VALUES (10, 10, 10, '2023-07-01 00:00:00', '2023-07-15 00:00:00');

-- ----------------------------
-- Table structure for reader_card
-- ----------------------------
DROP TABLE IF EXISTS `reader_card`;
CREATE TABLE `reader_card`  (
  `reader_id` bigint NOT NULL COMMENT '读者证号',
  `password` varchar(15) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin NOT NULL COMMENT '密码',
  `username` varchar(15) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin NOT NULL COMMENT '用户名',
  PRIMARY KEY (`reader_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of reader_card
-- ----------------------------
INSERT INTO `reader_card` VALUES (1, '123456', 'zhangsan');
INSERT INTO `reader_card` VALUES (2, '123456', 'lisi');
INSERT INTO `reader_card` VALUES (3, '123456', 'wangwu');
INSERT INTO `reader_card` VALUES (4, '123456', 'zhaoliu');
INSERT INTO `reader_card` VALUES (5, '123456', 'sunqi');
INSERT INTO `reader_card` VALUES (6, '123456', 'zhoub');
INSERT INTO `reader_card` VALUES (7, '123456', 'wuj');
INSERT INTO `reader_card` VALUES (8, '123456', 'zhengs');
INSERT INTO `reader_card` VALUES (9, '123456', 'feng11');
INSERT INTO `reader_card` VALUES (10, '123456', 'chen12');

-- ----------------------------
-- Table structure for reader_info
-- ----------------------------
DROP TABLE IF EXISTS `reader_info`;
CREATE TABLE `reader_info`  (
  `reader_id` bigint NOT NULL COMMENT '读者证号',
  `name` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin NOT NULL COMMENT '姓名',
  `sex` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin NOT NULL COMMENT '性别',
  `birth` datetime NOT NULL COMMENT '生日',
  `address` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin NOT NULL COMMENT '地址',
  `phone` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin NOT NULL COMMENT '电话',
  PRIMARY KEY (`reader_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of reader_info
-- ----------------------------
INSERT INTO `reader_info` VALUES (1, '张三', '男', '1995-02-15 00:00:00', '北京市海淀区', '13800138001');
INSERT INTO `reader_info` VALUES (2, '李四', '女', '1992-07-23 00:00:00', '上海市浦东新区', '13800138002');
INSERT INTO `reader_info` VALUES (3, '王五', '男', '1989-11-30 00:00:00', '广州市天河区', '13800138003');
INSERT INTO `reader_info` VALUES (4, '赵六', '女', '1998-03-12 00:00:00', '深圳市南山区', '13800138004');
INSERT INTO `reader_info` VALUES (5, '孙七', '男', '1990-05-20 00:00:00', '北京市朝阳区', '13800138005');
INSERT INTO `reader_info` VALUES (6, '周八', '女', '1985-10-10 00:00:00', '上海市徐汇区', '13800138006');
INSERT INTO `reader_info` VALUES (7, '吴九', '男', '1992-01-18 00:00:00', '成都市武侯区', '13800138007');
INSERT INTO `reader_info` VALUES (8, '郑十', '女', '1997-08-25 00:00:00', '武汉市武昌区', '13800138008');
INSERT INTO `reader_info` VALUES (9, '冯十一', '男', '2000-06-05 00:00:00', '重庆市渝中区', '13800138009');
INSERT INTO `reader_info` VALUES (10, '陈十二', '女', '1993-12-30 00:00:00', '南京市鼓楼区', '13800138010');

SET FOREIGN_KEY_CHECKS = 1;
