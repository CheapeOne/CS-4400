CREATE TABLE Data_Type (
  Type  VARCHAR(20) NOT NULL,
  PRIMARY KEY (Type)
);

CREATE TABLE City_State (
  City      VARCHAR(50) NOT NULL,
  State     VARCHAR(50) NOT NULL,
  PRIMARY KEY (City, State)
);

CREATE TABLE User (
  Email   VARCHAR(20) NOT NULL,
  Username  VARCHAR(20) NOT NULL,
  Password  VARCHAR(20) NOT NULL,
  User_Type   ENUM("admin", "city official", "city scientist") NOT NULL,
  PRIMARY KEY (Username),
  UNIQUE KEY (Email)
);

CREATE TABLE POI_Location (
  Location_Name VARCHAR(40) NOT NULL,
  City      VARCHAR(50) NOT  NULL,
  State     VARCHAR(50) NOT NULL,
  Zip_Code    CHAR(5),
  Flagged   TINYINT(1) DEFAULT 0,
  Date_Flagged    TIMESTAMP DEFAULT 0,
  PRIMARY KEY (Location_Name),
  FOREIGN KEY (City, State) REFERENCES City_State
  ON DELETE CASCADE
  ON UPDATE CASCADE
);

CREATE TABLE Data_Point (
  POI_Location_Name   VARCHAR(40) NOT NULL,
  Date_Time    TIMESTAMP NOT NULL,
  Data_Value      FLOAT NOT NULL,
  Data_Type     VARCHAR(40) NOT NULL,
  Accepted    ENUM("pending", "approved", "rejected") NOT NULL,
  PRIMARY KEY (Date_Time, POI_Location_Name),
  FOREIGN KEY (POI_Location_Name) REFERENCES POI(Location_Name)
  ON DELETE CASCADE
  ON UPDATE CASCADE,
  FOREIGN KEY (Data_Type) REFERENCES Data_Type(Type)
  ON DELETE CASCADE
  ON UPDATE CASCADE
);

CREATE TABLE City_Official(
  Username  VARCHAR(20) NOT NULL,
  Title   VARCHAR(20) NOT NULL,
  City    VARCHAR(50) NOT NULL,
  State     VARCHAR(50) NOT NULL,
  PRIMARY KEY (Username),
  FOREIGN KEY (City, State) REFERENCES City_State
  ON DELETE CASCADE
  ON UPDATE CASCADE,
  FOREIGN KEY(Username) REFERENCES User
  ON DELETE CASCADE
  ON UPDATE CASCADE
);
