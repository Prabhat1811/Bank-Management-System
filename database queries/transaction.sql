CREATE TABLE `bms`.`transaction`(
	`tranid` INT AUTO_INCREMENT,
	`trandate` DATETIME DEFAULT CURRENT_TIMESTAMP,
    `tranamt` INT,
	`senderaccno` INT,
	`recieveraccno` INT,
	PRIMARY KEY (`tranid`),
	FOREIGN KEY (`senderaccno`) REFERENCES `bms`.`account`(accno)
    );

INSERT INTO `bms`.`transaction`(`tranamt`,`senderaccno`,`recieveraccno`) VALUES
('5000','1','2'),
('2100','2','3'),
('2350','3','1');