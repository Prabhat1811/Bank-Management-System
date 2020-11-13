CREATE TABLE `bms`.`card`(
	`cardno` INT AUTO_INCREMENT,
	`cardpin` INT,
    `cardcvv` INT,
    `cardtype` VARCHAR(10) DEFAULT 'rupay',
    `accno` INT,
    PRIMARY KEY (`cardno`),
    FOREIGN KEY (accno) REFERENCES `bms`.`account`(accno)
);

INSERT INTO `bms`.`card` (`cardpin`,`cardcvv`,`cardtype`,`accno`) VALUES
(1234,456,'rupay',1),
(2345,876,'mastercard',2),
(3456,890,'visa',3);