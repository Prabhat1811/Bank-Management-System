CREATE TABLE `bms`.`customer`(
	`custid` INT AUTO_INCREMENT,
    `custname` VARCHAR(50),
    `custemail` VARCHAR(50) UNIQUE,
    `custphone` VARCHAR(10) UNIQUE,
	PRIMARY KEY (`custid`)
);

INSERT INTO `bms`.`customer` (`custname`,`custemail`,`custphone`) VALUES
('prabhat','sooperprabhat@gmail.com','9627850233'),
('bipin','bipin94179@gmail.com','9456554282'),
('anshul','anshul1995@gmail.com','9785634564');