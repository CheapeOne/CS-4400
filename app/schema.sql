CREATE TABLE Data_Type (
  Type  VARCHAR(100) NOT NULL,
  PRIMARY KEY (Type)
)ENGINE=InnoDB;

CREATE TABLE City_State (
  City      VARCHAR(100) NOT NULL,
  State     VARCHAR(100) NOT NULL,
  PRIMARY KEY (City, State) 
)ENGINE=InnoDB;

CREATE TABLE User (
  Email   VARCHAR(100) NOT NULL,
  Username  VARCHAR(100) NOT NULL,
  Password  VARCHAR(100) NOT NULL,
  User_Type   ENUM('admin', 'city official', 'city scientist') NOT NULL,
  PRIMARY KEY (Username),
  UNIQUE KEY (Email)
)ENGINE=InnoDB;

CREATE TABLE POI (
  Date_Flagged    TIMESTAMP,
  Flagged   TINYINT(1) DEFAULT 0,
  Location_Name VARCHAR(100) NOT NULL,
  Zip_Code    CHAR(5),
  City      VARCHAR(100) NOT  NULL,
  State     VARCHAR(100) NOT NULL,
  PRIMARY KEY (Location_Name),
  FOREIGN KEY (City, State) REFERENCES City_State (City, State)
  ON DELETE CASCADE 
  ON UPDATE CASCADE
)ENGINE=InnoDB;

CREATE TABLE Data_Point (
  Date_Time    TIMESTAMP NOT NULL,
  POI_Location_Name   VARCHAR(100) NOT NULL,
  Data_Value      FLOAT NOT NULL,
  Accepted    ENUM('pending', 'approved', 'rejected') NOT NULL,
  Data_Type     VARCHAR(100) NOT NULL,
  PRIMARY KEY (Date_Time, POI_Location_Name),
  FOREIGN KEY (POI_Location_Name) REFERENCES POI(Location_Name)
  ON DELETE CASCADE
  ON UPDATE CASCADE,
  FOREIGN KEY (Data_Type) REFERENCES Data_Type(Type)
  ON DELETE CASCADE
  ON UPDATE CASCADE
)ENGINE=InnoDB;

CREATE TABLE City_Official(
  Username  VARCHAR(100) NOT NULL,
  Title   VARCHAR(100) NOT NULL,
  City    VARCHAR(100) NOT NULL,
  State     VARCHAR(100) NOT NULL,
  Approved ENUM('pending','approved','rejected'),
  PRIMARY KEY (Username),
  FOREIGN KEY (City, State) REFERENCES City_State (City, State)
  ON DELETE CASCADE
  ON UPDATE CASCADE,
  FOREIGN KEY (Username) REFERENCES User (Username)
  ON DELETE CASCADE 
  ON UPDATE CASCADE
)ENGINE=InnoDB;
