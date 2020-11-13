CREATE TABLE `bms`.`account`(
	`accno` INT AUTO_INCREMENT,
    `accamt` FLOAT DEFAULT 0,
    `acctype` VARCHAR(10),
    `status` VARCHAR(10) DEFAULT 'active',
	`password` VARCHAR(50),
    `custid` INT UNIQUE,
    PRIMARY KEY (`accno`),
    FOREIGN KEY (`custid`) REFERENCES `bms`.`customer`(`custid`)
);

INSERT INTO `bms`.`account`(`accamt`,`acctype`,`status`,`password`,`custid`) VALUES
('1000','savings','active','qwerty12345','1'),
('1200','current','active','qwetry12345','2'),
('1500','savings','inactive','qwerty12345','3');